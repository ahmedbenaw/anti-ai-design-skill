# 13 — Stale-risk and contested-claim re-check

**Date of sweep:** 2026-09-05
**Route used:** Exa MCP **not authorized** in this session. All verification done with
WebSearch, WebFetch, and direct `curl` against authoritative endpoints
(npm registry API, `raw.githubusercontent.com` LICENSE files, arXiv `/abs/`
submission histories, MediaWiki `action=raw`). No blog summary was used as
evidence for any licence, version, or API fact.
**Claims re-checked:** 29
**Sources opened today:** 34 distinct URLs — 14 npm registry endpoints, 4 raw LICENSE
files, 6 arXiv `/abs/` pages, 2 arXiv `/html/` full texts, 1 Wikipedia raw wikitext,
and 7 documentation/article pages. Plus 5 web searches used for lead-finding only
(logged in Gaps; not cited as evidence).
**Baseline being re-checked:** the library layer in `sources-compendium.md` was last
verified **2026-09-04**, one day before this sweep. The rest is older.

---

## 1. Verdict table

| # | Claim (quoted from the skill) | File / IDs | Status | Evidence checked today | Action |
|---|---|---|---|---|---|
| 1 | "GSAP is not MIT. The npm licence field points at this proprietary Webflow licence." | compendium L3, L4; `libraries/README.md`; `libraries/motion.md` | **HOLDS** | `registry.npmjs.org/gsap/latest` → version 3.15.0, `license` field reads literally `Standard 'no charge' license: https://gsap.com/standard-license.` `@gsap/react` → 2.1.2, `SEE LICENSE AT https://gsap.com/standard-license`. Licence page opened: commercial use free, Prohibited Uses clause intact, IP "remain the exclusive property of Webflow". Not an OSI licence. | None. |
| 2 | "Commercial usage is covered under the standard license." | L3 | **HOLDS** | gsap.com/standard-license read today; the quoted sentence is still present verbatim. | None. |
| 3 | GSAP's Prohibited Uses clause covers tools that compete with Webflow's visual animation building | L3 | **HOLDS** | Clause read today: prohibits use in "tools that allow users to build visual animations without code that…competes with Webflow's visual animation building capabilities." | None. |
| 4 | GSAP version 3.15.0 | L2, L4, L5 | **HOLDS** | npm registry `latest` = 3.15.0. | None. |
| 5 | "SurveyJS splits between an MIT renderer and a commercial Creator." | L61, L63, L64; `libraries/README.md`; `maps-forms.md` | **HOLDS** | `survey-library/master/LICENSE` → "MIT License / Copyright (c) 2015-2025 Devsoft Baltic OÜ". `survey-creator/master/LICENSE` → "Commercial developer license for SurveyJS Creator, SurveyJS PDF Generator and SurveyJS Dashboard libraries", full EULA, © 2015-2026. npm: `survey-core@3.0.3` MIT, `survey-react-ui@3.0.3` MIT, `survey-creator-core@3.0.3` `SEE LICENSE IN LICENSE`. | None. |
| 6 | SurveyJS Creator is "commercial, per-developer and perpetual with 40% annual updates" | L63, L64 | **HOLDS** | surveyjs.io/licensing today: "We license our software development product(s) on a per-developer basis"; perpetual use of the received version; renewal priced as "a discount of around 60% of the current license fee". Arithmetically identical to the skill's phrasing (Basic $239/$589 = 40.6%; PRO $419/$1,059 = 39.6%). | Record the page's own phrasing ("60% discount") alongside the skill's "40%" in L64, so a future reviewer does not read a mismatch where there is none. |
| 7 | SurveyJS v3.0.3 | L62 | **HOLDS** | npm: `survey-core`, `survey-react-ui` and `survey-creator-core` all at 3.0.3. | None. |
| 8 | "Leaflet tiles are not free by default. OpenStreetMap has a tile usage policy with real limits, and attribution is required." | `libraries/README.md`; L56, L57 | **HOLDS** | operations.osmfoundation.org/policies/tiles/ read today: attribution required on the map; bulk downloading defined as "any pre-emptive fetching of tiles other than those a user is actively viewing" and prohibited; a clear unique User-Agent required and library defaults disallowed; "Access may be blocked without prior notice"; caching floor of 7 days. Substance identical; two quotes have been rephrased upstream — see Notes on HOLDS rows, item i. | Refresh L56's quotes to the current page wording. No change to the rule. |
| 9 | OSM attribution "is required, not optional" | L57 | **HOLDS** | osmfoundation.org/wiki/Licence/Attribution_Guidelines, page last revised **16 March 2022**, i.e. unchanged: "If you want to use OpenStreetMap data in something you create and distribute, you must attribute OpenStreetMap." | None. |
| 10 | Leaflet is BSD-2-Clause | L54, L55 | **HOLDS** | `Leaflet/main/LICENSE` → "BSD 2-Clause License, Copyright (c) 2010-2026, Volodymyr Agafonkin". npm `leaflet@1.9.4`, `license: BSD-2-Clause`. | None. |
| 11 | "Leaflet with a 2.0 alpha in flight"; 2.0 carries breaking changes | L52; Stale section | **HOLDS** | npm dist-tags: `latest 1.9.4` (published 2023-05-18), `alpha 2.0.0-alpha.1` (published 2025-08-16). Nothing published since — 13 months static. | Keep. Listed under Still stale. |
| 12 | "animate.css says MIT on npm and Hippocratic 2.1 in the shipped LICENSE." | L15; Stale section | **HOLDS** | npm `animate.css@4.1.1` → `license: MIT`. `animate-css/animate.css/main/LICENSE` → "Animate.css Copyright 2021 Daniel Eden … Hippocratic License Version Number: 2.1." The contradiction is live today. | None. This remains the skill's strongest live example of "metadata lies". |
| 13 | "react-leaflet v5.0.0 is also Hippocratic 2.1." | L15; Stale section | **HOLDS** | npm `react-leaflet/latest` → version 5.0.0, `license: Hippocratic-2.1` as a literal registry string. | None. |
| 14 | anime.js 4.5.0, licence MIT | L10 | **HOLDS** | npm `animejs/latest` → 4.5.0, MIT. | None. |
| 15 | Lenis 1.3.26, licence MIT | L22, L28 | **HOLDS** | npm `lenis/latest` → 1.3.26, MIT. | None. |
| 16 | PixiJS 8.20.1, licence MIT | L39 | **HOLDS** | npm `pixi.js/latest` → 8.20.1, MIT. | None. |
| 17 | "animate-ui has no published npm package, so there is no upgrade path and no CVE channel." | L17; Stale section | **HOLDS** | The name `animate-ui` **does** resolve on npm, but to an unrelated abandoned stub: version 0.0.4, description "``` yarn install ```", no repository field, created 2019-08-19, last modified 2022-04. It is not imskyleen's component distribution. `@animate-ui/core` returns 404. | Add one line to L17: `npm i animate-ui` installs a dead 2019 stub, not the component distribution. This is a live trap for a generating agent and the claim is currently phrased in a way that would let an agent walk into it. |
| 18 | "AI vocabulary shifts by era. 2023 to mid-2024: `delve`, `tapestry`, `testament`, `pivotal`. Mid-2024 to 2025: `align with`, `fostering`, `showcasing`. 2025 onward: `emphasizing`, `enhance`, `highlighting`." | M11; Stale section | **HOLDS** | Wikipedia:Signs of AI writing fetched as raw wikitext today. All three era bullets present and matching, including the GPT-4 / GPT-4o / GPT-5 attributions. "delve … became less frequent later in 2024, then dropped off sharply in 2025" also intact, cited to Merrill et al. (Washington Post, 13 Nov 2025) and Geng & Trotta (ACL Findings 2025). | None to the claim. But see row 19 — the scanner has not followed it. |
| 19 | "The word lists live in `scripts/rules.json` (grouped, weighted)" — CP2, "AI-cadence set", weight 1-2, status "Verified" | tells-register CP2; `scripts/rules.json` → `copy_tells.ai_cadence` | **WRONG** | `ai_cadence` contains, as its only single-word entries, `delve`, `testament to`, `tapestry`, `plays a pivotal role` — all four from the era Wikipedia labels 2023 to mid-2024 and says "dropped off sharply in 2025". Nothing from the mid-2024 set (`align with`, `fostering`, `showcasing`) or the mid-2025+ set (`emphasizing`, `enhance`, `highlighting`) is present, nor `deep dive`. The register's own text says word lists date quickly; the implementation encodes exactly the era that has expired. Checked `scripts/copy_check.py` for a second list: it contains none of these words, so the defect is confined to `rules.json`. | **Rule change required.** See §2, item A. |
| 20 | M11's context block, as the skill's record of the Wikipedia page | M11 | **HOLDS** | M11 records the three era bullets (all confirmed, row 18), the shortcut sections, the "Not all text featuring these indicators is AI-generated" caveat, and the Economist em-dash citation of 30 Jul 2026 — all still present today. M11 does **not** record the page's separate "words to watch" box, so no drift in that box can be demonstrated against it. The box today contains, among others, `deep dive` (cited to the Economist, 30 Jul 2026 — a date predating M11's own read), `robust`, `showcase`, `highlight` as a verb, `landscape` as an abstract noun. The page also carries a generator-specific paragraph M11 does not record. | Not a change in the source — a gap in the compendium. Add the box's current contents and the Grok paragraph to M11. See §3, item B. |
| 21 | "The Economist study cited there, dated 30 Jul 2026, found only Claude used em dashes more than professional writers. ChatGPT used them less." | M11; Contested section; CP2 | **HOLDS** | Citation intact in the live wikitext under ref name `economistJul2026`, dated 30 July 2026, accessed 8 August 2026, with exactly that finding. | None. |
| 22 | CP2 treats em-dash density as a live signal, era "evergreen" | tells-register CP2 | **HOLDS** | The tell is still documented. But the section now carries a maintenance banner dated **September 2026**: "If more recent examples of this AI sign can't be found, it should probably be moved to Historical indicators, as it seems to be less common in current LLM output." The page also notes vendors actively suppressing it, citing OpenAI's GPT-5.1 (Ars Technica, 14 Nov 2025). The signal is fading, not gone. | Era-tag CP2's em-dash component `2023-2025`. Note the Part 3 copy table has no Era column (ID / Tell / Examples / Weight / FP risk / Status), so in practice: append `era 2023-2025` to CP2's Status cell rather than adding a column. Do **not** raise its weight. Recheck Dec 2026. |
| 23 | "No screenshot classifier works on UI. Photo-trained detectors are near coin-toss and untested on flat UI renders." | Stale section; tells-register Part 0 finding 5; R19, A15, A16 | **HOLDS** | R19 re-opened: aimultiple.com/ai-image-detector, last updated **14 May 2026** (unchanged), 7 detectors, "most perform no better than a coin toss", test material still 5 Shutterstock photos plus 5 ChatGPT images — zero rendered UI. Two targeted searches surfaced no UI-design classifier. Newly found corroboration for the second half of the claim: arXiv 2606.19259 measures photo-trained detectors over-flagging *real* UI screenshots (see Notes on HOLDS rows, item ii). | Keep. Read this HOLDS as "no evidence found today", not "confirmed absent" — see Gap 1. |
| 24 | "No labelled corpus of AI versus human-designed UIs exists (R gap 4)." | Stale section; R gap 4 | **CHANGED** | PAGEN was released with *Generative UI: LLMs are Effective UI Generators*, Leviathan et al., Google Research, arXiv 2604.09577, submitted 24 Feb 2026. Abstract: "we create and release PAGEN, a novel dataset of expert-crafted results". 200 pages, human side built by 18 contracted developers, paired with the authors' system's generations for the same prompts. | **Replace the sentence.** See §2, item B. |
| 25 | "Detectors trained on GANs fail on diffusion output"; "a detector tuned on this quarter's tools may fail next quarter" | A16; Stale section | **HOLDS** | arXiv 2502.15176 submission history: v1 21 Feb 2025, v2 17 Oct 2025. No version published since the compendium's read, so the 92–94% cross-generator figure has not moved and there is no retraction notice. | None. |
| 26 | "Only 8% of photorealistic AI images now show detectable flaws." | V10 | **HOLDS** | arXiv 2409.17484 submission history: v1 26 Sep 2024, v2 14 Mar 2025. The compendium already cites v2, which remains current. No newer version, no retraction. | None. |
| 27 | "Humans score 53.76% against MidJourney v7 portraits, near chance." | A15 | **HOLDS** | arXiv 2512.22236 submission history shows **v1 only**, 23 Dec 2025. The compendium's `v1` URL pin is still the current version. No revision, no retraction. | None. |
| 28 | "Colour statistics detect it at 93.27% average accuracy across generators, and 99.4% for Stable Diffusion against COCO." | V9 | **HOLDS** | arXiv 2606.02224: v1 1 Jun 2026, v2 9 Jun 2026. v2 predates the compendium's 2026-09-04 read, so the recorded figures were taken from the current version. Identical file size across versions, consistent with a metadata-only revision. | None. |
| 29 | "Ran an automated Playwright scan of 1,590 Show HN pages. 22% carried four or more slop patterns. Measured prevalence: permanent dark theme 34%, gradients 27%, icon-card grids 22%. False-positive rate around 5% to 10%." | P1 | **HOLDS** | developersdigest.tech article re-opened: 1,590 pages; "22% of pages were heavy slop, triggering four or more of the sixteen patterns"; 34% / 27% / 22% intact; "5-10 percent false positives on manual QA, which is tolerable for bucketing". One metadata discrepancy: the page shows publication **2026-04-22 with no updated date displayed**, while P1's source line records "Apr 2026 (updated Jun 2026)". | Drop "(updated Jun 2026)" from P1's source line unless it can be re-sourced. The measurements themselves are unchanged. |

