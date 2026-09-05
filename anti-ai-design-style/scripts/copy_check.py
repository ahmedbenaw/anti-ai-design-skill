#!/usr/bin/env python3
"""copy_check.py - checks writing for AI-sounding copy and hard-to-read text.

Part of the anti-ai-design-style skill. Python 3.8+, standard library only.

What it does, in plain words:
  1. Reading grade - estimates how hard the text is to read
     (Flesch-Kincaid). Target: grade 9 or lower for anything users read
     (GOV.UK guidance: aim for reading age ~9 even for expert audiences).
  2. Sentence length - flags sentences over 25 words (GOV.UK hard limit;
     comprehension drops below 10% at 43 words).
  3. AI-copy tells - buzzwords, AI cadence phrases, em-dash density,
     fake-proof numbers. These use the same rules.json as the code scanner.

  It works on .md, .txt, and .html files (HTML tags are stripped first).

Usage:
  python3 copy_check.py README.md page.html
  python3 copy_check.py docs/ --max-grade 9
  python3 copy_check.py --selftest

Exit codes: 0 = pass, 1 = findings to fix, 3 = usage error.
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# One loader, used by both run() and selftest(). They read the same rule file
# as ai_tell_scan.py, so a copy tell and a code tell can never drift apart.
sys.path.insert(0, HERE)
from ai_tell_scan import load_rules, fingerprint  # noqa: E402
VOWELS = "aeiouy"


def strip_html(text):
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", text,
                  flags=re.DOTALL | re.IGNORECASE)
    # A closing block tag ends a thought. Insert a full stop so nav links,
    # table cells and headings are not glued into one giant "sentence".
    text = re.sub(r"</(p|li|h[1-6]|td|th|tr|div|section|article|nav|header|"
                  r"footer|button|a|dt|dd|label|figcaption|summary)>|<br\s*/?>",
                  ". ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"(\.\s*){2,}", ". ", text)   # collapse runs of full stops
    text = re.sub(r"&[a-z]+;", " ", text)
    return text


def strip_markdown(text):
    """Keep only running prose. Code, tables, front-matter and quoted
    examples (in backticks or "double quotes") are not the author's voice,
    so they are dropped before scoring."""
    text = re.sub(r"\A---.*?---", " ", text, flags=re.DOTALL)         # front-matter
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)            # code blocks
    text = re.sub(r"`[^`]+`", " ", text)                               # inline code
    text = re.sub(r"^\s*\|.*$", " ", text, flags=re.MULTILINE)         # table rows
    text = re.sub(r"\"[^\"\n]{3,120}\"", " ", text)                    # quoted examples
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)               # links -> text
    # headings and list items end where the line ends - give them a full
    # stop so they are not glued onto the next paragraph as one sentence
    text = re.sub(r"^(#+\s*.+?)\s*$", r"\1.", text, flags=re.MULTILINE)
    text = re.sub(r"^(\s*(?:[-*]|\d+\.)\s+.*[^.!?:\s])\s*$", r"\1.", text, flags=re.MULTILINE)
    text = re.sub(r"\[ \]", " ", text)                                 # checkboxes
    text = re.sub(r"^[#>\-\*\|\s]+", "", text, flags=re.MULTILINE)     # list/heading marks
    return text


def count_syllables(word):
    """Rough but consistent syllable estimate - fine for grade scoring."""
    word = word.lower().strip(".,;:!?\"'()")
    if not word:
        return 0
    count, prev_vowel = 0, False
    for ch in word:
        is_vowel = ch in VOWELS
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel
    if word.endswith("e") and count > 1 and not word.endswith(("le", "ee")):
        count -= 1
    return max(count, 1)


def sentences_of(text):
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [s.strip() for s in parts if len(s.strip().split()) >= 3]


def fk_grade(text):
    sents = sentences_of(text)
    words = [w for s in sents for w in s.split()]
    if not sents or len(words) < 20:
        return None  # too little prose to score honestly
    syllables = sum(count_syllables(w) for w in words)
    grade = (0.39 * (len(words) / len(sents))
             + 11.8 * (syllables / len(words)) - 15.59)
    return round(grade, 1)


def check_text(name, raw, rules, max_grade):
    text = raw
    if name.endswith((".html", ".htm")):
        text = strip_html(text)
    if name.endswith((".md", ".mdx")):
        text = strip_markdown(text)

    findings = []
    lower = text.lower()

    grade = fk_grade(text)
    if grade is not None and grade > max_grade:
        findings.append((
            f"Reading grade {grade} (target: {max_grade} or lower)",
            "Shorter sentences and everyday words. 'Use' beats 'utilize'."))

    long_sents = [s for s in sentences_of(text) if len(s.split()) > 25]
    if long_sents:
        example = " ".join(long_sents[0].split()[:12]) + "..."
        findings.append((
            f"{len(long_sents)} sentence(s) over 25 words (e.g. \"{example}\")",
            "Split them. One idea per sentence."))

    ct = rules["copy_tells"]
    # Headings are labels and cited titles, not the author's own marketing
    # copy. A paper called "Unlocking ..." is a proper noun, not a buzzword.
    # Drop headings from the RAW text, before the markdown marks are stripped.
    if name.endswith((".md", ".mdx")):
        body_raw = "\n".join(ln for ln in raw.splitlines()
                             if not re.match(r"^\s*#", ln))
        body_only = strip_markdown(body_raw).lower()
    else:
        body_only = lower
    buzz = sorted({w for w in ct["transformation_verbs"] if w in body_only})
    if buzz:
        findings.append((
            "Buzzwords: " + ", ".join(buzz[:6]),
            "Swap each for the concrete thing the product does."))
    # Cadence is scored per era, and never on a single hit. One fashionable
    # word is a coincidence; several together is a habit. The 2025 bucket
    # needs three because those words - "enhance", "highlighting" - are
    # ordinary marketing English. Two of them in honest copy is normal, and
    # a rule that flags honest copy gets switched off, taking the rest with it.
    for key, need, era in (("ai_cadence", 2, "structural"),
                           ("ai_cadence_legacy_2023", 2, "2023-24 era"),
                           ("ai_cadence_current_2025", 3, "2025-26 era"),
                           ("ai_cadence_generator_specific", 3, "Grok-flavoured")):
        hits = sorted({w for w in ct.get(key, []) if w in body_only})
        if len(hits) >= need:
            findings.append((
                "AI cadence phrases (%s): %s" % (era, ", ".join(hits[:4])),
                "Rewrite in the words you would say out loud to a customer."))

    words_n = max(len(text.split()), 1)
    # Count dashes in running prose only. A dash used as a separator in a
    # heading ("Part 1 - Setup") or a list label ("- `cmd` - what it does")
    # is typography, not the AI writing cadence the register describes.
    no_code = re.sub(r"```.*?```", " ", raw, flags=re.DOTALL)
    no_code = re.sub(r"\A---.*?---", " ", no_code, flags=re.DOTALL)
    prose_lines = []
    for ln in no_code.splitlines():
        if re.match(r"^\s*(#|\|)", ln):
            continue                      # headings and table rows: typography
        # drop the list marker itself so "  - item" is not counted as a dash
        ln = re.sub(r"^\s*([-*+]|\d+\.)\s+", "", ln)
        prose_lines.append(ln)
    prose = "\n".join(prose_lines)
    dashes = prose.count("—") + len(re.findall(r"\S[ \t]--?[ \t]\S", prose))
    per_1000 = dashes * 1000 / words_n
    if dashes >= 3 and per_1000 > 8:
        findings.append((
            f"Heavy em-dash use ({dashes} dashes, ~{per_1000:.0f} per 1000 words)",
            "Most can become commas, colons, or full stops."))

    for pat in ct["fake_proof_regex"]:
        m = re.search(pat, text)
        if m:
            findings.append((
                f"Unverifiable-looking stat: \"{m.group(0)}\"",
                "Real number you can back up, or cut the claim."))
            break

    return grade, findings


def run(paths, max_grade, as_json=False):
    rules = load_rules()
    files = []
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, fs in os.walk(p):
                dirs[:] = [d for d in dirs if d not in
                           {"node_modules", ".git", "dist", "build"}]
                files += [os.path.join(root, x) for x in fs
                          if x.endswith((".md", ".mdx", ".txt", ".html", ".htm"))]
        elif os.path.isfile(p):
            files.append(p)
    if not files:
        print("No .md/.txt/.html files found to check.")
        return 3

    any_findings = False
    results = {}
    for path in files:
        with open(path, encoding="utf-8", errors="replace") as f:
            raw = f.read()
        grade, findings = check_text(path, raw, rules, max_grade)
        results[path] = {"grade": grade, "findings": [f[0] for f in findings]}
        if not as_json:
            gtxt = f"grade {grade}" if grade is not None else "too short to grade"
            print(f"\n{path}  ({gtxt})")
            if findings:
                any_findings = True
                for what, fix in findings:
                    print(f"  - {what}")
                    print(f"    do this: {fix}")
            else:
                print("  reads clean")
        elif findings:
            any_findings = True
    if as_json:
        print(json.dumps(results, indent=2))
    else:
        print("\nVerdict:", "FIX AND RE-CHECK" if any_findings else "PASS")
    return 1 if any_findings else 0


SLOP_COPY = """Elevate your workflow with our cutting-edge, all-in-one platform.
In today's fast-paced world, it's not just a tool - it's a revolution - a
comprehensive solution that seamlessly integrates every aspect of your
operational infrastructure while simultaneously empowering your organization
to unlock unprecedented productivity gains across all departments and teams.
Trusted by 10,000+ teams. 99.9% uptime."""

CLEAN_COPY = """Fadl's Ledger tracks the invoices your bakery sends each week.
You type a customer's name once. After that, the app fills it in for you.
Most bakeries finish their weekly billing in ten minutes.
It costs 120 EGP a month. The first month is free."""


# Copy in the vocabulary era current as of 2026. These words are ordinary
# marketing English, unlike "delve" or "tapestry", so the scanner must need
# several of them together before it says anything.
CURRENT_ERA_COPY = """
Our platform emphasizing collaboration is designed to enhance how your team
works. By highlighting the metrics that matter and showcasing progress in real
time, we align with the way modern teams operate. Take a deep dive into your
data and see the difference.
"""

# The false-positive guard. Real human product copy that happens to reach for
# two of the same ordinary words. If the scanner flags this, the rule is worse
# than useless: people will turn it off and lose the rest of the checks too.
HONEST_MARKETING_COPY = """
We built this to enhance the weekly shop. It shows what you spent, and it
sorts the list by aisle so you walk the shop once. Two taps to add a receipt.
No account needed for the first month.
"""


def selftest():
    rules = load_rules()
    g1, f1 = check_text("slop.txt", SLOP_COPY, rules, 9)
    g2, f2 = check_text("clean.txt", CLEAN_COPY, rules, 9)
    _, f3 = check_text("current-era.txt", CURRENT_ERA_COPY, rules, 9)
    _, f4 = check_text("honest.txt", HONEST_MARKETING_COPY, rules, 9)
    problems = []
    if not any("cadence" in x[0].lower() for x in f3):
        problems.append(
            "current-era AI copy was not caught as cadence: "
            f"{[x[0] for x in f3]}")
    if any("cadence" in x[0].lower() for x in f4):
        problems.append(
            "honest marketing copy wrongly flagged as AI cadence: "
            f"{[x[0] for x in f4]}")
    if len(f1) < 3:
        problems.append(f"slop copy raised only {len(f1)} findings: {[x[0] for x in f1]}")
    if f2:
        problems.append(f"clean copy wrongly flagged: {[x[0] for x in f2]}")
    if g2 is not None and g2 > 9:
        problems.append(f"clean copy graded {g2}, expected <= 9")
    if problems:
        print("SELFTEST: FAIL")
        for p in problems:
            print("  -", p)
        return 1
    print(f"SELFTEST: PASS (slop copy: {len(f1)} findings, grade {g1};"
          f" clean copy: 0 findings, grade {g2};"
          f" current-era copy caught; honest copy not flagged)")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check writing for AI-sounding copy and readability.")
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--max-grade", type=float, default=9.0)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.paths:
        ap.print_help()
        return 3
    return run(args.paths, args.max_grade, args.json)


if __name__ == "__main__":
    sys.exit(main())
