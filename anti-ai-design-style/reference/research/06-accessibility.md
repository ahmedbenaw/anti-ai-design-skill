# 06 — Accessibility & Neurodivergent-Friendly Design and Documentation

Research compiled 2026-08-28. All thresholds quoted from the cited primary sources; quotation marks indicate exact source wording.

---

# Part A — Accessible, neurodivergent-friendly output design

## Sources

| # | Title | Org | Date/version | URL |
|---|-------|-----|--------------|-----|
| A1 | Web Content Accessibility Guidelines (WCAG) 2.2 | W3C | W3C Recommendation, 5 Oct 2023 (updated Dec 2024) | https://www.w3.org/TR/WCAG22/ |
| A2 | What's New in WCAG 2.2 | W3C WAI | 2023, maintained | https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/ |
| A3 | Understanding SC 2.5.8: Target Size (Minimum) | W3C WAI | WCAG 2.2 Understanding docs | https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html |
| A4 | Understanding SC 1.4.3: Contrast (Minimum) | W3C WAI | WCAG 2.2 Understanding docs | https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html |
| A5 | Understanding SC 2.3.1: Three Flashes or Below Threshold | W3C WAI | WCAG Understanding docs | https://www.w3.org/WAI/WCAG21/Understanding/three-flashes-or-below-threshold.html |
| A6 | Understanding SC 2.3.3: Animation from Interactions (+ Technique C39, prefers-reduced-motion) | W3C WAI | WCAG Understanding docs | https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions.html and https://www.w3.org/WAI/WCAG22/Techniques/css/C39 |
| A7 | Understanding SC 2.2.1: Timing Adjustable | W3C WAI | WCAG 2.2 Understanding docs | https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html |
| A8 | Making Content Usable for People with Cognitive and Learning Disabilities ("COGA Content Usable") | W3C Cognitive and Learning Disabilities Accessibility Task Force | W3C Working Group Note, 29 Apr 2021 | https://www.w3.org/TR/coga-usable/ |
| A9 | BDA Dyslexia Style Guide 2023 | British Dyslexia Association | 2023 (PDF) | https://cdn.bdadyslexia.org.uk/uploads/documents/Advice/style-guide/BDA-Style-Guide-2023.pdf |
| A10 | Designing for accessibility posters (autism, dyslexia, anxiety, low vision, motor, screen readers) | UK Home Office Digital (Karwai Pun) | 2016, hosted ongoing | https://ukhomeoffice.github.io/accessibility-posters/ |
| A11 | "Dos and don'ts on designing for accessibility" | GOV.UK Accessibility blog (Karwai Pun, Home Office) | 2 Sep 2016 | https://accessibility.blog.gov.uk/2016/09/02/dos-and-donts-on-designing-for-accessibility/ |
| A12 | "One thing per page" | GDS Design Notes (Tim Paul) | 3 Jul 2015 | https://designnotes.blog.gov.uk/2015/07/03/one-thing-per-page/ |
| A13 | Foundations: target sizes (collates Apple HIG 44pt, Material 48dp, WCAG values) | TetraLogical | 20 Dec 2022 | https://tetralogical.com/blog/2022/12/20/foundations-target-size/ |
| A14 | "WCAG 3 is not ready yet" (APCA status) | Eric Eggert (yatil.net) | updated 28 Mar 2023 | https://yatil.net/blog/wcag-3-is-not-ready-yet |
| A15 | "Good Fonts for Dyslexia" — Rello & Baeza-Yates, ACM ASSETS 2013 (summary) | dyslexia.com blog (study: Univ. Pompeu Fabra / Yahoo Labs) | study 2013 | https://blog.dyslexia.com/good-fonts-for-dyslexia-an-experimental-study/ |
| A16 | "Do Dyslexia Fonts Actually Work?" (covers Wery & Diliberto 2017; Kuster et al. 2018) | Edutopia | — | https://www.edutopia.org/article/do-dyslexia-fonts-actually-work/ |
| A17 | Understanding SC 1.4.8: Visual Presentation (line length, spacing, justification) | W3C WAI | WCAG Understanding docs | https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html |

## Rules MEASURABLE in code

