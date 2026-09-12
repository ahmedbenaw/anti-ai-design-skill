---
description: Interview the user in plain words and write their DESIGN.md
allowed-tools: Read, Write, AskUserQuestion
---

The user wants a design direction file so generated designs stop looking
like everyone else's.

Interview them using `/Users/ben/.claude/skills/anti-ai-design-style/templates/design-brief.md` as the script.
Rules for the interview:

- One question at a time. Wait for the answer before the next.
- Plain words only. If they say "I don't know", offer 2-3 concrete options
  drawn from what they've told you about the product, and let them pick.
- Never accept marketing words as answers. If they say "modern and clean",
  ask: "If your product were a place or an object, what would it be?"
- The most important answer is question 2 (three things only this product
  could show). Push gently until there are three real ones.
- For colours: if they have no idea, derive 3-4 candidates from their
  question-3 answer (the product's world), show hex swatches, let them pick.
  Check the text/background pair meets 4.5:1 contrast before writing it in.

Then write the completed `DESIGN.md` to the project root. Show it to them
in full. Finish with: "This file now drives every design I make here.
Say the word and I'll adjust any line."