**Counts: HOLDS 27 · CHANGED 1 · WRONG 1 · UNVERIFIABLE 0. Total 29.**

---

## Notes on HOLDS rows

**i. OSM tile policy wording has moved, substance has not (row 8).**
L56 records "Stripping the Referer header at a CDN or proxy is explicitly called out."
The live page frames it as a directive instead:

> "Do not set a restrictive Referrer-Policy that prevents the Referer header being sent."

It adds an enforcement sentence L56 does not carry — traffic using "generic defaults,
referer-stripping, or spoofed identities may be blocked without notice" — and a caching
floor: cache per HTTP headers "or at least 7 days if your cache cannot read them". The
page displays no last-updated date. Status stays HOLDS; L56's quotes are worth refreshing.

**ii. New measured corroboration for row 23, which is not a counter-example.**
R19's argument that flat fills, crisp vector type and exact geometry break photo-trained
detectors was an *inference* the skill drew — R19 itself tested no UI. There is now a
measured result pointing the same way. *A Multi-Domain Benchmark for Detecting
AI-Generated Text-Rich Images from GPT-Image-2* (College of Computer Science, Sichuan
University; arXiv 2606.19259, v1 17 Jun 2026, v2 26 Jul 2026) includes UI screenshots as
one of six categories and reports that on UI, detectors reach high recall on generated
images but **low recall on real ones** — they systematically false-flag genuine
screenshots — with CNNSpot scoring F1 0.00 on the category outright.

