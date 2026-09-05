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

import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# Bounded so that a long session cannot turn the end of a turn into a scan of
# every file it ever mentioned.
MAX_FILES = 12


def ui_files_from(transcript_path):
    """Every existing UI file path the transcript mentions, newest first.

    Deliberately loose. This is a reminder, and a path that appears in the
    transcript but was only read rather than written costs one extra file in
    a scan. Missing a file that was written costs the thing the hook is for.
    """
    try:
        with open(transcript_path, encoding="utf-8", errors="replace") as f:
            body = f.read()
    except OSError:
        return []
    pattern = r'["\']([^"\']+?\.(?:html|htm|css|scss|jsx|tsx|vue|svelte|astro))["\']'
    seen, out = set(), []
    for match in reversed(re.findall(pattern, body)):
        if match in seen:
            continue
        seen.add(match)
        if os.path.isfile(match):
            out.append(match)
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
    files = ui_files_from(transcript)
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
    brand_missing = "brand distance NOT RUN" in line
    brand_crashed = "DID NOT RUN" in line
    others_ok = all(
        summary.get(k, {}).get("ok", False) for k in ("scan", "copy")) \
        if summary else False

    if brand_missing and others_ok:
        print("The design guards passed, but brand distance never ran: the "
              "anti-antropik-design\nskill is not installed. Install it, or "
              "set ANTI_ANTROPIK_PATH to point at it.\n\n  " + line +
              "\n\nFiles checked: " + checked)
        return 0                      # informative, not a blocker

    sys.stderr.write(
        "This session changed UI files, and they do not pass the design "
        "guards yet.\n\n"
        "  " + line + "\n\n"
        "Files checked: " + checked + "\n\n" +
        ("Some of this is the missing brand guard, which no edit can fix. "
         "Install\nanti-antropik-design to clear that part.\n\n"
         if brand_missing else "") +
        ("The brand guard is installed but did not return a verdict. Run "
         "verify_all.py\nby hand to see its error.\n\n"
         if brand_crashed else "") +
        "Fix what the line names, then run verify_all.py again. Do not "
        "present unscanned\nvisual output: everything AI makes looks fine, so "
        "\"it looks fine\" is not a check.\n")
    return 2


def selftest():
    """Both directions, driven through real transcript files."""
    import tempfile
    here = os.path.dirname(HERE)
    slop = os.path.join(here, "examples", "slop-example.html")
    fixed = os.path.join(here, "examples", "fixed-example.html")
    cases = [
        ("speaks up when a touched page fails", slop, 2),
        ("stays silent when the page passes", fixed, 0),
        ("stays silent when no UI file was touched", None, 0),
    ]
    ok = True
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
    t.write(json.dumps({"file_path": fixed}) + "\n")
    t.close()
    env = dict(os.environ, HOME=tempfile.mkdtemp())
    env.pop("ANTI_ANTROPIK_PATH", None)
    out = subprocess.run(
        [sys.executable, os.path.abspath(__file__)],
        input=json.dumps({"hook_event_name": "Stop", "transcript_path": t.name}),
        capture_output=True, text=True, env=env)
    good = out.returncode == 0 and "not installed" in out.stdout
    ok = ok and good
    print("  {} a clean page with no brand guard informs, does not block"
          .format("ok  " if good else "FAIL"))

    for label, path, want in cases:
        t = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
        t.write(json.dumps({"tool": "Write",
                            "file_path": path or "scripts/etl.py"}) + "\n")
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
