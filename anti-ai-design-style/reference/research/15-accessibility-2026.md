# 15 — Accessibility and neurodivergence guidance, 2026 sweep

**Topic:** Current accessibility and neurodivergence guidance, for (a) thresholds the skill enforces on designs it checks, and (b) how the skill's own docs should be written for non-technical "vibe coders" and neurodivergent readers.

**Date of sweep:** 2026-09-05.

**Route used:** The Exa MCP server was **not** authorized in this session. All research done with **WebSearch + WebFetch** only.

**Sources actually opened (WebFetch returned content):**
w3.org/TR/WCAG22/ · w3.org/WAI/WCAG22/errata/ · Understanding pages for 1.4.3, 1.4.10, 1.4.11, 1.4.12, 2.3.3, 2.4.13, 2.5.5, 2.5.8 · w3.org/TR/wcag-3.0/ · w3.org/TR/coga-usable/ · w3.org/TR/2026/DNOTE-coga-research-modules-20260205/ · guidance.publishing.service.gov.uk (clear-language) · insidegovuk.blog.gov.uk (sentence length) · gov.uk GOV.UK content principles · design.homeoffice.gov.uk readability · designnotes.blog.gov.uk validation messages · PMC5629233 (Wery & Diliberto) · PMC5934461 (Kuster et al.) · PMC7188700 (Galliussi et al.) · ukhomeoffice.github.io/accessibility-posters/ (index page only) · daringfireball.net (commentary only, no new evidence).

**Would not load:**
- `https://design-system.service.gov.uk/components/error-message/` and `/patterns/validation/` — WebFetch returned no output on two attempts. GOV.UK Design System error-message rules below are therefore taken from the GDS design-notes blog (X47) and search index summaries, and are marked as such.
- `https://www.pnas.org/doi/10.1073/pnas.1205566109` (Zorzi et al. 2012) — HTTP 403. Listed as X50 with the explicit caveat that only the search-index summary was seen, not the paper.
- `https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/` — loaded but is a navigation hub with no rules; the rules live on `/clear-language/` (X43).

---

## Source table

| ID | Title | Publisher | Status | Date | URL |
|---|---|---|---|---|---|
| X30 | Web Content Accessibility Guidelines (WCAG) 2.2 | W3C | **W3C Recommendation** (normative) | 12 December 2024 | https://www.w3.org/TR/WCAG22/ |
| X31 | WCAG 2.2 Errata | W3C WAI | Errata list (editorial only) | latest entries 17 August 2026 | https://www.w3.org/WAI/WCAG22/errata/ |
| X32 | Understanding SC 1.4.3 Contrast (Minimum) | W3C WAI | Understanding doc (**non-normative**, quotes normative SC text) | WCAG 2.2 series | https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html |
| X33 | Understanding SC 1.4.11 Non-text Contrast | W3C WAI | Understanding doc (non-normative) | WCAG 2.2 series | https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html |
| X34 | Understanding SC 2.5.8 Target Size (Minimum) | W3C WAI | Understanding doc (non-normative) | WCAG 2.2 series | https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html |
| X35 | Understanding SC 2.5.5 Target Size (Enhanced) | W3C WAI | Understanding doc (non-normative) | WCAG 2.2 series | https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html |
| X36 | Understanding SC 2.4.13 Focus Appearance | W3C WAI | Understanding doc (non-normative) | WCAG 2.2 series | https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html |
| X37 | Understanding SC 1.4.10 Reflow | W3C WAI | Understanding doc (non-normative) | WCAG 2.2 series | https://www.w3.org/WAI/WCAG22/Understanding/reflow.html |
| X38 | Understanding SC 1.4.12 Text Spacing | W3C WAI | Understanding doc (non-normative) | WCAG 2.2 series | https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html |
| X39 | Understanding SC 2.3.3 Animation from Interactions | W3C WAI | Understanding doc (non-normative) | WCAG 2.2 series | https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html |
| X40 | W3C Accessibility Guidelines (WCAG) 3.0 | W3C | **Working Draft** (not a standard) | 3 March 2026 | https://www.w3.org/TR/wcag-3.0/ |
| X41 | Making Content Usable for People with Cognitive and Learning Disabilities | W3C COGA TF / APA WG / AG WG | **W3C Working Group Note** (non-normative) | 29 April 2021 | https://www.w3.org/TR/coga-usable/ |
| X42 | Cognitive Accessibility Research Modules | W3C APA WG (COGA TF) | **Group Note Draft** (non-normative) | 5 February 2026 | https://www.w3.org/TR/2026/DNOTE-coga-research-modules-20260205/ |
| X43 | Use clear language (GOV.UK content and publishing guidance) | UK Government Digital Service | Government guidance | current (fetched 2026-09-05) | https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/ |
| X44 | Sentence length: why 25 words is our limit | Inside GOV.UK (GDS) | Government blog post | 4 August 2014 | https://insidegovuk.blog.gov.uk/2014/08/04/sentence-length-why-25-words-is-our-limit/ |
| X45 | GOV.UK content principles: conventions and research background | GDS | Government publication (research synthesis) | published, ongoing | https://www.gov.uk/government/publications/govuk-content-principles-conventions-and-research-background/govuk-content-principles-conventions-and-research-background |
| X46 | Readability — Home Office User-Centred Design Manual | UK Home Office | Government design-manual guidance | current | https://design.homeoffice.gov.uk/accessibility/written-content/readability |
| X47 | Exploring validation messages | GDS Design Notes | Government blog post (user research) | 14 November 2013 | https://designnotes.blog.gov.uk/2013/11/14/exploring-validation-messages/ |
| X48 | The effect of a specialized dyslexia font, OpenDyslexic, on reading rate and accuracy | Wery & Diliberto, *Annals of Dyslexia* 67(2) 114–127 | Peer-reviewed study | 2016/2017 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5629233/ |
| X49 | Dyslexie font does not benefit reading in children with or without dyslexia | Kuster, van Weerdenburg, Gompel & Bosman, *Annals of Dyslexia* 68(1) 25–42 | Peer-reviewed study | 2017/2018 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5934461/ |
| X50 | Extra-large letter spacing improves reading in dyslexia | Zorzi et al., *PNAS* | Peer-reviewed study — **page would not load (403); summary only** | 4 June 2012 | https://www.pnas.org/doi/10.1073/pnas.1205566109 |
| X51 | Inter-letter spacing, inter-word spacing, and font with dyslexia-friendly features | Galliussi, Perondi, Chia, Gerbino & Bernardis, *Annals of Dyslexia* 70(1) 141–152 | Peer-reviewed study | 2020 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7188700/ |
| X52 | Designing for accessibility posters (index) | UK Home Office Digital, Data and Technology | Practitioner guidance (posters; index page only opened) | undated | https://ukhomeoffice.github.io/accessibility-posters/ |

