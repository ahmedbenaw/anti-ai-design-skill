"""Verdict-for-verdict comparison: our brand_distance.py vs the installed
anti-antropik-design audit_file.py, on every HTML page we have. Any difference
is printed. Exit 1 on any difference."""
import glob, json, os, subprocess, sys
ROOT = "/Users/ben/Downloads/Repos/Anti-AI-design skill"
OURS = os.path.join(ROOT, "anti-ai-design-style/scripts/brand_distance.py")
BG = subprocess.run([sys.executable, os.path.join(ROOT, "anti-ai-design-style/scripts/find_brand_guard.py")],
                    capture_output=True, text=True).stdout.strip()
THEIRS = os.path.join(BG, "scripts/audit_file.py")
pages = []
for pat in sys.argv[1:]:
    pages += glob.glob(pat, recursive=True)
pages = sorted(set(p for p in pages if "partial-429" not in p))
def run(cmd):
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    return json.loads(out[out.index("{"):])
diffs = 0
for p in pages:
    a = run([sys.executable, OURS, "--json", p]); b = run([sys.executable, THEIRS, "--json", p])
    fa, fb = a["files"][0], b["files"][0]
    ours = {"verdict": a["verdict"], "violations": a["violations"],
            "fail_colors": sorted(c["hex"] for c in fa["colors"] if c["verdict"] == "FAIL"),
            "fail_fonts": sorted(f["family"] for f in fa["fonts"] if f["verdict"] == "FAIL"),
            "n_colors": len(fa["colors"]), "n_fonts": len(fa["fonts"])}
    theirs = {"verdict": b["verdict"], "violations": b["violations"],
              "fail_colors": sorted(c["hex"] for c in fb["colors"] if c["verdict"] == "FAIL"),
              "fail_fonts": sorted(f["family"] for f in fb["fonts"] if f["verdict"] == "FAIL"),
              "n_colors": len(fb["colors"]), "n_fonts": len(fb["fonts"])}
    same = ours == theirs
    diffs += 0 if same else 1
    print("%s %-70s ours=%s/%d theirs=%s/%d" % ("same" if same else "DIFF", p[-70:], ours["verdict"], ours["violations"], theirs["verdict"], theirs["violations"]))
    if not same:
        for k in ours:
            if ours[k] != theirs[k]: print("      %s: ours=%s theirs=%s" % (k, ours[k], theirs[k]))
print("pages: %d, differences: %d, fingerprints ours=%s theirs=%s" % (len(pages), diffs, a["exclusion_fingerprint"], b["exclusion_fingerprint"]))
sys.exit(1 if diffs else 0)
