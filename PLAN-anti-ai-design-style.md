# Build plan v2: anti-ai-design-style skill

**Who this is for:** Claude Code. Paste this file into your project and say
"follow PLAN-anti-ai-design-style.md, task by task". Each task names the exact
skill to invoke.

**What we are building:** a skill that measures, rather than guesses, how
"AI-generated" a web or mobile design looks, then fixes it. It works for people
who do not code. It is written to be easy to follow for neurodivergent readers.

**Status: v1 is built, tested and packaged.** This plan now covers what
changed in v2 and what remains. Tasks 0 to 7 are done. Tasks 8 to 12 are the
v2 work triggered by review feedback.

**Two rules for the whole build:**

1. Every claim traces to a source in `reference/sources-compendium.md`.
   No tell goes in the register from memory.
2. Two guards, not one. Passing the AI-look scanner is not the same as being
   distinct. See Task 8.

---

## What v1 got wrong, and why it matters

The v1 fixed example scored 0 out of 100 on the skill's own scanner and still
looked like Claude's design system. Warm cream, a bookish serif, a terracotta
accent. The register had already named this trap as rule CO6, "the tasteful
escape look". The example walked into the rule that describes it.

Measured with `anti-antropik-design`:

```
FAIL #F5F1E8   2.74 Delta-E from a brand neutral, needs 12 or more
FAIL "georgia" excluded typeface
VERDICT: NON-COMPLIANT
```

The lesson is structural, not cosmetic. A skill that removes one family of
defaults will push output toward the next family of defaults. The only durable
answer is to measure against more than one axis, and to generate palettes
rather than pick them.

---

## Task 0: Set up

Skills: `skill-creator` (read its SKILL.md first).

Create `anti-ai-design-style/` with `scripts/`, `reference/`,
`reference/research/`, `reference/libraries/`, `templates/`, `examples/`,
`hookify/`, `commands/`, `evals/`. Create a sibling
`anti-ai-design-style-workspace/` for test results.

**Status: DONE.**

## Task 1: Research

Skills: `/exa:search` if Exa is connected, otherwise WebSearch and WebFetch.

Eight parallel sweeps. Each writes one sourced file into
`reference/research/`. The eight areas: practitioners, academic, community and
wiki, real AI-generated code samples, mobile and copy, accessibility
standards, prior art, visual science.

Rules: every tell needs a source that was actually opened. Quotes capped at 30
words. Each file ends with a "Gaps" section naming what could not be found.

**Status: DONE. 174 sources.** Exa was never connected, so this used web
search, page fetches and the arXiv database. Reddit was unreachable.

## Task 2: Verify the register

Skills: `adversarial-verify`, `live-state-truth`.

Merge the eight files into `reference/tells-register.md`. Attack every tell.
Does it have two or more independent sources? Is it dated? Does it also appear
in good human design? Can a script measure it, or does it need eyes? Record a
verdict, a weight, an era tag and a false-positive note for each.

**Status: DONE. About 60 tells.** Three popular claims were downgraded by the
evidence. Purple gradient classes appeared in 0 of 12 modern AI repos. The
sparkle icon studies conflict. Dyslexia fonts do not work.

## Task 3: Build the skill core

Skills: `skill-creator`, `live-state-truth`.

Build `scripts/ai_tell_scan.py` (AI-look score plus craft flags, stdlib only,
with `--selftest`), `scripts/copy_check.py` (readability and copy tells),
`scripts/rules.json`, the reference files, templates, examples and `SKILL.md`.

**Status: DONE.** Both scripts self-test. The bad example scores 52 and fails.

## Task 4: Claude Code layer

Skills: `/hookify:writing-rules`, `/hookify:hookify`,
`/plugin-dev:command-development`.

Four hookify rules and three slash commands: `/design-check`, `/design-fix`,
`/design-brief`. Plus a plain-language `reference/setup-guide.md`.

**Status: DONE.** Note: `/claude-tag-troubleshoot:config-guide` documents
@Claude-in-Slack admin settings and has nothing to do with design. Its plain
reference style shaped the setup guide. Its content was not used.

## Task 5: Neurodivergent and non-technical pass

Skills: `i-have-adhd`, `ruthless-editor`, plus the accessibility research.

Rewrite every user-facing file: TL;DR first, numbered steps, one action per
step, jargon defined inline, reading grade 9 or lower.

**Status: DONE.** All user-facing docs pass the skill's own copy checker.
The technical references and the bundled research are explicitly exempt, and
`SKILL.md` states that exemption.

## Task 6: Test with the skill-creator eval loop

Skills: `skill-creator`.

Three realistic prompts. Run each with the skill and without it. Grade against
assertions. Aggregate.

**Status: DONE.** 18 of 18 assertions passed with the skill. 15 of 18 without.
Honest reading: the baseline already avoids purple gradients. The measured
wins were accessibility craft, and refusing to keep fake testimonials when
told "do not remove real information".

## Task 7: Verify and package

Skills: `adversarial-verify`, `live-state-truth`, then `skill-creator`.

**Status: DONE for v1.** Repackage after Tasks 8 to 12.

---

# v2 tasks

## Task 8: Wire in the second guard (brand distance)

Skills: `anti-antropik-design`, `live-state-truth`.

The problem: this skill measures distance from generic AI output. It does not
measure distance from a named company's brand. Fixing one can cause the other.

