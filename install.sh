#!/bin/sh
# anti-ai-design-style universal installer (POSIX core) — macOS / Linux / Unix.
# Zero prerequisites: needs only `sh` + one of curl/wget (OS defaults). The
# hooks run on python3, which ships with macOS and most Linux.
# Auto-detects Claude Code, Claude Cowork, Codex, and your editors, installs to
# each, verifies with the skill's own proof line, and self-troubleshoots. Reads
# installer/manifest.json semantics when run from a clone; otherwise downloads
# the tarball.
#
#   curl -fsSL https://raw.githubusercontent.com/ahmedbenaw/anti-ai-design-skill/main/install.sh | sh
#
# Flags: --yes --dry-run --only <ids> --skip <ids> --owner <name> --details --uninstall
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
    -h|--help) sed -n '2,12p' "$0"; exit 0 ;;
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
# Named hdr, not head: a function called head would shadow the head(1) used
# below to pick the first line out of find's output, and the tarball path
# would then quietly install nothing.
hdr() { printf '\n%s%s%s\n' "$B" "$*" "$N"; }
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
  URL=$(printf '%s' "$REPO_DEFAULT_TARBALL" | sed "s/ahmedbenaw/${OWNER}/g")
  if have curl; then curl -fsSL "$URL" -o "$TB" || { bad "download failed ($URL)"; exit 1; }
  elif have wget; then wget -qO "$TB" "$URL" || { bad "download failed ($URL)"; exit 1; }
  else bad "need curl or wget to download (both missing)"; exit 1; fi
  ( cd "$TMP" && tar -xzf "$TB" ) || { bad "extract failed"; exit 1; }
  # depth 4: <tmp>/<repo>-main/<skill>/.claude-plugin/plugin.json
  SRC=$(find "$TMP" -maxdepth 4 -name plugin.json -path "*/$SKILL/.claude-plugin/*" -exec dirname {} \; | head -1 | sed "s#/$SKILL/.claude-plugin##")
  [ -n "$SRC" ] || { bad "could not find the skill in the tarball"; exit 1; }
  ok "downloaded"
fi
SKILL_SRC="$SRC/$SKILL"
[ $DETAILS -eq 1 ] && say "${D}source: $SKILL_SRC${N}"

# ---- 2. detect platform + runtime ----
OS=$(uname -s 2>/dev/null || echo unknown)
case "$OS" in Darwin) OSN="macOS" ;; Linux) OSN="Linux" ;; *) OSN="$OS" ;; esac
PM=""
for c in brew apt-get dnf pacman zypper apk; do have "$c" && { PM="$c"; break; }; done
PY=""
for c in python3 python; do have "$c" && "$c" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' 2>/dev/null && { PY=$(command -v "$c"); break; }; done
hdr "${SKILL} installer  ·  $OSN  ·  package manager: ${PM:-none}  ·  python: ${PY:-missing}"

ensure_python() {
  [ -n "$PY" ] && return 0
  [ -n "$PM" ] || return 1
  say "  ${D}python3 not found — bootstrapping via $PM…${N}"
  case "$PM" in
    brew) brew install python >/dev/null 2>&1 || return 1 ;;
    apt-get) sudo apt-get update >/dev/null 2>&1 && sudo apt-get install -y python3 >/dev/null 2>&1 || return 1 ;;
    dnf) sudo dnf install -y python3 >/dev/null 2>&1 || return 1 ;;
    pacman) sudo pacman -Sy --noconfirm python >/dev/null 2>&1 || return 1 ;;
    zypper) sudo zypper install -y python3 >/dev/null 2>&1 || return 1 ;;
    apk) sudo apk add python3 >/dev/null 2>&1 || return 1 ;;
  esac
  have python3 && PY=$(command -v python3)
}
node_bin() { for c in node "$HOME_DIR/.local/node-current/bin/node"; do command -v "$c" >/dev/null 2>&1 && { command -v "$c"; return 0; }; [ -x "$c" ] && { echo "$c"; return 0; }; done; return 1; }
ensure_node() {
  node_bin >/dev/null 2>&1 && return 0
  [ -n "$PM" ] || return 1
  say "  ${D}Node not found (only editors need it) — bootstrapping via $PM…${N}"
  case "$PM" in
    brew) brew install node >/dev/null 2>&1 || return 1 ;;
    apt-get) sudo apt-get update >/dev/null 2>&1 && sudo apt-get install -y nodejs npm >/dev/null 2>&1 || return 1 ;;
    dnf) sudo dnf install -y nodejs >/dev/null 2>&1 || return 1 ;;
    pacman) sudo pacman -Sy --noconfirm nodejs npm >/dev/null 2>&1 || return 1 ;;
    zypper) sudo zypper install -y nodejs >/dev/null 2>&1 || return 1 ;;
    apk) sudo apk add nodejs npm >/dev/null 2>&1 || return 1 ;;
  esac
  node_bin >/dev/null 2>&1
}

