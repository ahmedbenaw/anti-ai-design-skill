# The library layer: nine libraries, one discipline

## Installed versions, checked 2026-09-05

Every version below was installed with npm on the date shown. Every API name
the scanner's twelve library rules depend on was then found in that installed
code. Licences were read from the package and from the repo's own LICENSE
file, because those two disagree more often than you would think.

| Library | Version | Licence (npm field) | Licence (repo LICENSE) | Note |
|---|---|---|---|---|
| gsap | 3.15.0 | Standard "no charge" | no LICENSE file; README links the same | Free for commercial use, not OSI open source |
| animejs | 4.5.0 | MIT | MIT | 5.0.0-beta.2 exists on the `beta` tag; not used here |
| animate.css | 4.1.1 | MIT | **Hippocratic 2.1 on GitHub main** | The npm release is MIT; newer source is not |
| lenis | 1.3.26 | MIT | MIT | |
| pixi.js | 8.20.1 | MIT | MIT | |
| leaflet | 1.9.4 | BSD-2-Clause | BSD-2-Clause | 2.0.0-alpha.1 is a breaking rewrite; stay on 1.9.4 |
| react-leaflet | (not installed) | Hippocratic 2.1 | Hippocratic 2.1 | Named here because people reach for it; check the licence first |
| survey-core | 3.0.3 | MIT | MIT | The renderer. Survey Creator is commercial |
| survey-js-ui | 3.0.3 | MIT | MIT | |
| uiverse galaxy | repo, no package | see repo | see repo | A gallery of 3000+ elements, not a dependency |

The Leaflet plugins page carried 36 categories and 612 table rows when
checked. The categorised table in `maps-forms.md` is a curated subset, not a
mirror.

The two official skill repos for GSAP and PixiJS are vendored under
`vendor/`, SKILL.md files only. See `vendor/README.md` for the override rule.


**TL;DR:** these nine libraries are installed and ported into this skill. They
are not a shopping list. Each one earns its place only when the page
genuinely needs what it does. Each one also has a documented way of producing
the exact AI-slop tells this skill exists to stop. Read the rule below before
reaching for any of them.

## The rule

> A library earns its place when it lets the page **show the real product**.
> It fails when it decorates a page that has nothing to show.

That single line resolves every case here. A map with your actual delivery
area earns its place. A particle field behind a headline does not. A working
multi-step form with real validation earns its place. A fade-up on every
section does not.

## The uncomfortable finding from the research

Every animation library here ships a one-line API for the tells in
`../tells-register.md`. Fade-up-on-scroll, hover-scale, infinite pulse,
marquee and particle backgrounds are not misuse of these tools. They are the
most discoverable feature on each library's own homepage. That is why this
layer names the specific API. "Use motion tastefully" would be useless.

Only one of the four motion libraries ships a reduced-motion default
(animate.css, and only for its own `.animate__animated` class). GSAP and
anime.js give you an opt-in mechanism. animate-ui gives you nothing.

## The nine, by what they are actually for

| Library | Category | Earns its place when | Turns into slop when |
|---|---|---|---|
| **GSAP** | motion engine | state change, FLIP layout continuity, SVG drawing, sequenced timelines | ScrollTrigger carpet, ScrollSmoother on a content site, `repeat: -1` decoration |
| **anime.js** | motion engine (light) | small state transitions, SVG morph/draw, draggable | `onScroll()` on every section, `loop: true` decoration, grid-stagger particle fields |
| **animate.css** | motion presets | one entrance, on one element, once | any `animate__infinite`; entrance classes on mapped list items |
| **animate-ui** | React motion components | pre-built accessible primitives you then restyle | shipping its demo components unchanged (the copy-paste failure) |
| **Lenis** | smooth scroll | almost never on a content site; only where scroll IS the interaction | any use that overrides the user's native scroll on a reading page |
| **PixiJS** | WebGL 2D renderer | thousands of sprites, real games, image filters, heavy data viz | hero particle backgrounds, floating blobs, decorative canvas |
| **uiverse galaxy** | CSS component gallery | studying a technique, then rebuilding it in your own tokens | pasting a component in as-is (this is the core failure mode) |
| **Leaflet** (+ plugins) | maps | showing real places: your delivery area, branches, coverage | a map with no data on it, or one shipped without attribution |
| **SurveyJS** | forms | real multi-step forms with validation, error and empty states | a form that has no error states designed |

## How this layer connects to the scanner

`../../scripts/rules.json` carries a `library_misuse` block with regex
signatures drawn from these files. Examples: the animate.css entrance carpet,
GSAP `repeat: -1`, anime.js `onScroll()` density, Lenis without a
reduced-motion guard, a Leaflet map with no attribution. Findings appear under
"library misuse" in the scan report, separate from the design tells. The fix
is different too. You are not changing the look. You are removing motion, or
adding the accessibility path the library did not give you.

## The two libraries that are pure antidote

Leaflet and SurveyJS are the only two here that add *function* rather than
*motion*. They matter most. The single strongest tell in the register is
"polish without depth" (JD2): a beautiful surface with no working states.
A real map and a real validated form are the direct cure. When a page needs
to prove something, reach for these two before any of the other seven.

## Files

| File | What is in it |
|---|---|
| `motion.md` | GSAP, anime.js, animate.css, animate-ui: install, real API snippets, adopt/avoid, reduced-motion patterns, scanner signatures, licence facts |
| `scroll-canvas-ui.md` | Lenis, PixiJS, uiverse galaxy: same structure, plus the scroll-hijacking and canvas-accessibility cases |
| `maps-forms.md` | Leaflet with its categorised plugin table, and SurveyJS with its licence split spelled out |

## Licence facts worth knowing before you ship

- **GSAP is not MIT.** The npm licence field points at a proprietary Webflow
  "standard no-charge licence". Free, including commercial use, but not OSI
  open source. Details in `motion.md`.
- **SurveyJS splits.** The form renderer and the visual Survey Creator carry
  different licences. `maps-forms.md` states which is which.
- **Leaflet tiles are not free by default.** OpenStreetMap has a tile usage
  policy with real limits, and attribution is required. `maps-forms.md` quotes
  it and lists alternatives.