Read the scope carefully before citing it. Its "UI screenshots" are images *synthesized
by GPT-Image-2* from layout prompts derived from the Enrico dataset, not browser renders
of AI-*designed* pages. It is **not** a counter-example to row 23 and must not be cited as
one. It is evidence that photo-trained detectors misbehave specifically on UI-shaped
input, which strengthens the skill's existing position.

---

## 2. Fuller entries for the CHANGED and WRONG rows

### A. WRONG — the scanner's `ai_cadence` list encodes a retired vocabulary era (row 19)

This is the one finding that forces a rule change.

`tells-register.md` and the compendium both state, correctly and with a live source, that
AI vocabulary shifts roughly every 12–18 months and that word lists date quickly. The
scanner does not implement that finding. `scripts/rules.json` → `copy_tells.ai_cadence`
currently reads:

```
"it's not just", "isn't just", "in today's fast-paced", "welcome to the future",
"say goodbye to", "whether you're a", "it's important to note", "delve",
"testament to", "tapestry", "evolving landscape", "plays a pivotal role", "stands as a"
```

The four vocabulary entries — `delve`, `testament to`, `tapestry`, `plays a pivotal role`
— are all drawn from the era Wikipedia labels **2023 to mid-2024 (GPT-4)**, and the same
page says of the flagship one:

