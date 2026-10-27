#!/usr/bin/env python3
"""Before the session ends, check the UI files it actually touched.

Why this is a separate hook: the per-file hook sees one file at a time and
speaks only when that file is bad. Neither of those catches the failure this
skill exists to prevent, which is presenting work that was never scanned at
all. Four of four pages generated with an earlier version of this skill were
presented having passed one guard and failed another.

It finds the files from the session transcript rather than from a marker file
it wrote earlier. A marker is state that goes stale, gets deleted, or survives
into the next session and reports on work that is already finished. The
transcript is what actually happened.

It nags once, and only about things an edit can fix.

Exit 2 on a Stop event stops the session ending and hands the text back to
Claude, so this is a blocking hook whether or not that was intended. Two
guards keep it from becoming a trap. It returns immediately when
stop_hook_active is set, which is the field that exists to break exactly this
loop, so the reminder happens once rather than forever. And when the only
thing wrong is that the brand guard is not installed, it reports on stdout and
does not block at all - no amount of editing fixes a missing checker, so
holding the session hostage over it would be cruel and pointless.

Reads the hook payload on stdin. Exit 0 with nothing to say, or 2 with the
reminder on stderr.
"""

import datetime
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# Bounded so that a long session cannot turn the end of a turn into a scan of
# every file it ever mentioned.
MAX_FILES = 12


# Recorded evidence is not work in progress. An eval baseline is *supposed* to
# fail: that failure is the measurement. Editing it to clear this hook would
# falsify the record, which is the one thing this skill must never do. So these
# paths are skipped, and the hook says which ones, because a silent skip is how
# a guard quietly stops guarding.
EVIDENCE_DIR = re.compile(r"(?:^|/)[\w.-]*-workspace/")
EVIDENCE_FIXTURE = re.compile(r"(?:^|/)anti-ai-design-style/examples/")


def skipped_note(evidence):
    if not evidence:
        return ""
    return ("\nSkipped as recorded evidence (measurements, not work): "
            + ", ".join(os.path.basename(e) for e in evidence[:6]))


def is_recorded_evidence(path):
    """True for measurements and fixtures that exist to be looked at, not fixed.

    Two shapes. Eval workspaces hold recorded measurements; a baseline that
    fails is the result, and editing it would falsify the record. The skill's
    own examples/ folder holds fixtures; slop-example.html fails on purpose.
    The match is on the skill's own folder name, so a user's file that merely
    shares the name examples/slop-example.html is still checked.

    The first version kept the slop fixture checked because the selftest used
    it to prove the hook speaks up. The selftest now proves that on a copy at
    a neutral path, so the rule and its proof both survive.
    """
    norm = path.replace(os.sep, "/")
    return bool(EVIDENCE_DIR.search(norm) or EVIDENCE_FIXTURE.search(norm))


UI_EXT = r"(?:html|htm|css|scss|jsx|tsx|vue|svelte|astro)"
QUOTED_UI = re.compile(r'["\']([^"\'\n]+?\.' + UI_EXT + r')["\']')
BARE_UI = re.compile(r'(?<![\w./~$-])([\w./~-]*[\w-]\.' + UI_EXT + r')(?![\w.-])')
# Tools that only look. A file a session merely read is not its work.
READ_ONLY_TOOLS = {"Read", "Grep", "Glob", "LS", "NotebookRead", "WebFetch", "WebSearch"}


def _strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from _strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from _strings(v)


def _epoch(timestamp):
    try:
        return datetime.datetime.fromisoformat(timestamp.replace("Z", "+00:00")).timestamp()
    except (AttributeError, TypeError, ValueError):
        return None