# ---- 3. detect surfaces ----
CLAUDE_HOME="$HOME_DIR/.claude"
CODEX_HOME="$HOME_DIR/.codex"
has_app() { [ -d "/Applications/$1.app" ] || [ -d "$HOME_DIR/Applications/$1.app" ]; }
has_vsext() { ls -d "$HOME_DIR/.vscode/extensions/$1"* >/dev/null 2>&1 || ls -d "$HOME_DIR/.vscode-oss/extensions/$1"* >/dev/null 2>&1; }
detect_editor() {
  case "$1" in
    cursor)     has_app Cursor || have cursor ;;
    vscode)     has_app "Visual Studio Code" || has_app VSCodium || have code || have codium ;;
    windsurf)   has_app Windsurf || have windsurf ;;
    zed)        has_app Zed || have zed ;;
    cline)      has_vsext saoudrizwan.claude-dev ;;
    roo)        has_vsext rooveterinaryinc.roo-cline ;;
    continue)   [ -d "$HOME_DIR/.continue" ] ;;
    gemini-cli) have gemini || [ -d "$HOME_DIR/.gemini" ] ;;
    aider)      have aider ;;
    opencode)   have opencode ;;
    amp)        have amp ;;
    *) return 1 ;;
  esac
}
agent_for() { case "$1" in vscode) echo github-copilot ;; aider) echo aider-desk ;; *) echo "$1" ;; esac; }
EDITORS="cursor vscode windsurf zed cline roo continue gemini-cli aider opencode amp"

wants() {
  [ -n "$ONLY" ] && { in_list "$ONLY" "$1" || return 1; }
  [ -n "$SKIP" ] && { in_list "$SKIP" "$1" && return 1; }
  return 0
}

# ---- 4. plan ----
if [ $UNINSTALL -eq 1 ]; then ACT="uninstall"; else ACT="install"; fi
hdr "Here's what I found (and will ${ACT}):"
PLAN_CLAUDE=0; PLAN_CODEX=0; PLAN_ED=""
if wants claude-code; then
  if [ -d "$CLAUDE_HOME" ] || [ $UNINSTALL -eq 0 ]; then PLAN_CLAUDE=1; ok "Claude Code / Cowork  (~/.claude)"; fi
fi
if wants codex && [ -d "$CODEX_HOME" ]; then PLAN_CODEX=1; ok "Codex  (~/.codex)"; fi
for e in $EDITORS; do
  wants "$e" || continue
  if detect_editor "$e"; then PLAN_ED="$PLAN_ED $e"; ok "$e  (via skills CLI)"; else [ $DETAILS -eq 1 ] && skip "$e (not found)"; fi
done
[ -z "$PLAN_ED$PLAN_CLAUDE$PLAN_CODEX" ] && { skip "no supported surfaces detected"; }
[ -z "$PY" ] && [ $UNINSTALL -eq 0 ] && skip "python3 is missing; the hooks need it. I will try to install it via ${PM:-a package manager}."

if [ $DRYRUN -eq 1 ]; then hdr "Dry run — nothing installed."; exit 0; fi
if [ $YES -eq 0 ] && [ -t 0 ]; then
  printf '\n%sProceed? [Y/n] %s' "$B" "$N"; read -r ans || ans=y
  case "$ans" in n*|N*) say "Cancelled."; exit 0 ;; esac
fi