> "delve … became less frequent later in 2024, then dropped off sharply in 2025."

Source: `https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing`, wikitext read
2026-09-05, citing Merrill et al. (Washington Post, 13 Nov 2025) and Geng & Trotta
(ACL Findings 2025).

Nothing from the two later eras appears in the scanner at all. The structural phrases
(`it's not just`, `in today's fast-paced`, `stands as a`) are era-robust and should stay;
the vocabulary entries are scoring a generation of output that has largely stopped being
produced. The practical effect runs in both directions: the copy scanner under-detects
current AI copy, and over-flags 2023–24 human marketing prose that happened to reach for
"tapestry".

`scripts/copy_check.py` was checked for a second word list and contains none of these
terms, so the defect is confined to `rules.json`.

Recommended replacement for the vocabulary entries — structural phrases kept as they are,
buckets era-tagged so the next reviewer can retire one cleanly, exactly as CO1 and LA12
are already handled:

> **`ai_cadence_legacy_2023`** (weight 1, era-tagged, retained as a legacy signal):
> `delve`, `tapestry`, `testament to`, `plays a pivotal role`, `intricate`, `meticulous`.
> **`ai_cadence_current_2025`** (the live set): `emphasizing`, `enhance`, `highlighting`,
> `showcasing`, `align with`, `fostering`, `deep dive`.
> **`ai_cadence_generator_specific`** (Grok): `causal`, `empirical`, `correlate`,
> `underscore`. Note `underscore` deliberately sits here rather than in the legacy
> bucket — Wikipedia records Grok "continues to overuse" it as of 2026, so it is
> generator-dependent rather than retired.
> Score on density and co-occurrence, never on a single hit. Wikipedia's own rule is
> that one or two words may be coincidental and only "lots of them, lots of times" is
> a strong tell.
>
> **Set the FP risk higher when you ship this.** `delve` and `tapestry` were odd words;
> `enhance`, `highlighting`, `showcasing` and `align with` are ordinary marketing
> vocabulary. Wikipedia's list is drawn from encyclopedic and academic prose, and
> transferring it to UI marketing copy raises false positives sharply. Raise CP2's
> FP risk to **high** and hold its weight where it is.