def ui_files_from(transcript_path, cwd=None):
    """UI files this session changed, newest first.

    A file counts when two things hold. One of the session's own tool calls
    named it, and it was modified after the session's first transcript line.

    Named: the input of every tool call the session made, except tools that
    only read. Edit and Write name the file they change. A Bash command
    counts too, quoted or not, because `sed -i`, `cat >` and `tee` write
    files without an Edit. Text the session did not write does not count.
    That covers tool output, the user's messages, hook feedback, and context
    injected at session start.

    Modified: a Bash command that only reads names a file just as one that
    writes it does. The file's mtime tells them apart. When no timestamp in
    the transcript can be read, this test is skipped and every named file is
    scanned.

    The first version read the whole transcript. On 2026-10-11 that blocked
    a client session over two screen files, which it never
    changed. One path came from a memory injected out of another session.
    The other came from the output of a read-only sweep, and later from
    read-only Bash commands. Each file fails on copy its owner wrote, so the
    block stood, and no edit by that session could clear it.

    The trade-offs:
    - A script that writes a UI file without naming it is missed.
    - `git checkout`, `merge` or `stash apply` refresh mtimes, so a named file
      the session checked out is scanned.
    - In a worktree created after the first transcript line, every named file
      looks modified, which is the old behaviour.
    The last two err toward guarding. Relative paths resolve against the
    session's cwd from the hook payload. The hook's own cwd can be another
    checkout.
    """
    names, start = [], None
    try:
        with open(transcript_path, encoding="utf-8", errors="replace") as f:
            for line in f:
                if start is None and '"timestamp"' in line:
                    try:
                        start = _epoch(json.loads(line).get("timestamp"))
                    except ValueError:
                        pass
                if '"tool_use"' not in line:
                    continue
                try:
                    entry = json.loads(line)
                except ValueError:
                    continue
                message = entry.get("message") if entry.get("type") == "assistant" else None
                content = message.get("content") if isinstance(message, dict) else None
                for block in content if isinstance(content, list) else []:
                    if (not isinstance(block, dict) or block.get("type") != "tool_use"
                            or block.get("name") in READ_ONLY_TOOLS):
                        continue
                    for text in _strings(block.get("input")):
                        names += QUOTED_UI.findall(text) + BARE_UI.findall(text)
    except OSError:
        return []
    base = cwd or os.getcwd()
    seen, out = set(), []
    for name in reversed(names):
        path = os.path.normpath(os.path.join(base, os.path.expanduser(name)))
        if path in seen:
            continue
        seen.add(path)
        # The mtime test runs before the cap, or a dozen files that were only
        # read would crowd out the one that was edited.
        if os.path.isfile(path) and (start is None or os.path.getmtime(path) >= start):
            out.append(path)
        if len(out) >= MAX_FILES:
            break
    return out


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    # Set on the second and later passes, when the session is already being
    # continued because of a stop hook. Without this check the hook fires
    # again on the retry, and again, and the session cannot end.
    if payload.get("stop_hook_active"):
        return 0

    transcript = payload.get("transcript_path")
    if not transcript:
        return 0
    files = ui_files_from(transcript, payload.get("cwd"))
    evidence = [f for f in files if is_recorded_evidence(f)]
    files = [f for f in files if not is_recorded_evidence(f)]
    if not files:
        return 0                      # no UI work this session; stay quiet

    try:
        out = subprocess.run(
            [sys.executable, os.path.join(HERE, "verify_all.py"),
             "--json"] + files,
            capture_output=True, text=True, timeout=120)
    except Exception:
        return 0

    line = out.stdout.strip().splitlines()[-1] if out.stdout.strip() else ""
    if out.returncode == 0:
        return 0                      # everything passed; nothing to say

    checked = ", ".join(os.path.basename(f) for f in files)

    # Work out whether anything here is actually fixable. If the design is
    # clean and the only failure is a checker that is not installed, saying
    # "fix what the line names" is nonsense and blocking on it is worse.
    # verify_all --json prints the JSON object and then the proof line, so
    # the stream is not a single JSON document. raw_decode reads the object
    # and stops where it ends, instead of choking on the trailing line.
    summary = {}
    text = out.stdout.lstrip()
    if text.startswith("{"):
        try:
            summary, _ = json.JSONDecoder().raw_decode(text)
        except ValueError:
            summary = {}
    # "NOT RUN" means not installed; "DID NOT RUN" means installed and it
    # failed to produce a verdict. Only the first deserves install advice.
    # "NOT RUN" cannot happen any more: the brand check ships in this skill.
    # A crash still can, and it needs a different sentence.
    brand_missing = "brand distance NOT RUN" in line
    brand_crashed = "DID NOT RUN" in line
    others_ok = all(
        summary.get(k, {}).get("ok", False) for k in ("scan", "copy")) \
        if summary else False

    if brand_missing and others_ok:
        print("The design guards passed, but brand distance never ran. That "
              "check ships inside\nthis skill, so this is a fault to report, "
              "not something to install.\n\n  " + line +
              "\n\nFiles checked: " + checked)
        return 0                      # informative, not a blocker

    sys.stderr.write(
        "This session changed UI files, and they do not pass the design "
        "guards yet.\n\n"
        "  " + line + "\n\n"
        "Files checked: " + checked + skipped_note(evidence) + "\n\n" +
        ("The brand check did not return a verdict. Run "
         "scripts/brand_distance.py by hand\non the same files to see its "
         "error; no edit to the page can fix it.\n\n"
         if (brand_missing or brand_crashed) else "") +
        "Fix what the line names, then run verify_all.py again. Do not "
        "present unscanned\nvisual output: everything AI makes looks fine, so "
        "\"it looks fine\" is not a check.\n")
    return 2


