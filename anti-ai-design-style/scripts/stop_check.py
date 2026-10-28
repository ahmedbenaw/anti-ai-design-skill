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
import io
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


def ui_regexes(sep=os.sep):
    """The two path patterns, built for this platform's separator.

    On Windows a path is `C:\\Users\\me\\page.html`, and neither the
    backslash nor the colon was in the character class. The pattern therefore
    matched only `page.html`, which was then joined to the session's cwd,
    pointed at nothing, and was dropped - so on Windows the hook went silent
    on every absolute path it was handed. Found by running the selftests on a
    Windows runner on 2026-10-28; four blame cases returned 0 where they must
    return 2.

    The separator is a parameter so both platforms' behaviour can be proven
    from either one. The Unix class is left exactly as it was: a backslash is
    a legal character in a POSIX filename, and widening the class there would
    change what the guard matches on the platform it already worked on.
    """
    extra = r"\\:" if sep == "\\" else ""
    quoted = re.compile(r'["\']([^"\'\n]+?\.' + UI_EXT + r')["\']')
    bare = re.compile(r'(?<![\w./~$' + extra + r'-])([\w./~' + extra +
                      r'-]*[\w-]\.' + UI_EXT + r')(?![\w.-])')
    return quoted, bare


QUOTED_UI, BARE_UI = ui_regexes()
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


def session_id_for(payload):
    """This session's id: the hook payload's, else the transcript's filename.

    The filename is the id. Measured on 2026-10-28 across this project's
    three transcripts: every line of the file named for a session carried
    that session's id, 15,367 of 15,367. The fallback exists so the filter
    holds on a payload that omits the field rather than quietly reverting to
    reading every session's lines.
    """
    sid = payload.get("session_id")
    if sid:
        return sid
    path = payload.get("transcript_path") or ""
    stem = os.path.splitext(os.path.basename(path))[0]
    return stem or None


def _is_other_session(entry, session_id):
    """True when this line belongs to a session that is not the current one."""
    if not session_id:
        return False
    theirs = entry.get("sessionId")
    return bool(theirs) and theirs != session_id


