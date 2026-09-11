#!/usr/bin/env python3
"""Set up this skill's warning rules and slash commands in a project.

Why this exists: the hookify rules and slash commands ship with placeholder
paths in them, because the skill does not know where it lives until it is on
your computer. Editing five files by hand is the step people get wrong, and a
rule with a broken path fails silently - it loads, it never fires, and you
think you are protected when you are not.

This copies the files and fills the paths in for you. Run it, read what it
says, done. Nothing outside <target>/.claude/ is touched.
"""

import argparse
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(HERE)
NAME_DIR = os.path.basename(SKILL_DIR) or "anti-ai-design-style"

sys.path.insert(0, HERE)
from find_brand_guard import locate  # noqa: E402

# One token set, two install modes. The plugin loader expands
# ${CLAUDE_PLUGIN_ROOT} itself. This script does the same job for people who
# copy the files into a project instead of installing a plugin, so a command
# file works either way and there is only one thing to keep correct.
SKILL_TOKEN = "${CLAUDE_PLUGIN_ROOT}"
# There is no brand-guard token any more. The shipped files resolve that path
# at run time with find_brand_guard.py, so nothing needs substituting here.

EXIT_OK = 0
EXIT_ERROR = 1
EXIT_NO_BRAND_GUARD = 3


def plan_files(skill_dir=SKILL_DIR):
    """Which file goes where. Rules sit in .claude/, commands one level down."""
    jobs = []
    hookify = os.path.join(skill_dir, "hookify")
    if os.path.isdir(hookify):
        for name in sorted(os.listdir(hookify)):
            if name.endswith(".md"):
                jobs.append((os.path.join(hookify, name),
                             os.path.join(".claude", name)))
    commands = os.path.join(skill_dir, "commands")
    if os.path.isdir(commands):
        for name in sorted(os.listdir(commands)):
            if name.endswith(".md"):
                jobs.append((os.path.join(commands, name),
                             os.path.join(".claude", "commands", name)))
    return jobs


# Codex reads skills from .agents/skills/<name>/SKILL.md and knows nothing
# about slash commands, hooks or ${CLAUDE_PLUGIN_ROOT}. So the Codex layout is
# the skill body and everything SKILL.md points at, and nothing else.
CODEX_SKIP = {"commands", "hooks", "hookify", ".claude-plugin", "__pycache__",
              "evals", ".impeccable"}


def codex_files(skill_dir=SKILL_DIR):
    """Every file the Codex copy needs, as (source, relative destination)."""
    jobs = []
    for root, dirs, files in os.walk(skill_dir):
        dirs[:] = [d for d in dirs if d not in CODEX_SKIP]
        for f in files:
            if f.endswith((".pyc", ".DS_Store")):
                continue
            src = os.path.join(root, f)
            rel = os.path.relpath(src, skill_dir)
            jobs.append((src, os.path.join(".agents", "skills", NAME_DIR, rel)))
    return jobs


def shell_safe(path):
    """Quote a path that a shell would otherwise split.

    Real install paths contain spaces - "Anti-AI-design skill" and macOS's
    "Application Support" both do. The rules and commands paste these into
    shell commands, so an unquoted path produces a confusing "No such file"
    for the exact user this script exists to protect. Quoting only the
    directory keeps the rest of the command readable, and adjacent quoted
    and bare segments join into one word in every POSIX shell.
    """
    if path and any(c in path for c in ' \t"\'\\$`&|;<>()*?[]#~!'):
        return '"{}"'.format(path.replace('\\', '\\\\').replace('"', '\\"'))
    return path


def fill(text, skill_dir, brand_dir):
    """Replace the skill-path placeholder with a real, shell-safe path."""
    # The tokens are written already wrapped in quotes, because the plugin
    # loader substitutes a bare path and the shell needs those quotes. So
    # replace the token WITH its surrounding quotes, or the result ends up
    # double-quoted ("" around the path), which the shell splits right back
    # apart at the first space.
    text = text.replace('"%s"' % SKILL_TOKEN, shell_safe(skill_dir))
    text = text.replace(SKILL_TOKEN, shell_safe(skill_dir))
    return text