EVIDENCE_CASES = [
    # (path, should_be_skipped, why)
    ("proj/anti-ai-design-style-workspace/iteration-2/x/with_skill/outputs/page.html", True,
     "an eval output is a recorded measurement"),
    ("proj/my-skill-workspace/iteration-1/review.html", True,
     "the eval viewer is generated, not authored"),
    ("proj/src/pages/index.html", False, "ordinary work is not evidence"),
    ("proj/workspace-notes/index.html", False,
     "a folder merely containing the word workspace is not an evidence archive"),
    ("proj/anti-ai-design-style/examples/slop-example.html", True,
     "the skill's own bad example exists to fail; the selftest proves the hook on a copy"),
    ("proj/anti-ai-design-style/examples/fixed-example.html", True,
     "the skill's own good example is a fixture too"),
    ("proj/site/examples/slop-example.html", False,
     "a user's own file with the same name is real work"),
]


def _tool_call(name, timestamp=None, **tool_input):
    """One transcript line in Claude Code's real shape: the session's own call."""
    entry = {"type": "assistant", "message": {"role": "assistant", "content": [
        {"type": "tool_use", "id": "toolu_test", "name": name, "input": tool_input}]}}
    if timestamp:
        entry["timestamp"] = timestamp
    return json.dumps(entry) + "\n"


