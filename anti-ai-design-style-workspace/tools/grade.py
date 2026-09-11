#!/usr/bin/env python3
"""Grade the mechanical assertions from captured measurements.

Judgment assertions are left for a reading pass and marked "judgment" here, so
that nothing silently counts as passed because a script could not check it.
"""
import json, os, re, sys

W = "anti-ai-design-style-workspace/iteration-2"
EVALS = {
    "clinic-landing-page": "clinic.html",
    "student-budget-app-screen": "budget-home.html",
    "deslop-lovable-page": "fixed.html",
}

PLACEHOLDER_PEOPLE = re.compile(r"pravatar|John Doe|Jane Smith|Sarah Chen|randomuser\.me", re.I)
FAKE_STATS = re.compile(r"10[,.]?000\+|10K\+|99\.9%\s*uptime|Trusted by\s*[\d,]+\+", re.I)
GLASSY = re.compile(r"backdrop-filter|glassmorph", re.I)
PURPLE_GRAD = re.compile(r"linear-gradient\([^)]*(#(6|7|8)[0-9a-f]{2}(f|e|d)[0-9a-f]{2}|purple|indigo|violet)", re.I)


def grade(ev, cfg):
    d = f"{W}/{ev}/{cfg}"
    m = json.load(open(f"{d}/measured.json"))[0]
    html_path = f"{d}/outputs/{EVALS[ev]}"
    html = open(html_path, encoding="utf-8", errors="replace").read() if os.path.exists(html_path) else ""
    resp_path = f"{d}/outputs/response.md"
    resp = open(resp_path, encoding="utf-8", errors="replace").read() if os.path.exists(resp_path) else ""
    craft = set(m["craft_ids"])
    out = []

    def add(aid, text, passed, evidence):
        out.append({"id": aid, "text": text, "passed": passed, "evidence": evidence})

    # Judgment verdicts from the reading pass, each with the evidence that
    # settled it, so the grade can be re-checked rather than taken on trust.
    # The button height is measured on the button element at 390px viewport -
    # iteration 1 passed this by reading the phone frame's 844px instead.
    JUDGED = {
      ("clinic-landing-page","with_skill"): {"a5": (True, "EGP x6, WhatsApp/wa.me x9, Alexandria x7, hours x4, therapists x16")},
      ("clinic-landing-page","without_skill"): {"a5": (True, "EGP x12, WhatsApp/wa.me x15, Alexandria x11, hours x7, therapists x23")},
      ("student-budget-app-screen","with_skill"): {
         "a3": (True, "3 class=cat rows: Fares/Handouts/Food on campus, plus allowance and one button"),
         "a4": (True, "button.log measured 56.0px tall at 390px viewport (Playwright bounding box)"),
         "a6": (True, "'23 microbus rides and 7 metro trips', 'photocopy kiosk by gate 3, 1 EGP a page'")},
      ("student-budget-app-screen","without_skill"): {
         "a3": (True, "allowance, 3 categories and a log button present"),
         "a4": (True, "button.cta measured 62.0px tall at 390px viewport (Playwright bounding box)"),
         "a6": (True, "Abou Tarek, microbus/metro, printing mulakhasat, EGP")},
      ("deslop-lovable-page","with_skill"): {
         "a4": (True, "invoicing product and its real sections preserved"),
         "a5": (True, "response.md carries a plain-language change summary"),
         "a6": (True, "4 mentions of placeholder/fake/assumption findings reported to the user")},
      ("deslop-lovable-page","without_skill"): {
         "a4": (True, "product preserved; testimonials and stats kept verbatim"),
         "a5": (True, "response.md carries a plain-language change summary"),
         "a6": (True, "3 mentions; flagged the placeholders honestly but left them in the file")},
    }

    def judgment(aid, text):
        v = JUDGED.get((ev, cfg), {}).get(aid)
        if v is None:
            out.append({"id": aid, "text": text, "passed": None, "evidence": "not yet judged"})
        else:
            out.append({"id": aid, "text": text, "passed": v[0], "evidence": v[1]})

    ai_ok = m["ai_score"] < 20
    if ev == "clinic-landing-page":
        add("a1", "AI-look score below 20", ai_ok, f"ai_score={m['ai_score']}")
        add("a2", "No near-proof findings", m["near_proof"] == 0, f"near_proof={m['near_proof']}")
        add("a3", "No CR1/CR2 craft flags", not (craft & {"CR1", "CR2"}), f"craft={sorted(craft) or 'none'}")
        add("a4", "copy_check passes (grade <= 9, no findings)", bool(m["copy_pass"]),
            f"grade={m['copy_grade']}, findings={m['copy_findings']}")
        judgment("a5", "Three elements specific to this clinic")
        add("a6", "No invented testimonials/stats/logo bars",
            not (PLACEHOLDER_PEOPLE.search(html) or FAKE_STATS.search(html)),
            "no placeholder-person or fake-stat pattern in the HTML")
    elif ev == "student-budget-app-screen":
        add("a1", "AI-look score below 20", ai_ok, f"ai_score={m['ai_score']}")
        add("a2", "No CR1/CR2 craft flags", not (craft & {"CR1", "CR2"}), f"craft={sorted(craft) or 'none'}")
        judgment("a3", "Shows allowance, top 3 categories, log button")
        judgment("a4", "Log-expense button at least 44px tall")
        add("a5", "No purple/indigo gradient, glow or glassmorphism",
            not (PURPLE_GRAD.search(html) or GLASSY.search(html)),
            "no purple-gradient or backdrop-filter pattern")
        judgment("a6", "Two design choices explained by student context")
    else:
        add("a1", "AI-look score below 20 (input scores 52)", ai_ok, f"ai_score={m['ai_score']} (input=52)")
        add("a2", "No placeholder people remain", not PLACEHOLDER_PEOPLE.search(html),
            "no pravatar/John Doe/Jane Smith/Sarah Chen in the HTML")
        add("a3", "No fake stats remain", not FAKE_STATS.search(html),
            "no 10K+/99.9% uptime/Trusted by N+ in the HTML")
        judgment("a4", "Product and real information preserved")
        judgment("a5", "Plain-language summary of changes")
        judgment("a6", "Pre-existing findings reported, not silently fixed")

    add("a7", "audit_file.py reports COMPLIANT (brand gate)", m["brand"] == "COMPLIANT",
        f"{m['brand']}, {m['brand_violations']} violations")
    add("a8", "library_misuse == 0 or justified", m["library_misuse"] == 0,
        f"library_misuse={m['library_misuse']}")
    return {"eval": ev, "config": cfg, "expectations": out, "response_chars": len(resp)}


if __name__ == "__main__":
    allr = []
    for ev in EVALS:
        for cfg in ("with_skill", "without_skill"):
            g = grade(ev, cfg)
            json.dump(g, open(f"{W}/{ev}/{cfg}/grading.json", "w"), indent=2)
            allr.append(g)
    for g in allr:
        e = g["expectations"]
        p = sum(1 for x in e if x["passed"] is True)
        f = sum(1 for x in e if x["passed"] is False)
        j = sum(1 for x in e if x["passed"] is None)
        print(f"  {g['eval']:28} {g['config']:14} mechanical {p}/{p+f} pass, {j} judgment"
              + (("   FAILED: " + ",".join(x["id"] for x in e if x["passed"] is False)) if f else ""))
