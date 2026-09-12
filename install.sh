#!/bin/sh
# anti-ai-design-style installer (POSIX) — macOS / Linux / Unix.
#
# It installs this skill and nothing else. It does not fetch Node, npm
# packages, or any other tool, and it does not shell out to a third-party
# installer. Everything it writes is listed before it writes it, and every
# path it touches belongs to this skill.
#
# Needs only `sh` + one of curl/wget (OS defaults). The two hooks run on
# python3, which ships with macOS and most Linux; if it is missing the
# installer says so and prints the one command to fix it, rather than
# installing software you did not ask for.
#
#   curl -fsSL https://raw.githubusercontent.com/ahmedbenaw/anti-ai-design-skill/main/install.sh | sh
#
# Flags: --yes --dry-run --only <ids> --skip <ids> --owner <name> --details --uninstall
#        ids: claude-code, codex
set -eu

OWNER="ahmedbenaw"
REPO_NAME="anti-ai-design-skill"
SKILL="anti-ai-design-style"
REPO_DEFAULT_TARBALL="https://github.com/${OWNER}/${REPO_NAME}/archive/refs/heads/main.tar.gz"
YES=0; DRYRUN=0; DETAILS=0; UNINSTALL=0; ONLY=""; SKIP=""
while [ $# -gt 0 ]; do
  case "$1" in
    --yes|-y) YES=1 ;;
    --dry-run) DRYRUN=1 ;;
    --details|-v) DETAILS=1 ;;
    --uninstall) UNINSTALL=1 ;;
    --only) ONLY="${2:-}"; shift ;;
    --skip) SKIP="${2:-}"; shift ;;
    --owner) OWNER="${2:-}"; shift ;;
    -h|--help) sed -n '2,18p' "$0" 2>/dev/null || true; exit 0 ;;
    *) ;;
  esac
  shift
done

# ---- pretty output (colour only on a TTY) ----
if [ -t 1 ]; then B="$(printf '\033[1m')"; D="$(printf '\033[2m')"; G="$(printf '\033[32m')"; Y="$(printf '\033[33m')"; R="$(printf '\033[31m')"; N="$(printf '\033[0m')"; else B=; D=; G=; Y=; R=; N=; fi
say()  { printf '%s\n' "$*"; }
ok()   { printf '  %s✓%s %s\n' "$G" "$N" "$*"; }
skip() { printf '  %s–%s %s\n' "$Y" "$N" "$*"; }
bad()  { printf '  %s✗%s %s\n' "$R" "$N" "$*"; }
# Named hdr, not head: a function called head shadows head(1), and the pipe
# below that picks the first line of find's output would then get this
# function's text instead. That is how a download quietly installs nothing.
hdr()  { printf '\n%s%s%s\n' "$B" "$*" "$N"; }
in_list() { case ",$1," in *",$2,"*) return 0 ;; *) return 1 ;; esac }

have() { command -v "$1" >/dev/null 2>&1; }
HOME_DIR="${HOME:-$(cd ~ && pwd)}"

# ---- 1. locate the source ----
SELF_DIR=$(CDPATH='' cd -- "$(dirname -- "$0")" 2>/dev/null && pwd || echo "")
SRC=""
if [ -n "$SELF_DIR" ] && [ -f "$SELF_DIR/$SKILL/.claude-plugin/plugin.json" ]; then
  SRC="$SELF_DIR"
elif [ -f "./$SKILL/.claude-plugin/plugin.json" ]; then
  SRC="$(pwd)"
