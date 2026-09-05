#!/usr/bin/env python3
"""Find the anti-antropik-design skill on this machine.

Why this exists: the brand guard is the second half of the verification, and
it lives outside this skill. Its path differs per machine and, when it is
installed as a plugin, changes between sessions. Hard-coding a path means the
guard silently stops running, and a silently skipped guard is worse than no
guard - it produces a verdict that looks complete and is not.

So this searches, validates, and fails closed: a directory only counts if it
actually contains scripts/audit_file.py. Exit 2 means "not found", and the
callers treat that as a FAIL, never as a pass.
"""

import argparse
import glob
import os
import shutil
import sys
import tempfile

NAME = "anti-antropik-design"
MARKER = os.path.join("scripts", "audit_file.py")


def _usable(path):
    """A candidate counts only if the script we intend to call is really there."""
    return bool(path) and os.path.isfile(os.path.join(path, MARKER))


def candidates(home=None, env=None):
    """Every place worth looking, in priority order.

    Env var first so anyone can override. Then the plain skills folder, which
    is stable. Plugin and session-cache paths come last and are globbed,
    because their middle segments are generated ids.
    """
    home = home or os.path.expanduser("~")
    env = os.environ if env is None else env
    out = []
    override = env.get("ANTI_ANTROPIK_PATH")
    if override:
        out.append(override)
    out.append(os.path.join(home, ".claude", "skills", NAME))
    out.extend(sorted(glob.glob(
        os.path.join(home, ".claude", "plugins", "**", NAME), recursive=True)))
    out.extend(sorted(glob.glob(
        os.path.join(home, "Library", "Application Support", "Claude",
                     "**", "skills", NAME), recursive=True)))
    return out


def locate(home=None, env=None):
    """Return the path to the brand guard, or None.

    Among globbed hits, newest wins: a session cache can hold several copies
    and the most recently written one is the one the running session uses.
    """
    found = [p for p in candidates(home, env) if _usable(p)]
    if not found:
        return None
    override = (os.environ if env is None else env).get("ANTI_ANTROPIK_PATH")
    if override and found[0] == override:
        return override
    return max(found, key=lambda p: os.path.getmtime(p))


def selftest():
    """Known-answer tests, including the case where nothing is installed."""
    checks = []
    root = tempfile.mkdtemp(prefix="fbg-selftest-")
    try:
        empty_home = os.path.join(root, "empty-home")
        os.makedirs(empty_home)
        checks.append(("nothing installed returns None",
                       locate(home=empty_home, env={}) is None))

        real = os.path.join(root, "real", NAME)
        os.makedirs(os.path.join(real, "scripts"))
        open(os.path.join(real, MARKER), "w").close()
        checks.append(("env override is used",
                       locate(home=empty_home,
                              env={"ANTI_ANTROPIK_PATH": real}) == real))

        hollow = os.path.join(root, "hollow", NAME)
        os.makedirs(hollow)
        checks.append(("folder without audit_file.py is rejected",
                       locate(home=empty_home,
                              env={"ANTI_ANTROPIK_PATH": hollow}) is None))

        home = os.path.join(root, "home")
        skills = os.path.join(home, ".claude", "skills", NAME, "scripts")
        os.makedirs(skills)
        open(os.path.join(skills, "audit_file.py"), "w").close()
        checks.append(("installed skill is found",
                       locate(home=home, env={}) ==
                       os.path.join(home, ".claude", "skills", NAME)))
    finally:
        shutil.rmtree(root, ignore_errors=True)

    for label, ok in checks:
        print("  {} {}".format("ok  " if ok else "FAIL", label))
    passed = all(ok for _, ok in checks)
    print("SELFTEST: {}".format("PASS" if passed else "FAIL"))
    return 0 if passed else 1


def main():
    ap = argparse.ArgumentParser(
        description="Print the path to the anti-antropik-design brand guard.")
    ap.add_argument("--selftest", action="store_true",
                    help="run the built-in checks and exit")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    path = locate()
    if not path:
        sys.stderr.write(
            "brand guard NOT FOUND.\n"
            "This skill needs anti-antropik-design to check brand distance.\n"
            "Fix it in one of two ways:\n"
            "  1. Put the skill in ~/.claude/skills/anti-antropik-design\n"
            "  2. Or point this at it: export ANTI_ANTROPIK_PATH=/path/to/it\n")
        return 2
    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
