---
description: Scan files for AI-look tells and craft problems, explain plainly
argument-hint: [file-or-folder]
allowed-tools: Bash(python3:*), Read, Glob
---

The user wants to know whether their design reads as AI-generated.

1. Determine what to scan: use `"$ARGUMENTS"` if given; otherwise the UI files
   changed in this session; otherwise ask which folder in ONE short question.
2. Run every guard with one command:
   `python3 /Users/ben/.claude/skills/anti-ai-design-style/scripts/verify_all.py <the files from step 1>`
   It prints a single verdict line. Quote that line. Do not write your own
   summary of it. A hand-written summary is where a failed guard quietly
   turns into a passing sentence.
   Then run these for the findings:
   - `python3 /Users/ben/.claude/skills/anti-ai-design-style/scripts/ai_tell_scan.py <the files from step 1>`
   - `python3 /Users/ben/.claude/skills/anti-ai-design-style/scripts/copy_check.py <the files from step 1>` (pages and docs)
   - `python3 /Users/ben/.claude/skills/anti-ai-design-style/scripts/brand_distance.py <the files from step 1> --suggest`
     (only when brand distance failed; it prints replacement hex values)
3. If the line says `brand distance DID NOT RUN`, say this first, in plain
   words. That checker ships inside this skill. So it is a fault in the tool,
   not in their page. No edit of theirs can clear it. Run
   `scripts/brand_distance.py` on the same files to see the error. Then report
   the rest of the findings normally. Never let a first-time user think their
   page failed on its merits when a checker broke.
   If the line says `cross-check DISAGREES`, say that too. A separate copy of
   the standard reached a different verdict. Nobody should trust the result
   until a person looks at it.
4. Report back in plain language, for a non-technical reader:
   - Start with the verify_all line exactly as printed, then one sentence
     saying what it means.
   - Then a numbered list of at most 7 findings, worst first. For each:
     what it is (no jargon), why it matters (one line), and the exact fix.
   - If there were near-proof findings (generator plumbing), say plainly:
     "this project carries its generator's fingerprints" and what they are.
   - Keep craft/accessibility flags in a separate short list, labelled
     "not AI signs — just worth fixing".
5. End with exactly one question: "Want me to fix these? (/design-fix)"
   Do not start fixing unless asked.

Never dump raw scanner output at the user. Never claim a PASS proves human
authorship — the scanner measures the AI look, not authorship.