# ---- 5. install: claude-home (Claude Code + Cowork share ~/.claude) ----
register_hooks_py() { # $1 = settings/hooks json, $2 = scripts dir
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
fill_commands() { # $1 = source commands dir, $2 = dest dir, $3 = installed skill path
  for c in "$1"/*.md; do
    [ -f "$c" ] || continue
    # ${CLAUDE_PLUGIN_ROOT} is unset outside a plugin; the commands would call nothing
    sed "s#\${CLAUDE_PLUGIN_ROOT}#$3#g; s#<skill-path>#$3#g" "$c" > "$2/$(basename "$c")"
  done
}
verify_claude() { # $1 = installed skill path
  [ -n "$PY" ] || return 1
  "$PY" "$1/scripts/verify_all.py" "$1/examples/fixed-example.html" 2>/dev/null | tail -1 | grep -q '^PASS:'
}
install_claude() {
  TGT="$1"; DEST="$TGT/skills/$SKILL"   # not $D: that is the dim colour code
  mkdir -p "$TGT/skills" "$TGT/commands"
  rm -rf "$DEST"; cp -R "$SKILL_SRC" "$DEST"
  find "$DEST" -name __pycache__ -type d -prune -exec rm -rf {} + 2>/dev/null || true
  fill_commands "$SKILL_SRC/commands" "$TGT/commands" "$DEST"
  SCRIPTS_DIR="$DEST/scripts"
  case "$SCRIPTS_DIR" in *" "*) bad "hook path has a space ($SCRIPTS_DIR) — skipping hook registration (a hook path with a space breaks tool use)"; return 0 ;; esac
  ensure_python || { skip "Claude files installed; the hooks need python3 (install it, then re-run)"; return 0; }
  [ -f "$TGT/settings.json" ] && cp "$TGT/settings.json" "$TGT/settings.json.bak.aads" 2>/dev/null || true
  [ -f "$TGT/settings.json" ] || echo '{}' > "$TGT/settings.json"
  if register_hooks_py "$TGT/settings.json" "$SCRIPTS_DIR"; then ok "Claude Code / Cowork — skill, 3 commands, 2 hooks registered"; else bad "hook registration failed; settings.json left as it was (backup: settings.json.bak.aads)"; fi
  if verify_claude "$DEST"; then ok "verified: the installed skill printed PASS on its own example"; else bad "installed, but the skill's own proof line did not print PASS. Run: $PY \"$DEST/scripts/verify_all.py\" \"$DEST/examples/fixed-example.html\""; fi
}
uninstall_claude() {
  TGT="$1"; rm -rf "$TGT/skills/$SKILL" 2>/dev/null || true
  rm -f "$TGT/commands/design-check.md" "$TGT/commands/design-fix.md" "$TGT/commands/design-brief.md" 2>/dev/null || true
  [ -n "$PY" ] && [ -f "$TGT/settings.json" ] && "$PY" - "$TGT/settings.json" <<'PYEOF' 2>/dev/null || true
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
  ok "Claude Code / Cowork — removed (skill, commands, hooks)"
}

# ---- install: codex-home ----
install_codex() {
  DEST="$CODEX_HOME/plugins/$SKILL"
  mkdir -p "$CODEX_HOME/plugins"; rm -rf "$DEST"; cp -R "$SKILL_SRC" "$DEST"
  SD="$DEST/scripts"
  case "$SD" in *" "*) bad "codex hook path has a space — skipping hooks"; return 0 ;; esac
  ensure_python || { skip "Codex plugin copied; hooks need python3"; return 0; }
  [ -f "$CODEX_HOME/hooks.json" ] && cp "$CODEX_HOME/hooks.json" "$CODEX_HOME/hooks.json.bak.aads" || true
  [ -f "$CODEX_HOME/hooks.json" ] || echo '{}' > "$CODEX_HOME/hooks.json"
  if register_hooks_py "$CODEX_HOME/hooks.json" "$SD"; then ok "Codex — plugin + 2 hooks"; else skip "Codex plugin copied; hook registration failed"; fi
  say "  ${D}For a project Codex reads directly (.agents/skills/): $PY \"$DEST/scripts/install.py\" --codex <project>${N}"
}
uninstall_codex() { rm -rf "$CODEX_HOME/plugins/$SKILL" 2>/dev/null || true; ok "Codex — removed"; }

# ---- install: editors via skills CLI ----
install_editor() {
  e="$1"; ag=$(agent_for "$e")
  ensure_node || { skip "$e — needs Node/npx (couldn't bootstrap). Manual: npx -y skills@latest add ${OWNER}/${REPO_NAME} --global --agent $ag --copy --full-depth"; return 0; }
  NB=$(node_bin); NPX=$(dirname "$NB")/npx
  if "$NPX" -y skills@latest add "${OWNER}/${REPO_NAME}" --global --agent "$ag" --skill '*' -y --copy --full-depth >/dev/null 2>&1; then ok "$e — installed (agent: $ag)"; else skip "$e — skills CLI failed; manual: npx -y skills@latest add ${OWNER}/${REPO_NAME} --global --agent $ag --copy --full-depth"; fi
}
uninstall_editor() { e="$1"; ag=$(agent_for "$e"); NB=$(node_bin) && NPX=$(dirname "$NB")/npx && "$NPX" -y skills@latest remove "$SKILL" --global --agent "$ag" >/dev/null 2>&1 || true; ok "$e — remove attempted"; }

hdr "${ACT}ing…"
if [ $UNINSTALL -eq 1 ]; then
  [ $PLAN_CLAUDE -eq 1 ] && uninstall_claude "$CLAUDE_HOME"
  [ $PLAN_CODEX -eq 1 ] && uninstall_codex
  for e in $PLAN_ED; do uninstall_editor "$e"; done
  hdr "Uninstalled. Restart your editor to clear loaded skills."
  exit 0
fi
[ $PLAN_CLAUDE -eq 1 ] && install_claude "$CLAUDE_HOME"
[ $PLAN_CODEX -eq 1 ] && install_codex
for e in $PLAN_ED; do install_editor "$e"; done

# ---- 6. summary ----
hdr "Done."
say ""
say "${B}Next:${N} open Claude Code and type ${B}/design-check <a page>${N} — or just build a page; the hooks run by themselves."
say "${B}One thing this installer cannot do:${N} the five warning rules only load from the folder you work in."
say "  Inside any project, run:  ${B}python3 \"$CLAUDE_HOME/skills/$SKILL/scripts/install.py\" .${N}"
say "${D}Tips: /design-fix (repair what the scan found) · /design-brief (before building) · re-run with --uninstall to remove.${N}"