I have not edited `rules.json`. This is a recommendation only.

### B. CHANGED — a labelled AI-versus-human webpage corpus now exists (row 24)

The Stale section's sentence "No labelled corpus of AI versus human-designed UIs exists
(R gap 4)" is no longer accurate as written.

Evidence: *Generative UI: LLMs are Effective UI Generators*, Leviathan, Valevski, Kalman,
Lumen, Segalis, Molad, Pasternak, Natchu, Nygaard, Venkatachary, Manyika, Matias —
affiliation confirmed from the paper's title block as **Google Research** (all authors
carry `@google.com` addresses). arXiv 2604.09577, submitted 24 February 2026.
`https://arxiv.org/abs/2604.09577`. From the abstract:

> "We also create and release PAGEN, a novel dataset of expert-crafted results to aid in
> evaluating Generative UI implementations, as well as the results of our system for
> future comparisons."

Composition, from the full text: 200 pages — 100 queries randomly sampled from LMArena
plus 100 manually selected across domains. The human half was built by contracted
developers: "we reached out to 34 contractors, out of which 18 contractors accepted",
each producing 5–20 sites at $100–130 and 3–5 hours per page. Interactive examples at
`generativeui.github.io`.

Recommended replacement wording for the Stale section:

> **A paired corpus now exists, but it will not serve as a detection corpus.**
> PAGEN (Google Research, arXiv 2604.09577, Feb 2026) releases 200 expert-human-built
> web pages alongside one generator's output for the same prompts. That is the first
> AI-versus-human-designed page set this skill has found. Three limits keep R gap 4 open in substance:
> it is 200 pages, not thousands; it was built to score generation *quality*, not to
> train a detector; and its AI half comes from a single in-house research system, not
> from the Lovable, v0, Bolt and Claude output the K methodology measured. No classifier
> trained on it was found. The downstream claim — that no screenshot classifier works on
> UI — is unaffected.

