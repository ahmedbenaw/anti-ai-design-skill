#!/usr/bin/env python3
"""Measure one eval output against the mechanical assertions.

The judgment assertions still need a human or a grader agent. Everything here
is a number a tool printed, so that the benchmark never rests on "it looks
fine" - which is the same bar the skill under test holds itself to.
"""
import json, os, subprocess, sys

SKILL = "/Users/ben/Downloads/Repos/Anti-AI-design skill/anti-ai-design-style"
VENV  = "/Users/ben/Downloads/Repos/Anti-AI-design skill/.venv-render/bin/python3"
PY    = VENV if os.path.exists(VENV) else sys.executable


def _json_cmd(cmd):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    except Exception as e:
        return {"_error": str(e)}
    out = p.stdout.strip()
    # Some guards print a human line before the JSON body.
    i = out.find("{")
    if i < 0:
        return {"_error": "no json", "_stderr": p.stderr[-400:], "_stdout": out[-400:]}
    try:
        return json.loads(out[i:])
    except json.JSONDecodeError as e:
        return {"_error": f"bad json: {e}"}


def brand_dir():
    p = subprocess.run([PY, os.path.join(SKILL, "scripts", "find_brand_guard.py")],
                       capture_output=True, text=True)
    return p.stdout.strip() if p.returncode == 0 else None


def measure(path):
    r = {"file": path, "exists": os.path.exists(path)}
    if not r["exists"]:
        return r
    scan = _json_cmd([PY, os.path.join(SKILL, "scripts", "ai_tell_scan.py"), "--json", path])
    r["ai_score"] = scan.get("ai_score")
    r["ai_verdict"] = scan.get("verdict")
    r["fingerprint"] = scan.get("rules_fingerprint")
    r["near_proof"] = len(scan.get("near_proof") or [])
    craft = scan.get("craft_flags") or scan.get("craft") or []
    r["craft_ids"] = sorted({c.get("id", c.get("rule_id", "?")) for c in craft}) if craft else []
    lib = scan.get("library_misuse") or []
    r["library_misuse"] = len(lib) if isinstance(lib, list) else lib
    r["library_ids"] = sorted({l.get("id", l.get("rule_id", "?")) for l in lib}) if isinstance(lib, list) else []

    # copy_check keys its JSON by filename, not at the top level.
    cc = _json_cmd([PY, os.path.join(SKILL, "scripts", "copy_check.py"), "--json", path])
    body = next((v for v in cc.values() if isinstance(v, dict) and "grade" in v), {})
    r["copy_grade"] = body.get("grade")
    r["copy_findings"] = len(body.get("findings") or [])
    r["copy_finding_text"] = body.get("findings") or []
    # The skill's own bar: grade 9 or lower and nothing flagged.
    r["copy_pass"] = (r["copy_grade"] is not None
                      and r["copy_grade"] <= 9.0 and r["copy_findings"] == 0)

    # The brand check ships inside the skill now, so this cannot be missing.
    # An installed anti-antropik-design is recorded as a cross-check only.
    b = _json_cmd([PY, os.path.join(SKILL, "scripts", "brand_distance.py"), "--json", path])
    r["brand"] = b.get("verdict") or b.get("_error", "?")
    v = b.get("violations")
    r["brand_violations"] = v if isinstance(v, int) else len(v or [])
    r["brand_fingerprint"] = b.get("exclusion_fingerprint")
    bd = brand_dir()
    if bd and os.path.exists(os.path.join(bd, "scripts", "audit_file.py")):
        t = _json_cmd([PY, os.path.join(bd, "scripts", "audit_file.py"), "--json", path])
        r["brand_cross_check"] = ("agrees" if t.get("verdict") == r["brand"]
                                  else "DISAGREES: %s" % t.get("verdict"))
    return r


if __name__ == "__main__":
    print(json.dumps([measure(p) for p in sys.argv[1:]], indent=2))