fi
TMP=""
cleanup() { [ -n "$TMP" ] && rm -rf "$TMP" 2>/dev/null || true; }
trap cleanup EXIT INT TERM
if [ -z "$SRC" ]; then
  hdr "Downloading ${SKILL}…"
  TMP=$(mktemp -d 2>/dev/null || echo "/tmp/aads.$$"); mkdir -p "$TMP"
  TB="$TMP/skill.tgz"
  URL="${AADS_TARBALL_URL:-$(printf '%s' "$REPO_DEFAULT_TARBALL" | sed "s/ahmedbenaw/${OWNER}/g")}"
  if have curl; then curl -fsSL "$URL" -o "$TB" || { bad "download failed ($URL)"; exit 1; }
  elif have wget; then wget -qO "$TB" "$URL" || { bad "download failed ($URL)"; exit 1; }
  else bad "need curl or wget to download (both missing)"; exit 1; fi
  ( cd "$TMP" && tar -xzf "$TB" ) || { bad "extract failed"; exit 1; }
  # depth 4: <tmp>/<repo>-main/<skill>/.claude-plugin/plugin.json
  SRC=$(find "$TMP" -maxdepth 4 -name plugin.json -path "*/$SKILL/.claude-plugin/*" 2>/dev/null \
        | sed -n "1s#/$SKILL/.claude-plugin/plugin.json##p")
  [ -n "$SRC" ] || { bad "could not find the skill in the downloaded archive"; exit 1; }
  ok "downloaded"
fi
SKILL_SRC="$SRC/$SKILL"
VERSION=$(awk -F'"' '/"version"[[:space:]]*:/{print $4; exit}' "$SKILL_SRC/.claude-plugin/plugin.json" 2>/dev/null || true)
[ $DETAILS -eq 1 ] && say "${D}source: $SKILL_SRC${N}"

# ---- 2. platform and runtime ----
OS=$(uname -s 2>/dev/null || echo unknown)
case "$OS" in Darwin) OSN="macOS" ;; Linux) OSN="Linux" ;; *) OSN="$OS" ;; esac
PY=""
for c in python3 python; do
  have "$c" && "$c" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' 2>/dev/null \
    && { PY=$(command -v "$c"); break; }
done
hdr "${SKILL}${VERSION:+ $VERSION} installer  ·  $OSN  ·  python: ${PY:-missing}"

python_hint() {
  case "$OSN" in
    macOS) say "  ${D}Install it with:  brew install python${N}" ;;
    Linux) say "  ${D}Install it with your package manager, e.g.  sudo apt install python3${N}" ;;
    *)     say "  ${D}Install Python 3.8 or newer from https://python.org${N}" ;;
  esac
}

# ---- 3. surfaces ----
# Two, both of them this skill in a place that reads skills. No editor
# plugins, no third-party CLI: an editor install is one command, printed at
# the end, so you run it knowingly rather than having it happen to you.
CLAUDE_HOME="$HOME_DIR/.claude"
CODEX_HOME="$HOME_DIR/.codex"
AGENTS_SKILLS="$HOME_DIR/.agents/skills"

wants() {
  [ -n "$ONLY" ] && { in_list "$ONLY" "$1" || return 1; }
  [ -n "$SKIP" ] && { in_list "$SKIP" "$1" && return 1; }
  return 0
}

if [ $UNINSTALL -eq 1 ]; then ACT="uninstall"; else ACT="install"; fi
hdr "Here's what I found (and will ${ACT}):"
PLAN_CLAUDE=0; PLAN_CODEX=0
if wants claude-code; then
  if [ -d "$CLAUDE_HOME" ] || [ $UNINSTALL -eq 0 ]; then
    PLAN_CLAUDE=1
    ok "Claude Code / Cowork  —  the skill, 3 commands, 2 hooks  (~/.claude)"
  fi
fi
if wants codex && [ -d "$CODEX_HOME" ]; then
  PLAN_CODEX=1
  ok "Codex  —  the skill only, no hooks  (~/.agents/skills)"
fi
[ $PLAN_CLAUDE -eq 0 ] && [ $PLAN_CODEX -eq 0 ] && skip "nothing to do (no matching surface found)"
if [ -z "$PY" ] && [ $UNINSTALL -eq 0 ]; then
  skip "python3 is missing. Files will still install; the two hooks need it."
  python_hint
fi

