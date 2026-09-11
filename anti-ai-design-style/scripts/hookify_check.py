#!/usr/bin/env python3
"""Prove this skill's hookify rules actually fire.

Why this exists: a hookify rule that never fires looks exactly like a hookify
rule that works. It sits in .claude/, it is listed as enabled, and it is
silent - which is also what a correct rule looks like on a clean page. Two
real defects hid in that silence:

  1. The stop rule used the simple `pattern:` form. For event: stop that binds
     to a `content` field the stop event never provides, so it never fired.
  2. The four file rules used `field: new_text`, which the engine resolves to
     `new_string`. The Write tool has no `new_string` - it has `content`. So
     the rules fired on Edit and never on Write, and writing a brand new page
     bypassed every one of them.

Both were found by running the rules through hookify's own engine rather than
by reading them. This script keeps that check runnable, so a future edit to a
rule cannot quietly turn it off again.

Run it from the skill directory:  python3 scripts/hookify_check.py
"""

import glob
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(HERE)
# The marketplace cache path varies by install; HOOKIFY_PATH overrides it the
# way ANTI_ANTROPIK_PATH overrides the brand guard location.
HOOKIFY = os.environ.get("HOOKIFY_PATH") or os.path.expanduser(
    "~/.claude/plugins/marketplaces/claude-plugins-official/plugins/hookify")

# A trigger per rule, plus the file it would be written to. Each trigger is a
# minimal example of the thing the rule exists to catch.
TRIGGERS = {
    "warn-ai-gradient-tells": (
        "page.html", '<h1 class="bg-clip-text text-transparent">Hi</h1>'),
    "warn-ai-copy-tells": (
        "page.html", "<p>Unlock the power of seamless workflows.</p>"),
    "block-fake-proof": (
        "page.html", '<img src="https://i.pravatar.cc/80" alt="John Doe">'),
    "warn-claude-escape-look": (
        "styles.css", "body{background:#FAF9F5;font-family:Georgia,serif}"),
}

# A page with nothing wrong with it. Every rule must stay quiet on this, or
# the rule is noise and people will turn it off.
CLEAN = ("page.html",
         "<h1>Rent, split three ways</h1>"
         "<p>Add what you paid. We do the maths.</p>")

UI_TRANSCRIPT = '{"tool":"Write","file_path":"src/landing.html"}'
NON_UI_TRANSCRIPT = '{"tool":"Write","file_path":"scripts/etl.py"}'


def _transcript(line):
    f = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
    f.write(line + "\n")
    f.close()
    return f.name


def run():
    if not os.path.isdir(HOOKIFY):
        print("hookify plugin not installed, so its rules cannot be tested.")
        print("That is fine: the rules are optional. Everything else in this")
        print("skill works without them.")
        print("SELFTEST: SKIPPED")
        return 0

    sys.path.insert(0, HOOKIFY)
    from core.config_loader import load_rule_file
    from core.rule_engine import RuleEngine

    engine = RuleEngine()
    rules = {}
    for path in sorted(glob.glob(os.path.join(SKILL_DIR, "hookify",
                                              "*.local.md"))):
        rule = load_rule_file(path)
        if rule:
            rules[rule.name] = rule

    def fires(rule, tool, tool_input):
        return bool(engine.evaluate_rules(
            [rule], {"hook_event_name": "PostToolUse", "tool_name": tool,
                     "tool_input": tool_input}))

    results = []
    for name, (filename, text) in TRIGGERS.items():
        rule = rules.get(name)
        if rule is None:
            results.append((name, False, "rule file not found"))
            continue
        # Write and Edit pass the new text under different keys. Both matter:
        # Write is how a new page is created, Edit is how one is changed.
        on_write = fires(rule, "Write", {"file_path": filename,
                                         "content": text})
        on_edit = fires(rule, "Edit", {"file_path": filename,
                                       "new_string": text, "old_string": ""})
        quiet = not fires(rule, "Write", {"file_path": CLEAN[0],
                                          "content": CLEAN[1]})
        ok = on_write and on_edit and quiet
        results.append((name, ok, "write={} edit={} quiet-on-clean={}".format(
            on_write, on_edit, quiet)))

    stop = rules.get("require-design-scan-before-done")
    if stop is None:
        results.append(("require-design-scan-before-done", False,
                        "rule file not found"))
    else:
        def stop_fires(line):
            return bool(engine.evaluate_rules(
                [stop], {"hook_event_name": "Stop",
                         "transcript_path": _transcript(line)}))
        on_ui = stop_fires(UI_TRANSCRIPT)
        quiet = not stop_fires(NON_UI_TRANSCRIPT)
        results.append(("require-design-scan-before-done", on_ui and quiet,
                        "ui-session={} quiet-on-non-ui={}".format(on_ui, quiet)))

    for name, ok, detail in results:
        print("  {} {:<34} {}".format("ok  " if ok else "FAIL", name, detail))

    passed = len(results) == 5 and all(ok for _, ok, _ in results)
    print("SELFTEST: {} ({} of 5 rules fire on their trigger and stay quiet "
          "otherwise)".format("PASS" if passed else "FAIL",
                              sum(1 for _, ok, _ in results if ok)))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(run())