---

## Per-source entries

### X30 — Web Content Accessibility Guidelines (WCAG) 2.2
- **Source:** W3C, W3C Recommendation (normative), 12 December 2024. https://www.w3.org/TR/WCAG22/
- **Context:**
  - Header reads "This version: https://www.w3.org/TR/2024/REC-WCAG22-20241212/" and "W3C Recommendation, 12 December 2024". The first WCAG 2.2 Recommendation was 5 October 2023; 12 Dec 2024 is the current dated version. **There is no 2025 or 2026 republication.**
  - The header notes "Errata exists" and links to X31.
  - A search-index result stated WCAG 2.2 is also an ISO standard (ISO/IEC 40500) tracking an earlier snapshot. **Not verified — no ISO or W3C page confirming this was opened.** Cite W3C's dated Recommendation for numbers regardless.
  - Only the SC text in this document is normative. Understanding documents and Techniques are informative.
- **Tags:** `[ADOPT: cite WCAG 2.2 as "W3C Recommendation, 12 December 2024"]`
- **Feeds:** Version string in `reference/accessibility.md`; every threshold in the checker.

### X31 — WCAG 2.2 Errata
- **Source:** W3C WAI, errata list, latest entries dated 17 August 2026. https://www.w3.org/WAI/WCAG22/errata/
- **Context:**
  - 15 entries listed as "since current publication" with the 2026-08-17 date, plus 9 entries logged against the October 2023 publication (dated Nov 2024).
  - All entries are classified **Editorial Errata** — terminology consistency, definition ordering, grammar, harmonising the word "breakpoint", the wording of the motion-animation definition.
  - **No erratum changes any numeric threshold in any success criterion.** Substantive corrections would be marked as such and "not to be considered normative until a new Recommendation is published".
  - An errata date is not a republication date: the Recommendation is still 12 December 2024 (X30).
- **Tags:** `[ADOPT: no threshold changes; keep current numbers]` `[EVIDENCE-ONLY]`
- **Feeds:** Re-verification of every number in `reference/accessibility.md`.

### X32 — Understanding SC 1.4.3 Contrast (Minimum)
- **Source:** W3C WAI, Understanding document (non-normative, quoting normative SC), WCAG 2.2 series. https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- **Context:**
  - Normative SC 1.4.3 (Level AA): text and images of text have "a contrast ratio of at least 4.5:1", except Large Text at "3:1", Incidental text, and Logotypes.
  - "large scale (text)" is defined as "at least 18 point or 14 point bold" or an equivalent for CJK.
  - Point/pixel conversion given by W3C: "1pt = 1.333px, therefore 14pt and 18pt are equivalent to approximately 18.5px and 24px". Exact arithmetic is 14 × 1.333 = 18.662px; a checker should use the stricter 18.66px, not 18.5px.
  - Explicit no-rounding rule: computed values "should not be rounded (e.g., 4.499:1 would not meet the 4.5:1 threshold)".
- **Tags:** `[ADOPT: 4.5:1 / 3:1, no rounding, large-text boundary 24px or 18.66px bold]`
- **Feeds:** Contrast check; the "do not round" rule in the checker's comparison logic.

### X33 — Understanding SC 1.4.11 Non-text Contrast
- **Source:** W3C WAI, Understanding document, WCAG 2.2 series. https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- **Context:**
  - Level AA. Requires "a contrast ratio of at least 3:1 against adjacent color(s)" for two categories.
  - User Interface Components: "Visual information required to identify user interface components and states", except inactive components, or where appearance is "determined by the user agent and not modified by the author".
  - Graphical Objects: "Parts of graphics required to understand the content", except where a particular presentation "is essential to the information being conveyed".
  - Consequence for a checker: a default, unstyled browser control is exempt; a custom-styled input border, custom checkbox, icon-only button, or chart series colour is not.
- **Tags:** `[ADOPT: 3:1 with the author-modified test as the trigger]`
- **Feeds:** Non-text contrast check; exempting user-agent default controls to avoid false positives.

### X34 — Understanding SC 2.5.8 Target Size (Minimum)
- **Source:** W3C WAI, Understanding document, WCAG 2.2 series. https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- **Context:**
  - Level AA: "The size of the target for pointer inputs is at least 24 by 24 CSS pixels, except when:".
  - Spacing exception (verbatim, the part a checker must implement): "if a 24 CSS pixel diameter circle is centered on the bounding box of each, the circles do not intersect another target or the circle for another undersized target".
  - Other exceptions: Equivalent function elsewhere on the page, Inline targets (in a sentence or block of text), User Agent Control, Essential.
  - Note that "24 by 24 CSS pixels" is the AA floor, not a design recommendation; 2.5.5 (X35) is the AAA figure.
- **Tags:** `[ADOPT: 24×24 CSS px + the spacing-circle rule]`
- **Feeds:** Target-size check; inline-link exemption so body-text links do not generate noise.