def install_codex(target, skill_dir=SKILL_DIR, dry_run=False, out=sys.stdout):
    """Write the Codex layout. Verbatim copies; no placeholders to fill."""
    jobs = codex_files(skill_dir)
    for src, rel in jobs:
        dest = os.path.join(target, rel)
        if dry_run:
            continue
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(src, dest)
    agents_md = os.path.join(target, "AGENTS.md")
    line = ("\n## Design checks\n\nBefore presenting any web or mobile UI, load the "
            "`anti-ai-design-style` skill from `.agents/skills/` and quote the line "
            "`verify_all.py` prints. Paths in that skill are relative to its own folder.\n")
    if not dry_run:
        existing = open(agents_md).read() if os.path.exists(agents_md) else ""
        if "anti-ai-design-style" not in existing:
            with open(agents_md, "a") as fh:
                fh.write(line)
    print("{} {} files into {}".format("Would copy" if dry_run else "Copied", len(jobs),
          os.path.join(target, ".agents", "skills", NAME_DIR)), file=out)
    print("Also added a short 'Design checks' section to {} (created it if missing).".format(agents_md), file=out)
    print("Codex has no slash commands or hooks, so only the skill body is installed.\n"
          "What you will see next: in Codex, the skill loads when you ask for a design;\n"
          "it runs the same scanners and prints the same proof line.", file=out)
    return 0


def install(target, skill_dir=SKILL_DIR, brand_dir=None, dry_run=False,
            out=sys.stdout):
    jobs = plan_files(skill_dir)
    if not jobs:
        out.write("Nothing to install: no hookify or commands files found.\n")
        return EXIT_ERROR

    verb = "Would write" if dry_run else "Wrote"
    for src, rel in jobs:
        dest = os.path.join(target, rel)
        if not dry_run:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(src, encoding="utf-8") as f:
                body = fill(f.read(), skill_dir, brand_dir)
            with open(dest, "w", encoding="utf-8") as f:
                f.write(body)
        out.write("{} {}\n".format(verb, dest))

    out.write("\nPaths filled in:\n")
    out.write("  this skill      {}\n".format(skill_dir))
    out.write("  brand guard     {}\n".format(brand_dir or "NOT FOUND"))

    if not brand_dir:
        out.write(
            "\nHeads up: the brand guard (anti-antropik-design) is not "
            "installed.\nThe files are in place and will find it on their own "
            "once it is. Until then\nevery verify_all.py run reports 'brand "
            "distance NOT RUN' and fails, on purpose.\nInstall it, or set "
            "ANTI_ANTROPIK_PATH to point at it.\n")
        return EXIT_NO_BRAND_GUARD

    out.write("\nWhat you will see next: open Claude Code in this folder and "
              "edit a web page.\nWhen it writes something that looks "
              "AI-generated - a gradient headline, a\nfake statistic - a "
              "warning appears in its context and it corrects itself.\n"
              "Rules load on the next tool use. No restart needed.\n")
    return EXIT_OK


def uninstall(target, skill_dir=SKILL_DIR, dry_run=False, out=sys.stdout):
    removed = 0
    verb = "Would remove" if dry_run else "Removed"
    for _, rel in plan_files(skill_dir):
        dest = os.path.join(target, rel)
        if os.path.isfile(dest):
            if not dry_run:
                os.remove(dest)
            out.write("{} {}\n".format(verb, dest))
            removed += 1
    if not removed:
        out.write("Nothing to remove: no files from this skill in {}\n".format(
            os.path.join(target, ".claude")))
    return EXIT_OK


