#!/usr/bin/env python3
"""Run every guard over some files and print one line you can quote.

Why this exists: there are three separate checks, and a page can pass one
while failing another. Four of four pages this skill generated passed the
AI-look scanner and failed the brand guard. When each check is run by hand,
the easy mistake is to quote the one that passed.

So this runs all of them and prints a single verdict line. If a guard could
not run, the line says so and the verdict is FAIL. A missing check never
reads as a passing check. Exit 0 means every guard actually ran and passed.

Usage:
  python3 verify_all.py page.html styles.css
  python3 verify_all.py page.html --json
"""

import argparse
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ai_tell_scan import fingerprint, load_rules  # noqa: E402
from find_brand_guard import locate, source_of  # noqa: E402

NOT_RUN = "NOT RUN"


def band_label(score, rules):
    """The short half of the band text, for a line that stays readable.

    The register writes bands as "distinct - no meaningful AI-look signals".
    The part before the dash is the label; the rest is advice that belongs in
    the scanner's own output, not in a one-line summary.
    """
    for low, high, text in rules["scoring"]["ai_bands"]:
        if low <= score <= high:
            return text.split(" - ")[0].strip()
    return "unknown band"


def _json_cmd(cmd):
    """Run a tool and return its parsed JSON, or None if it could not run."""
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except OSError:
        return None
    try:
        return json.loads(out.stdout)
    except ValueError:
        return None


def render_result(paths, enabled, allow_network=False):
    """Run the rendered check if it can run at all.

    It is optional by design, and a missing browser must not fail the build:
    most of this skill works without one. But "not installed" and "installed
    and failing" have to look different in the proof line, or a skipped check
    reads as a passed one.
    """
    if not enabled:
        return {"state": "SKIPPED", "detail": "not requested"}
    html = [p for p in paths if p.lower().endswith((".html", ".htm"))]
    if not html:
        return {"state": "SKIPPED", "detail": "no HTML files given"}
    try:
        import playwright  # noqa: F401
    except ImportError:
        return {"state": "SKIPPED", "detail": "playwright not installed"}
    worst = "PASS"
    fails = 0
    for f in html:
        cmd = [sys.executable, os.path.join(HERE, "render_check.py"), "--json", f]
        if allow_network:
            cmd.append("--allow-network")
        data = _json_cmd(cmd)
        if data is None:
            return {"state": "ERROR", "detail": "render_check did not run"}
        fails += data.get("aa_failures", 0)
        if data["verdict"] == "INCONCLUSIVE":
            worst = "INCONCLUSIVE"
        elif data["verdict"] == "FAIL" and worst != "INCONCLUSIVE":
            worst = "FAIL"
    return {"state": worst, "detail": "{} WCAG AA failures".format(fails),
            "aa_failures": fails}


def gather(paths, brand_dir, max_grade=9.0, render=False, allow_network=False):
    """brand_dir=None means the guard was not found. A guard that was found
    and then produced no JSON is a different failure and is reported as such,
    because telling someone to install a thing they already have is the kind
    of advice that gets a tool uninstalled."""
    """Run the guards and collect what each one reported.

    brand_dir is passed in rather than looked up here so the fail-closed path
    can be tested directly. Relying on an env var would not work: on a machine
    where the guard is installed, an override pointing at nothing simply falls
    through to the real copy and the test would pass without testing anything.
    """
    scan = _json_cmd([sys.executable, os.path.join(HERE, "ai_tell_scan.py"),
                      "--json"] + list(paths))
    copy = _json_cmd([sys.executable, os.path.join(HERE, "copy_check.py"),
                      "--json", "--max-grade", str(max_grade)] + list(paths))
    brand = None
    if brand_dir:
        brand = _json_cmd([sys.executable,
                           os.path.join(brand_dir, "scripts", "audit_file.py"),
                           "--json"] + list(paths))
    return {"scan": scan, "copy": copy, "brand": brand,
            "brand_found": brand_dir is not None,
            "brand_source": source_of(brand_dir) if brand_dir else None,
            "render": render_result(paths, render, allow_network)}