if [ $DRYRUN -eq 1 ]; then hdr "Dry run — nothing installed."; exit 0; fi
if [ $YES -eq 0 ] && [ -t 0 ]; then
  printf '\n%sProceed? [Y/n] %s' "$B" "$N"; read -r ans || ans=y
  case "$ans" in n*|N*) say "Cancelled."; exit 0 ;; esac
fi

# ---- helpers ----
copy_skill() { # $1 = destination
  rm -rf "$1"; mkdir -p "$(dirname "$1")"; cp -R "$SKILL_SRC" "$1"
  find "$1" -name __pycache__ -type d -prune -exec rm -rf {} + 2>/dev/null || true
}
fill_commands() { # $1 = source dir, $2 = dest dir, $3 = installed skill path
  mkdir -p "$2"
  for c in "$1"/*.md; do
    [ -f "$c" ] || continue
    # ${CLAUDE_PLUGIN_ROOT} is unset outside a plugin; unsubstituted, the
    # command would call nothing at all.
    sed "s#\${CLAUDE_PLUGIN_ROOT}#$3#g; s#<skill-path>#$3#g" "$c" > "$2/$(basename "$c")"
  done
}
register_hooks() { # $1 = settings json, $2 = scripts dir
  [ -n "$PY" ] || return 1
  "$PY" - "$1" "$2" "$PY" <<'PYEOF'
import json, sys
p, d, py = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    s = json.load(open(p))
except Exception:
    s = {}
if not isinstance(s, dict):
    s = {}
H = [("PostToolUse", "Write|Edit|MultiEdit", "hook_scan.py", 30),
     ("Stop", "*", "stop_check.py", 60)]
hooks = s.setdefault("hooks", {})
for ev, m, f, t in H:
    # Only entries that are ours are removed, so other tools' hooks survive.
    keep = [b for b in hooks.get(ev, [])
            if not any("anti-ai-design-style/scripts/" in (h.get("command") or "")
                       for h in b.get("hooks", []))]
    entry = {"hooks": [{"type": "command", "command": '%s "%s/%s"' % (py, d, f), "timeout": t}]}
    if m != "*":
        entry["matcher"] = m
    keep.append(entry)
    hooks[ev] = keep
json.dump(s, open(p, "w"), indent=2)
PYEOF
}
drop_hooks() { # $1 = settings json
  [ -n "$PY" ] && [ -f "$1" ] && "$PY" - "$1" <<'PYEOF' 2>/dev/null || true
import json, sys
p = sys.argv[1]
try:
    s = json.load(open(p))
    for ev in list((s.get("hooks") or {}).keys()):
        s["hooks"][ev] = [b for b in s["hooks"][ev]
                          if not any("anti-ai-design-style/scripts/" in (h.get("command") or "")
                                     for h in b.get("hooks", []))]
    json.dump(s, open(p, "w"), indent=2)
except Exception:
    pass
PYEOF
}
verify() { # $1 = installed skill path. A copied file is not a working install.
  [ -n "$PY" ] || return 1
  "$PY" "$1/scripts/verify_all.py" "$1/examples/fixed-example.html" 2>/dev/null | tail -1 | grep -q '^PASS:'
}

# ---- Claude Code / Cowork (they share ~/.claude) ----
install_claude() {
  DEST="$CLAUDE_HOME/skills/$SKILL"
  copy_skill "$DEST"
  fill_commands "$SKILL_SRC/commands" "$CLAUDE_HOME/commands" "$DEST"
  case "$DEST/scripts" in
    *" "*) bad "hook path contains a space ($DEST/scripts) — hooks not registered, because a hook command with a space breaks tool use"
           ok "Claude Code / Cowork — skill and 3 commands (no hooks)"; return 0 ;;
  esac
  if [ -z "$PY" ]; then
    ok "Claude Code / Cowork — skill and 3 commands"
    skip "hooks not registered: python3 is missing. Re-run this installer once it is there."
    return 0
  fi
  [ -f "$CLAUDE_HOME/settings.json" ] && cp "$CLAUDE_HOME/settings.json" "$CLAUDE_HOME/settings.json.bak.aads" 2>/dev/null || true
  [ -f "$CLAUDE_HOME/settings.json" ] || echo '{}' > "$CLAUDE_HOME/settings.json"
  if register_hooks "$CLAUDE_HOME/settings.json" "$DEST/scripts"; then
    ok "Claude Code / Cowork — skill, 3 commands, 2 hooks registered"
  else
    bad "hook registration failed; your settings.json is unchanged (backup: settings.json.bak.aads)"
  fi
  if verify "$DEST"; then
    ok "verified: the installed skill printed PASS on its own example"
  else
    bad "installed, but its own check did not print PASS. Run by hand:"
    say "  ${D}$PY \"$DEST/scripts/verify_all.py\" \"$DEST/examples/fixed-example.html\"${N}"
  fi
}
uninstall_claude() {
  rm -rf "$CLAUDE_HOME/skills/$SKILL" 2>/dev/null || true
  rm -f "$CLAUDE_HOME/commands/design-check.md" "$CLAUDE_HOME/commands/design-fix.md" \
        "$CLAUDE_HOME/commands/design-brief.md" 2>/dev/null || true
  drop_hooks "$CLAUDE_HOME/settings.json"
  ok "Claude Code / Cowork — removed (skill, commands, hooks)"
}

# ---- Codex ----
# Codex reads skills from the .agents/skills convention, which is also what
# this skill's own scripts/install.py --codex writes for a single project.
# No hooks: Codex hook wiring is not something this installer can verify, so
# it does not claim it.
install_codex() {
  DEST="$AGENTS_SKILLS/$SKILL"
  copy_skill "$DEST"
  ok "Codex — skill copied to ~/.agents/skills/$SKILL"
  AGENTS_MD="$CODEX_HOME/AGENTS.md"
  if [ -f "$AGENTS_MD" ] && ! grep -q "$SKILL" "$AGENTS_MD" 2>/dev/null; then
    printf '\n## Design checks\n\nBefore presenting any web or mobile UI, load the `%s` skill from `~/.agents/skills/` and quote the line `verify_all.py` prints.\n' "$SKILL" >> "$AGENTS_MD"
    ok "Codex — noted the skill in ~/.codex/AGENTS.md"
  fi
  say "  ${D}For one project instead: python3 \"$DEST/scripts/install.py\" --codex <project>${N}"
}
uninstall_codex() {
  rm -rf "$AGENTS_SKILLS/$SKILL" 2>/dev/null || true
  ok "Codex — removed (~/.agents/skills/$SKILL; the AGENTS.md note, if any, is left for you to delete)"
}

hdr "${ACT}ing…"
if [ $UNINSTALL -eq 1 ]; then
  [ $PLAN_CLAUDE -eq 1 ] && uninstall_claude
  [ $PLAN_CODEX -eq 1 ] && uninstall_codex
  hdr "Uninstalled. Restart Claude Code to clear the loaded skill."
  exit 0
fi
[ $PLAN_CLAUDE -eq 1 ] && install_claude
[ $PLAN_CODEX -eq 1 ] && install_codex

hdr "Done."
say ""
say "${B}Next:${N} open Claude Code and type ${B}/design-check <a page>${N} — or just build a page; the hooks run on their own."
say ""
say "${B}Two things this installer deliberately leaves to you:${N}"
say "  1. The five warning rules load only from the folder you work in. Inside a project:"
say "     ${B}python3 \"$CLAUDE_HOME/skills/$SKILL/scripts/install.py\" .${N}"
say "  2. For Cursor, VS Code and other editors, one command adds the skill."
say "     It needs Node and downloads a third-party tool, so it is yours to run:"
say "     ${B}npx -y skills@latest add ${OWNER}/${REPO_NAME} --global --agent cursor --copy${N}"
say ""
say "${D}Re-run with --uninstall to remove everything above. --dry-run shows the plan and writes nothing.${N}"