Each entry: rule → exact threshold → standard + criterion → source # → how to check in HTML/CSS.

1. **Text contrast (AA).** Text and images of text must have "a contrast ratio of at least 4.5:1"; "large-scale text and images of large-scale text have a contrast ratio of at least 3:1." Large-scale = "at least 18 point or 14 point bold" (≈24px, or ≈18.66px bold). Do not round: "4.499:1 would not meet the 4.5:1 threshold." — WCAG 2.2 SC 1.4.3, Level AA — A1, A4. **Check:** compute the WCAG relative-luminance contrast ratio between the resolved CSS `color` and effective background for every text node; compare against 4.5 (or 3.0 when `font-size >= 24px` or `>= 18.66px` with `font-weight >= 700`).
2. **Text contrast (AAA).** 7:1 for normal text, 4.5:1 for large text. — WCAG 2.2 SC 1.4.6, Level AAA — A1, A4. **Check:** same computation, higher thresholds.
3. **Non-text contrast.** UI components and graphical objects needed to understand content: contrast ratio ≥ 3:1 against adjacent colors. — WCAG 2.2 SC 1.4.11, Level AA — A1, A4. **Check:** compare border/icon/focus-indicator colors against adjacent backgrounds; applies to input borders, icon-only buttons, chart elements.
4. **Use of colour alone.** Colour must not be "the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element." — WCAG 2.2 SC 1.4.1, Level A — A1. **Check:** links inside body text need a non-colour cue (e.g. `text-decoration: underline`); required-field/error states need text or an icon, not only a red border; chart series need labels/patterns, not only hue.
5. **Target size.** "The size of the target for pointer inputs is at least 24 by 24 CSS pixels", with 5 exceptions — Spacing ("if a 24 CSS pixel diameter circle is centered on the bounding box of each, the circles do not intersect another target or the circle for another undersized target"), Equivalent, Inline, User-agent control, Essential. — WCAG 2.2 SC 2.5.8, Level AA — A1, A2, A3. Platform minima are stricter: Apple HIG "minimum tappable area of 44×44 points"; Google Material "at least 48dp by 48dp"; WCAG SC 2.5.5 (AAA) requires 44×44 CSS px. — A13. **Check:** `getBoundingClientRect()` of every interactive element ≥ 24×24 (audit target 44/48 for touch UIs); check padding on icon buttons, checkbox/radio hit areas, close buttons.
6. **Focus not obscured.** "When a user interface component receives keyboard focus, the component is not entirely hidden due to author-created content." — WCAG 2.2 SC 2.4.11 Focus Not Obscured (Minimum), Level AA — A1, A2. (Note: in the final WCAG 2.2 numbering, 2.4.11 is *Focus Not Obscured*; *Focus Appearance* is SC 2.4.13.) **Check:** with sticky headers/footers/cookie banners present, tab through the page and verify each focused element is at least partly visible (`elementFromPoint` / intersection tests against `position: fixed|sticky` layers).
7. **Focus appearance.** Focus indicator must be "at least as large as the area of a 2 CSS pixel thick perimeter" of the unfocused component and have "a contrast ratio of at least 3:1 between the same pixels in the focused and unfocused states." — WCAG 2.2 SC 2.4.13, Level AAA (plus SC 2.4.7 Focus Visible, AA) — A1, A2. **Check:** never `outline: none` without a replacement; a `outline: 2px solid` with ≥3:1 change passes; verify `:focus-visible` styles exist for all interactive elements.
8. **Dragging movements.** "All functionality that uses a dragging movement for operation can be achieved by a single pointer without dragging, unless dragging is essential." — WCAG 2.2 SC 2.5.7, Level AA — A1, A2. **Check:** every drag-and-drop, slider, or swipe interaction has click/tap or button alternatives.
9. **Consistent help.** Help mechanisms (contact details, help link, chat) repeated across pages must "occur in the same relative order to other page content." — WCAG 2.2 SC 3.2.6, Level A — A1, A2. **Check:** help/contact link is in the same template position (e.g. header or footer partial) on every page.
10. **Redundant entry.** Information previously entered in the same process must be "auto-populated, or available for the user to select." — WCAG 2.2 SC 3.3.7, Level A — A1, A2. **Check:** multi-step forms carry values forward; use `autocomplete` attributes; never re-ask for the same data (also SC 1.3.5 Identify Input Purpose requires `autocomplete` tokens on personal-data fields).
11. **Accessible authentication.** "A cognitive function test is not required for any step in an authentication process" unless an alternative method or assistance mechanism exists (object recognition and identifying user-supplied personal content are permitted exceptions at AA). — WCAG 2.2 SC 3.3.8, Level AA (3.3.9 AAA removes the exceptions) — A1, A2. **Check:** no memorise-and-retype codes, no transcription puzzles; password fields must allow paste (`onpaste` not blocked) and password-manager autofill; support email/magic-link or OAuth alternatives.
12. **Flashing.** "Web pages do not contain anything that flashes more than three times in any one second period, or the flash is below the general flash and red flash thresholds." General flash = "a pair of opposing changes in relative luminance of 10% or more of the maximum relative luminance where the relative luminance of the darker image is below 0.80"; area threshold ≈ "25% of any 10 degree visual field" (guidance approximates this as a 341×256 px rectangle at typical desktop viewing); red flash = "any pair of opposing transitions involving a saturated red." — WCAG 2.2 SC 2.3.1, Level A — A1, A5. **Check:** no CSS/JS animation, video, or GIF that alternates luminance/saturated red more than 3 times per second over a large area; run PEAT (Photosensitive Epilepsy Analysis Tool) on video.
13. **Moving/auto-updating content.** For "moving, blinking, scrolling" content that "(1) starts automatically, (2) lasts more than five seconds, and (3) is presented in parallel with other content, there is a mechanism for the user to pause, stop, or hide it" (same for auto-updating content). — WCAG 2.2 SC 2.2.2, Level A — A1, A6. **Check:** carousels, tickers, autoplaying video/background video, animated hero sections must have a visible pause/stop control or stop within 5 s.
14. **Motion animation / reduced motion.** "Motion animation triggered by interaction can be disabled, unless the animation is essential." — WCAG 2.2 SC 2.3.3, Level AAA — A1, A6. **Check (Technique C39):** wrap all non-essential transitions/parallax/scroll effects in `@media (prefers-reduced-motion: no-preference) { ... }` or zero them under `@media (prefers-reduced-motion: reduce)`; grep the stylesheet — a site with keyframe animations and no `prefers-reduced-motion` query fails this pattern.
15. **Timeouts.** For each time limit, at least one of: user can "turn off the time limit before encountering it"; "adjust the time limit ... over a wide range that is at least ten times the length of the default"; or is "warned before time expires and given at least 20 seconds to extend the time limit with a simple action" and can "extend the time limit at least ten times." Exceptions: real-time events, essential, or limits "longer than 20 hours." — WCAG 2.2 SC 2.2.1, Level A — A1, A7. COGA goes further: "Avoid Data Loss and Timeouts" — A8. **Check:** session-expiry JS must warn ≥20 s ahead with a one-click extend; forms preserve entered data after timeout.
16. **Text spacing must survive overrides.** No loss of content when users set: "Line height (line spacing) to at least 1.5 times the font size; Spacing following paragraphs to at least 2 times the font size; Letter spacing (tracking) to at least 0.12 times the font size; Word spacing to at least 0.16 times the font size." — WCAG 2.2 SC 1.4.12, Level AA — A1. **Check:** inject that CSS via bookmarklet; nothing may clip or overlap; avoid fixed-height text containers and `overflow: hidden` on prose.
17. **Resize and reflow.** Text resizable "up to 200 percent" without loss (SC 1.4.4 AA); content reflows with no 2-D scrolling at "320 CSS pixels" width equivalent (SC 1.4.10 AA). — A1. **Check:** use `rem` units; test at 400% zoom / 320px viewport; no horizontal scrollbars for prose.
18. **Line length.** AAA: "width is no more than 80 characters or glyphs (40 if CJK)"; also line spacing "at least space-and-a-half within paragraphs", paragraph spacing "at least 1.5 times larger than the line spacing", "text is not justified." — WCAG 2.2 SC 1.4.8, Level AAA — A1, A17. Typographic best practice narrows this to 45–75 characters per line; BDA: "short simple sentences: 60 to 70 characters is optimal" per line — A9. **Check:** set `max-width: 70ch` (or ≤ 75ch) on prose containers; `text-align: justify` on body copy is a defect.
19. **Dyslexia-friendly typography (BDA).** "Font size should be 12-14 point or equivalent (e.g. 1-1.2em / 16-19 px)"; inter-letter spacing "ideally around 35% of the average letter width"; "inter-word spacing should be at least 3.5 times the inter-letter spacing"; line spacing "1.5 / 150% is preferable"; headings "at least 20% larger than the normal text"; "Left align text, without justification"; "Avoid underlining and italics"; "Avoid using ... uppercase letters for continuous text"; use "sans serif fonts, such as Arial"/Verdana/Tahoma/Calibri/Open Sans; "dark coloured text on a light (not white) background"; "avoid green and red/pink" colour combinations. — BDA Style Guide 2023 — A9. **Check:** body `font-size >= 16px`, `line-height: 1.5`, `text-align: left`, no `font-style: italic` or `text-transform: uppercase` for running text, sans-serif stack, off-white background token (e.g. #FAFAF5) rather than pure #FFFFFF-on-#000.
20. **Colour-independent link affordance + simple colour palettes for autism.** "Use simple colours"; "Don't use bright contrasting colours." — Home Office autism poster — A10, A11. **Check:** count of saturated accent hues in the palette (lint token files); avoid pure saturated primaries as large background fills.

## Rules needing judgment

| Rule | Why it can't be fully automated | Source # |
|---|---|---|
| "Write in plain English"; "Don't use figures of speech and idioms" (autism) | Idiom/figurative-language detection is semantic; readability scores only approximate | A10, A11 |
| "Use simple sentences and bullets ... Don't create a wall of text" | "Wall" is a density judgment relative to purpose | A10 |
| "Make buttons descriptive ... Don't make buttons vague and unpredictable" | Label meaningfulness ("Continue" vs "Click here") needs context | A10 |
| "Build simple and consistent layouts ... Don't build complex and cluttered layouts" | Clutter is holistic; no single CSS metric | A10 |
| COGA Objective 3 "Use clear and understandable content"; patterns "Use Clear Words", "Keep Text Succinct", "Avoid Too Much Content" | Requires editorial review and user testing with people with cognitive disabilities | A8 |
| COGA Objective 6 "Ensure processes do not rely on memory"; pattern "Provide a Login that Does Not Rely on Memory or Other Cognitive Skills" | Partially checkable (see rule 11) but flow-level memory demands need walkthroughs | A8 |
| COGA "Make the Purpose of Your Page Clear", "Use a Familiar Hierarchy and Design" (search top-right, home top-left conventions) | Convention-matching is a design judgment | A8 |
| COGA "Limit Interruptions" (modals, toasts, autoplay, notifications) | Frequency/necessity of interruptions is contextual | A8 |
| Anxiety: "Give users enough time"; "Explain what will happen after completing a service"; "Make important information clear"; make support easy to access; "Let users check their answers before they submit them" | Consequence-clarity and reassurance are content judgments | A10 |
| One thing per page: start form design with each question on its own page — "low-confidence users find them easier to use; they work well on mobile devices; they're better at handling things like errors, branches, loops and saving progress" | Whether to merge questions is a research-driven decision | A12 |
| Dyslexia: "Use images and diagrams to support text"; "Don't rely on accurate spelling. Use autocorrect or provide suggestions"; "Don't force users to remember things from previous pages" | Requires content/flow design, not markup inspection | A10 |
| Consistent, predictable navigation and component behaviour (WCAG 3.2.3/3.2.4 across a whole site) | Cross-page pattern equivalence needs human review at scale | A1, A8 |

## AI-design tells → harm to neurodivergent/disabled users

| AI tell | Harm | Source # |
|---|---|---|
| **Gradient text** (`background-clip: text` hero headlines) | Contrast is unverifiable/failing at the light stops of the gradient — SC 1.4.3 has no "average" allowance; text disappears in Windows High Contrast/forced-colors mode; extra visual noise for dyslexic and autistic readers who need "dark coloured text on a light background" | A1, A4, A9 |
| **Low-contrast grey body copy** (e.g. #999/#888 on white ≈ 2.8–3.5:1, thin 300-weight) | Fails 4.5:1 (SC 1.4.3); directly the low-vision poster's "Don't use low colour contrasts and small font size"; raises reading effort for dyslexia | A4, A10, A11 |
| **Glass blur / translucent panels** (frosted cards over images) | Text-over-variable-background makes contrast indeterminate and frequently sub-4.5:1; layered visual noise conflicts with "use simple colours" and COGA "Avoid Too Much Content" | A4, A10, A8 |
| **Autoplaying motion**: hero videos, parallax, scroll-triggered reveals, shimmer/sparkle loops | Vestibular disorders: "dizziness, nausea, migraines"; violates SC 2.2.2 if >5 s without pause and SC 2.3.3 if not disabled under `prefers-reduced-motion`; constant motion is an attention magnet that derails ADHD readers (COGA "Limit Interruptions") | A6, A1, A8 |
| **Emoji used as icons without labels** (✨🚀 bullet decorations, emoji-only buttons) | Screen readers announce literal Unicode names ("sparkles", "rocket") or garbage; meaning is idiomatic/figurative — exactly what the autism poster bans ("Don't use figures of speech and idioms"); ambiguous affordance ("Don't make buttons vague") | A10, A11 |
| **Walls of cards** (uniform 3-column card grids repeated section after section) | The card-grid version of "Don't create a wall of text": choice overload, no visual hierarchy of importance, high working-memory demand scanning equal-weight boxes; COGA "Avoid Too Much Content", "Use White Spacing" | A10, A8 |
| **Bright saturated multi-hue palettes and neon gradients** | Autism poster: "Don't use bright contrasting colours" — sensory overwhelm; BDA warns against green and red/pink combinations | A10, A9 |
| **ALL-CAPS letter-spaced micro-labels** ("EYEBROW" headings, uppercase buttons) | BDA: avoid "uppercase letters for continuous text" — uppercase removes word shape cues dyslexic readers rely on | A9 |
| **Center-justified or full-justified long copy** | BDA/WCAG 1.4.8: justified text creates "rivers" of uneven spacing; left alignment required for dyslexic readers | A9, A17 |
| **Fake-urgency patterns** (countdown timers, "only 2 left", auto-advancing carousels) | Anxiety poster: don't "rush users or set impractical time limits"; timers also trigger SC 2.2.1 obligations | A10, A7 |
| **Decorative icon-buttons with tiny hit areas** (ghost buttons, 16px icon links) | Fails SC 2.5.8 24px minimum and platform 44pt/48dp minima; motor-disability poster: don't "demand precision" or "bunch interactions together" | A3, A13, A11 |
| **Novel/unpredictable interaction patterns** (hover-only reveals, custom scroll-jacking) | Breaks COGA "Use a Familiar Hierarchy and Design" and predictability needs of autistic users; hover-only content also fails SC 1.4.13 | A8, A10 |

## Evidence-status notes

- **Dyslexia fonts are NOT evidence-supported.** Rello & Baeza-Yates (ACM ASSETS 2013), eye-tracking study of 48 dyslexic readers aged 11–50 reading 12 typefaces: "reading performance was best with sans serif, monospaced, and roman fonts" — Helvetica, Courier, Arial, Verdana and CMU performed best; "use of the OpenDyslexic font did not enhance text readability or reading speed", and participants preferred standard fonts; the authors "cautioned against the use of italic texts." — A15. Wery & Diliberto (2017): OpenDyslexic vs Arial/Times New Roman "actually reduced reading speed and accuracy", and children preferred the mainstream fonts. Kuster et al. (2018) on Dyslexie: "does not have the desired effect" — no accuracy or speed gains. — A16. The BDA itself does not require a special dyslexia font; it recommends ordinary sans serifs (Arial, Verdana, Tahoma, Calibri, Open Sans) with generous size and spacing — A9. **Practical rule: ship a plain sans serif with 16px+/1.5 line-height; do not default to OpenDyslexic; spacing and layout matter more than glyph shape.**
- **APCA is NOT a compliance standard.** APCA is a candidate contrast model for WCAG 3, which is an early Working Draft: "These guideline drafts should not be considered as final content of WCAG 3.0." For legal/policy conformance "you cannot rely on APCA for compliance (simply because it does not exist in WCAG 2)." — A14. **Practical rule: conformance = WCAG 2.x ratios (4.5:1 / 3:1 / 7:1); APCA may be used additionally as a design-time perceptual check (e.g. flagging light-grey-on-white that technically passes 2.x, or dark-mode pairs that 2.x mis-scores), never as the pass/fail gate.**
- **COGA "Content Usable" is a W3C Working Group Note, not a normative standard** — it supplements WCAG for cognitive accessibility and carries no conformance levels; treat its patterns as strongly recommended heuristics validated with users with cognitive disabilities. — A8.
- **The Home Office posters are heuristics from practitioner experience** (published to "highlight what good (and bad) design looks like"), not controlled studies; same for GDS "one thing per page", where the author acknowledges no formal A/B data. — A11, A12.

---

# Part B — Docs for neurodivergent and non-technical users

## Sources

| # | Title | Org | Date/version | URL |
|---|-------|-----|--------------|-----|
| B1 | Federal Plain Language Guidelines / Plain language guide series (plainlanguage.gov, now hosted on Digital.gov) | U.S. General Services Administration / PLAIN | Guidelines Mar 2011; site migrated to digital.gov | https://digital.gov/guides/plain-language (formerly https://www.plainlanguage.gov/guidelines/) |
| B2 | "Clear and short" — plain language writing guide | Digital.gov (PLAIN) | current | https://digital.gov/guides/plain-language/writing/clear-short |
| B3 | "Sentence length: why 25 words is our limit" | Inside GOV.UK (Sara Vincent, GDS) | 4 Aug 2014 | https://insidegovuk.blog.gov.uk/2014/08/04/sentence-length-why-25-words-is-our-limit/ |
| B4 | Writing for GOV.UK / GOV.UK writing guidelines (content design guidance) | GDS | ongoing | https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/ |
| B5 | Readability — Home Office User-Centred Design Manual | UK Home Office | current | https://design.homeoffice.gov.uk/accessibility/written-content/readability |
| B6 | Error-Message Guidelines | Nielsen Norman Group (Tim Neusesser & Evan Sunwall) | 14 May 2023 | https://www.nngroup.com/articles/error-message-guidelines/ |
| B7 | The Inverted Pyramid: Writing for Comprehension | Nielsen Norman Group (Amy Schade) | 11 Feb 2018 | https://www.nngroup.com/articles/inverted-pyramid/ |
| B8 | Inclusive Design for Cognition Guidebook | Microsoft Inclusive Design | 2023 | https://inclusive.microsoft.design/tools-and-activities/InclusiveDesignForCognitionGuidebook.pdf |
| B9 | Designing for users with anxiety (poster) | UK Home Office | 2016+ | https://ukhomeoffice.github.io/accessibility-posters/anxiety |
| B10 | Designing for users with dyslexia (poster) | UK Home Office | 2016+ | https://ukhomeoffice.github.io/accessibility-posters/dyslexia |
| B11 | COGA Content Usable (Objectives 4, 5, 6, 7 apply directly to documentation) | W3C | 29 Apr 2021 | https://www.w3.org/TR/coga-usable/ |
| B12 | Plain Writing Act of 2010 (statutory basis) | U.S. Congress, via Digital.gov principles page | 2010 | https://digital.gov/guides/plain-language/principles |

## Concrete rules

1. **Lead with the point (TL;DR first / inverted pyramid).** "The most important information (or what might even be considered the conclusion) is presented first"; "readers can stop reading at any point on the page and still come away with the main point." *Example:* start a setup guide with "**TL;DR — install X, run `x init`, paste your key. Takes about 5 minutes.**" — B7; also Federal PL "organize to serve the reader — most important first" — B1.
2. **Sentences ≤ 25 words.** GOV.UK's hard limit; cited comprehension research: at 14 words readers understand "more than 90% of what they're reading"; at 43 words comprehension "dropped below 10 percent." *Example:* split "After you have installed the client, which requires administrator rights, you should configure..." into "Install the client. You need administrator rights. Then configure..." — B3.
3. **One idea per sentence; one topic per paragraph.** "Express only one idea in each sentence"; "Limit each paragraph or section to one topic"; paragraphs "of no more than 150 words in three to eight sentences" and "never ... longer than 250 words." — B2.
4. **Write for a reading age of about 9, even for experts.** "Usually we recommend writing for a maximum reading age of 9, even if you are writing for a specialist audience"; "Simple language doesn't mean dumbing down – short, clear sentences are easier to understand for everyone." Complicated words are a barrier "for users with learning disabilities or cognitive issues; users with lower reading ability; users whose first language is not English." Tools: Hemingway Editor, Word's readability checker (Flesch-Kincaid). *Target: US grade ~6 or below for public-facing docs.* — B5, B4.
5. **Active voice, present tense, address the reader as "you".** "Active voice makes it clear who should do what. It eliminates ambiguity about responsibilities"; "The present tense makes your writing simpler, more direct, and more forceful." Avoid hidden verbs (-ment/-tion nominalizations). *Example:* "You must submit the form" not "The form must be submitted." — B1.
6. **Numbered steps, one action per step, in the order performed.** COGA: "Make Each Step Clear"; plain-language design guidance favours vertical lists for procedures. *Example:* "3. Click **Save**." — never "Click Save after choosing a folder and confirming your name is correct" (three actions hidden in one step). — B11, B1.
7. **Tell users what they'll see after each significant action ("what you'll see" confirmations).** Anxiety poster: "Explain what will happen after completing a service"; don't "leave users confused about next steps or timeframes"; "Let users check their answers before they submit them." *Example:* after an install step add: "*You'll see 'Setup complete' and the app icon appears in your menu bar. This can take up to a minute.*" — B9.
8. **Error messages: say what happened, in human words, and what to do next.** "Avoid technical jargon and use language familiar to your users"; generic "An error occurred" lacks context; "offer solutions, not just problems"; never phrase errors so they blame users; "preserve the user's input" so people fix rather than retype. *Example:* "We couldn't save your file because the disk is full (error 507). Free up space, then select File > Save again. Your work is still open." — B6.
9. **Don't make readers remember things between pages/steps.** Dyslexia poster: "Don't force users to remember things from previous pages - give reminders and prompts." COGA Objective 6: "Ensure processes do not rely on memory." *Example:* restate the value ("the API key you copied in step 2") instead of "the key from earlier." Mirrors WCAG 3.3.7 Redundant Entry for forms. — B10, B11.
10. **Chunk with informative, front-loaded headings and generous white space.** COGA: "Break media into chunks", "Use White Spacing", "Avoid Too Much Content"; each paragraph should "start with a topic sentence." *Example:* heading "Install on Windows" (keyword first), not "Notes concerning how one might proceed with installation on Windows." — B11, B2.
11. **No idioms, no figurative language, no unexplained jargon or abbreviations.** Autism poster: "Don't use figures of speech and idioms." Define every technical term at first use, or link a short glossary. *Example:* "kill the process (stop the running program)" → better: just "stop the program." — A10 (poster set), B1.
12. **Give time estimates and prerequisites up front.** Anxiety guidance: don't "rush users"; make consequences clear before actions. *Example:* "Before you start — you need: an admin account, ~10 minutes, the installer file (120 MB)." — B9.
13. **Make help easy to reach from within the doc.** Anxiety poster: don't "make support or help hard to access"; COGA Objective 7 "Provide help and support"; put the same "Get help" link in the same place on every page (WCAG 3.2.6). — B9, B11, A1.
14. **Design for cognition: motivation must outweigh load.** Microsoft: "For any task to be successful, motivation must equal or surpass cognitive load"; design for five demands — learning, focus, decision-making, recall, communication; "solve for one, extend to many." Practical reading: every extra decision, tab, or cross-reference in a doc is load — cut or default it. — B8.
15. **Test the docs with real users, including people with cognitive disabilities.** Plain Writing Act requires audience-appropriate writing; PLAIN's fourth pillar is "Test for understanding"; Microsoft: "co-create with cognitive diversity"; COGA: involve people with cognitive disabilities throughout. — B12, B1, B8, B11.
16. **Prefer paths of one decision.** GDS "one thing per page" applies to instructions too: one question or one branch at a time; if platforms differ, give separate sections ("On Windows / On Mac") rather than interleaved conditionals. — A12.

## Short template for a setup-guide page

```markdown
# Set up [Product] on [Platform]

**TL;DR:** Install [Product], sign in, and connect your account.
Takes about 10 minutes. No coding needed.

## Before you start
You need:
- [ ] A [Product] account (free) — [create one here](#)
- [ ] Admin rights on your computer
- [ ] About 10 minutes

## Steps

1. **Download the installer.**
   Go to [example.com/download](#) and select **Download for [Platform]**.
   *You'll see:* a file called `product-setup.exe` in your Downloads folder.

2. **Run the installer.**
   Double-click `product-setup.exe`, then select **Install**.
   *You'll see:* a progress bar, then "Installation complete". This takes 1–2 minutes.

3. **Sign in.**
   Open [Product] and enter the email and password for your [Product] account
   (the account from "Before you start").
   *You'll see:* your name in the top-right corner.

4. **Connect your account.**
   Select **Settings**, then **Connect**, then **Allow**.
   *You'll see:* "Connected" with a green tick.

## You're done
[Product] is ready. Next, you can [do first useful thing](#).

## If something goes wrong
- **"Installation failed" message** — you may not have admin rights.
  Ask your IT team to run the installer, then continue from step 3.
- **Can't sign in** — reset your password at [example.com/reset](#).
  Your setup so far is saved; nothing is lost.

## Get help
Email [support@example.com](#) or use live chat (bottom-right of every page).
We reply within 1 working day.
```

Why this shape: TL;DR first (B7); prerequisites and time up front (B9); numbered one-action steps (B11, B1); "*You'll see*" confirmation after every step (B9); no memory reliance — the account is re-referenced explicitly (B10); errors say what happened and what to do next, and reassure that work is preserved (B6); help is at a consistent, easy-to-find place (B9, A1 SC 3.2.6); sentences under 25 words (B3); reading age ≈ 9 (B5).

## Gaps

- **ADHD-specific guidance has no dedicated standard.** WCAG, COGA and the poster set cover attention indirectly ("Help users focus", "Limit Interruptions", chunking); there is no Home Office ADHD poster and little peer-reviewed guidance specific to ADHD readers of documentation — current practice extrapolates from cognitive-load and dyslexia research.
- **plainlanguage.gov link rot.** The canonical guidelines URLs now 302-redirect to digital.gov guide pages; the classic "Federal Plain Language Guidelines" PDF is no longer directly served from plainlanguage.gov. Cite digital.gov paths for durability.
- **Non-normative status.** COGA Content Usable is a W3C Note and the Home Office posters/GDS blogs are practitioner heuristics — valuable, but they carry no conformance requirement and mostly lack controlled-study evidence (GDS explicitly concedes no A/B data for one-thing-per-page).
- **No AA-level numeric rule for line length or line spacing in WCAG.** 80-char/1.5-line-spacing limits sit at AAA (SC 1.4.8) and in the BDA guide; teams targeting only AA can legally ship 120-character lines. Recommend adopting 45–75ch (≤ 70ch) as a house rule anyway.
- **Contrast science in flux.** WCAG 2.x ratios are known to over-penalize some dark-mode pairs and under-penalize thin light-grey text; APCA addresses this but is not yet standardized (WCAG 3 timeline uncertain). Until then, dual-check: WCAG 2.x for conformance, APCA as advisory.
- **Dyslexia-font research is limited in scale** (48 participants in Rello & Baeza-Yates; small samples in Wery & Diliberto and Kuster) and language-specific (Spanish, Dutch, English); the robust finding is the *absence* of benefit from special fonts, not a precise ranking of ordinary ones.
- **Readability formulas are proxies.** Flesch-Kincaid/Hemingway measure sentence and word length, not clarity of meaning, ordering, or idiom use — passing a grade target does not guarantee a document is usable by autistic or non-technical readers; only user testing does (B5, B8, B12).
