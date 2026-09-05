#!/usr/bin/env python3
"""Scan the one file Claude just wrote, and say something only if it matters.

Why this exists alongside the hookify rules: those are regex patterns that
warn. This runs the real scanner, so it sees co-occurrence and scoring rather
than single patterns, and it can tell a page that leans generic from one that
reads as AI-generated. The regex rules stay as the zero-install tier for
people who have not set up a plugin.

Two design rules, both learned the hard way:

  Stay quiet unless there is something worth saying. A hook that comments on
  every file is noise, and noise gets switched off, taking the useful warnings
  with it.

  Never block. This runs after the write has already happened, and a design
  opinion is not grounds for stopping someone's work. It reports and lets
  Claude decide.

Reads the hook payload on stdin. Exits 0 with nothing to say, or 2 with the
finding on stderr so Claude sees it.
"""

import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

UI_SUFFIXES = (".html", ".htm", ".css", ".scss", ".jsx", ".tsx",
               ".vue", ".svelte", ".astro")


def target_file(payload):
    """The file this event is about, if it is one we have anything to say on."""
    tool_input = payload.get("tool_input") or {}
    path = tool_input.get("file_path") or ""
    if not path or not path.lower().endswith(UI_SUFFIXES):
        return None
    return path if os.path.isfile(path) else None


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0                      # not our payload; say nothing

    path = target_file(payload)
    if not path:
        return 0

    # Call the scanner rather than importing its internals. It already has a
    # --json path that does gathering, scoring and banding; reimplementing any
    # of that here would let the hook and the command-line tool drift apart
    # and disagree about the same file.
    try:
        out = subprocess.run(
            [sys.executable, os.path.join(HERE, "ai_tell_scan.py"),
             "--json", path],
            capture_output=True, text=True, timeout=30)
        result = json.loads(out.stdout)
    except Exception:
        return 0                      # a hook must never break the session

    score = result.get("ai_score", 0)
    near = result.get("near_proof") or []
    lib = result.get("library_misuse") or []

    # The bar for speaking up. Below 20 the register calls a page distinct,
    # and saying so unprompted is exactly the noise that gets hooks disabled.
    if score < 20 and not near and not lib:
        return 0

    lines = ["anti-ai-design-style scanned {}".format(os.path.basename(path)),
             "AI-look score {}/100 (rules {})".format(
                 score, result.get("rules_fingerprint", "?"))]
    if near:
        lines.append("Generator fingerprints found: " +
                     ", ".join(n.get("name", n.get("id", "?")) for n in near[:3]))
    for tell in (result.get("tells") or [])[:3]:
        lines.append("- {} -> {}".format(tell.get("name"), tell.get("fix", "")))
    for m in lib[:2]:
        lines.append("- library misuse: {} -> {}".format(m.get("name"),
                                                         m.get("fix", "")))
    # Absolute and quoted. Claude's working directory is the user's project,
    # not the skill, so a relative path here resolves to nothing. Both paths
    # can contain spaces.
    lines.append('Run: python3 "{}" "{}" before presenting.'.format(
        os.path.join(HERE, "verify_all.py"), os.path.abspath(path)))
    sys.stderr.write("\n".join(lines) + "\n")
    return 2                          # exit 2 feeds stderr back to Claude


def selftest():
    """Four behaviours, each one a way this hook could go wrong in practice."""
    here = os.path.dirname(HERE)
    cases = [
        ("speaks up about an AI-looking page",
         {"tool_input": {"file_path": os.path.join(here, "examples",
                                                   "slop-example.html")}}, 2),
        ("stays silent on a clean page",
         {"tool_input": {"file_path": os.path.join(here, "examples",
                                                   "fixed-example.html")}}, 0),
        ("ignores files that are not UI",
         {"tool_input": {"file_path": os.path.join(here, "scripts",
                                                   "rules.json")}}, 0),
        ("ignores a path that does not exist",
         {"tool_input": {"file_path": "/nowhere/x.html"}}, 0),
    ]
    ok = True
    for label, payload, want in cases:
        out = subprocess.run([sys.executable, os.path.abspath(__file__)],
                             input=json.dumps(payload),
                             capture_output=True, text=True)
        good = out.returncode == want
        # Silence means silence: an exit 0 that still printed is noise.
        if want == 0 and out.stderr.strip():
            good = False
        ok = ok and good
        print("  {} {} (exit {})".format("ok  " if good else "FAIL",
                                         label, out.returncode))
    # Junk on stdin must not crash a session.
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
