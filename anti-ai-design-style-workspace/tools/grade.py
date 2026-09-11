#!/usr/bin/env python3
"""Grade the mechanical assertions from captured measurements.

Usage: grade.py [iteration-dir]   (default: iteration-2)

Reads each eval's eval_metadata.json for its name and assertions, and picks
the output page as the one .html in outputs/ that is not input.html, the way
capture.sh does. Judgment assertions are left as None until a reading pass
records a verdict with evidence; the benchmark builder refuses to count a
None as a pass or a fail.
"""
import glob, json, os, re, sys

W = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "anti-ai-design-style-workspace/iteration-2"


def evals_in(w):
    out = {}
    for meta in sorted(glob.glob(os.path.join(w, "*", "eval_metadata.json"))):
        d = json.load(open(meta))
        out[d["eval_name"]] = d
    return out


def output_html(run_dir):
    cands = [p for p in glob.glob(os.path.join(run_dir, "outputs", "*.html"))
             if os.path.basename(p) != "input.html"]
    return cands[0] if cands else None


EVALS = evals_in(W)

PLACEHOLDER_PEOPLE = re.compile(r"pravatar|John Doe|Jane Smith|Sarah Chen|randomuser\.me", re.I)
FAKE_STATS = re.compile(r"10[,.]?000\+|10K\+|99\.9%\s*uptime|Trusted by\s*[\d,]+\+", re.I)
GLASSY = re.compile(r"backdrop-filter|glassmorph", re.I)
PURPLE_GRAD = re.compile(r"linear-gradient\([^)]*(#(6|7|8)[0-9a-f]{2}(f|e|d)[0-9a-f]{2}|purple|indigo|violet)", re.I)


def grade(ev, cfg):
    d = f"{W}/{ev}/{cfg}"
    m = json.load(open(f"{d}/measured.json"))[0]
    html_path = output_html(d) or ""
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
      ("scroll-story-with-library","with_skill"): {
         "a3": (True, "5 <section> steps (01-05) plus a Leaflet map section with OSM attribution and the address as text"),
         "a5": (True, "springs not the Nile; salty sandy soil; groves in date-palm shade; near the fortress of Shali; Matrouh Governorate; town-centre pin flagged as a stand-in"),
         "a6": (True, "no testimonials, awards or counts; '27 degrees' is a process claim, not proof; only '100%'/'85%' hits are CSS max-width and a ScrollTrigger start")},
      ("scroll-story-with-library","without_skill"): {
         "a3": (True, "5 numbered sections (grove, harvest, press, rest, bottle) plus a 'Where to find us' Leaflet map with OSM attribution"),
         "a5": (True, "Siwi olive variety; springs not the Nile; ~50 km from the Libyan border; salt lakes; Matrouh Governorate"),
         "a6": (True, "no testimonials, awards or statistics; 'a few hundred very old trees' is descriptive, not a proof number; '100%'/'85%' hits are CSS and ScrollTrigger")},
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
    elif ev == "deslop-lovable-page":
        add("a1", "AI-look score below 20 (input scores 50)", ai_ok, f"ai_score={m['ai_score']} (input=50)")
        add("a2", "No placeholder people remain", not PLACEHOLDER_PEOPLE.search(html),
            "no pravatar/John Doe/Jane Smith/Sarah Chen in the HTML")
        add("a3", "No fake stats remain", not FAKE_STATS.search(html),
            "no 10K+/99.9% uptime/Trusted by N+ in the HTML")
        judgment("a4", "Product and real information preserved")
        judgment("a5", "Plain-language summary of changes")
        judgment("a6", "Pre-existing findings reported, not silently fixed")
    else:
        # Any newer eval: the shared mechanical set, judgment items by id text.
        add("a1", "AI-look score below 20", ai_ok, f"ai_score={m['ai_score']}")
        add("a2", "No CR1/CR2 craft flags", not (craft & {"CR1", "CR2"}), f"craft={sorted(craft) or 'none'}")
        for a in EVALS[ev]["assertions"]:
            if a["check"] == "judgment":
                judgment(a["id"], a["text"])
            elif a["id"] == "a4":
                add("a4", a["text"], bool(m["copy_pass"]), f"grade={m['copy_grade']}, findings={m['copy_findings']}")

    # a9: visible text only. Strip tags and scripts first, then look for a
    # bracketed run that reads like a placeholder: all-caps words, or ending
    # in "name", or starting with a field word. Markdown links are not HTML.
    import html as _h
    visible = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", html, flags=re.S | re.I)
    visible = _h.unescape(re.sub(r"<[^>]+>", " ", visible))
    PLACEHOLDER = re.compile(r"\[\s*(?:[A-Z][A-Z ]{2,40}|[A-Za-z ]{2,30}\bname|(?:Street|Address|Phone|Email|Logo|Your|Landmark)\b[^\]]{0,40})\s*\]")
    ph = PLACEHOLDER.findall(visible)
    add("a9", "No bracketed placeholders remain in visible copy", not ph,
        ("none found" if not ph else f"{len(ph)} found, e.g. {ph[0][:40]!r}"))
    add("a7", "brand_distance.py reports COMPLIANT (brand gate)", m["brand"] == "COMPLIANT",
        f"{m['brand']}, {m['brand_violations']} violations")
    add("a8", "library_misuse == 0 or justified", m["library_misuse"] == 0,
        f"library_misuse={m['library_misuse']}")
    return {"eval": ev, "config": cfg, "expectations": out, "response_chars": len(resp)}


if __name__ == "__main__":
    allr = []
    for ev in EVALS:
        for cfg in ("with_skill", "without_skill"):
            if not os.path.exists(f"{W}/{ev}/{cfg}/measured.json"):
                continue
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
