# 14 — Rendered-Output Metrics: what can actually be measured on a screenshot or a live page

**Topic:** Published metrics that operate on rendered output (screenshots, live pages) rather than source code. Design Homogeneity Index and follow-ups; screenshot-level generative-UI benchmarks; reproducible computational-aesthetics measures; accessibility-as-craft at render time; whether any AI-UI screenshot detector exists with real numbers.

**Date of sweep:** 2026-09-05

**Route used:** `WebSearch` + `WebFetch` only. The Exa MCP server was **not authorized** in this session and was not used. **alphaXiv MCP tools were not usable** — I ran a tool search for `alphaxiv` and the only alphaXiv tool exposed in this session is `edit_private_paper_metadata`, a write tool for the user's own uploads. No alphaXiv search or read tool exists here, so the topic's suggested alphaXiv route could not be taken. Two supplementary mechanics were used, both via WebFetch/local tooling and both noted per-source: the **Semantic Scholar Graph API** (`api.semanticscholar.org/graph/v1`) to retrieve citation counts and one abstract that ACM DL refused, and **local PDF text extraction** (pypdf in a scratch venv) for two PDFs that WebFetch returned as binary.

**Sources actually opened (full text or abstract, at the URL given):**
- arXiv abstract + HTML full text: 2607.22928 (Design Theater), 2606.01050 (TextFake), 2606.19259, 2605.15124, 2503.15885, 2404.12500 (UIClip)
- Full PDF text extracted locally: AIM UIST 2018 adjunct paper; "Good Accessibility, Handcuffed Creativity" (DIS '25, author-hosted open PDF)
- GitHub: `aalto-ui/aim` README; `dequelabs/axe-core` `doc/rule-descriptions.md`
- W3C: WCAG 2.2 Recommendation
- Google: Lighthouse accessibility scoring docs
- Deque: automated-coverage blog post
- Semantic Scholar API: citation record for 2607.22928; full abstract for the W4A '26 paper
- Commercial: `anonymiz.com/ai-website-detector`

**Could NOT open:** ACM Digital Library landing pages returned **HTTP 403** for both `10.1145/3800424.3800430` and `10.1145/3715336.3735691`. For the first I recovered the publisher abstract via the Semantic Scholar API (gold OA, CC-BY) and cite only what that record contains. For the second I used the authors' open PDF at `mintviz.usv.ro`. `interfacemetrics.aalto.fi` and `userinterfaces.aalto.fi/aim/` returned only a page title / 404 through WebFetch, so the AIM metric list here comes from the **paper**, not the live service.

---

## Source table

| ID | Title | Venue / type | Date | URL |
|---|---|---|---|---|
| V21 | Design Theater: Evaluating the Gap Between User-Facing Design Reasoning and Implementation in Generative UI Tools | arXiv preprint, accepted AAAI/AIES | 2026-07-24 (rev. 2026-07-31) | https://arxiv.org/abs/2607.22928 |
| V22 | UIClip: A Data-driven Model for Assessing User Interface Design | ACM UIST '24 (full paper) | arXiv 2024-04-18; UIST 2024-10 | https://arxiv.org/abs/2404.12500 |
| V23 | Aalto Interface Metrics (AIM): A Service and Codebase for Computational GUI Evaluation | ACM UIST '18 Adjunct + open-source codebase | 2018-10 | https://dl.acm.org/doi/10.1145/3266037.3266087 (PDF: https://www.kashyaptodi.com/data/AIM-UIST2018.pdf) |
| V24 | Good Accessibility, Handcuffed Creativity: AI-Generated UIs Between Accessibility Guidelines and Practitioners' Expectations | ACM DIS '25 (full paper) | 2025-07 | https://mintviz.usv.ro/publications/2025.DIS.2.pdf |
| V25 | Generated Inaccessible: Measuring WCAG Violations in AI UI Design Tools | ACM W4A '26 (full paper, gold OA CC-BY) | 2026-06 | https://dl.acm.org/doi/10.1145/3800424.3800430 |
| V26 | Usable but Conventional: An Empirical Study on the UX of AI-Generated Interface Prototypes | arXiv preprint, accepted SEMISH 2026 (SBC) | 2026-05-14 | https://arxiv.org/abs/2605.15124 |
| V27 | TextFake: Benchmarking AI-Generated Image Detection on Text-Rich Images | arXiv preprint | 2026-05-31 | https://arxiv.org/abs/2606.01050 |
| V28 | TextRich: A Multi-Domain Benchmark for Detecting AI-Generated Text-Rich Images from GPT-Image-2 | arXiv preprint | 2026-06-17 (rev. 2026-07-26) | https://arxiv.org/abs/2606.19259 |
| V29 | Did I Just Browse A Website Written by LLMs? | ACM IMC 2025 poster | 2025-07-18 | https://www.arxiv.org/abs/2507.13933 |
| V30 | axe-core rule descriptions (rule → WCAG SC mapping) | Open-source docs (Deque) | current (v4.11 referenced) | https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md |
| V31 | Web Content Accessibility Guidelines (WCAG) 2.2 | W3C Recommendation | current | https://www.w3.org/TR/WCAG22/ |
| V32 | Lighthouse accessibility scoring | Google developer docs | current | https://developer.chrome.com/docs/lighthouse/accessibility/scoring |
| V33 | Automated Testing Identifies 57% of Digital Accessibility Issues | Vendor study (Deque) | — | https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues/ |
| V34 | AI Website Detector | Commercial web tool | accessed 2026-09-05 | https://anonymiz.com/ai-website-detector |
| V35 | Human or LLM? A Comparative Study on Accessible Code Generation Capability | arXiv preprint (cs.SE) | 2025-03-20 | https://arxiv.org/abs/2503.15885 |

---

## Per-source entries

### V21 — Design Theater: Evaluating the Gap Between User-Facing Design Reasoning and Implementation in Generative UI Tools
- **Source:** Kashif Imteyaz, Kaif Imteyaz, Nakul Rajpal, Kaif Shaikh, Michael Muller, Saiph Savage; arXiv preprint, accepted at AAAI/AIES; 2026-07-24, revised 2026-07-31. https://arxiv.org/abs/2607.22928
- **Context:**
  - 24 UI-generation tasks × 5 tools (ChatGPT, Claude, Firebase Studio, Vercel v0, Bolt) = **120 interfaces**. For each the authors captured generated code, the rendered interface, and the full user-facing reasoning trace. Rendered output was standardised as **1200×1200 PNG screenshots**.
  - Headline (code/rationale, not render): **>25% of user-facing design rationales are not implemented** in the interface, rising to **34% for functional requirements**; tools recognise ~half the UX principles embedded in the prompt (mean 0.54); four of five tools implement **≤6% of functional principles**.
  - **Design Homogeneity Index (DHI)** is the render-layer contribution. It is not one number but three screenshot-computed pairwise-similarity sub-measures: **visual** via UIClip embeddings; **colour** via CIELCh colour histograms compared with Earth Mover's Distance; **layout** via OmniParser v2.0 element detection followed by tree edit distance. Reported over 24 tasks × 10 tool pairs: visual 0.119–0.151 (mean 0.137), colour 20.6–39.7 (mean 31.9), layout 0.181–0.211 (mean 0.196); lower = more similar. Colour varies most.
  - **Critical limitation, stated by the authors themselves:** DHI is computed only among the five tools, "without a reference distribution such as interfaces produced by human designers or a corpus of deployed sites." So DHI **cannot** speak to AI-vs-human. It is a between-tools convergence measure requiring N generations of the same prompt; it is undefined for a single page.
  - Citation count as of 2026-09-05: **0** (Semantic Scholar Graph API). Single paper, n=120, **unreplicated**.
- **Tags:** `[ADOPT: screenshot-normalisation protocol — fixed viewport, standardised PNG capture]` `[EVIDENCE-ONLY]` `[AVOID: using DHI or "homogeneity" as an AI-detection signal on a single page]` `[STALE-RISK]`
- **Feeds:** Fixed-viewport deterministic screenshot capture in the render layer. Optionally an *opt-in, multi-generation* homogeneity comparison if the skill ever scores N variants of one prompt — never a single-page verdict.

### V22 — UIClip: A Data-driven Model for Assessing User Interface Design
- **Source:** Jason Wu, Yi-Hao Peng, Amanda Li, Amanda Swearngin, Jeffrey P. Bigham, Jeffrey Nichols; arXiv submitted 2024-04-18, published at ACM UIST '24 (DOI 10.1145/3654777.3676408). https://arxiv.org/abs/2404.12500
- **Context:**
  - Takes a **UI screenshot plus a natural-language description** and returns a numeric design-quality/relevance score plus design recommendations. Trained on a large UI dataset built by "a combination of automated crawling, synthetic augmentation, and human ratings," collated by description and ranked by quality.
  - Validation: outputs compared against UIs ranked by **12 human designers**; UIClip achieved the highest agreement with the ground-truth ranking among the baselines tested.
  - Demonstrated downstream uses: UI code generation, design-tip generation, and quality-aware UI example search.
  - It is a **craft-quality** model calibrated to human designer preference. It has no AI/human label in its training signal and makes no claim to detect provenance.
  - It is the visual-similarity engine underneath V21's DHI, and V24 explicitly considered and rejected it as an accessibility instrument because its score is holistic rather than criterion-specific.
- **Tags:** `[ADOPT: screenshot → design-quality score, as a craft signal only]` `[AVOID: describing a UIClip score as AI detection]` `[EVIDENCE-ONLY]`
- **Feeds:** An optional render-layer "does this look like a competently designed UI" score. Reported as craft, never as provenance.

### V23 — Aalto Interface Metrics (AIM)
- **Source:** Antti Oulasvirta, Samuli De Pascale, Janin Koch, Thomas Langerak, Jussi Jokinen, Kashyap Todi, Markku Laine, Manoj Kristhombuge, Yuxi Zhu, Aliaksei Miniukovich, Gregorio Palmas, Tino Weinkauf; UIST '18 Adjunct; 2018-10. Code: https://github.com/aalto-ui/aim (MIT licence, Aalto UI group, active `aim2` branch).
- **Context:**
  - This is the single most useful source in the sweep for topic 3: **17 published metrics with an open implementation**, in four categories — Colour Perception, Perceptual Fluency, Visual Guidance, Accessibility.
  - Pipeline (matters for the skill): user supplies a **URL**; AIM captures a screenshot with **Headless Chrome**, runs a segmentation script producing elements with id / absolute position / size / base64 image, and feeds screenshot + segments to each metric. This is exactly the architecture the skill's render layer is proposing.
  - Metric table as published, with the reference each is grounded in: **File size** (Miniukovich & De Angeli 2015); **Colour Variability** — count of distinct colours in RGB/HSV/LAB (Hasler & Süsstrunk 2003; Miniukovich & De Angeli 2014, 2015); **Static Colour Clusters** — bins with >5 px, 32³ RGB bins; **Dynamic Clusters**; **Colourfulness** — SD of pixels in RGB (Hasler & Süsstrunk 2003); **Luminance** — SD of display-corrected luminance; **Colour Harmony** — summed distance of all pixels to a colour scheme (Cohen-Or et al. 2006); **Edge Density** — ratio of edge pixels to all pixels (Miniukovich & De Angeli 2014; Rosenholtz et al. 2007); **Contour Congestion** (Levi 2008; Van den Berg et al. 2009); **Figure-Ground Contrast** (Hall & Hanna 2004; Reber et al. 2004); **Symmetry** — ratio of edges mirrored horizontally/vertically/diagonally; **Visual Complexity** — balance, symmetry and equilibrium via quadtree decomposition (Ngo, Teo & Byrne 2003; Reinecke et al. CHI 2013; Zheng et al. 2009); **Grid Quality** — alignment to grids; **White Space** — proportion of non-covered space; **Itti-Koch Saliency** (Itti & Koch 2000); **Visual Search Performance** (Jokinen et al. 2017); **Colour Blindness** simulation (Machado et al. 2009).
  - What they correlate with, per the cited literature: perceived **visual complexity**, **aesthetic first impressions**, **clutter**, and **visual search time** — i.e. human perceptual and aesthetic response. Nothing in the chain is about authorship. The paper's own framing is "predictive of how users perceive, search, and aesthetically experience a design."
  - Caveat on reproducibility: grid-quality and visual-search metrics are implemented in **MATLAB and Common Lisp** respectively, so those two are not drop-in for a Node/Python headless script. Colour, edge, symmetry, white-space and complexity metrics are Python.
- **Tags:** `[ADOPT: colour count, edge density, white space, grid quality, symmetry, figure-ground contrast — as craft metrics with published implementations]` `[AVOID: any claim these separate AI from human output]` `[EVIDENCE-ONLY]` `[STALE-RISK: 2018 paper; verify the aim2 branch still runs before depending on it]`
- **Feeds:** The entire computational-aesthetics half of the render layer — palette count, whitespace ratio, alignment/grid conformity, edge density, symmetry, visual complexity. Each reported as a craft number with a histogram-style comparison, exactly as AIM does.

### V24 — Good Accessibility, Handcuffed Creativity
- **Source:** Alexandra-Elena Guriţă, Radu-Daniel Vatavu (MintViz Lab, Ştefan cel Mare University of Suceava); ACM DIS '25, Funchal; 2025-07-05. https://mintviz.usv.ro/publications/2025.DIS.2.pdf
- **Context:**
  - 2×3×5 factorial: 2 tools (**FigmaAI, Galileo**) × 3 app types × 5 prompt types × 3 repetitions = **90 UIs**. Plus interviews with **8 professional designers**.
  - Four WCAG **2.1** criteria assessed, chosen for objective measurability: **1.3.1** visual hierarchy, **1.4.3** colour contrast, **1.4.12** text spacing, **2.5.5** target size. Measured with the **WebAIM Contrast Checker** and the **Stark** Figma plugin, plus two blinded accessibility experts on a 0–4 severity scale; inter-rater agreement **87.3%** before consensus.
  - Result: **very few violations**. Overall Violation-Rate 0.189; contrast 0.111 (10 violations), visual hierarchy 0.067 (6), target size 0.011 (1), text spacing 0.000. All violations severity 1 or 2; none severity 3 or 4. Typical failures were near-misses — contrast ratios of 4.37:1, 4.46:1, 4.47:1 against the 4.5:1 threshold, with one genuine 3.05:1.
  - Prompting explicitly for accessibility **did not help**: base prompt 4 violations, generic-accessibility 4, visual-accessibility 4 (and it introduced the only target-size violation and both severity-2 violations), motor-accessibility 2, comprehensive-accessibility 3.
  - Homogeneity was measured as **UI-Similarity**: normalised centroid x–y coordinates of matching component types compared pairwise, 0–1. Averages **0.88** (fitness), **0.90** (recipes), with financial components as high as 0.94. Again **no human-designed comparator** — the scores are AI-vs-AI only.
  - Important scope limit: these are **static Figma mockups**, not rendered HTML. Contrast was checked on colour values, not on computed styles in a browser.
- **Tags:** `[ADOPT: 1.3.1 / 1.4.3 / 1.4.12 / 2.5.5 as the objectively-measurable core]` `[CONTESTED — flatly contradicted by V25 on compliance rate]` `[AVOID: treating "UI-Similarity ≈ 0.9" as an AI fingerprint; there is no human baseline]`
- **Feeds:** Contrast auditing (1.4.3), text-spacing (1.4.12), target-size (2.5.5/2.5.8) checks. Also the evidence that *asking* an AI for accessibility does not reliably produce it — which is a reason the render layer must verify rather than trust.

### V25 — Generated Inaccessible: Measuring WCAG Violations in AI UI Design Tools
- **Source:** Wajdi M. Aljedaani, Lyan Ibrahim Koumu, Alexandra-Elena Guriță; ACM W4A '26 (23rd International Web for All Conference); 2026-06. Gold OA, CC-BY. https://dl.acm.org/doi/10.1145/3800424.3800430
- **Context:**
  - **I could not open the ACM landing page (HTTP 403).** Everything below comes from the publisher abstract retrieved via the Semantic Scholar Graph API record for the DOI. I have not read the methods section, so treat the internals as unverified.
  - Design: **54 designers** manually created interfaces in Figma, then generated comparable designs with **six AI tools**. **21,880 accessibility assessments** across **five WCAG success criteria**.
  - Headline: AI-generated interfaces achieved **29.0% compliance**; colour contrast **26.8%**; use of colour **19.2%**.
  - As in V24, explicitly specifying accessibility in the prompt **decreased** compliance.
  - Human comparator, indirectly: participants reported **39% of AI violations required "major redesign"** to remediate versus **22% for manual designs**. Designer trust in AI to produce accessible output stayed low (M=3.60/5) and confidence in evaluating outputs *fell* after using AI (M=3.2/5 vs 3.8/5).
  - **This directly contradicts V24's "consistently achieve basic accessibility compliance."** Note that Guriță is an author on both, so this is not two independent teams disagreeing — it is more likely a methodological difference (different tools, different criteria set, per-element vs per-interface scoring, mockups vs generated designs). Neither result is replicated. Do not present either number as settled.
- **Tags:** `[CONTESTED]` `[EVIDENCE-ONLY]` `[ADOPT: the finding that prompting for accessibility does not deliver it — replicated across V24 and V25]`
- **Feeds:** Justification for running an actual axe/contrast audit at render time rather than trusting generated markup or an AI's own accessibility claims.

### V26 — Usable but Conventional: An Empirical Study on the UX of AI-Generated Interface Prototypes
- **Source:** Karoline Romero, Igor Wiese, Renato Balancieri, Gislaine Camila Leal, Guilherme Guerino; arXiv preprint, accepted SEMISH 2026 (53rd Integrated Software and Hardware Seminar, Brazilian Computer Society); 2026-05-14. https://arxiv.org/abs/2605.15124
- **Context:**
  - **92 participants** evaluated AI-generated and human-created prototypes **blind to authorship**, using the **UEQ-S** (short User Experience Questionnaire), which splits pragmatic from hedonic quality.
  - Result: AI prototypes scored **positively on pragmatic** dimensions (usability, efficiency) but **neutral-to-negative on hedonic** dimensions (originality, innovation).
  - Authors' conclusion: GenAI produces functional interfaces but reinforces established visual and structural conventions, limiting perceived originality.
  - This is the closest thing in the sweep to an AI-vs-human comparison with a human baseline — but the instrument is a **human questionnaire**, not an automated metric. It says people *feel* the difference on originality; it does not say a machine can measure it.
- **Tags:** `[EVIDENCE-ONLY]` `[ADOPT: framing — the AI signal lives in originality/hedonic quality, not in usability]` `[AVOID: reading "humans perceive it" as "a metric can detect it"]`
- **Feeds:** Nothing directly computable. It supports the skill's overall thesis (AI output is conventional) while making clear the evidence is perceptual, not algorithmic.

### V27 — TextFake: Benchmarking AI-Generated Image Detection on Text-Rich Images
- **Source:** Yuning Zhang, Changtao Miao, Mingyu Liao, Tingyu Liu, Xinghao Wang, Tao Gong, Qi Chu, Nenghai Yu; arXiv preprint; submitted 2026-05-31. https://arxiv.org/abs/2606.01050
- **Context:**
  - **20,000 images** spanning **28 languages, 4 topic categories, 2 scene modalities**, built by a four-stage pipeline using distribution-aligned structured prompting to remove covariate shortcuts. Content is text-rich forgeries — fabricated screenshots, documents, news pages. (A search summary gave a 10,000 real / 10,000 fake split with 8,002 screenshots; **that split is not in the abstract I opened, so I do not rely on it.**)
  - Zero-shot evaluation of **14 specialised detectors plus 3 frontier VLM APIs**: **no method exceeds 80% accuracy**, with some dropping **over 60 points** from their natural-image benchmark performance.
  - Three named failure modes: the **Text Density Curse** (dense text overwhelms detectors), **Cloaking via Rendering Fidelity** (high-quality text rendering masks AI artefacts), and **Threshold Collapse** (routine perturbations drive detectors to chance).
  - **Task mismatch — this is the important caveat.** TextFake asks "was this *image* synthesised by a diffusion/image model?" The skill's render layer produces a **pixel-exact browser screenshot of real HTML**. There is no generative image pipeline in the loop and therefore no synthesis artefact to find. Note that "Cloaking via Rendering Fidelity" is precisely the limit case: a genuine browser render has *perfect* rendering fidelity and zero artefacts. TextFake is strong evidence that the screenshot domain is hostile to detectors, and it is the nearest published work, but it is **not** evidence about detecting AI-*designed* interfaces.
- **Tags:** `[EVIDENCE-ONLY]` `[AVOID: citing this as proof that AI-UI detection fails — it measures a different task]`
- **Feeds:** Nothing. Cited in the verdict as adjacent context with the mismatch stated.

### V28 — TextRich: A Multi-Domain Benchmark for Detecting AI-Generated Text-Rich Images from GPT-Image-2
- **Source:** Yijin Wang, Shuyi Wang, Wenhan Zhang, Yuqi Ouyang; arXiv preprint; 2026-06-17, revised 2026-07-26. https://arxiv.org/abs/2606.19259
- **Context:**
  - **12,095 images** across six categories: commercial posters, infographic charts, academic posters, receipts, tables, and **UI screenshots**. All fakes from GPT-Image-2.
  - **Five** representative AI-generated-image detectors evaluated zero-shot, plus one multimodal VLM. The abstract reports the strongest detector is "competitive overall" but remains ineffective on certain structured categories and is sensitive to JPEG compression. **No per-category accuracy figures are given in the abstract, and I did not open the full text** — so I quote no number here.
  - Same task mismatch as V27: synthesised images of UIs, not rendered real UIs.
- **Tags:** `[EVIDENCE-ONLY]` `[AVOID: as above — different task]` `[STALE-RISK: preprint, revised twice in five weeks]`
- **Feeds:** Nothing. Corroborates that "UI screenshot" as a detection domain is currently studied only in the image-forgery sense.

### V29 — Did I Just Browse A Website Written by LLMs?
- **Source:** Sichang Steven He, Ramesh Govindan, Harsha V. Madhyastha; ACM Internet Measurement Conference 2025, poster; 2025-07-18. https://www.arxiv.org/abs/2507.13933
- **Context:**
  - Detects "**LLM-dominant**" websites — pages automatically generated by LLMs with little human input. The unit of classification is the **whole site**, not the page: they aggregate an LLM text-detector's output across multiple prose-like pages.
  - Two ground-truth datasets totalling **120 sites**; they report **100% accuracy** on them. Also applied at scale to 10,000 sites from search results and 10,000 from Common Crawl.
  - **The signal is prose, not pixels or layout.** This is the closest published thing to "detecting an AI-built website" and it works entirely on text. It says nothing about visual design, and it is a poster on 120 ground-truth sites, so the 100% figure is on a small hand-built set and is **not** a general-population accuracy.
  - Practical read for the skill: the detectable AI fingerprint on a web page is **copy**, which the skill already handles via its copy checks. Adding a render layer will not add detection power; it adds craft measurement.
- **Tags:** `[EVIDENCE-ONLY]` `[ADOPT: reinforces that copy is where provenance signal lives]` `[AVOID: quoting "100% accuracy" without the n=120 hand-built-set caveat]`
- **Feeds:** Nothing in the render layer. It bounds what the render layer could ever claim.

### V30 — axe-core rule descriptions
- **Source:** Deque Labs, open-source docs, `develop` branch (Lighthouse references v4.11). https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md
- **Context:**
  - The rules that genuinely require **render-time computed styles and geometry** rather than static DOM inspection, with the WCAG tags the doc itself carries: `color-contrast` → `wcag143`, `wcag2aa`; `color-contrast-enhanced` → `wcag146`, `wcag2aaa`; `target-size` → `wcag258`, `wcag22aa`; `meta-viewport` → `wcag144`, `wcag2aa`.
  - `target-size` carrying the `wcag22aa` tag confirms axe-core implements **SC 2.5.8 Target Size (Minimum)**, the WCAG 2.2 addition — this is the one genuinely new render-time check available since 2.2.
  - Scope caveat: I asked the fetch to filter to these specific rules, so this is *not* an exhaustive audit of which axe rules are render-dependent — others (e.g. link-in-text-block, scrollable-region-focusable, hidden-content) also depend on rendering. The claim is narrower: **of the rules checked, these four are the computed-style/geometry ones**. Separately, axe-core as a whole should be run in a real browser regardless, so it evaluates the final computed tree.
- **Tags:** `[ADOPT: color-contrast (1.4.3), color-contrast-enhanced (1.4.6), target-size (2.5.8), meta-viewport (1.4.4)]` `[EVIDENCE-ONLY]`
- **Feeds:** The defensible core of the render layer's accessibility checks — these four are computed-style/geometry checks with a maintained open implementation and an explicit SC mapping.

### V31 — WCAG 2.2 (W3C Recommendation)
- **Source:** W3C. https://www.w3.org/TR/WCAG22/
- **Context:**
  - Criterion numbers verified at source rather than from memory: **1.4.3 Contrast (Minimum)** AA, 4.5:1; **1.4.4 Resize Text** AA, 200%; **1.4.6 Contrast (Enhanced)** AAA, 7:1; **1.4.10 Reflow** AA; **1.4.11 Non-text Contrast** AA, 3:1; **1.4.12 Text Spacing** AA; **2.4.7 Focus Visible** AA.
  - **New in WCAG 2.2:** **2.4.11 Focus Not Obscured (Minimum)** AA; **2.4.13 Focus Appearance** AAA; **2.5.8 Target Size (Minimum)** AA. **2.5.5 Target Size** is the pre-existing AAA criterion, renamed **Target Size (Enhanced)** in 2.2.
  - This matters for citing V24 correctly: V24 audited against **WCAG 2.1** and used **2.5.5** (AAA, 44px), not 2.5.8 (AA, 24px). Do not conflate the two.
- **Tags:** `[ADOPT: all criterion numbers above]` `[EVIDENCE-ONLY]`
- **Feeds:** Every SC number cited in the recommended-checks section below.

### V32 — Lighthouse accessibility scoring
- **Source:** Google, Chrome developer docs. https://developer.chrome.com/docs/lighthouse/accessibility/scoring
- **Context:**
  - The Lighthouse accessibility score is a **weighted average of its accessibility audits**, weighted by **axe user-impact assessments**. The engine underneath is **axe-core** (the page links axe v4.11 rule descriptions).
  - Each audit is **binary pass/fail** — no partial credit. Manual and low-impact/best-practice audits do not affect the score.
  - The page does **not** state any coverage percentage or acknowledge automated-testing limits. So a "Lighthouse a11y: 100" is not a claim of accessibility, and Google does not present it as one on this page.
- **Tags:** `[ADOPT: Lighthouse as a convenient axe harness]` `[AVOID: reporting the Lighthouse accessibility score as an accessibility verdict, or as a craft score]` `[EVIDENCE-ONLY]`
- **Feeds:** If the render layer uses Lighthouse, report the individual failing audits and their SC numbers, not the aggregate score.

### V33 — Automated Testing Identifies 57% of Digital Accessibility Issues
- **Source:** Deque Systems (vendor study). https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues/
- **Context:**
  - Anonymised data from **2,000+ audits**, **13,000+ pages** (all first-time assessments), **~300,000 issues**, across various industries. Automated testing with Deque's axe suite (axe-core rules) identified **57% of accessibility issues** — which Deque contrasts with a prior industry assumption of 20–30% coverage.
  - **The definition is the whole story.** Deque explicitly changed the metric from "share of WCAG success criteria that are automatable" to "**total volume of issues detected by severity and impact**," on the argument that some issue types occur far more frequently than others. The 57% is therefore a share of *issue instances*, not a share of *criteria*, and the two are not interchangeable.
  - **Vendor-authored study on their own product** — the incentive is to make automated coverage look good, and the counting method (share of *issue volume* rather than share of *success criteria*) is explicitly chosen because it flatters automation. Treat 57% as an upper-ish bound from an interested party, not a neutral figure.
- **Tags:** `[CONTESTED]` `[EVIDENCE-ONLY]` `[ADOPT: the honesty framing — automated a11y checks are partial, ~half by the vendor's own generous count]`
- **Feeds:** The caveat text the render layer must print alongside any axe result.

### V34 — AI Website Detector (anonymiz.com)
- **Source:** Commercial web tool, accessed 2026-09-05. https://anonymiz.com/ai-website-detector
- **Context:**
  - Claims to detect ChatGPT, Lovable, Bolt.new, Framer, v0 and "20+ more" builders.
  - Its actual signals are **HTML source and infrastructure**, not pixels: builder fingerprints (CDN domains, CSS class conventions, attribution badges), HTML comments left by Lovable.dev / Cursor, direct references to OpenAI/Anthropic/Google/xAI API endpoints in page source, Vercel/Netlify headers, IP ranges and CNAME targets, and the HTML `generator` meta tag.
  - It publishes **no accuracy figures, no test set, and no validation**. It states its own limitation plainly: it detects technical fingerprints and infrastructure, not developer intent, and AI-written code is identical to human-written code absent explicit comments or API references.
  - Relevance: this is what a "working AI website detector" looks like in 2026 — **metadata archaeology, not design analysis**. It would score a hand-written page deployed to Vercel as AI, and an AI-designed page served from a custom host as human.
- **Tags:** `[AVOID: as a model for the render layer, and as a citation for "detection is possible"]` `[EVIDENCE-ONLY]`
- **Feeds:** Nothing. Included because it is the strongest "detector" claim findable, and it is unvalidated and non-visual.

### V35 — Human or LLM? A Comparative Study on Accessible Code Generation Capability
- **Source:** Hyunjae Suh, Mahan Tafreshipour, Sam Malek, Iftekhar Ahmed; arXiv preprint (cs.SE); 2025-03-20. https://arxiv.org/abs/2503.15885
- **Context:**
  - Compares accessibility of web code from two LLMs (GPT-4o, Qwen2.5-Coder-32B-Instruct-AWQ) against human-written code.
  - Finding: **LLMs often produce *more* accessible code**, particularly on basic features like colour contrast and alt text; both LLMs and humans struggle with ARIA attributes.
  - Also introduces FeedA11y, a feedback-driven ReAct approach, reported to outperform Zero-Shot / Few-Shot / Self-Criticism prompting.
  - **I read the abstract only** — sample sizes, the measurement tool, and the specific criteria are not stated there and I did not open the full text, so I report no numbers.
  - Consequence for the skill: accessibility scores point in the **opposite** direction to intuition. A well-formed a11y result is not evidence of human authorship — if anything V35 says the reverse. This kills any temptation to use a11y pass-rate as a provenance signal.
- **Tags:** `[CONTESTED — points opposite to V25]` `[AVOID: using accessibility quality as an AI-vs-human discriminator, in either direction]` `[EVIDENCE-ONLY]`
- **Feeds:** A hard guardrail on how a11y results may be reported.

---

## Measurable at render time

| Metric | What it needs | Published implementation? | What it actually tells you | Distinguishes AI from human? |
|---|---|---|---|---|
| Colour count / palette entropy (Colour Variability, Static & Dynamic Clusters) | Screenshot pixels | **Yes** — AIM, Python, MIT (V23); refs Hasler & Süsstrunk 2003, Miniukovich & De Angeli 2014/2015 | Palette breadth; correlates with perceived visual complexity and aesthetic first impressions | **No.** Nothing in the literature ties a palette count to authorship. |
| Colourfulness / Luminance SD | Screenshot pixels | **Yes** — AIM (V23) | Chromatic energy and tonal spread; input to first-impression models (Reinecke et al. 2013) | **No.** |
| Colour Harmony | Screenshot pixels | **Yes** — AIM (V23), Cohen-Or et al. 2006 | Distance of the page's pixels from a canonical colour scheme | **No.** A "harmonious" palette is equally a mark of a good designer and of a default template. |
| Whitespace ratio | Screenshot + element segmentation | **Yes** — AIM "White Space" (V23), Miniukovich & De Angeli 2015 | Proportion of uncovered area; a density/breathing-room proxy | **No.** |
| Alignment / grid conformity | Segmented elements | **Yes** — AIM "Grid Quality" (V23), but implemented in **MATLAB**; not drop-in for a JS/Python script | Count of grid alignment lines the elements fall on | **No.** Strong grid conformity is a craft virtue and a framework default simultaneously. |
| Edge density / contour congestion | Screenshot pixels | **Yes** — AIM (V23), Rosenholtz et al. 2007 clutter model | Visual clutter; empirically correlates with perceived complexity | **No.** |
| Symmetry | Screenshot edges | **Yes** — AIM (V23) | Ratio of edges mirrored H / V / diagonal | **No.** |
| Visual complexity / balance / equilibrium | Segmented elements, quadtree | **Yes** — AIM (V23), Ngo/Teo/Byrne 2003 formulas | Ngo-style layout balance; correlated with rapid aesthetic judgement (Zheng et al. 2009) | **No.** |
| Figure-ground contrast | Screenshot pixels | **Yes** — AIM (V23) | Foreground/background discriminability; a readability proxy distinct from WCAG contrast | **No** — but it is a genuine craft signal. |
| Saliency (Itti-Koch) | Screenshot pixels | **Yes** — AIM via pySaliencyMap (V23) | Where the eye is predicted to land | **No.** |
| UIClip design-quality score | Screenshot + a description string | **Yes** — UIClip, UIST '24 (V22) | A learned quality score agreeing with 12 human designers' ranking | **No.** No provenance label anywhere in its training. |
| DHI: visual / colour / layout similarity | **N screenshots of the same prompt**, UIClip + CIELCh/EMD + OmniParser v2 | **Yes**, described in V21; needs UIClip + OmniParser | How much N generations converge on one another | **No** — and the authors say so: no human reference distribution exists. Undefined for a single page. |
| Computed colour contrast (SC 1.4.3 / 1.4.6) | Live page, computed styles | **Yes** — axe-core `color-contrast`, `color-contrast-enhanced` (V30) | A real, binary WCAG pass/fail per text node | **No.** V25 says AI is worse (26.8%), V24 says AI is fine, V35 says AI is better. Contested in every direction. |
| Target size (SC 2.5.8) | Live page, element geometry | **Yes** — axe-core `target-size`, tagged `wcag22aa` (V30) | Whether interactive targets meet the 24×24 CSS-px minimum | **No.** |
| Viewport / zoom permission (SC 1.4.4) | Rendered `<meta name=viewport>` | **Yes** — axe-core `meta-viewport` (V30) | Whether the page blocks pinch-zoom | **No.** |
| Text spacing tolerance (SC 1.4.12) | Live page, restyle-and-reflow | Partially — not an axe automated rule; V24 measured it manually with Stark | Whether content survives forced spacing overrides | **No.** |
| Reflow (SC 1.4.10) | Live page at 320 CSS px | Partially — requires a scripted viewport resize + overflow detection; no single canonical implementation found | Whether the page reflows without 2-D scrolling | **No.** |
| Focus visibility (SC 2.4.7 / 2.4.11) | Live page, keyboard traversal + computed focus styles | Partially — axe does not fully automate these; requires custom traversal | Whether a keyboard user can see where they are | **No.** |
| Lighthouse accessibility score | Live page | **Yes** — Lighthouse, axe-backed (V32) | A weighted average of binary axe audits. Not an accessibility verdict, and Google does not present it as one | **No.** |

**Every row says No.** That is the finding, not a hedge.

---

## Verdict on screenshot AI-detection

**The skill's current position holds, with two refinements. As of 2026-09-05 I found no published classifier — academic or commercial — that detects AI-*designed* user interfaces from rendered output, with an accuracy figure and a real test set.** Nothing in this sweep should be described as one.

What exists instead, and why none of it is the thing:

1. **Image-forgery detection on screenshot-shaped images (V27, V28).** TextFake (20,000 text-rich images, 14 specialised detectors + 3 frontier VLM APIs) finds **no method above 80% accuracy**, some dropping over 60 points from their natural-image scores, and names *Threshold Collapse* — routine perturbations driving detectors to chance. TextRich (12,095 images including a UI-screenshot category) reports no detector effective across structured categories. **But this is a different task.** These benchmarks ask whether an *image was synthesised by a diffusion/image model*. A headless browser screenshotting real HTML produces a pixel-exact render with no synthesis artefacts at all — TextFake's own *Cloaking via Rendering Fidelity* failure mode is exactly this, taken to its limit. So these papers are evidence that the screenshot *domain* is hostile to detectors; they are not evidence about the skill's question, and should not be cited as if they were.

2. **Text-based site-level detection (V29).** "Did I Just Browse A Website Written by LLMs?" reports **100% accuracy on two hand-built ground-truth sets totalling 120 sites** — a small poster-scale result, not a population accuracy. Crucially it classifies **prose**, aggregated across a site's pages. It confirms that the reliably detectable AI signal on the web is **copy**, which the skill already targets. Adding a render layer will not extend detection; it extends craft measurement.

3. **Commercial "AI website detectors" (V34).** The strongest such claim I could open works on **HTML comments, CSS class conventions, `generator` meta tags, CDN domains, and Vercel/Netlify headers/IP ranges**. It publishes **no accuracy figure, no test set, no validation**, and states outright that AI-written code is indistinguishable from human-written code absent those explicit markers. This is metadata archaeology. It would flag a hand-written page on Vercel as AI and miss an AI-designed page on custom hosting. It is not a visual detector and is not evidence that visual detection works.

**Refinement 1 — "no labelled UI corpus exists" needs softening.** It is no longer strictly true. Design Theater (V21) assembled **120 AI-generated interfaces with standardised 1200×1200 screenshots, code, and reasoning traces**, and V24 assembled **90 AI-generated UIs**, and V25 ran **21,880 accessibility assessments over 54 designers' manual work plus six AI tools' output**. Corpora are appearing. But none is a **paired AI/human screenshot corpus at a scale that could train or validate a classifier**: V21 and V24 are AI-only with no human comparator, and V25 is an accessibility-assessment dataset, not a labelled image set. So the operative claim should be restated as: *labelled AI-UI corpora now exist at the scale of tens-to-low-hundreds of interfaces, all AI-only or accessibility-annotated; no paired AI-vs-human rendered-UI corpus exists, and consequently no detector has been trained or validated on one.*

**Refinement 2 — homogeneity is real but is not a per-page signal.** Both V21 (DHI: visual 0.137, colour 31.9, layout 0.196 mean pairwise) and V24 (UI-Similarity 0.88–0.90) find AI tools converging hard on shared defaults, and V26 finds **92 blind human raters** scoring AI prototypes neutral-to-negative on originality while positive on usability. That is three independent findings that AI output is *conventional*. But **DHI and UI-Similarity are both pairwise measures across multiple generations, and both lack a human baseline** — V21's authors state this explicitly, that DHI is computed only among their five tools "without a reference distribution such as interfaces produced by human designers." A single rendered page has no DHI. Convergence-to-defaults cannot be read off one screenshot, and even across many it has no calibrated human comparator to be scored against.

**One further guardrail, from V35 and the V24/V25 contradiction.** Accessibility quality must never be used as a provenance signal. V24 says AI UIs are highly compliant (violation rate 0.189, no severity-3 or -4 issues). V25 says AI UIs hit **29.0% compliance**. V35 says LLM-generated code is often **more** accessible than human code on contrast and alt text. Three published results, three directions, none replicated. Any inference from "this page passes axe" to "a human made it" — or the reverse — is unsupported.

---

## Recommended render checks

Every check below is a **craft or conformance measurement**. None detects AI. The layer should say so in its own output.

**Accessibility conformance (highest confidence — real spec, real implementation, real SC number):**

1. **Computed colour contrast — WCAG 2.2 SC 1.4.3 Contrast (Minimum), AA, 4.5:1.** axe-core rule `color-contrast`, tagged `wcag143`/`wcag2aa` (V30). Must run on the live page against computed styles, not on CSS declarations. V24 found this is where AI output fails most, and fails by *narrow margins* (4.37:1, 4.46:1, 4.47:1 against a 4.5:1 threshold) — so report the actual ratio, not just pass/fail.
2. **Enhanced contrast — SC 1.4.6, AAA, 7:1.** axe-core `color-contrast-enhanced`, tagged `wcag146` (V30). Report as an aspiration, never as a failure.
3. **Target size — SC 2.5.8 Target Size (Minimum), AA, new in WCAG 2.2.** axe-core `target-size`, tagged `wcag258`/`wcag22aa` (V30, V31). Note this is the 2.2 AA criterion; V24's 44px figure is the older **2.5.5** AAA criterion (renamed Target Size (Enhanced) in 2.2) — do not conflate them.
4. **Zoom not blocked — SC 1.4.4 Resize Text, AA, 200%.** axe-core `meta-viewport`, tagged `wcag144` (V30, V31).
5. **Text spacing tolerance — SC 1.4.12, AA.** Apply the spec's spacing overrides and detect clipping/overlap. Not an axe automated rule; V24 measured it with the Stark plugin. Implement as a scripted restyle-and-reflow, and label it as a custom check.
6. **Reflow — SC 1.4.10, AA.** Render at 320 CSS px width and detect horizontal overflow. No canonical published implementation found, so this is a custom check against a spec, not an inherited one.
7. **Focus visibility — SC 2.4.7 Focus Visible (AA) and SC 2.4.11 Focus Not Obscured (Minimum) (AA, new in 2.2).** Requires scripted keyboard traversal plus computed focus-style inspection. axe does not fully automate these (V30). Custom check, clearly labelled.

**Mandatory caveat on all of the above:** Deque's own study (V33) puts automated coverage at **57% of issue *instances*** — a counting method they adopted in place of "share of WCAG criteria," and one that flatters automation. It is not a claim that 57% of WCAG is automatable. Lighthouse's aggregate accessibility score is a **weighted average of binary axe audits** (V32) and is not an accessibility verdict — report failing audits with their SC numbers, never the score alone.

**Computational aesthetics (craft only — all from AIM, V23, MIT-licensed Python, headless-Chrome pipeline):**

8. **Colour count / palette breadth** — AIM Colour Variability and Static Colour Clusters (Hasler & Süsstrunk 2003; Miniukovich & De Angeli 2014/2015). Correlates with perceived complexity.
9. **Whitespace ratio** — AIM White Space (Miniukovich & De Angeli 2015).
10. **Edge density** — AIM Edge Density (Rosenholtz et al. 2007 clutter model). Correlates with perceived complexity.
11. **Symmetry** — AIM Symmetry.
12. **Layout balance / equilibrium** — AIM Visual Complexity, via Ngo/Teo/Byrne 2003 quadtree decomposition; correlated with rapid aesthetic judgement (Zheng et al. 2009, Reinecke et al. 2013).
13. **Figure-ground contrast** — AIM Figure-Ground Contrast (Hall & Hanna 2004; Reber et al. 2004). A readability proxy distinct from WCAG contrast; worth having both.
14. **Grid / alignment conformity** — AIM Grid Quality. **Caveat:** implemented in MATLAB in the published codebase, so it is not drop-in; either reimplement or drop it.

Report each of 8–14 the way AIM does: a number **plus a comparison distribution**, so it reads as "denser than most pages" rather than as a verdict.

**Optional, and only under its stated constraints:**

15. **UIClip design-quality score** (V22) — screenshot + description → a quality score validated against 12 human designers' rankings. Craft signal. Never described as provenance.
16. **Multi-generation homogeneity, DHI-style** (V21) — only if the skill ever renders **N variants of the same prompt**. Visual similarity via UIClip, colour via CIELCh histograms + Earth Mover's Distance, layout via OmniParser v2 + tree edit distance. Must be reported as tool-vs-tool convergence with **no human baseline**, per the authors' own limitation.

**Capture protocol:** fixed viewport, headless Chrome, standardised screenshot (V21 used 1200×1200 PNG; V23 used headless Chrome plus element segmentation producing id / absolute position / size / base64 per element). Both the aesthetics metrics and the accessibility geometry checks need the same segmentation pass, so capture once and fan out.

---

## Gaps

1. **No paired AI-vs-human rendered-UI corpus exists.** V21 (n=120) and V24 (n=90) are AI-only. V26 has human comparators but its instrument is a 92-person questionnaire, not images. Until someone publishes a paired, labelled, rendered corpus at scale, no detector can be trained or honestly evaluated. This is the single biggest gap, and it is the reason the skill's position holds.
2. **DHI has no reference distribution.** The authors say so. Nobody has computed a DHI-equivalent over a corpus of human-designed deployed sites, so there is no number to say what "normal" convergence looks like. Without that, "homogeneous" is unfalsifiable.
3. **The accessibility literature is in open contradiction and nobody has replicated anything.** V24 (0.189 violation rate, all low severity) vs V25 (29.0% compliance) vs V35 (LLMs often more accessible than humans). Different tools, different criteria, different scoring units, overlapping authorship between V24 and V25. Someone needs to run one protocol across both mockup and rendered-HTML pipelines.
4. **Design Theater is 5 weeks old and has zero citations** (Semantic Scholar, checked 2026-09-05). There is no follow-up work on DHI to draw on. Recheck in six months.
5. **AIM has not been revalidated in the LLM era.** Its metrics are grounded in 2003–2017 perceptual studies on pre-LLM web pages. Whether Colour Variability or Grid Quality distributions have shifted across the 2023–2026 web is unmeasured. Also, two of the 17 metrics (Grid Quality, Visual Search) are MATLAB/Common Lisp and are not practically reusable.
6. **No published implementation for SC 1.4.10 Reflow, 1.4.12 Text Spacing, or 2.4.11 Focus Not Obscured as automated render-time checks.** axe-core does not cover them (V30). Anything the skill builds here is custom code against a spec, with no reference implementation to validate against.
7. **I could not read V25 or V24 through ACM DL (403).** V25's methods are unverified — I have only the CC-BY abstract via the Semantic Scholar API. If the 29.0% figure is going to carry weight in the skill, someone should obtain the full text and check how "compliance" was counted.
8. **Nobody has tested whether the AIM/computational-aesthetics numbers differ at all between AI-generated and human-designed pages.** It is a cheap, obvious experiment — run AIM over V21's 120 AI screenshots and a matched set of human-designed pages — and as far as this sweep found, it has not been done. If it were, and the distributions overlapped (which is the expectation), that would be the first *direct* published evidence for the skill's position rather than the current inference from absence.