---

## 3. New sources opened

### Library, version and licence sources — IDs assigned L77 onward

| ID | Source | What it establishes |
|---|---|---|
| **L77** | npm registry, `survey-creator-core` package metadata. `https://registry.npmjs.org/survey-creator-core/latest` | Version 3.0.3; `license: "SEE LICENSE IN LICENSE"`. Machine-readable confirmation of the SurveyJS licence split from the registry side, complementing L63's LICENSE-file evidence. Also shows the Creator tracks the same version number as the MIT renderer, which is exactly why the split is easy to miss in a lockfile. |
| **L78** | npm registry, `react-leaflet` package metadata. `https://registry.npmjs.org/react-leaflet/latest` | Version 5.0.0; `license: "Hippocratic-2.1"` as a literal registry string. Previously the Hippocratic fact for react-leaflet was carried only inside L15's prose, with no source of its own. |
| **L79** | npm registry, `animate-ui` package metadata. `https://registry.npmjs.org/animate-ui/latest` and `https://registry.npmjs.org/animate-ui` | The name-collision hazard: `animate-ui@0.0.4`, MIT, description "``` yarn install ```", no repository field, created 2019-08-19, last modified 2022-04 — unrelated to imskyleen's animate-ui. `@animate-ui/core` returns 404. Backs L17 and supplies the install trap it currently lacks. |

### Other sources opened — no IDs assigned, prefix suggested

| Source | Suggested prefix | Why it belongs |
|---|---|---|
| Leviathan et al., *Generative UI: LLMs are Effective UI Generators*, Google Research, arXiv 2604.09577, 24 Feb 2026. `https://arxiv.org/abs/2604.09577` and `https://arxiv.org/html/2604.09577v1` | **A** (academic) | The PAGEN release. Directly amends the Stale section and R gap 4. Also carries a finding relevant to the JD-series tells: the system's output was "worse than those crafted by human experts" but "comparable in 50% of cases". |
| Ouyang et al., *A Multi-Domain Benchmark for Detecting AI-Generated Text-Rich Images from GPT-Image-2*, Sichuan University, arXiv 2606.19259, v2 26 Jul 2026. `https://arxiv.org/html/2606.19259v1` | **V** (visual science), or **A** | Measured evidence that photo-trained detectors over-flag *real* UI screenshots. Corroborates R19's inference. Must be logged with its scope caveat — synthesized UI images, not rendered pages — so a future reader does not mistake it for a UI-design detector. |

