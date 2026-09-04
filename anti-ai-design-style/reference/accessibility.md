# Accessibility rules this skill enforces

**TL;DR:** these are the exact numbers your output must meet, with the
standard each one comes from. The scanner catches some automatically
(craft flags); the rest are on the checklist in SKILL.md. Full citations:
`research/06-accessibility.md`.

## The numbers (machine-checkable)

| Rule | Threshold | Standard |
|---|---|---|
| Body text contrast | at least **4.5:1** (3:1 for text ≥24px, or ≥18.66px bold) | WCAG 2.2 SC 1.4.3 (AA) |
| UI parts and icons contrast | at least **3:1** against what's next to them | SC 1.4.11 (AA) |
| Click/tap targets | at least **24×24 px**; aim **44pt** (Apple) / **48dp** (Material) on touch | SC 2.5.8 (AA) |
| Reduced motion | every non-essential animation inside `@media (prefers-reduced-motion: no-preference)` | SC 2.3.3, technique C39 |
| Auto-moving content | pause/stop control if it moves longer than **5 seconds** | SC 2.2.2 (A) |
| Flashing | nothing flashes more than **3 times per second** | SC 2.3.1 (A) |
| Keyboard focus | always visible; never `outline: none` without a replacement | SC 2.4.7 (AA) |
| Line length | at most **75 characters** (sweet spot 45-75; `max-width: 70ch`) | SC 1.4.8 + BDA |
| Body size / spacing | at least **16px**, line-height **1.5**, left-aligned, never justified | BDA Style Guide 2023 |
| Colour alone | never the only way to show meaning (add text, underline, or icon) | SC 1.4.1 (A) |
| Reading level | about **grade 9 or lower** for anything users read | GOV.UK content guidance |

## Rules that need your eyes (no script can check these)

- One main thing per screen; predictable, consistent layout page to page
  (W3C COGA; GOV.UK "one thing per page").
- No idioms or figures of speech in UI text; define jargon on first use
  (Home Office autism guidance).
- Buttons say what they do ("Save invoice", not "Continue" or "Click here").
- Don't make people remember things between steps. Restate them
  (COGA Objective 6; WCAG 3.3.7 handles the form version).
- No fake urgency (countdowns, "only 2 left"). It harms anxious users and
  is a slop tell anyway.
- Warn before timeouts, at least 20 seconds ahead, and keep entered data
  (SC 2.2.1).
- Design the empty, error, and loading states. Their absence is both an
  accessibility failure and the strongest real AI fingerprint (JD2 in the
  register).

## Two evidence warnings (so this skill never spreads myths)

1. **"Dyslexia fonts" are not a fix.** Three studies found OpenDyslexic and
   Dyslexie give no benefit. One found they *slowed* readers. The
   British Dyslexia Association itself recommends ordinary sans faces at
   16px+, line-height 1.5, left-aligned, on a light (not pure white)
   background. Do that instead of shipping a special font.
2. **APCA is advisory only.** WCAG 3 isn't a standard yet. Conformance means
   the WCAG 2.2 ratios above; APCA is a useful extra check for edge cases
   (thin light-grey text, dark mode), never the pass/fail gate.

## Why AI-default design hits disabled and neurodivergent users hardest

Each of these is a scanner tell AND a documented harm. Gradient text:
unverifiable contrast, breaks high-contrast mode. Grey-on-white body copy:
fails 4.5:1. Glass blur panels: contrast indeterminate. Autoplaying
scroll motion: vestibular disorders, ADHD attention traps. Emoji icons:
screen readers announce "sparkles rocket". ALL-CAPS labels: removes the
word shapes dyslexic readers use. Walls of identical cards: choice
overload, no hierarchy. Fixing the AI look and fixing accessibility are
mostly the same work. That's why this skill scores both.