def ui_files_from(transcript_path, cwd=None, session_id=None):
    """UI files this session changed, newest first.

    A file counts when three things hold. This session's own line named it,
    one of the session's own tool calls made it, and it was modified after
    the session's first transcript line.

    This session's: a fork or a compaction copies the parent's history into
    the child transcript, so a line in the file is not necessarily a line of
    this session. A line whose sessionId differs is another session's and is
    skipped, for the first timestamp as well as for the names. A line with no
    id cannot be attributed, so it counts; treating it as foreign would turn
    the guard off wherever ids are absent.

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
                looks_relevant = '"tool_use"' in line
                if start is None and '"timestamp"' in line:
                    looks_relevant = True
                if not looks_relevant:
                    continue
                try:
                    entry = json.loads(line)
                except ValueError:
                    continue
                if _is_other_session(entry, session_id):
                    continue
                if start is None:
                    start = _epoch(entry.get("timestamp"))
                if '"tool_use"' not in line:
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


def unmeasured_note(render, line, checked, files):
    """What to say when the rendered check could not reach a verdict.

    ERROR and INCONCLUSIVE are different problems and must not read the same.
    ERROR means no browser would start: nothing about the page is at fault and
    nothing the reader types will change it here. INCONCLUSIVE means the page
    was loaded but its styling was never fetched, so contrast was measured
    against an unstyled page - a number that would be wrong rather than
    missing. That one is recoverable, and the reader is owed the hosts that
    would be contacted and the command that gets a verdict.

    The earlier version printed the same sentence for both and named neither,
    which left the reader with a dead end: no way to tell a missing webfont
    from a missing stylesheet, and no command to run.
    """
    state = render.get("state", "")
    hosts = render.get("blocked_styling") or []
    head = ("The design guards passed. The rendered check could not return a "
            "verdict, so\ncontrast, tap targets and focus are unmeasured "
            "here - no edit to the page\nchanges that.")
    if state == "INCONCLUSIVE":
        head = ("The design guards passed. The page's styling was never "
                "fetched, so contrast\nwas measured against an unstyled page "
                "and is reported as no verdict rather\nthan a wrong number.")
        if hosts:
            head += ("\n\nStyling blocked from: " + ", ".join(hosts) +
                     "\nTo get a verdict, allowing those hosts to be "
                     "contacted:\n  python3 \"" +
                     os.path.join(HERE, "verify_all.py") +
                     "\" --render --allow-network " +
                     " ".join('"%s"' % f for f in files[:4]))
    return head + "\n\n  " + line + "\n\nFiles checked: " + checked


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
    files = ui_files_from(transcript, payload.get("cwd"),
                          session_id_for(payload))
    evidence = [f for f in files if is_recorded_evidence(f)]
    files = [f for f in files if not is_recorded_evidence(f)]
    if not files:
        return 0                      # no UI work this session; stay quiet

    try:
        out = subprocess.run(
            # --render is explicit: verify_all leaves the browser check off
            # by default, so without it every hook run reported
            # "rendered SKIPPED" and contrast, tap targets and focus were
            # never measured. Measured on 2026-10-27: about 10s fixed plus
            # 2s per file, so the 120s timeout below holds ~50 files. When
            # no browser is installed the check still reports SKIPPED
            # rather than failing, so this is safe on a bare machine.
            [sys.executable, os.path.join(HERE, "verify_all.py"),
             "--render", "--json"] + files,
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

    # The rendered check is the only guard that depends on a browser being
    # launchable, and a browser can be installed and still refuse to start:
    # a sandbox, a container, or a CI box with no Mach ports gives ERROR, and
    # a page whose styling lives on a CDN gives INCONCLUSIVE offline. Neither
    # is fixable by editing the page, so blocking every stop on it would be
    # the brand-missing mistake again. Say it plainly instead, and keep the
    # proof line visible so a skipped measurement never reads as a passed one.
    render_state = (summary.get("render") or {}).get("state", "")
    design_ok = all(
        summary.get(k, {}).get("ok", False) for k in ("scan", "copy", "brand")) \
        if summary else False
    if design_ok and render_state in ("ERROR", "INCONCLUSIVE"):
        print(unmeasured_note(summary.get("render") or {}, line, checked, files))
        return 0                      # informative, not a blocker

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


def _tool_call(name, timestamp=None, session_id=None, **tool_input):
    """One transcript line in Claude Code's real shape: the session's own call.

    session_id attributes the line to a session, as the real transcript does.
    Left off, the line carries no id, which is how the other cases here are
    written and how an unattributable line must still be treated.
    """
    entry = {"type": "assistant", "message": {"role": "assistant", "content": [
        {"type": "tool_use", "id": "toolu_test", "name": name, "input": tool_input}]}}
    if timestamp:
        entry["timestamp"] = timestamp
    if session_id:
        entry["sessionId"] = session_id
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

    # A fork or a compaction copies the parent's whole history into the child
    # transcript, so reading the file as one session blames the child for
    # every file the parent ever named. Measured on 2026-10-28: two of three
    # transcripts in this project carried another session's lines, one of
    # them 14,661 of 14,763. That is the same trap the 2026-10-11 blame rule
    # was written to stop, reached by a different route - a correct mtime
    # window and a correct tool list, computed over the wrong population.
    # A line with no id at all still counts: it cannot be attributed, and
    # treating it as foreign would switch the guard off on transcripts that
    # carry no ids.
    mine, theirs = "aaaaaaaa-0000-0000-0000-000000000001", "bbbbbbbb-0000-0000-0000-000000000002"
    for label, lines, payload_id, name_as, want in (
            ("ignores a failing page named only by another session's line",
             [_tool_call("Write", session_id=theirs, file_path=slop, content=""),
              _tool_call("Edit", session_id=mine, file_path="scripts/etl.py",
                         old_string="a", new_string="b")], mine, None, 0),
            ("still speaks up when this session's own line names it",
             [_tool_call("Write", session_id=mine, file_path=slop, content="")],
             mine, None, 2),
            ("falls back to the transcript's own filename for the session id",
             [_tool_call("Write", session_id=theirs, file_path=slop, content="")],
             None, mine, 0)):
        tdir = tempfile.mkdtemp()
        tname = os.path.join(tdir, (name_as or "transcript") + ".jsonl")
        with io.open(tname, "w", encoding="utf-8") as fh:
            for line in lines:
                fh.write(line)
        payload = {"hook_event_name": "Stop", "transcript_path": tname}
        if payload_id:
            payload["session_id"] = payload_id
        out = subprocess.run(
            [sys.executable, os.path.abspath(__file__)], input=json.dumps(payload),
            capture_output=True, text=True)
        good = out.returncode == want and not (want == 0 and out.stderr.strip())
        ok = ok and good
        print("  {} {} (exit {})".format("ok  " if good else "FAIL", label,
                                         out.returncode))

    # The session filter applies to the first timestamp too, and the three
    # cases above cannot see that: none of them carries a stamp, so the mtime
    # window never runs. Here the parent's line is older than the page and
    # this session's is newer. Take the start from the parent and the page
    # looks modified during the session, which is the bug. Take it from this
    # session and the page is correctly left alone.
    old_page = os.path.join(scratch, "parent-aged-page.html")
    shutil.copy(slop, old_page)
    os.utime(old_page, (now - 60, now - 60))
    def _stamp(offset):
        return datetime.datetime.fromtimestamp(
            now + offset, datetime.timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    tdir = tempfile.mkdtemp()
    tname = os.path.join(tdir, mine + ".jsonl")
    with io.open(tname, "w", encoding="utf-8") as fh:
        fh.write(_tool_call("Bash", timestamp=_stamp(-120), session_id=theirs,
                            command="grep -c div " + old_page))
        fh.write(_tool_call("Bash", timestamp=_stamp(0), session_id=mine,
                            command="grep -c div " + old_page))
    out = subprocess.run(
        [sys.executable, os.path.abspath(__file__)],
        input=json.dumps({"hook_event_name": "Stop", "transcript_path": tname,
                          "session_id": mine}),
        capture_output=True, text=True)
    good = out.returncode == 0 and not out.stderr.strip()
    ok = ok and good
    print("  {} takes the first timestamp from this session, not the parent "
          "(exit {})".format("ok  " if good else "FAIL", out.returncode))

    # ERROR and INCONCLUSIVE are different problems. One is "no browser
    # started", which the reader cannot fix by typing anything; the other is
    # "the styling was never fetched", which they can. The old message was
    # identical for both and named neither the hosts nor a command, so a
    # reader could not tell a missing webfont from a missing stylesheet.
    note_err = unmeasured_note({"state": "ERROR", "detail": "no browser"},
                               "PASS: ...", "a.html", ["a.html"])
    note_inc = unmeasured_note(
        {"state": "INCONCLUSIVE",
         "blocked_styling": ["cdn.tailwindcss.com", "fonts.googleapis.com"]},
        "PASS: ...", "a.html", ["a.html"])
    for label, good in (
            ("an inconclusive note names the blocked hosts",
             "cdn.tailwindcss.com" in note_inc and
             "fonts.googleapis.com" in note_inc),
            ("an inconclusive note gives the command that gets a verdict",
             "--render --allow-network" in note_inc and "a.html" in note_inc),
            ("an inconclusive note says the number would be wrong, not missing",
             "wrong number" in note_inc),
            ("a browser that will not start names no hosts and no command",
             "--allow-network" not in note_err),
            ("both notes still carry the proof line and the file list",
             "PASS: ..." in note_err and "Files checked: a.html" in note_err and
             "PASS: ..." in note_inc),
            ("an inconclusive note with no hosts still avoids a dead end",
             "--allow-network" not in unmeasured_note(
                 {"state": "INCONCLUSIVE"}, "PASS: ...", "a.html", ["a.html"]))):
        ok = ok and good
        print("  {} {}".format("ok  " if good else "FAIL", label))

    # Windows paths. The class had neither a backslash nor a colon, so an
    # absolute Windows path yielded the bare filename, resolved against the
    # wrong folder and was dropped: the hook went silent on exactly the paths
    # a Windows session hands it. Both separators are asserted here so the
    # fix is provable from either platform.
    win_q, win_bare = ui_regexes("\\")
    nix_q, nix_bare = ui_regexes("/")
    winpath = r"C:\Users\runneradmin\AppData\Local\Temp\t1\bad-page.html"
    for label, good in (
            ("a Windows absolute path is matched whole, drive letter included",
             win_bare.findall("sed -i '' s/a/b/ " + winpath) == [winpath]),
            ("a Windows path inside a longer command is still matched whole",
             winpath in win_bare.findall("type " + winpath + " | findstr div")),
            ("the Unix pattern is unchanged by the fix",
             nix_bare.findall("sed -i '' s/a/b/ /tmp/t1/bad-page.html") ==
             ["/tmp/t1/bad-page.html"]),
            ("a Unix path still matches under the Unix pattern",
             nix_bare.pattern == BARE_UI.pattern if os.sep == "/" else True),
            ("a plain filename still matches on both",
             win_bare.findall("x page.html y") == ["page.html"] and
             nix_bare.findall("x page.html y") == ["page.html"])):
        ok = ok and good
        print("  {} {}".format("ok  " if good else "FAIL", label))

    out = subprocess.run([sys.executable, os.path.abspath(__file__)],
                         input="not json", capture_output=True, text=True)
    good = out.returncode == 0
    ok = ok and good
    print("  {} survives junk input".format("ok  " if good else "FAIL"))
    # The rendered check is opt-in, so leaving --render off the invocation
    # silently drops contrast, tap targets and focus from every hook run and
    # still prints a PASS line. That is the failure this skill exists to
    # prevent, and nothing caught it for three releases. Assert on the source
    # of both hooks, because an argv built without the flag is the bug.
    # Anchor on each hook's actual invocation text. hook_scan builds a command
    # string for Claude to run; this file builds an argv list.
    for mod, want in (("stop_check.py", '"--render", "--json"] + files'),
                      ("hook_scan.py", 'Run: python3 "{}" --render')):
        src = io.open(os.path.join(HERE, mod), encoding="utf-8").read()
        good = want in src
        ok = ok and good
        print("  {} {} asks verify_all for the rendered check".format(
            "ok  " if good else "FAIL", mod))

    print("SELFTEST: {}".format("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(main())