def selftest():
    """Both directions, driven through real transcript files."""
    ok = True
    for path, want_skip, why in EVIDENCE_CASES:
        got = is_recorded_evidence(path)
        print("  {} {}: {}".format("ok  " if got == want_skip else "FAIL", why, path))
        ok = ok and got == want_skip
    import tempfile
    import shutil
    here = os.path.dirname(HERE)
    # The skill's own examples are skipped as fixtures, so the proof that the
    # hook speaks up runs on copies at neutral paths. The rule and its proof
    # both survive that way.
    scratch = tempfile.mkdtemp(prefix="stop-check-")
    slop = os.path.join(scratch, "bad-page.html")
    fixed = os.path.join(scratch, "good-page.html")
    shutil.copy(os.path.join(here, "examples", "slop-example.html"), slop)
    shutil.copy(os.path.join(here, "examples", "fixed-example.html"), fixed)
    cases = [
        ("speaks up when a touched page fails", slop, 2),
        ("stays silent when the page passes", fixed, 0),
        ("stays silent when no UI file was touched", None, 0),
    ]
    # The loop guard, and the case that would otherwise trap a user.
    out = subprocess.run(
        [sys.executable, os.path.abspath(__file__)],
        input=json.dumps({"hook_event_name": "Stop", "stop_hook_active": True,
                          "transcript_path": "/nonexistent"}),
        capture_output=True, text=True)
    good = out.returncode == 0
    ok = ok and good
    print("  {} stop_hook_active means nag once, never loop".format(
        "ok  " if good else "FAIL"))

    t = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
    t.write(_tool_call("Write", file_path=fixed, content=""))
    t.close()
    env = dict(os.environ, HOME=tempfile.mkdtemp())
    env.pop("ANTI_ANTROPIK_PATH", None)
    # No installed sibling on this fake HOME, so there is no cross-check. The
    # brand verdict must still be produced, by this skill's own checker.
    env["ANTI_ANTROPIK_NO_VENDORED"] = "1"
    out = subprocess.run(
        [sys.executable, os.path.abspath(__file__)],
        input=json.dumps({"hook_event_name": "Stop", "transcript_path": t.name}),
        capture_output=True, text=True, env=env)
    good = out.returncode == 0
    ok = ok and good
    print("  {} a clean page with no installed sibling still passes and does "
          "not block".format("ok  " if good else "FAIL"))

    for label, path, want in cases:
        t = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
        t.write(_tool_call("Write", file_path=path or "scripts/etl.py", content=""))
        t.close()
        out = subprocess.run(
            [sys.executable, os.path.abspath(__file__)],
            input=json.dumps({"hook_event_name": "Stop",
                              "transcript_path": t.name}),
            capture_output=True, text=True)
        good = out.returncode == want and not (want == 0 and out.stderr.strip())
        ok = ok and good
        print("  {} {} (exit {})".format("ok  " if good else "FAIL", label,
                                         out.returncode))
    # Code is not copy. On 2026-10-11 every session in a client repo that touched a
    # stylesheet or a component was blocked here: the copy check graded
    # app.css at reading grade 627, on its selectors. Nothing an edit could
    # fix. The same shapes must now pass, and slop copy inside a component
    # must still block, or the fix only switched the check off.
    sys.path.insert(0, HERE)
    from copy_check import STYLESHEET, COMPONENT, SLOP_COMPONENT
    code_files = {}
    for fname, body in (("app.css", STYLESHEET), ("DecisionRecord.jsx", COMPONENT),
                        ("Hero.jsx", SLOP_COMPONENT)):
        code_files[fname] = os.path.join(scratch, fname)
        with open(code_files[fname], "w", encoding="utf-8") as f:
            f.write(body)
    for label, names, want in (
            ("stays silent on a clean stylesheet and component",
             ("app.css", "DecisionRecord.jsx"), 0),
            ("speaks up on slop copy inside a component", ("Hero.jsx",), 2)):
        t = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
        for n in names:
            t.write(_tool_call("Edit", file_path=code_files[n], old_string="a",
                               new_string="b"))
        t.close()
        out = subprocess.run(
            [sys.executable, os.path.abspath(__file__)],
            input=json.dumps({"hook_event_name": "Stop", "transcript_path": t.name}),
            capture_output=True, text=True)
        good = out.returncode == want and not (want == 0 and out.stderr.strip())
        ok = ok and good
        print("  {} {} (exit {})".format("ok  " if good else "FAIL", label,
                                         out.returncode))

    # Only the session's own actions count. On 2026-10-11 a client session
    # was blocked over two screens it never touched: one path came from a
    # memory injected at session start, one from a sweep's printed output.
    # The failing page must block when the session's own call names it, and
    # must not when it only appears in text the session did not write.
    # Single quotes, as in a printed Python list: that is how the real paths
    # got in. JSON leaves them unescaped, so the old whole-text scan saw them.
    quoted = "['" + slop + "']"
    not_its_work = [
        ("a path only in a tool's output", json.dumps({"type": "user", "message": {
            "role": "user", "content": [{"type": "tool_result", "tool_use_id": "toolu_test",
                                         "content": "graded " + quoted + " at 12.3"}]}})),
        ("a path only in context injected at session start", json.dumps({
            "type": "attachment", "attachment": {"type": "hook_additional_context",
                                                 "content": ["see " + quoted]}})),
        ("a path only in the user's message", json.dumps({"type": "user", "message": {
            "role": "user", "content": "look at " + quoted}})),
        ("a path the session only read", _tool_call("Read", file_path=slop).strip()),
    ]
    for label, line in not_its_work:
        t = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
        t.write(line + "\n")
        t.close()
        out = subprocess.run(
            [sys.executable, os.path.abspath(__file__)],
            input=json.dumps({"hook_event_name": "Stop", "transcript_path": t.name}),
            capture_output=True, text=True)
        good = out.returncode == 0 and not out.stderr.strip()
        ok = ok and good
        print("  {} ignores {} (exit {})".format("ok  " if good else "FAIL", label,
                                                 out.returncode))
    elsewhere = tempfile.mkdtemp()
    for label, command, cwd in (
            ("a page a Bash command wrote, path unquoted", "sed -i '' s/a/b/ " + slop, None),
            ("a relative path, resolved against the session's cwd",
             "cat > bad-page.html <<'EOF'\nEOF", scratch)):
        t = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
        t.write(_tool_call("Bash", command=command))
        t.close()
        payload = {"hook_event_name": "Stop", "transcript_path": t.name}
        if cwd:
            payload["cwd"] = cwd
        out = subprocess.run(
            [sys.executable, os.path.abspath(__file__)], input=json.dumps(payload),
            capture_output=True, text=True, cwd=elsewhere)
        good = out.returncode == 2
        ok = ok and good
        print("  {} speaks up on {} (exit {})".format("ok  " if good else "FAIL", label,
                                                      out.returncode))

    # Named is not changed. A Bash command that only reads a page names it
    # too, so the page's mtime decides. Timestamps are in Claude Code's own
    # format, with milliseconds and a Z.
    import time
    now = time.time()
    stamp = datetime.datetime.fromtimestamp(now, datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    aged = os.path.join(scratch, "aged-page.html")
    shutil.copy(slop, aged)
    for label, stamped, mtime, want in (
            ("stays silent on a page a Bash command only read", True, now - 60, 0),
            ("speaks up on a page changed after the session began", True, now + 60, 2),
            ("scans every named page when the transcript has no timestamp", False,
             now - 60, 2)):
        os.utime(aged, (mtime, mtime))
        t = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
        t.write(_tool_call("Bash", timestamp=stamp if stamped else None,
                           command="grep -c div " + aged))
        t.close()
        out = subprocess.run(
            [sys.executable, os.path.abspath(__file__)],
            input=json.dumps({"hook_event_name": "Stop", "transcript_path": t.name}),
            capture_output=True, text=True)
        good = out.returncode == want and not (want == 0 and out.stderr.strip())
        ok = ok and good
        print("  {} {} (exit {})".format("ok  " if good else "FAIL", label, out.returncode))

    out = subprocess.run([sys.executable, os.path.abspath(__file__)],
                         input="not json", capture_output=True, text=True)
    good = out.returncode == 0
    ok = ok and good
    print("  {} survives junk input".format("ok  " if good else "FAIL"))
    print("SELFTEST: {}".format("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(main())