Steps:

1. Write `reference/brand-distance.md`. Explain the two guards, what each can
   and cannot see, and the v1 defect that proved it.
2. Make `SKILL.md` Step 3 require `audit_file.py` from `anti-antropik-design`
   alongside this skill's own scanners.
3. Stop picking colours by hand. Use
   `generate_palette.py --hue N --temp warm|neutral|cool --chroma low|medium|high`.
   It emits 16 verified roles in light and dark.
4. Rebuild `examples/fixed-example.html` on a generated palette. Document the
   v1 to v2 story in `examples/README.md`.

**Status: DONE.** The example now passes both guards. Worth knowing:
`--temp warm --chroma high` failed, because warm neutrals plus a clay accent
plus warm near-black ink reproduces three brand signature traits at once.

## Task 9: Install and port the nine libraries

Skills: `live-state-truth` (read the live docs, never quote from memory).

Libraries, with the commands the user specified:

| Library | Install |
|---|---|
| GSAP | `https://github.com/greensock/gsap-skills` |
| uiverse galaxy | `https://github.com/uiverse-io/galaxy` |
| anime.js | `npm i animejs` |
| animate.css | `https://github.com/animate-css/animate.css` |
| animate-ui | `https://github.com/imskyleen/animate-ui` |
| Lenis | `https://github.com/darkroomengineering/lenis` |
| PixiJS | `npx skills add https://github.com/pixijs/pixijs-skills` |
| Leaflet + plugins | `https://github.com/Leaflet/Leaflet`, plus `leafletjs.com/plugins.html` |
| SurveyJS | `https://github.com/surveyjs/survey-library` |

For each library, capture the same nine things. What it is. Its licence. Its
current version. Exact install commands. Real API snippets from the docs.
What it earns its place for. How it produces AI-slop tells. Its accessibility
position. Regex signatures for misuse, plus gotchas.

**Status: DONE.** Ported into `reference/libraries/` as `motion.md`,
`scroll-canvas-ui.md`, `maps-forms.md` and a `README.md` index.

Three findings worth carrying forward:

- **GSAP is not MIT.** Its npm licence field points at a proprietary Webflow
  standard licence. Free for commercial use, but not OSI open source.
- **SurveyJS splits.** The form renderer and the visual Survey Creator carry
  different licences.
- **Leaflet tiles are not free by default.** OpenStreetMap has a tile usage
  policy with real limits, and attribution is required.

## Task 10: Add library misuse rules to the scanner

Skills: `live-state-truth`, `adversarial-verify`.

Twelve `library_misuse` rules in `rules.json`, drawn from the ported files.
They report in their own section, because the fix differs from a design fix.
You remove motion, or add the accessibility path. You do not change the look.

Add a third selftest fixture: a page that uses the libraries in exactly the
wrong way. Untested rules are not verified rules.

**Status: DONE.** The fixture catches 9 of the 12 rules. Selftest passes.

## Task 11: Build the sources compendium

Skills: none needed. This is compilation, not research.

One file, `reference/sources-compendium.md`, with an entry per source:
ID, title, source line, two to four context bullets, tags, and which rules it
feeds. Tag vocabulary: `[AVOID: x]`, `[ADOPT: x]`, `[EVIDENCE-ONLY]`,
`[CONTESTED]`, `[STALE-RISK]`. Close with three synthesis sections: the AVOID
map, the ADOPT map, and contested or stale claims.

**Status: DONE. 254 entries, 138 AVOID tags, 129 ADOPT tags.**

## Task 12: Re-verify and repackage

Skills: `adversarial-verify`, `live-state-truth`, `skill-creator`.

1. Both selftests pass.
2. Both examples score correctly, and the fixed one passes the brand guard.
3. Every user-facing doc passes the copy checker.
4. Re-run the three evals against the v2 skill.
5. Repackage and deliver.

**Status: in progress.**

---

## Skill-to-task map

| Skill invoked | Used in | Role |
|---|---|---|
| `skill-creator` | 0, 3, 6, 7, 12 | structure, eval loop, packaging |
| `/exa:search` | 1 | research sweeps. Never connected, so web search was used |
| `live-state-truth` | 2, 3, 7, 9, 10, 12 | run the scripts, read the live docs, assert nothing from memory |
| `adversarial-verify` | 2, 7, 10, 12 | attack the register, then attack the build |
| `/hookify:hookify`, `/hookify:writing-rules` | 4 | the warning rules |
| `/plugin-dev:command-development` | 4 | slash command format |
| `/claude-tag-troubleshoot:config-guide` | 4, style only | it documents Slack admin settings, not design |
| `i-have-adhd` | 5 | action-first, numbered, state-restating docs |
| `ruthless-editor` | 5 | cut without losing information |
| `anti-antropik-design` | 8 | the second guard, and the palette generator |

## Open items after v2

1. **Re-run the evals against v2.** The v1 numbers do not cover the library
   rules or the brand guard.
2. **The register expires.** Eras run about 18 months. Re-verify against real
   generated repos before trusting version 2026.09 in 2027.
3. **Exa still not connected.** A re-sweep would mostly add depth on Reddit,
   which was blocked, and on mobile tells, which is the thinnest area.
4. **No Vue, React Native or Flutter code samples.** The code-pattern evidence
   is React and plain HTML only.