def selftest():
    """Prove the copy and the substitution, including the missing-guard case."""
    import io
    checks = []
    root = tempfile.mkdtemp(prefix="install-selftest-")
    try:
        skill = os.path.join(root, "skill")
        os.makedirs(os.path.join(skill, "hookify"))
        os.makedirs(os.path.join(skill, "commands"))
        with open(os.path.join(skill, "hookify", "hookify.x.local.md"), "w") as f:
            f.write('run python3 "{}"/scripts/s.py\n'.format(SKILL_TOKEN))
        with open(os.path.join(skill, "commands", "c.md"), "w") as f:
            f.write('see "{}"/templates/t.md\n'.format(SKILL_TOKEN))

        target = os.path.join(root, "proj")
        brand = os.path.join(root, "brand")
        code = install(target, skill, brand, out=io.StringIO())
        rule = open(os.path.join(target, ".claude", "hookify.x.local.md")).read()
        cmd = open(os.path.join(target, ".claude", "commands", "c.md")).read()
        checks.append(("install returns 0 when the guard is found", code == EXIT_OK))
        checks.append(("rule lands in .claude/",
                       os.path.isfile(os.path.join(target, ".claude",
                                                   "hookify.x.local.md"))))
        checks.append(("command lands in .claude/commands/",
                       os.path.isfile(os.path.join(target, ".claude",
                                                   "commands", "c.md"))))
        checks.append(("no placeholders remain", SKILL_TOKEN not in rule + cmd))
        checks.append(("real paths substituted", skill in rule and skill in cmd))
        # A doubled quote means the path was quoted twice and the shell will
        # split it at the first space, which is the whole bug this guards.
        checks.append(('no doubled quotes around a substituted path',
                       '""' not in rule + cmd))

        bare = os.path.join(root, "proj2")
        code = install(bare, skill, None, out=io.StringIO())
        rule2 = open(os.path.join(bare, ".claude", "hookify.x.local.md")).read()
        checks.append(("missing guard exits 3", code == EXIT_NO_BRAND_GUARD))
        checks.append(("missing guard still installs a complete file",
                       SKILL_TOKEN not in rule2 and skill in rule2))

        spacey_skill = os.path.join(root, "a skill dir")
        shutil.copytree(skill, spacey_skill)
        spacey_brand = os.path.join(root, "Application Support", "brand")
        os.makedirs(spacey_brand)
        spaced = os.path.join(root, "proj4")
        install(spaced, spacey_skill, spacey_brand, out=io.StringIO())
        rule3 = open(os.path.join(spaced, ".claude",
                                  "hookify.x.local.md")).read()
        checks.append(("paths with spaces are quoted exactly once",
                       '"{}"/scripts/s.py'.format(spacey_skill) in rule3 and
                       '""' not in rule3))
        checks.append(("paths without spaces are left bare",
                       '"' not in open(os.path.join(
                           target, ".claude", "commands", "c.md")).read()))

        dry = os.path.join(root, "proj3")
        install(dry, skill, brand, dry_run=True, out=io.StringIO())
        checks.append(("dry run writes nothing",
                       not os.path.exists(os.path.join(dry, ".claude"))))

        uninstall(target, skill, out=io.StringIO())
        checks.append(("uninstall removes what it installed",
                       not os.path.isfile(os.path.join(
                           target, ".claude", "hookify.x.local.md"))))
    finally:
        shutil.rmtree(root, ignore_errors=True)

    for label, ok in checks:
        print("  {} {}".format("ok  " if ok else "FAIL", label))
    passed = all(ok for _, ok in checks)
    print("SELFTEST: {}".format("PASS" if passed else "FAIL"))
    return EXIT_OK if passed else EXIT_ERROR


def main():
    ap = argparse.ArgumentParser(
        description="Copy this skill's warning rules and slash commands into a "
                    "project, with the file paths filled in for you.")
    ap.add_argument("target", nargs="?", default=".",
                    help="the project folder to set up (default: this folder)")
    ap.add_argument("--dry-run", action="store_true",
                    help="show what would happen, change nothing")
    ap.add_argument("--uninstall", action="store_true",
                    help="remove the files this script installed")
    ap.add_argument("--codex", action="store_true",
                    help="install the Codex layout (.agents/skills/) instead")
    ap.add_argument("--selftest", action="store_true",
                    help="run the built-in checks and exit")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    target = os.path.abspath(args.target)
    if args.uninstall:
        return uninstall(target, dry_run=args.dry_run)
    if args.codex:
        if not os.path.isdir(target):
            print("No such folder: {}".format(target)); return EXIT_ERROR
        return install_codex(target, dry_run=args.dry_run)
    if not os.path.isdir(target):
        sys.stderr.write("No such folder: {}\n".format(target))
        return EXIT_ERROR
    return install(target, brand_dir=locate(), dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
