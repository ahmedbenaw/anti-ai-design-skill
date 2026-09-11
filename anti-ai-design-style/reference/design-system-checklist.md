# Design-system checklist (judgment axis)

**Read this when:** a page passes the scanner and you want to know whether
it is also a complete, well-run design. **Time:** 10 to 20 minutes for a
page, longer for a product.

## What this is, and what it is not

The scanner measures four things: AI-look, craft, copy and brand distance.
None of them measures "does this look composed" or "is this system run
well". This checklist covers that ground. It is **judged by a person**, never
scored by the scanner, and never mixed into the proof line. Where an item can
be measured, the table says which tool measures it. Where it cannot, it says
"judgment". The scanner will never claim to check governance.

The source is a full end-to-end design-system standard, condensed here to
the questions that decide whether something is a design system or a UI kit.

## The four connected systems

| System | Question it answers | Sections below |
|---|---|---|
| Design language | What are the rules and materials? | 1, 4, 5, 6 |
| Experience system | How is it built and how do people move? | 2, 3, 7, 8 |
| Delivery system | How does design become working software? | 9, 10, 11 |
| Operating system | Who owns it, and how does it stay alive? | 12, 13, 14 |

The composition model that holds them together:

```
Tokens define Atoms
Atoms compose Molecules
Molecules compose Organisms
Organisms implement Patterns
Patterns populate Templates
Templates become Pages
Pages connect into Flows
```

A folder of colours, fonts and buttons is a UI kit. Add patterns and
templates and it is a component library. It is a design system only when
all four systems above work as one.

## Legend

- **[scanner]**: a tool measures it. The tool is named.
- **[render]**: `render_check.py --render` or the live-audit mode measures it.
- **[judgment]**: a person decides. Write one line of evidence, not a tick.

## 1. Direction and governance [judgment]

- [ ] The system has a name, a purpose, and a list of what it does not cover.
- [ ] One source of truth is named: Figma-led, code-led, or token-led.
- [ ] Someone owns it. Someone decides. Both are written down.
- [ ] There is a way to propose a change and a way to say no.

Core artefact: a one-page charter.

## 2. What already exists [judgment, with tools]

- [ ] Existing colours, type and components are listed before anything new
      is made. **[scanner]** `ai_tell_scan.py` reports hardcoded hex values
      and library misuse as a starting inventory.
- [ ] What is in code but not in design, and the reverse, is written down.
- [ ] Duplicates and dead components are named, not quietly kept.

## 3. Evidence and brief [judgment]

- [ ] Who this is for, what they are trying to do, and where they are when
      they do it: all three answered from evidence, not guesses.
- [ ] `DESIGN.md` exists and names: the human problem, three things only
      this product could show, the feeling in the user's own words, and what
      is out of scope. The skill's Step 1 writes this.
- [ ] No more than three experience principles, each resolving a real
      tension (for example: confidence over speed).

## 4. Foundations and tokens

- [ ] Colours, type sizes, spacing, radii, shadows and motion timings come
      from named tokens, not typed-in values. **[scanner]** rule CR7 reports
      the share of hex values that bypass `var(--...)`.
- [ ] Tokens have three levels: raw value, meaning, component. `blue-500`
      is a value. `color-text-link` is a meaning. `button-primary-bg` is a
      component token. [judgment]
- [ ] Dark mode is designed, not inverted. **[scanner]** rule CR8 flags a
      dark-mode block that only inverts the light one.
- [ ] Tokens export to web, iOS and Android where those platforms exist.
      [judgment]

## 5. Visual, responsive and motion foundations

- [ ] A type hierarchy with at least one strong size step. **[render]** the
      flat-hierarchy check.
- [ ] Breakpoints for phone, tablet and desktop, with content re-ordered by
      priority, not just squeezed. [judgment]
- [ ] Every animation has a reduced-motion version. **[scanner]** rule CR2.
- [ ] Motion has a duration scale and an easing scale, and nothing autoplays
      without a pause control. [judgment]

## 6. Accessibility (WCAG 2.2 AA)

- [ ] Text contrast 4.5:1, non-text 3:1. **[render]**
- [ ] Touch targets 24px minimum, 44px on touch surfaces. **[render]**
- [ ] Focus is visible and never removed without a replacement.
      **[scanner]** rule CR9 flags `outline: none` with no `:focus-visible`.
- [ ] Nothing is communicated by colour alone. [judgment]
- [ ] Keyboard-only walk-through completed, and one screen-reader pass.
      [judgment, record the date]
- [ ] Alternatives exist for dragging and for complex gestures. [judgment]

## 7. Atoms, molecules, organisms [judgment]

Every component, at every level, has the same eight things written down:
purpose, tokens used, variants, sizes, states, behaviour, accessibility
contract, and a code example. If one is missing, the component is a sketch.

- [ ] States include: default, hover, focus-visible, active, disabled,
      loading, error, empty. Not just the first two.
- [ ] Organisms were stress-tested with real content: shortest, longest,
      empty, translated.

## 8. Patterns, templates, pages, flows [judgment]

- [ ] Patterns solve a user problem (search, validation, empty state,
      destructive confirmation), not just group visuals.
- [ ] Every page shows loading, empty, error and success, in light and dark,
      on phone and desktop.
- [ ] Every flow names its entry, its goal, its failure paths, and what
      happens on back and cancel.
- [ ] Copy follows the formulas. Error: what happened, why, how to fix.
      Empty state: what this is, why it is empty, how to begin.
      **[scanner]** `copy_check.py` catches buzzwords, fake stats and
      shipped placeholders; the formula itself is judgment.

## 9. Design library (Figma or equivalent) [judgment]

- [ ] Variables carry the tokens, with light, dark and any brand modes.
- [ ] Components use auto-layout and bind fills, strokes, spacing and radii
      to tokens. No typed-in values.
- [ ] Deterministic names, descriptions, and usage notes on every component.

## 10. Code library [judgment, with tools]

- [ ] Framework-neutral token source with generated outputs per platform.
- [ ] Semantic HTML, keyboard behaviour and screen-reader behaviour in every
      component. **[render]** checks the rendered result.
- [ ] Tests: unit, interaction, visual regression, accessibility. A bundle
      size budget.

## 11. Design-to-code handoff [judgment]

- [ ] Every design component maps to a code component, by name and import.
- [ ] Every meaningful state is specified. If it is not, engineering guesses.
- [ ] Edge cases listed: empty, longest translation, offline, slow network,
      permissions.

## 12. Documentation [judgment]

- [ ] Getting started, token usage, component docs with do and don't
      examples, migration guides. If it is not documented, it does not
      reliably exist.

## 13. Quality, release and change [judgment, with tools]

- [ ] Before release: the proof line from `verify_all.py`, this checklist,
      and one accessibility walk-through. **[scanner]** for the first.
- [ ] Versioned releases with a changelog and a migration note for any
      breaking change.
- [ ] A contribution path: request, evidence, search for an existing
      pattern, proposal, review, build, document, release.

## 14. Adoption and upkeep [judgment]

- [ ] Someone counts: how many products use it, how many components are
      detached or locally modified, how many hardcoded values remain.
- [ ] A periodic audit is scheduled, and this register's own maintenance
      steps run with it.

## How to report against this list

Do not tick boxes. For each section, write one line: what you checked, what
you found, and what is missing. Attach the proof line for the measured
items. A list of ticks proves nothing; a list of evidence does.
