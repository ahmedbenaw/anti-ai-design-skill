---
description: Scan files for AI-look tells and craft problems, explain plainly
argument-hint: [file-or-folder]
allowed-tools: Bash(python3:*), Read, Glob
---

The user wants to know whether their design reads as AI-generated.

1. Determine what to scan: use `$ARGUMENTS` if given; otherwise the UI files
   changed in this session; otherwise ask which folder in ONE short question.
2. Run every guard with one command:
   `python3 <skill-path>/scripts/verify_all.py $ARGUMENTS`
   It prints a single verdict line. Quote that line. Do not write your own
   summary of it. A hand-written summary is where a failed guard quietly
   turns into a passing sentence.
   Then run these for the findings:
   - `python3 <skill-path>/scripts/ai_tell_scan.py $ARGUMENTS`
   - `python3 <skill-path>/scripts/copy_check.py $ARGUMENTS` (pages and docs)
   - `python3 <anti-antropik-design>/scripts/audit_file.py $ARGUMENTS --suggest`
     (only when brand distance failed; it prints replacement hex values)
3. Report back in plain language, for a non-technical reader:
   - Start with the verify_all line exactly as printed, then one sentence
     saying what it means.
   - Then a numbered list of at most 7 findings, worst first. For each:
     what it is (no jargon), why it matters (one line), and the exact fix.
   - If there were near-proof findings (generator plumbing), say plainly:
     "this project carries its generator's fingerprints" and what they are.
   - Keep craft/accessibility flags in a separate short list, labelled
     "not AI signs — just worth fixing".
4. End with exactly one question: "Want me to fix these? (/design-fix)"
   Do not start fixing unless asked.

Never dump raw scanner output at the user. Never claim a PASS proves human
authorship — the scanner measures the AI look, not authorship.
