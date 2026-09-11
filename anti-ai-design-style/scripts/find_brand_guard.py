#!/usr/bin/env python3
"""Find an installed anti-antropik-design skill, if there is one.

This used to be load-bearing: the brand half of every verdict came from that
skill, so a missing copy meant `brand distance NOT RUN` and a FAIL. It is not
load-bearing any more. This skill measures brand distance itself, in
scripts/brand_distance.py, against the same published standard.

What a found copy is still good for:

  * a cross-check. verify_all.py asks it for a second opinion and fails the
    run if the two implementations disagree, which is how a port earns trust.
  * generate_palette.py, which builds a verified 16-role colour system. That
    tool has no equivalent here yet.

So "not found" is now an ordinary outcome, not a failure. Exit 2 still means
nothing usable was found, and callers treat that as "no cross-check", never
as a failed check.
"""

import argparse
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile

NAME = "anti-antropik-design"
MARKER = os.path.join("scripts", "audit_file.py")


def _usable(path):
    """A candidate counts only if the script we intend to call is really there."""
    return bool(path) and os.path.isfile(os.path.join(path, MARKER))




def source_of(path):
    """Where a found copy came from. Kept for the proof line's source tag.

    Structural, not positional: a second copy of this skill in a plugin cache
    carries its own vendor/ folder, and the plugin glob can find it.
    """
    try:
        real = os.path.realpath(path)
        return "vendored" if os.path.basename(os.path.dirname(real)) == "vendor" else "installed"
    except Exception:
        return "installed"


def candidates(home=None, env=None, allow_vendored=True):
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


def locate(home=None, env=None, allow_vendored=True):
    """Return the path to the brand guard, or None.

    Among globbed hits, newest wins: a session cache can hold several copies
    and the most recently written one is the one the running session uses.
    """
    found = [p for p in candidates(home, env, allow_vendored) if _usable(p)]
    if not allow_vendored or (os.environ if env is None else env).get("ANTI_ANTROPIK_NO_VENDORED"):
        found = [p for p in found if source_of(p) != "vendored"]
    if not found:
        return None
    override = (os.environ if env is None else env).get("ANTI_ANTROPIK_PATH")
    if override and found[0] == override:
        return override
    installed = [p for p in found if source_of(p) == "installed"]
    if installed:
        return max(installed, key=lambda p: os.path.getmtime(p))
    return found[-1]  # the vendored copy, only when nothing else exists


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
                              env={"ANTI_ANTROPIK_PATH": hollow}, allow_vendored=False) is None))

        home = os.path.join(root, "home")
        skills = os.path.join(home, ".claude", "skills", NAME, "scripts")
        os.makedirs(skills)
        open(os.path.join(skills, "audit_file.py"), "w").close()
        checks.append(("installed skill is found",
                       locate(home=home, env={}) ==
                       os.path.join(home, ".claude", "skills", NAME)))

        # A second copy of THIS skill in the plugin cache carries its own
        # vendor/ folder, and the plugin glob finds it. It must be labelled
        # vendored, must lose to a real install however old, and the switch
        # must remove it too.
        cached = os.path.join(home, ".claude", "plugins", "cache", "x",
                              "anti-ai-design-style", "vendor", NAME)
        os.makedirs(os.path.join(cached, "scripts"))
        open(os.path.join(cached, MARKER), "w").close()
        os.utime(os.path.join(home, ".claude", "skills", NAME), (1, 1))
        checks.append(("a vendored copy reached through the plugin glob is labelled vendored",
                       source_of(cached) == "vendored"))
        checks.append(("an older real install beats a newer vendored copy in the plugin cache",
                       locate(home=home, env={}) ==
                       os.path.join(home, ".claude", "skills", NAME)))
        shutil.rmtree(os.path.join(home, ".claude", "skills"))
        checks.append(("ANTI_ANTROPIK_NO_VENDORED=1 refuses a plugin-cache vendored copy",
                       locate(home=home, env={"ANTI_ANTROPIK_NO_VENDORED": "1"}) is None))
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
            "No installed anti-antropik-design found.\n"
            "Brand distance still runs: this skill measures it itself, in\n"
            "scripts/brand_distance.py. An installed copy only adds a\n"
            "cross-check and the generate_palette.py tool.\n"
            "To point at one: export ANTI_ANTROPIK_PATH=/path/to/it\n")
        return 2
    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
