#!/usr/bin/env python3
"""Build benchmark.json in the viewer's schema from the captured evidence.

The bundled aggregate_benchmark.py expects eval-N/<config>/run-N directories.
This workspace uses named eval directories with one run per cell, matching
iteration 1, so the numbers are assembled here instead of restructuring the
workspace and breaking the comparison with iteration 1.
"""
import json, statistics, datetime, glob, os, sys

W = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "anti-ai-design-style-workspace/iteration-2"
EVALS = []
for meta in sorted(glob.glob(os.path.join(W, "*", "eval_metadata.json"))):
    d = json.load(open(meta)); EVALS.append((d["eval_name"], d["eval_id"]))
runs, by_cfg = [], {"with_skill": [], "without_skill": []}

for name, eid in EVALS:
    for cfg in ("with_skill", "without_skill"):
        g = json.load(open(f"{W}/{name}/{cfg}/grading.json"))
        t = json.load(open(f"{W}/{name}/{cfg}/timing.json"))
        m = json.load(open(f"{W}/{name}/{cfg}/measured.json"))[0]
        unjudged = [e["id"] for e in g["expectations"] if e["passed"] is None]
        if unjudged:
            sys.exit(f"REFUSING: {name}/{cfg} has unjudged assertions {unjudged}; "
                     "record a verdict with evidence in grade.py before building a benchmark")
        exp = [{"text": f"{e['id']}: {e['text']}", "passed": bool(e["passed"]), "evidence": e["evidence"]}
               for e in g["expectations"]]
        passed = sum(1 for e in exp if e["passed"])
        total = len(exp)
        runs.append({
            "eval_id": eid, "eval_name": name, "configuration": cfg, "run_number": 1,
            "result": {"pass_rate": round(passed / total, 4), "passed": passed,
                       "failed": total - passed, "total": total,
                       "time_seconds": t["total_duration_seconds"], "tokens": t["total_tokens"],
                       "tool_calls": t.get("tool_uses", 0), "errors": 0},
            "expectations": exp,
            "notes": [f"AI-look {m['ai_score']}/100", f"craft {m['craft_ids'] or 'none'}",
                      f"copy grade {m['copy_grade']}", f"brand {m['brand']} ({m['brand_violations']})",
                      f"library misuse {m['library_misuse']}", f"fingerprint {m['fingerprint']}"],
        })
        by_cfg[cfg].append((passed / total, t["total_duration_seconds"], t["total_tokens"]))


def stat(vals):
    return {"mean": round(statistics.mean(vals), 4),
            "stddev": round(statistics.stdev(vals), 4) if len(vals) > 1 else 0.0,
            "min": round(min(vals), 4), "max": round(max(vals), 4)}


summary = {c: {"pass_rate": stat([v[0] for v in r]),
               "time_seconds": stat([v[1] for v in r]),
               "tokens": stat([v[2] for v in r])} for c, r in by_cfg.items()}

out = {
    "metadata": {
        "skill_name": "anti-ai-design-style",
        "skill_path": os.path.abspath("anti-ai-design-style"),
        "executor_model": "claude-opus-5",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "evals_run": [e[1] for e in EVALS],
        "runs_per_configuration": 1,
        "note": "n = 1 per cell. No stddev claim is made across repeats; the "
                "stddev fields describe spread across the three evals, not across repeats.",
    },
    "runs": runs,
    "run_summary": summary,
}
json.dump(out, open(f"{W}/benchmark.json", "w"), indent=2)
wp = summary["with_skill"]["pass_rate"]["mean"]
bp = summary["without_skill"]["pass_rate"]["mean"]
tw=sum(r['result']['total'] for r in runs if r['configuration']=='with_skill')
tb=sum(r['result']['total'] for r in runs if r['configuration']=='without_skill')
print(f"  with_skill    {wp:.1%}   ({sum(r['result']['passed'] for r in runs if r['configuration']=='with_skill')}/{tw})")
print(f"  without_skill {bp:.1%}   ({sum(r['result']['passed'] for r in runs if r['configuration']=='without_skill')}/{tb})")
print(f"  delta         {wp-bp:+.1%}")
