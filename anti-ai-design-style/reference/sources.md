# Where the evidence lives

**TL;DR:** every rule here traces to a source that was opened and read.
The full dossiers are bundled in `reference/research/`. Each one carries a
source table, URLs, dates, quotes, counter-evidence and a gap list.
`sources-compendium.md` indexes all 254 entries with adopt and avoid tags.

| File | What it holds | Sources |
|---|---|---|
| `research/01-practitioners.md` | Designer/developer articles on AI-look tells; 41 tells; fixes; false-positive list | 24 |
| `research/02-academic.md` | arXiv/CHI papers: homogeneity measurements, benchmarks, detection limits | 18 papers |
| `research/03-community-wiki.md` | Hacker News, Wikipedia, Indie Hackers, GitHub; 45 tells; the pre-AI "generic" history | 23 |
| `research/04-code-patterns.md` | **Measured** pattern counts on 12 verified AI-generated repos (Lovable, v0, Bolt, Replit, Claude, GPT-3-era) | 12 repos |
| `research/05-mobile-and-copy.md` | Mobile-app tells + UI/marketing copy tells (incl. Wikipedia's Signs of AI Writing, read in full) | 20 |
| `research/06-accessibility.md` | WCAG 2.2, W3C COGA, British Dyslexia Association, GOV.UK — exact thresholds with criterion numbers | 29 |
| `research/07-prior-art.md` | Existing anti-slop tools, linters, prompting guides — what this skill reuses and what nobody built | 20 |
| `research/08-visual-science.md` | Colour statistics, imagery forensics, sparkle-icon studies, motion authorities | 20 |

Three honesty notes, so nobody over-trusts this skill:

1. **Some findings conflict.** NN/g found nobody reads the sparkle icon as
   "AI". Google's larger study found their users do. AI hero images now out-score real stock
   photos on trust when origin is hidden. The register keeps both sides.
2. **Several dossiers list gaps.** Things searched for and not found
   (Reddit was unreachable; no Vue/Flutter code samples; the "bento = AI"
   claim has no rigorous source). Rules were not written for those gaps.
3. **Detection has limits.** Humans score near chance on AI imagery;
   photo-trained detectors fail on UI screenshots. Every non-provenance
   tell also appears in some human work. That is why the scanner scores
   co-occurrence and never calls a single ordinary pattern "proof".