def summarise(results, rules):
    """Reduce the three reports to the facts the proof line states.

    Each guard's own verdict decides its half of the gate. This adds no new
    threshold: a rule that fails a page here but not in the scanner would be
    a rule with no row in the register and no fixture behind it.
    """
    scan, copy, brand = results["scan"], results["copy"], results["brand"]

    if scan is None:
        s = {"ok": False, "score": None, "band": "scan DID NOT RUN",
             "craft": None, "lib": None,
             "register": rules.get("register_version", "?"),
             "fingerprint": fingerprint()}
    else:
        s = {"ok": scan["verdict"] == "PASS",
             "score": scan["ai_score"],
             "band": band_label(scan["ai_score"], rules),
             "craft": len(scan["craft_flags"]),
             "lib": len(scan["library_misuse"]),
             "register": scan["register_version"],
             "fingerprint": scan["rules_fingerprint"]}

    if copy is None:
        c = {"ok": False, "grade": None}
    else:
        findings = sum(len(v.get("findings", [])) for v in copy.values())
        grades = [v["grade"] for v in copy.values() if v.get("grade") is not None]
        c = {"ok": findings == 0,
             "grade": max(grades) if grades else None,
             "findings": findings}

    if brand is None:
        found = results.get("brand_found", False)
        b = {"ok": False, "fingerprint": None,
             "verdict": "DID NOT RUN" if found else NOT_RUN}
    else:
        b = {"ok": brand["verdict"] == "COMPLIANT",
             "verdict": brand["verdict"],
             "fingerprint": brand.get("exclusion_fingerprint"),
             "source": results.get("brand_source")}

    # A skipped render check does not fail the run: it is optional, and
    # unlike the brand guard it measures craft the other scanners already
    # partly cover. An INCONCLUSIVE or failing one does fail, because that
    # means it ran and found something.
    r = results.get("render") or {"state": "SKIPPED", "detail": "not run"}
    r_ok = r["state"] in ("PASS", "SKIPPED")

    return {"scan": s, "copy": c, "brand": b, "render": r,
            "passed": s["ok"] and c["ok"] and b["ok"] and r_ok}


def proof_line(summary):
    """One quotable line. It leads with the verdict, never with "Verified".

    Leading with a claim of verification and then admitting a guard did not
    run is a sentence that argues with itself. The verdict comes first so a
    skimmed line cannot be misread as a pass.
    """
    s, c, b = summary["scan"], summary["copy"], summary["brand"]
    score = "{}/100".format(s["score"]) if s["score"] is not None else "not run"
    craft = s["craft"] if s["craft"] is not None else "?"
    lib = s["lib"] if s["lib"] is not None else "?"
    grade = c["grade"] if c["grade"] is not None else "not run"
    r = summary.get("render") or {"state": "SKIPPED"}
    return ("{verdict}: AI-look {score} ({band}), craft flags {craft}, "
            "library misuse {lib}, copy grade {grade}, brand distance {brand}, "
            "rendered {render} | register {reg}, rules {rf}, brand rules {bf}{src}"
            ).format(
        verdict="PASS" if summary["passed"] else "FAIL",
        score=score, band=s["band"], craft=craft, lib=lib, grade=grade,
        brand=b["verdict"], render=r["state"], reg=s["register"],
        src=(" ({})".format(b["source"]) if b.get("source") and b.get("fingerprint") else ""),
        rf=s["fingerprint"], bf=b["fingerprint"] or "-")


