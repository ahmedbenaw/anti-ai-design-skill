#!/usr/bin/env python3
"""Find the anti-antropik-design skill on this machine.

Why this exists: the brand guard is the second half of the verification, and
it lives outside this skill. Its path differs per machine and, when it is
installed as a plugin, changes between sessions. Hard-coding a path means the
guard silently stops running, and a silently skipped guard is worse than no
guard - it produces a verdict that looks complete and is not.

So this searches and validates: a directory only counts if it actually
contains scripts/audit_file.py. An installed copy always wins. When none is
installed, the copy vendored inside this skill is used and the proof line says
`(vendored)`, so the fallback is visible, never silent. Exit 2 means "nothing
usable at all", and the callers treat that as a FAIL, never as a pass. Set
ANTI_ANTROPIK_NO_VENDORED=1 to refuse every vendored copy, which is how the
tests reach that path.
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


VENDORED = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "vendor", NAME)


def source_of(path):
    """'vendored' when the guard is a copy shipped inside a `vendor/` folder.

    Structural, not positional: a second copy of this skill in a plugin cache
    carries its own vendor/ folder, and the plugin glob can find it. It must
    be labelled vendored there too, or the proof line would say (installed)
    about a frozen copy.
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
    # The copy vendored inside this skill comes last. It never competes on
    # modification time with an installed copy: a freshly copied folder is
    # always the newest, and it must never win on that basis.
    # ANTI_ANTROPIK_NO_VENDORED=1 switches the fallback off. Tests that must
    # see the fail-closed path use it, and it crosses subprocess boundaries
    # where a function argument cannot.
    if allow_vendored and not env.get("ANTI_ANTROPIK_NO_VENDORED"):
        out.append(VENDORED)
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
        checks.append(("nothing installed returns None (vendored copy excluded)",
                       locate(home=empty_home, env={}, allow_vendored=False) is None))
        checks.append(("nothing installed falls back to the vendored copy",
                       locate(home=empty_home, env={}) == VENDORED))
        checks.append(("ANTI_ANTROPIK_NO_VENDORED=1 switches the fallback off",
                       locate(home=empty_home, env={"ANTI_ANTROPIK_NO_VENDORED": "1"}) is None))

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
        checks.append(("ANTI_ANTROPIK_NO_VENDORED=1 also removes a plugin-cache vendored copy",
                       locate(home=home, env={"ANTI_ANTROPIK_NO_VENDORED": "1"}) is None))
    finally:
        shutil.rmtree(root, ignore_errors=True)

    # The vendored copy must report the fingerprint this skill's proof lines
    # were written against. If the installed copy is ever updated and this
    # copy is not, the two fingerprints in the proof line will differ.
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as fh:
            fh.write("<!doctype html><html><body><p>x</p></body></html>"); tiny = fh.name
        out = subprocess.run([sys.executable, os.path.join(VENDORED, "scripts", "audit_file.py"),
                              "--json", tiny], capture_output=True, text=True, timeout=60).stdout
        fp = json.loads(out[out.index("{"):]).get("exclusion_fingerprint")
        os.unlink(tiny)
    except Exception as e:  # noqa: BLE001
        fp = "error: {}".format(e)
    checks.append(("vendored copy reports fingerprint 5697117fa1b27195 (got {})".format(fp),
                   fp == "5697117fa1b27195"))
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