*(Additions to M11 arising from row 20 — the words-to-watch box contents and the
generator-specific paragraph — are updates to an existing entry, not a new source. The
box now includes `deep dive`, `robust`, `showcase`, `highlight` as a verb, and `landscape`
as an abstract noun; the paragraph reads that Grok "overuses superficially 'scientific'
words like causal, empirical, correlate, and continues to overuse underscore as of 2026".)*

---

## 4. Still stale — recheck these again

| Claim | Why it stays at risk | Suggested next check |
|---|---|---|
| Every version pin in the L layer (GSAP 3.15.0, anime.js 4.5.0, Lenis 1.3.26, PixiJS 8.20.1, SurveyJS 3.0.3, animate.css 4.1.1, Leaflet 1.9.4) | Six of the seven are actively released packages. This sweep found zero drift across a single day, which is no evidence of stability. | **2026-12-05**, and before any ship. A `curl` loop over `registry.npmjs.org/<pkg>/latest` covers the whole set in seconds. |
| Leaflet 2.0 | `2.0.0-alpha.1` published 2025-08-16 with nothing since. When it ships, L52's breaking changes become live and every generated Leaflet snippet needs checking against the installed major. | **2026-12-05**, or on any publish to the `alpha` or `latest` tags. |
| The em-dash component of CP2 | Wikipedia carries an active September 2026 proposal to demote it to Historical indicators, and vendors are tuning it out of models. It could be dead within two quarters. | **2026-12-05** — check whether the banner resolved and the section moved. |
| The `ai_cadence` word list, once fixed | Word lists have a demonstrated 12–18 month half-life. Whatever replaces the current list rots on the same clock. | **2027-03-05**, or whenever a new frontier model family ships. |
| "No screenshot classifier works on UI" | PAGEN's release removes the corpus excuse that made this claim structurally safe. Someone can now try. 200 pages is thin for training, but it is a public starting point. | **2026-12-05**. This is now the highest-value recheck in the file. |
| The GSAP licence | Ownership sits with Webflow and the Prohibited Uses clause is defined by Webflow's commercial interests, which can change without a version bump. The npm `license` field is a URL, so registry metadata will not signal a change. | **2026-12-05** — the licence *page* must be read, not the npm field. |
| P1's prevalence numbers | Still the only measured prevalence figures in the whole skill; still one scan, one author, one moment. | Re-run the K methodology rather than re-reading P1. **2027-03-05**. |
| OSM tile policy | Undated page, edited in place, with real enforcement consequences. Substance stable, wording moves. | **2027-03-05**. |

---

## 5. Gaps

1. **Negative claims cannot be closed.** Row 23 ("no screenshot classifier works on UI")
   is verified only to the depth of two targeted searches plus re-reading R19. Absence of
   a published classifier is not proof none exists — a commercial one would not
   necessarily be published at all. Read that HOLDS as "no evidence found today".
2. **Five search result sets were used for lead-finding only** and are not evidence for
   anything in the table: the Hive Moderation "94–98% cross-generator" figure, the
   PNAS/ANU trained-human-face-detection result, the TextFake benchmark (arXiv 2606.01050),
   the Webflow "GSAP becomes free" announcement, and the "Hallmark" anti-slop skill. None
   was opened. TextFake in particular sounds adjacent to row 23 and should be opened next
   sweep before anyone cites it.
3. **The Economist study is cited at second hand.** Both the em-dash finding and
   `deep dive` reach the skill through Wikipedia's citation of it
   (`https://www.economist.com/culture/2026/07/30/how-to-spot-ai-writing`). The Economist
   page itself was not opened and may be paywalled. Same for the Ars Technica GPT-5.1
   piece cited in row 22. If either becomes load-bearing, the primary source needs reading.
4. **PAGEN's artefact was not downloaded.** The release claim comes from the abstract and
   the composition from the paper body; I did not locate or verify a dataset download URL.
   The paper points at `generativeui.github.io` for interactive examples. "Publicly
   released" is the authors' claim, not something verified by fetching files.
5. **PDF tooling is unavailable in this environment.** `pdftotext`/poppler and `pypdf`
   could not be installed, and the Read tool's PDF path needs `pdftoppm`. PAGEN's details
   came from `arxiv.org/html/` instead. A future sweep needing PDF-only sources hits this.
6. **Two contested entries were not re-checked**, being out of scope for a stale sweep:
   "Should the tells be removed at all" (an ethics question the compendium records as
   unresolved by design) and "Sameness is bad" (a values disagreement between named
   commenters, not a factual claim with an expiry date).
7. **No re-check of the K methodology.** Claims resting on "0 of 12 verified repos" — CO1,
   LA12, and the raw-indigo-era finding — can only be re-verified by re-cloning and
   re-counting, which is a different job from a source sweep. They are among the oldest
   measurements in the skill and nothing here refreshed them.