def selftest():
    """Test the gate itself with synthetic reports, including every miss."""
    rules = load_rules()
    good = {
        "scan": {"verdict": "PASS", "ai_score": 0, "craft_flags": [],
                 "library_misuse": [], "register_version": "2026.09",
                 "rules_fingerprint": "abc123"},
        "copy": {"page.html": {"grade": 4.6, "findings": []}},
        "brand": {"verdict": "COMPLIANT", "exclusion_fingerprint": "def456"},
        "render": {"state": "PASS", "detail": "0 WCAG AA failures"},
    }
    checks = []

    ok = summarise(good, rules)
    checks.append(("all three passing gives PASS", ok["passed"]))
    checks.append(("PASS line names both fingerprints",
                   "abc123" in proof_line(ok) and "def456" in proof_line(ok)))

    missing = dict(good, brand=None)
    m = summarise(missing, rules)
    checks.append(("missing brand guard fails the gate", not m["passed"]))
    checks.append(("missing brand guard says NOT RUN",
                   NOT_RUN in proof_line(m)))
    checks.append(("a failing line never claims Verified",
                   not proof_line(m).startswith("Verified")))
    checks.append(("a failing line leads with FAIL",
                   proof_line(m).startswith("FAIL")))

    bad_scan = dict(good, scan=dict(good["scan"], verdict="FAIL", ai_score=52))
    b = summarise(bad_scan, rules)
    checks.append(("a failing scan fails the gate", not b["passed"]))
    checks.append(("band label is the short form",
                   b["scan"]["band"] == "reads as AI-generated"))

    bad_copy = dict(good, copy={"p.html": {"grade": 14.0,
                                           "findings": [{"x": 1}]}})
    checks.append(("copy findings fail the gate",
                   not summarise(bad_copy, rules)["passed"]))

    noncompliant = dict(good, brand={"verdict": "NON-COMPLIANT",
                                     "exclusion_fingerprint": "def456"})
    checks.append(("a NON-COMPLIANT brand verdict fails the gate",
                   not summarise(noncompliant, rules)["passed"]))

    skipped = dict(good, render={"state": "SKIPPED",
                                 "detail": "playwright not installed"})
    sk = summarise(skipped, rules)
    checks.append(("a skipped render check does not fail the run", sk["passed"]))
    checks.append(("the line still says the render check was skipped",
                   "rendered SKIPPED" in proof_line(sk)))

    r_fail = dict(good, render={"state": "FAIL", "detail": "2 WCAG AA failures"})
    checks.append(("a failing render check fails the run",
                   not summarise(r_fail, rules)["passed"]))
    r_inc = dict(good, render={"state": "INCONCLUSIVE", "detail": "styles blocked"})
    checks.append(("an inconclusive render check fails the run",
                   not summarise(r_inc, rules)["passed"]))

    dead = {"scan": None, "copy": None, "brand": None}
    checks.append(("every guard missing fails the gate",
                   not summarise(dead, rules)["passed"]))

    for label, passed in checks:
        print("  {} {}".format("ok  " if passed else "FAIL", label))
    allok = all(p for _, p in checks)
    print("SELFTEST: {}".format("PASS" if allok else "FAIL"))
    return 0 if allok else 1


def main():
    ap = argparse.ArgumentParser(
        description="Run every design guard and print one verdict line.")
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--max-grade", type=float, default=9.0)
    ap.add_argument("--json", action="store_true",
                    help="print the full summary as JSON as well")
    ap.add_argument("--allow-network", action="store_true",
                    help="let the rendered check load fonts, CDNs and images; "
                         "use for live sites, never for the repeatable local check")
    ap.add_argument("--render", action="store_true",
                    help="also load the page in a browser and measure craft. "
                         "Needs playwright; skipped cleanly without it")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if not args.paths:
        ap.error("give me at least one file to check")

    brand_dir = locate()
    summary = summarise(gather(args.paths, brand_dir, args.max_grade,
                               render=args.render,
                               allow_network=args.allow_network), load_rules())
    if args.json:
        print(json.dumps(summary, indent=2))
    print(proof_line(summary))
    if not brand_dir:
        sys.stderr.write(
            "\nThe brand guard did not run, so this is a FAIL no matter what "
            "the other checks said.\nInstall anti-antropik-design, or set "
            "ANTI_ANTROPIK_PATH to point at it.\n")
    return 0 if summary["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