### X35 — Understanding SC 2.5.5 Target Size (Enhanced)
- **Source:** W3C WAI, Understanding document, WCAG 2.2 series. https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html
- **Context:**
  - Level **AAA**: "The size of the target for pointer inputs is at least 44 by 44 CSS pixels", with Equivalent, Inline, User Agent Control and Essential exceptions.
  - There is no Spacing exception at AAA — unlike 2.5.8, closely spaced small targets cannot be excused.
  - Platform HIG minima (Apple 44pt, Material 48dp) are vendor guidance, not WCAG; do not present them as conformance requirements.
- **Tags:** `[ADOPT: 44×44 as an advisory AAA target, labelled AAA]`
- **Feeds:** The "aim for 44" advice in `accessibility.md` — must be labelled AAA/advisory, not AA.

### X36 — Understanding SC 2.4.13 Focus Appearance (and 2.4.11 / 2.4.12)
- **Source:** W3C WAI, Understanding document, WCAG 2.2 series. https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html
- **Context:**
  - 2.4.13 Focus Appearance, Level **AAA**: the indicator area "is at least as large as the area of a 2 CSS pixel thick perimeter of the unfocused component"; and it "has a contrast ratio of at least 3:1 between the same pixels in the focused and unfocused states".
  - Exceptions: the indicator is user-agent determined and not author-adjustable, or neither the indicator nor its background colour is author-modified.
  - 2.4.11 Focus Not Obscured (Minimum), Level **AA**: a focused component "is not entirely hidden due to author-created content". 2.4.12 Focus Not Obscured (Enhanced) is the AAA version (no part obscured).
  - Separately, SC 2.4.7 Focus Visible is the Level AA requirement that a visible focus indicator exists at all. The 2px/3:1 numbers are AAA and must not be quoted as AA.
- **Tags:** `[ADOPT: 2 CSS px perimeter + 3:1 state change, labelled AAA]`
- **Feeds:** Focus-indicator check; the sticky-header/cookie-banner obstruction check (AA).

### X37 — Understanding SC 1.4.10 Reflow
- **Source:** W3C WAI, Understanding document, WCAG 2.2 series. https://www.w3.org/WAI/WCAG22/Understanding/reflow.html
- **Context:**
  - Level AA: content presented "without requiring scrolling in two dimensions" for "Vertical scrolling content at a width equivalent to 320 CSS pixels" and "Horizontal scrolling content at a height equivalent to 256 CSS pixels".
  - Exception: "parts of the content which require two-dimensional layout for usage or meaning" (data tables, maps, code, some diagrams).
  - W3C states the 320px width is equivalent to a 1280 CSS pixel viewport at 400% zoom — a checker can emulate either.
  - The skill's existing text cites only the 320 value; the 256 height value is equally normative.
- **Tags:** `[ADOPT: 320 CSS px width AND 256 CSS px height]`
- **Feeds:** Reflow check; add the 256px-height case, currently missing.

### X38 — Understanding SC 1.4.12 Text Spacing
- **Source:** W3C WAI, Understanding document, WCAG 2.2 series. https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html
- **Context:**
  - Level AA. No loss of content or functionality when the user sets, and changes nothing else:
  - "Line height (line spacing) to at least 1.5 times the font size".
  - "Spacing following paragraphs to at least 2 times the font size"; "Letter spacing (tracking) to at least 0.12 times the font size"; "Word spacing to at least 0.16 times the font size".
  - Exception for languages and scripts that do not use one or more of these properties.
  - This is a **robustness** requirement (the page must survive injection of those values) — it is not an instruction to ship 1.5 line-height. Shipping 1.5 is separate typographic advice (BDA), not SC 1.4.12.
- **Tags:** `[ADOPT: inject the four values, then assert no clipping/overlap]`
- **Feeds:** Text-spacing check; correcting the common conflation of "must survive 1.5" with "must be 1.5".

### X39 — Understanding SC 2.3.3 Animation from Interactions
- **Source:** W3C WAI, Understanding document, WCAG 2.2 series. https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
- **Context:**
  - Level **AAA**: "Motion animation triggered by interaction can be disabled, unless the animation is essential to the functionality or the information being conveyed."
  - `prefers-reduced-motion` appears as **sufficient techniques** C39 (CSS) and SCR40 (JS), plus a general technique for an in-page preference. Sufficient techniques are informative ways to satisfy the SC, not requirements in themselves.
  - Motion animation is defined around "the illusion of movement"; colour changes, blurring and opacity changes that do not affect perceived size, shape or position are excluded.
  - There is **no Level AA reduced-motion requirement** in WCAG 2.2. The Level A rule that catches most autoplaying motion is 2.2.2 Pause, Stop, Hide (moving content that starts automatically and lasts more than five seconds needs a pause/stop/hide mechanism).
- **Tags:** `[ADOPT: grep for the media query as a proxy]` `[EVIDENCE-ONLY: it is an AAA technique, not an AA conformance check]`
- **Feeds:** Reduced-motion craft flag — must be reported as "AAA technique / craft", not "WCAG AA failure".

### X40 — W3C Accessibility Guidelines (WCAG) 3.0
- **Source:** W3C, **Working Draft**, 3 March 2026. https://www.w3.org/TR/wcag-3.0/
- **Context:**
  - Status wording: "This is a draft document and may be updated, replaced, or obsoleted by other documents at any time." Publication as a Working Draft "does not imply endorsement by W3C and its Members".
  - The draft itself signals that substantial work remains before completion; it is not a candidate for conformance use in 2026.
  - Practical consequence: APCA and any WCAG 3 scoring model remain design-time aids only. Conformance in 2026 = WCAG 2.2 ratios.
  - Do not describe WCAG 3 as "coming soon" with a date — the draft gives none.
- **Tags:** `[ADOPT: WCAG 3 is a Working Draft, no conformance value]` `[CONTESTED: APCA advocacy]`
- **Feeds:** The APCA evidence warning in `reference/accessibility.md` — still correct as written.

