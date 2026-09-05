---
name: require-design-scan-before-done
enabled: true
event: stop
action: warn
conditions:
  - field: transcript
    operator: regex_match
    pattern: "\.(html|css|jsx|tsx|vue|svelte)"
---

This session touched UI files. Before you finish, one check has to have run.

- [ ] `python3 "${CLAUDE_PLUGIN_ROOT}"/scripts/verify_all.py <changed files>` → a line
      starting with `PASS:` and exit code 0. It runs all three guards.
      `brand distance NOT RUN` in that line is a FAIL, not a pass.
      4 of 4 skill-generated pages passed the AI-look scan and failed the
      brand guard. That is why it is a gate and not a suggestion.

If it failed, apply the fixes it names and run it again before presenting.
Never present unscanned visual output. "It looks fine" is not a check.
Everything AI makes looks fine.

If this session only touched a stylesheet you did not change visually, say so
and move on. The rule fires on file extensions, not on intent.
