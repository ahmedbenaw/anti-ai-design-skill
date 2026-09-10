#!/usr/bin/env python3
"""Check that every citation in the tells register still points at something real.

The register cites two different things, and they used to look identical:

    P-T13   a numbered finding inside a research dossier   (hyphen = finding)
    R3      a source entry in sources-compendium.md        (no hyphen = source)

That collision is why this script exists. Before the 2026-09 sweep, `P25` in the
register meant "dossier 01, tell 25", while `P25` in the compendium was about to
mean a completely different source. Nothing crashed; the evidence chain just
quietly stopped meaning what it said. A citation that cannot be resolved is
reported, never assumed good.

Run it with no arguments to check the register, or with --selftest.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(os.path.dirname(HERE), "reference")
RESEARCH = os.path.join(REF, "research")

# Which dossier each letter names, and how that dossier numbers its findings.
# A dossier only appears here once its numbering is machine-readable; anything
# missing is reported as unverifiable rather than silently passed.
DOSSIERS = {
    "P": ("01-practitioners.md", r"^### T(\d+)\.", "T"),
    "A": ("02-academic.md", r"^### F(\d+)\.", "F"),
    "C": ("03-community-wiki.md", r"^(\d+)\. \*\*", ""),
    "V": ("08-visual-science.md", r"^\*\*(\d+)\. ", ""),
}
# Dossier 05 splits into two parts with separate numbering: A = mobile tells,
# B = copy sources. Both are cited as M-A2 / M-B7.
MOBILE = "05-mobile-and-copy.md"

# WCAG technique numbers read exactly like a C-series citation and are not one.
WCAG_TECHNIQUE = re.compile(r"(?:SC \d[\d.]*\s*/\s*|technique )C\d+")

CITE_FINDING = re.compile(r"(?<![A-Za-z0-9-])([A-Z])-([A-Z])(\d{1,3})(?![0-9])")
# A citation letter has to be a category that exists, or every `H1` in a sentence
# about headings reads as a citation.
CATEGORIES = "PACKMXRVL"
CITE_SOURCE = re.compile(r"(?<![A-Za-z0-9-])([" + CATEGORIES + r"])(\d{1,3})(?![0-9])")


def read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def compendium_ids(text):
    return set(re.findall(r"^### ([A-Z]+\d+) ", text, re.M))


def dossier_findings():
    """Map a citation prefix like 'PT' or 'MA' to the numbers that dossier defines."""
    found = {}
    for letter, (filename, pattern, marker) in DOSSIERS.items():
        path = os.path.join(RESEARCH, filename)
        if not os.path.exists(path):
            continue
        nums = set(re.findall(pattern, read(path), re.M))
        found[letter + (marker or "T")] = nums
    path = os.path.join(RESEARCH, MOBILE)
    if os.path.exists(path):
        text = read(path)
        parts = text.split("## Sources")
        # Part A: numbered tells. Part B: numbered rows in the second source table.
        # Both halves label their sources in the table itself: | A1 | ... , | B1 | ...
        found["MA"] = set(re.findall(r"^\| A(\d{1,3}) \|", text, re.M))
        found["MB"] = set(re.findall(r"^\| B(\d{1,3}) \|", text, re.M))
    return found


def check(register_text, compendium_text):
    """Return (resolved, problems, unverifiable)."""
    sources = compendium_ids(compendium_text)
    findings = dossier_findings()
    resolved, problems, unverifiable = 0, [], []

    for number, line in enumerate(register_text.split("\n"), 1):
        stripped = WCAG_TECHNIQUE.sub("", line)
        for match in CITE_FINDING.finditer(stripped):
            key = match.group(1) + match.group(2)
            cite = match.group(0)
            if key not in findings:
                unverifiable.append((number, cite, "no numbering known for " + key))
            elif match.group(3) in findings[key]:
                resolved += 1
            else:
                problems.append((number, cite, "dossier has no finding " + match.group(3)))
        # Bare citations only count once the hyphenated ones are removed, or
        # every "P-T13" would also read as a bare "T13".
        for match in CITE_SOURCE.finditer(CITE_FINDING.sub("", stripped)):
            cite = match.group(0)
            if cite in sources:
                resolved += 1
            else:
                problems.append((number, cite, "not in sources-compendium.md"))
    return resolved, problems, unverifiable


def report(resolved, problems, unverifiable):
    for number, cite, why in problems:
        print("  line %d: %s — %s" % (number, cite, why))
    for number, cite, why in unverifiable:
        print("  line %d: %s — cannot check (%s)" % (number, cite, why))
    print("Citations: %d resolved, %d broken, %d unverifiable."
          % (resolved, len(problems), len(unverifiable)))
    return 0 if not problems else 1


SELFTEST_REGISTER = """
| TY5 | eyebrow | ... | Verified (P-T13, C-T11, V-T23) |
| LA8 | stripe | ... | Verified (P-T22; R3, R6 call it out) |
| MO5 | motion | ... | Verified requirement (X SC 2.3.3/C39, V-T20). |
| XX1 | broken | ... | Verified (P-T999, R999) |
| XX2 | headings | micro-label over every H1/H2 | Verified (R3) |
"""


def selftest():
    compendium = read(os.path.join(REF, "sources-compendium.md"))
    resolved, problems, unverifiable = check(SELFTEST_REGISTER, compendium)
    broken = {cite for _, cite, _ in problems}
    checks = [
        ("a real finding resolves", resolved >= 6),
        ("an out-of-range finding is caught", "P-T999" in broken),
        ("an unknown source is caught", "R999" in broken),
        ("an HTML heading name is not read as a citation", "H1" not in broken),
        ("a real source is not flagged", "R3" not in broken),
        ("a WCAG technique number is not read as a citation", "C39" not in broken),
        ("nothing is silently unverifiable here", not unverifiable),
    ]
    for name, ok in checks:
        if not ok:
            print("SELFTEST: FAIL — " + name)
            return 1
    # And the real register must be clean.
    register = read(os.path.join(REF, "tells-register.md"))
    resolved, problems, unverifiable = check(register, compendium)
    if problems:
        print("SELFTEST: FAIL — the register itself has broken citations:")
        return report(resolved, problems, unverifiable)
    print("SELFTEST: PASS (%d citations resolve in the register, %d unverifiable)"
          % (resolved, len(unverifiable)))
    return 0


HELP = """Check that every citation in the tells register still points at something real.

  python3 scripts/check_citations.py              check the register now
  python3 scripts/check_citations.py --selftest   check the checker, then the register

Two kinds of citation, spelled differently on purpose:
  P-T13   a numbered finding inside reference/research/01-practitioners.md
  R3      a source entry in reference/sources-compendium.md

Exit 0 when every citation resolves, 1 when any does not. Takes about a second.
"""


def main(argv):
    if "--help" in argv or "-h" in argv:
        print(HELP)
        return 0
    if "--selftest" in argv:
        return selftest()
    resolved, problems, unverifiable = check(
        read(os.path.join(REF, "tells-register.md")),
        read(os.path.join(REF, "sources-compendium.md")),
    )
    return report(resolved, problems, unverifiable)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