### X41 — Making Content Usable for People with Cognitive and Learning Disabilities (COGA)
- **Source:** W3C COGA Task Force (APA WG + AG WG), **W3C Working Group Note**, 29 April 2021. https://www.w3.org/TR/coga-usable/
- **Context:**
  - Still the current published version as of this sweep: 29 April 2021, non-normative supplemental guidance beyond WCAG. No conformance levels.
  - Eight objectives, verbatim: help users understand what things are and how to use them; help users find what they need; use clear and understandable content; help users avoid mistakes and know how to correct them; help users focus; ensure processes do not rely on memory; provide help and support; support adaptation and personalization.
  - Concrete, checkable-ish patterns: a clear title or heading that summarises the page purpose; same-level headings styled identically and icons/controls with the same function looking the same; multi-step processes showing "the steps completed, the current step, the steps pending"; forms that "only give valid options"; login that does not require remembering or transcribing passwords or codes; distractions that users can "turn distractions off easily".
  - Objective 6 (memory) is the one most directly relevant to the skill's docs: restate state rather than making the reader carry it.
- **Tags:** `[ADOPT: patterns as heuristics]` `[EVIDENCE-ONLY: Note status, no conformance claim]`
- **Feeds:** The judgment-call list in `accessibility.md`; the docs rules in section 5 below.

### X42 — Cognitive Accessibility Research Modules
- **Source:** W3C APA WG (COGA TF), **Group Note Draft**, 5 February 2026. https://www.w3.org/TR/2026/DNOTE-coga-research-modules-20260205/
- **Context:**
  - Explicitly non-normative: "Group Note Drafts are not endorsed by W3C nor its Members".
  - Contains "a detailed analysis of accessibility issues for people with disabilities that may require cognitive accessibility supports, user needs, areas for further research, and directions for solutions".
  - Current live modules cover voice systems, indoor navigation, online safety and wellbeing, and supported decision-making; eleven older modules are deprecated.
  - Stated to be "used as source material for Making Content Usable" — i.e. COGA work is active in 2026 even though the published Making Content Usable Note is still the 2021 edition.
- **Tags:** `[EVIDENCE-ONLY]`
- **Feeds:** Status line for COGA; a watch item for a future Making Content Usable revision.

### X43 — Use clear language (GOV.UK content and publishing guidance)
- **Source:** UK Government Digital Service, government guidance, fetched 2026-09-05. https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/
- **Context:**
  - "Try to split up sentences that are over 25 words long."
  - "Paragraphs should have no more than 5 sentences each."
  - Literacy evidence cited as the reason: "1 in 6 adults in England have very poor literacy skills"; 1 in 4 in Scotland; 1 in 8 in Wales; 1 in 5 in Northern Ireland.
  - Plain-English preference evidence cited: "80% of people preferred sentences written in clear English", and the preference is *greater* among more educated, more specialist readers — plain language is not dumbing down.
  - No reading-age target was present in the fetched content of this page. Note the discrepancy: the search index attributes both "write for a 9 year old reading age" and the "around 5,000 words" vocabulary claim to this same guidance site, so the target may live on a sibling page that was not opened. The verified reading-age statement in this sweep is the Home Office one (X46).
- **Tags:** `[ADOPT: 25-word sentence cap, 5-sentence paragraph cap]` `[EVIDENCE-ONLY: the 80% figure is cited by GDS without a linked primary study on this page]`
- **Feeds:** `copy_check.py` sentence-length rule; adds a paragraph-length rule the skill does not yet have.

### X44 — Sentence length: why 25 words is our limit
- **Source:** Inside GOV.UK (GDS), government blog post, 4 August 2014. https://insidegovuk.blog.gov.uk/2014/08/04/sentence-length-why-25-words-is-our-limit/
- **Context:**
  - The rule: "if you have sentences longer than 25 words, try to break them up or condense them".
  - The comprehension claim, attributed to Ann Wylie: "when average sentence length is 14 words, readers understand more than 90% of what they're reading. At 43 words, comprehension dropped below 10 percent."
  - Difficulty banding quoted: 11 words easy, 21 words fairly difficult, 25 words difficult, 29+ words very difficult.
  - The post cites a consultant's restatement, not a locatable peer-reviewed study. The **rule** is a defensible convention; the **percentages** should not be presented as research findings.
- **Tags:** `[ADOPT: 25-word cap]` `[CONTESTED: the 90%/10% comprehension figures]`
- **Feeds:** `copy_check.py` — keep the 25-word flag, delete or re-caveat the "comprehension drops below 10% at 43 words" comment in the script header.

### X45 — GOV.UK content principles: conventions and research background
- **Source:** GDS, government publication (research synthesis). https://www.gov.uk/government/publications/govuk-content-principles-conventions-and-research-background/govuk-content-principles-conventions-and-research-background
- **Context:**
  - This is a synthesis of external research, not original GOV.UK experiments: it cites Nielsen Norman (2006) on F-shaped scanning, Delin (2005), Peters et al. (2006, 2007) on low numeracy.
  - Finding relevant to docs written for stressed or low-literacy readers: low-literacy users read "word by word rather than scanning" — long paragraphs are disproportionately costly for them.
  - Counter-finding worth keeping honest: Delin (2005) found government participants could read over-simplified language as "too friendly" and "false" — plain does not mean chatty.
  - It gives numeracy context ("42% of UK GCSE students failed to get A*–C", 2011) but **no** reading-age target, sentence-length number, or vocabulary-size benchmark.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED: the "5,000 common words by age 9" claim is repeated widely but is not sourced on this page]`
- **Feeds:** Justification (or lack of it) for the reading-grade target; the "no forced chattiness" rule for docs voice.

### X46 — Readability — Home Office User-Centred Design Manual
- **Source:** UK Home Office, government design-manual guidance, current. https://design.homeoffice.gov.uk/accessibility/written-content/readability
- **Context:**
  - The target, verbatim: "Usually we recommend writing for a maximum reading age of 9, even if you are writing for a specialist audience."
  - **Reading age 9 is a UK reading age, roughly US grade 4** — it is not "grade 9". The skill's `grade 9` target is a Flesch-Kincaid grade level (roughly age 14–15), about five school years easier said than the UK guidance.
  - The page references Flesch-Kincaid Grade Level and a conversion table for Word's reading-age output, i.e. the reading-age number is derived from a grade-level formula, not measured with readers.
  - No empirical data, percentages or literacy statistics are cited on this page — it is stated policy, not a study.
- **Tags:** `[ADOPT: state which scale a target is on]` `[CONTESTED: a specific cutoff number]`
- **Feeds:** Section 5 below; the mislabelled comment in `scripts/copy_check.py`.

### X47 — Exploring validation messages (GDS Design Notes)
- **Source:** GDS Design Notes, government blog post with user research, 14 November 2013. https://designnotes.blog.gov.uk/2013/11/14/exploring-validation-messages/
- **Context:**
  - Pattern tested: "errors are first grouped at the top of the page in a summary and then markers are placed next to the incorrectly completed fields".
  - Research finding: "In research users scrolled rather than clicking the links, but it is good accessibility with screen readers" — the summary earns its place for assistive-tech users, not because sighted users use the anchors.
  - Implementation detail from the same work: `tabindex="-1"` plus `.focus()` on the error-summary container so screen readers announce it.
  - Related finding: keeping page sections small (one thing per page, as in the Register to Vote exemplar) made "validation messages very easy to connect to the fields".
- **Tags:** `[ADOPT: error summary + inline message + focus move]` `[EVIDENCE-ONLY: small qualitative sample, 2013]`
- **Feeds:** Form/error-state checks; the "design the error state" rule (JD2 tell in the register).

### X48 — Wery & Diliberto: OpenDyslexic and reading rate/accuracy
- **Source:** Wery, J.J. & Diliberto, J.A., *Annals of Dyslexia* 67(2), 114–127, 2016/2017 (peer-reviewed). https://pmc.ncbi.nlm.nih.gov/articles/PMC5629233/
- **Context:**
  - Sample: **12** elementary students, grades 3–6, with diagnosed dyslexia. Single-subject alternating-treatment design; three tasks (letter naming, real-word decoding, nonsense-word decoding).
  - Result: OpenDyslexic "decreased students' outcomes compared to both Arial and TNR, on all three reading tasks", with fluency effect sizes from −88.65% to −49.65% and accuracy effects −73.53% to −63.62%.
  - Authors' conclusion: "no evidence" that OpenDyslexic has "a positive effect on reading speed or accuracy".
  - Stated limits: comprehension of connected text was not measured, and "multiple independent studies with similar results are needed". n = 12 is small — cite it as one of several converging nulls, not as decisive on its own.
- **Tags:** `[ADOPT: do not ship a dyslexia font]` `[EVIDENCE-ONLY: small n]`
- **Feeds:** The dyslexia-font evidence warning in `reference/accessibility.md`.

### X49 — Kuster et al.: Dyslexie font does not benefit reading
- **Source:** Kuster, van Weerdenburg, Gompel & Bosman, *Annals of Dyslexia* 68(1), 25–42, 2017/2018 (peer-reviewed). https://pmc.ncbi.nlm.nih.gov/articles/PMC5934461/
- **Context:**
  - Experiment 1: **170** Dutch children with dyslexia (ages ~7–12). Experiment 2: **102** with dyslexia plus **45** without.
  - Speed/accuracy: "Reading speed between Arial and Dyslexie did not differ significantly at Times 1 and 2, both F's < 1"; in Experiment 2, "Words written in Dyslexie font were not read faster or more accurately".
  - Preference: "The majority preferred reading in Arial"; in Experiment 2 more participants preferred Arial and Times New Roman over Dyslexie.
  - "Preference was not related to reading performance" — liking a font is not evidence it helps.
- **Tags:** `[ADOPT: do not ship a dyslexia font]` `[EVIDENCE-ONLY]`
- **Feeds:** Same warning; this is the largest-sample source in the dyslexia-font set.

### X50 — Zorzi et al.: extra-large letter spacing improves reading in dyslexia
- **Source:** Zorzi et al., *PNAS*, 4 June 2012. **Page returned HTTP 403 and was not opened**; details below come from the search-index summary only and are unverified against the paper. https://www.pnas.org/doi/10.1073/pnas.1205566109
- **Context:**
  - Reported design: 54 Italian and 40 French children with dyslexia read 24 short sentences at standard vs expanded letter spacing.
  - Reported result: roughly 20% faster reading and about half as many errors, with no training — an on-the-fly spacing manipulation.
  - If this holds, it supports the practical position that **spacing is the lever, glyph redesign is not** — which is also what BDA-style guidance and WCAG 1.4.12 point at.
  - **Do not cite this number in the skill until the paper itself has been read.** It is listed here so a later sweep can verify it.
- **Tags:** `[CONTESTED: unverified in this sweep]`
- **Feeds:** Nothing yet — verification task, not an adopted rule. Note that X51 (opened, 2020) partly contradicts the simple "more spacing is better" reading of it.

### X51 — Galliussi et al.: inter-letter spacing, inter-word spacing, and dyslexia-friendly letterforms
- **Source:** Galliussi, Perondi, Chia, Gerbino & Bernardis, *Annals of Dyslexia* 70(1), 141–152, 2020 (peer-reviewed). https://pmc.ncbi.nlm.nih.gov/articles/PMC7188700/
- **Context:**
  - Sample: **128** Italian children (64 with dyslexia, 64 controls), mean age 12.4, reading 8 equivalent texts aloud. Three manipulations crossed: letterform (dyslexia-friendly features vs not), inter-letter spacing, inter-word spacing.
  - Letterform: "the data collected failed to show any effect from the letterform" — no speed or accuracy benefit, in either group. This is a **third independent null on glyph design**, and the most likely source of the circulating "2020 review" claim.
  - Inter-letter spacing increased *alone* **impaired** speed (4.12 → 4.04 syllables/second, p < 0.001); increased inter-word spacing **improved** it (4.03 → 4.12 syll/s, p < 0.001). No accuracy effects either way.
  - Headline interaction: "reading speed is impaired by an increase in inter-letter spacing not combined with an adequate increase in inter-word spacing." So spacing is a lever, but letter-spacing without matching word-spacing is a *regression* — relevant to any CSS that sets `letter-spacing` on body copy.
- **Tags:** `[ADOPT: no dyslexia font; if you widen letter-spacing, widen word-spacing more]` `[EVIDENCE-ONLY]`
- **Feeds:** Dyslexia-font warning in `reference/accessibility.md`; a new rule against tracked-out body copy; supports WCAG 1.4.12's 0.12× letter / 0.16× word ratio ordering.

### X52 — Designing for accessibility posters (Home Office)
- **Source:** UK Home Office Digital, Data and Technology, practitioner guidance, undated. https://ukhomeoffice.github.io/accessibility-posters/
- **Context:**
  - Poster set covers: Anxiety, Autistic spectrum, Deaf or hard of hearing, Dyslexia, Low vision, Physical or motor disabilities, Screenreaders. **There is no ADHD poster.**
  - Only the index page loaded; the do/don't items live in a downloadable PDF that was not opened this sweep. The autism items quoted in `06-accessibility.md` (A10/A11) are therefore not re-verified here.
  - Status: practitioner heuristics published to illustrate good and bad design, not controlled studies. Treat as craft guidance, not evidence.
- **Tags:** `[EVIDENCE-ONLY]` `[CONTESTED: no study basis]`
- **Feeds:** Autism and anxiety heuristics in `accessibility.md` — keep, but keep labelled as heuristics.

---

## Thresholds table

Precision note: all values are CSS pixels and ratios exactly as written in the normative SC text (X30, quoted via X32–X39). "Level" is the WCAG conformance level; AAA items must never be reported as conformance failures. Rows for 1.4.6, 1.4.8, 2.2.1, 2.2.2, 2.3.1, 3.3.7 and 3.3.8 were re-fetched directly from X30 in a second pass; the one exception is 1.4.8's **80-character line-length** value, which the fetch did not return and which is carried from `06-accessibility.md` (not re-verified this sweep).

| Criterion | Name | Level | Exact threshold | Source ID | Script-checkable on a rendered page? |
|---|---|---|---|---|---|
| 1.4.3 | Contrast (Minimum) | AA | ≥ **4.5:1** normal text; ≥ **3:1** for large text (≥ 18pt / ≥ 24px, or ≥ 14pt bold / ≥ 18.66px bold). No rounding: 4.499:1 fails | X32 | **Yes** — resolve computed color vs effective background per text node. Fails on gradients, images, and translucent layers behind text (report as indeterminate, not pass) |
| 1.4.6 | Contrast (Enhanced) | AAA | ≥ **7:1** normal, ≥ **4.5:1** large | X30 | Yes, same computation, different constant |
| 1.4.11 | Non-text Contrast | AA | ≥ **3:1** against adjacent colours for UI-component identity/state and for graphics needed to understand content. Exempt: inactive components; user-agent-determined appearance not modified by the author; essential presentation | X33 | **Partly** — borders and icon fills are computable; "required to identify" and "essential" need judgment. Skip unstyled native controls |
| 2.5.8 | Target Size (Minimum) | AA | ≥ **24 × 24 CSS px**, OR the spacing exception: a **24 CSS px diameter** circle centred on each undersized target's bounding box does not intersect another target or another such circle. Also exempt: equivalent control, inline text targets, user-agent control, essential | X34 | **Yes** — `getBoundingClientRect()` plus a circle-intersection test. Must implement the inline exception or body links flood the report |
| 2.5.5 | Target Size (Enhanced) | AAA | ≥ **44 × 44 CSS px**; no spacing exception | X35 | Yes — same measurement, constant 44. Report as advisory |
| 2.4.7 | Focus Visible | AA | A visible focus indicator exists (no numeric threshold) | X30 | Partly — detect `outline: none` / `outline: 0` with no replacement `:focus-visible` style |
| 2.4.11 | Focus Not Obscured (Minimum) | AA | Focused component is **not entirely hidden** by author content | X36 | **Yes** — tab through, compare focused rect against fixed/sticky layers via `elementFromPoint` |
| 2.4.12 | Focus Not Obscured (Enhanced) | AAA | **No part** of the focused component is hidden | X36 | Yes, stricter version of the same test |
| 2.4.13 | Focus Appearance | AAA | Indicator area ≥ area of a **2 CSS px thick perimeter** of the component, and ≥ **3:1** contrast between focused and unfocused states of the same pixels | X36 | **Partly** — outline width is readable from computed style; true area comparison needs pixel diffing of screenshots |
| 1.4.10 | Reflow | AA | No two-dimensional scrolling at a width equivalent to **320 CSS px** (vertical content) or a height equivalent to **256 CSS px** (horizontal content). 320px ≡ 1280px viewport at **400%** zoom. Exempt: content needing 2-D layout | X37 | **Yes** — set viewport to 320 wide (and 256 tall), assert `scrollWidth <= clientWidth`. Exempt tables, maps, code blocks |
| 1.4.12 | Text Spacing | AA | Survive, with no other change: line height ≥ **1.5×** font size; paragraph spacing ≥ **2×**; letter spacing ≥ **0.12×**; word spacing ≥ **0.16×** | X38 | **Yes** — inject the four values, then detect clipping/overlap (scrollHeight vs clientHeight on text containers, overlapping rects) |
| 1.4.8 | Visual Presentation | AAA | A mechanism achieves: line spacing "at least space-and-a-half within paragraphs", paragraph spacing "at least 1.5 times larger than the line spacing"; text not justified; line length ≤ **80 characters** (40 CJK) *(the 80-char value is carried from 06, not re-fetched)* | X30 | Yes for `ch`-width and `text-align: justify`; the skill's stricter 75ch is typographic convention, not WCAG |
| 2.3.3 | Animation from Interactions | **AAA** | Interaction-triggered motion animation can be disabled unless essential. `prefers-reduced-motion` (C39/SCR40) is a **sufficient technique**, not the requirement | X39 | **Proxy only** — grep for `@media (prefers-reduced-motion)` alongside keyframes/transitions. Absence is a craft flag at AAA, **not an AA failure** |
| 2.2.2 | Pause, Stop, Hide | **A** | Auto-starting motion lasting more than **5 seconds** and shown in parallel with other content needs pause/stop/hide | X30 | Partly — detect infinite CSS animations, autoplaying video, carousels; then look for a control |
| 2.3.1 | Three Flashes or Below Threshold | A | Nothing flashes more than **3 times in any one second** unless below the general and red flash thresholds | X30 | Partly — needs frame analysis; static analysis catches obvious cases only |
| 2.2.1 | Timing Adjustable | A | Turn off, or adjust to **≥ 10×** the default, or warn with **≥ 20 seconds** to extend and allow extending **≥ 10 times**. Exempt above **20 hours** | X30 | No — behavioural; checklist item |
| 3.3.7 | Redundant Entry | A | Previously entered information is auto-populated or selectable | X30 | Partly — detect missing `autocomplete` and repeated field names across steps |
| 3.3.8 | Accessible Authentication (Minimum) | AA | No cognitive function test in any authentication step, unless an alternative or mechanism exists | X30 | Partly — detect paste-blocking on password fields, `autocomplete="off"` on credentials |

---

## Writing for neurodivergent readers

Split into rules with evidence behind them, and rules that are widely repeated conventions. The skill's docs should follow both, but should only *claim* evidence for the first group.

### Evidence-backed

1. **Cap sentences at 25 words; cap paragraphs at 5 sentences.** GOV.UK states both as rules, and grounds them in measured literacy: "1 in 6 adults in England have very poor literacy skills" (X43). The *rule* is evidenced as policy tested at national scale; the 90%/10% comprehension figures attached to it are not (see Contested).
2. **Write plainly even for expert readers.** GDS cites "80% of people preferred sentences written in clear English", with the preference *increasing* with education and specialism (X43). This directly answers the "but my users are developers" objection.
3. **Do not build walls of paragraph text for readers who are struggling.** Low-literacy users read "word by word rather than scanning" (X45) — length costs them linearly, not sub-linearly.
4. **Show state in multi-step processes.** COGA asks for "the steps completed, the current step, the steps pending, and any important choices" to be visible (X41). For docs: number the steps and say which one the reader is on.
5. **Do not require the reader to hold things in memory.** COGA Objective 6, "ensure processes do not rely on memory" (X41); the WCAG-conformance slice of this is 3.3.7 Redundant Entry (Level A). For docs: restate the value, path, or command rather than saying "the file from step 2".
6. **Error text goes next to the thing that failed *and* in a summary, and focus moves to the summary.** GDS user research found users "scrolled rather than clicking the links" but kept the summary because "it is good accessibility with screen readers" (X47).
7. **Small units beat big ones.** GDS found that keeping page sections small made "validation messages very easy to connect to the fields" (X47) — the same argument that produced one-thing-per-page.
8. **Don't overcorrect into chattiness.** Delin (2005), via X45, found government readers could hear over-simplified language as "too friendly" and "false". Plain and warm, not cute.
9. **Let the reader turn distractions off.** COGA: users should be able to "turn distractions off easily" (X41). For docs: no autoplaying demos, no animated call-outs, no interstitials.
10. **Keep the same thing looking the same.** COGA asks that same-level headings be styled identically, and that "icons, controls, and menu items that have same function and role have the same look" (X41). For docs: one term per concept, one format per command block.

### Widely repeated, weak or absent evidence (follow if useful, do not cite as research)

- **"Comprehension is 90% at 14 words and under 10% at 43 words."** Attributed by GDS to a consultant's restatement (X44); no locatable primary study. Use the 25-word rule, drop the percentages.
- **"Reading age 9" / "grade 8" / "grade 9" as a specific cutoff.** See section 5. The Home Office states age 9 as policy with no cited data (X46).
- **"By age 9 people know ~5,000 common words."** Circulates attached to GOV.UK guidance; it is not in the content-principles research background page that was opened (X45).
- **Time estimates on docs sections ("takes 5 minutes").** Sensible for ADHD readers and widely recommended, but this sweep found no controlled evidence for it in W3C or GOV.UK sources. Keep it; label it as craft.
- **"Use sans-serif for dyslexic readers."** Consistent with the studies' comparison fonts (Arial performed well, X48/X49) but none of them tested serif-vs-sans as the research question. Reasonable default, weak direct evidence.

### Concrete testable rules for this skill's own docs

| Rule | Threshold | Basis |
|---|---|---|
| Sentence length | ≤ 25 words | X43, X44 |
| Paragraph length | ≤ 5 sentences | X43 (new — the skill does not check this yet) |
| Reading grade | state the scale used; grade 9 FK is a convention, not evidence | X46, section 5 |
| Lead with the outcome | first paragraph says what the reader gets | X41 Objective 2 |
| Restate state | never "the value from step 2" — repeat the value | X41 Objective 6 |
| One concept, one name | no synonyms for the same command or file | X41 (consistent look/role) |
| Steps numbered with position shown | "Step 3 of 5" | X41 |
| No idioms, no figurative headings | literal labels | X41 Objective 3 |
| Line length | ≤ 80 chars (WCAG AAA); 70ch house style | X30 SC 1.4.8 |
| No autoplay, no animated call-outs in docs | none | X41, X39 |

---

## Contested

1. **Dyslexia-specific fonts. The skill's existing conclusion still holds, and is now better supported.** Three peer-reviewed studies opened in this sweep found no benefit from dyslexia-font glyph design: Kuster et al., n = 170 and n = 102 + 45, found Dyslexie no faster or more accurate than Arial, most participants preferred Arial, and "preference was not related to reading performance" (X49); Galliussi et al., n = 128, "failed to show any effect from the letterform" (X51); Wery & Diliberto, n = 12, found OpenDyslexic *decreased* fluency and accuracy versus Arial and Times New Roman (X48). Honest framing: **no study shows a benefit; one shows harm; users prefer standard fonts; the evidence base is still small and entirely children.** Absence of demonstrated benefit is not proof of impossibility, but there is no basis for shipping one. The circulating "2020 Kuster systematic review" is not a document this sweep could find; the real 2020 paper is Galliussi (X51) — cite that instead. On the alternative lever: spacing helps, but **not uniformly** — X51 found increased inter-word spacing improved speed while increased inter-letter spacing alone *impaired* it. So "just add letter-spacing" is wrong; word spacing must rise with it. The larger claimed spacing effect (X50, Zorzi 2012) remains unverified — the PNAS page would not load.
2. **The Wylie sentence-length comprehension curve.** Repeated across government and industry writing guidance; no traceable primary study (X44). The 25-word rule survives on its own merits.
3. **APCA / WCAG 3 contrast.** WCAG 3.0 is a Working Draft dated 3 March 2026 that says it is "inappropriate to cite this document as other than a work in progress" (X40). APCA remains a design-time perceptual aid; conformance means WCAG 2.2 ratios. The skill's existing warning is still accurate.
4. **"44px minimum touch target" presented as a requirement.** 44 × 44 is **AAA** (2.5.5, X35); 24 × 24 is the AA floor (2.5.8, X34). Apple's 44pt and Material's 48dp are vendor guidance, not WCAG. Report the distinction or the skill will be quoting a AAA number as a legal requirement.
5. **`prefers-reduced-motion` as a "WCAG requirement".** It is a sufficient technique for a **AAA** criterion (X39). The AA/A-level lever over autoplaying motion is 2.2.2 (5 seconds, pause/stop/hide).
6. **"Reading age 9" versus "grade 9".** These are routinely used interchangeably in design writing and differ by about five school years. See below.

---

## Reading-grade targets and their justification

**Verdict: convention, not evidence — and the skill currently mislabels which convention it follows.**

- The Home Office states "a maximum reading age of 9, even if you are writing for a specialist audience" (X46). That is a UK **reading age**, roughly a US grade 4 level.
- The skill's `scripts/copy_check.py` computes **Flesch-Kincaid Grade Level** and targets **grade 9 or lower**, while its header comment justifies that with "GOV.UK guidance: aim for reading age ~9". Those are two different scales. FK grade 9 corresponds to roughly age 14–15 — about five school years easier said than the GOV.UK target. The number matches by coincidence of the digit 9, not by derivation.
- Neither GOV.UK page opened in this sweep supplies empirical support for a specific cutoff. X45 is a synthesis of external studies with no reading-age target at all; X46 states the target as recommendation and points at Flesch-Kincaid and Word's converter.
- What *is* evidenced: readability formulas track relative difficulty (sentence length and syllable counts), literacy is genuinely low in a large minority of adults (X43), and low-literacy readers read word by word (X45). What is *not* evidenced: any particular threshold — US health-communication's grade 6/grade 8, GOV.UK's age 9, and the skill's FK grade 9 are all conventions.
- Recommendation for the skill: keep FK grade 9 as a **house convention**, but (a) say "Flesch-Kincaid grade 9" explicitly wherever it appears, (b) stop citing GOV.UK reading age 9 as its justification, and (c) note that FK is a proxy — passing it does not mean the text is clear, and failing it on a page full of unavoidable technical nouns is not automatically a defect.

---

## Gaps

1. **Zorzi et al. 2012 (X50) was not read** — PNAS returned 403. The "spacing beats glyph shape" claim therefore rests on a search summary. Verify via a library copy or the PubMed record before the skill states an effect size.
2. **GOV.UK Design System pages would not load** (`design-system.service.gov.uk` error-message and validation pattern pages). The error-message rules here come from a 2013 GDS blog post; the current normative-for-GOV.UK component text, and any research added since, is unread.
3. **The dyslexia-font evidence remains child-only.** Galliussi 2020 (X51) adds a third null, but its sample is 128 children (mean age 12.4), as are X48 and X49. **No adult-sample study was found, and no study of these fonts as a user-toggleable option.** Searched: one query for Zorzi 2012, one for Galliussi 2020; not searched exhaustively for post-2020 work.
4. **COGA's applied guidance is five years old.** Making Content Usable is still the 29 April 2021 Note (X41) while research modules were redrafted 5 February 2026 (X42) and the task force is discussing renaming the document. A revision is plausible within the skill's lifetime; recheck.
5. **No evidence found either way on time estimates, TL;DR blocks, or progress indicators in documentation** specifically for ADHD readers. Widely recommended, apparently untested. This is the single largest evidence hole for purpose (b).
6. **Focus Appearance (2.4.13) area comparison is not cleanly automatable** — the perimeter-area test needs pixel diffing. The skill will have to treat it as partly manual.
7. **Contrast over gradients, images and translucent surfaces has no defined WCAG procedure.** SC 1.4.3 assumes a single background colour. A checker must report "indeterminate", and the skill should say so rather than implying gradient text has a computable pass/fail.
8. **Autism-specific guidance: no primary source opened this sweep.** Only the Home Office poster index page loaded (X52); the do/don't items are in an unopened PDF, and the poster set is practitioner heuristics rather than research. The autism material the skill relies on is still `06-accessibility.md` A10/A11, unverified here. There is also **no ADHD poster** in that set — the Home Office set covers anxiety and dyslexia but not ADHD, so the skill's ADHD claims currently have no named source at all.
9. **Nothing in this sweep covers screen-reader output quality or ARIA correctness** — out of scope for the topic assigned, but a live gap for a skill that scores accessibility.
