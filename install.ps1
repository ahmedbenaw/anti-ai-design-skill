<#
.SYNOPSIS
  anti-ai-design-style installer (PowerShell) - Windows.

.DESCRIPTION
  It installs this skill and nothing else. It does not fetch Node, npm
  packages, or any other tool, and it does not shell out to a third-party
  installer. Everything it writes is listed before it writes it, and every
  path it touches belongs to this skill.

  Needs only Windows PowerShell 5.1+ (or PowerShell 7+) and Invoke-WebRequest,
  both OS defaults. The two hooks run on Python 3.8+; if it is missing the
  installer says so and prints the one command to fix it, rather than
  installing software you did not ask for.

  Run directly:
    irm https://raw.githubusercontent.com/ahmedbenaw/anti-ai-design-skill/main/install.ps1 | iex

  Or from a clone:
    powershell -ExecutionPolicy Bypass -File .\install.ps1

  Flags: -Yes -DryRun -Only <ids> -Skip <ids> -Owner <name> -Details -Uninstall -Help
         ids: claude-code, codex

.PARAMETER Yes
  Non-interactive; assume "yes" to the proceed prompt.
.PARAMETER DryRun
  Detect + plan only; install nothing.
.PARAMETER Only
  Comma-separated surface ids to act on exclusively (e.g. "claude-code,codex").
.PARAMETER Skip
  Comma-separated surface ids to skip.
.PARAMETER Owner
  GitHub owner to install from (default: ahmedbenaw).
.PARAMETER Details
  Verbose / technical output.
.PARAMETER Uninstall
  Remove anti-ai-design-style from each detected surface.
.PARAMETER Help
  Print this help and exit.
#>
[CmdletBinding()]
param(
  [Alias('y')][switch]$Yes,
  [switch]$DryRun,
  [string]$Only = '',
  [string]$Skip = '',
  [string]$Owner = 'ahmedbenaw',
  [Alias('v')][switch]$Details,
  [switch]$Uninstall,
  [Alias('h')][switch]$Help
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
# PowerShell 7.4+ would otherwise turn a non-zero exit from python into a
# terminating error; we read exit codes ourselves. Harmless on 5.1.
$PSNativeCommandUseErrorActionPreference = $false

$RepoName = 'anti-ai-design-skill'
$Skill    = 'anti-ai-design-style'
$Surfaces = @('claude-code', 'codex')

if ($Help) {
  Write-Host @"
anti-ai-design-style installer (Windows)

  irm https://raw.githubusercontent.com/$Owner/$RepoName/main/install.ps1 | iex
  powershell -ExecutionPolicy Bypass -File .\install.ps1 [flags]

Flags:
  -Yes          proceed without asking
  -DryRun       detect + show the plan, install nothing
  -Only <ids>   only these surfaces (comma-separated)
  -Skip <ids>   skip these surfaces (comma-separated)
  -Owner <name> GitHub owner to download from (default: ahmedbenaw)
  -Details      technical output
  -Uninstall    remove the skill, its commands and its hooks
  -Help         this text

Surface ids: $($Surfaces -join ', ')
"@
  exit 0
}

# ---- pretty output (colour only on a real console) ----
$script:UseColor = $false
try { if ($Host.UI.RawUI -and -not [Console]::IsOutputRedirected) { $script:UseColor = $true } } catch { $script:UseColor = $false }
# Non-ASCII lives in [char] codes, never in the file's bytes: PS 5.1 reads a
# BOM-less UTF-8 script as ANSI and would mangle a literal em dash or tick.
$Tick  = [char]0x2713   # checkmark
$Dash  = [char]0x2013   # en dash (skip marker)
$Cross = [char]0x2717   # ballot X
$Em    = [char]0x2014   # em dash (in prose)
$Dot   = [char]0x00B7   # middle dot (header separator)
$Ell   = [char]0x2026   # ellipsis
function Write-C([string]$Text, [string]$Color) {
  if ($script:UseColor -and $Color) { Write-Host $Text -ForegroundColor $Color } else { Write-Host $Text }
}
function Say   ([string]$m) { Write-Host $m }
function Ok    ([string]$m) { Write-C ("  $Tick $m") 'Green' }
function Skip  ([string]$m) { Write-C ("  $Dash $m") 'Yellow' }
function Bad   ([string]$m) { Write-C ("  $Cross $m") 'Red' }
function Head  ([string]$m) { Write-Host ""; Write-C $m 'Cyan' }
function Dim   ([string]$m) { Write-C ("  $m") 'DarkGray' }
function Detail([string]$m) { if ($Details) { Dim $m } }

function Test-InList([string]$csv, [string]$id) {
  if ([string]::IsNullOrEmpty($csv)) { return $false }
  foreach ($p in ($csv -split '[,\s]+')) { if ($p.Trim() -eq $id) { return $true } }
  return $false
}
function Have([string]$cmd) {
  try { return [bool](Get-Command $cmd -ErrorAction SilentlyContinue) } catch { return $false }
}
function Get-Prop($obj, [string]$name) {
  # Strict-mode-safe property read: $null when the property is absent.
  if ($null -eq $obj) { return $null }
  if ($obj -is [System.Collections.IDictionary]) { if ($obj.Contains($name)) { return $obj[$name] } else { return $null } }
  $p = $obj.PSObject.Properties[$name]
  if ($p) { return $p.Value } else { return $null }
}
function Invoke-Native {
  # Run a native program, return @{ Code; Out }. Never throws on stderr or exit code.
  param([string]$Exe, [string[]]$Arguments)
  $old = $ErrorActionPreference
  $ErrorActionPreference = 'Continue'
  try {
    $out = @(& $Exe @Arguments 2>$null | ForEach-Object { "$_" })
    $code = $global:LASTEXITCODE
    if ($null -eq $code) { $code = 0 }
    return @{ Code = $code; Out = $out }
  } catch {
    return @{ Code = 1; Out = @() }
  } finally {
    $ErrorActionPreference = $old
  }
}
function Write-Utf8NoBom([string]$Path, [string]$Text) {
  # PS 5.1's -Encoding UTF8 writes a BOM, which JSON readers reject. Avoid it on both versions.
  [System.IO.File]::WriteAllText($Path, $Text, (New-Object System.Text.UTF8Encoding($false)))
}
function Add-Utf8NoBom([string]$Path, [string]$Text) {
  [System.IO.File]::AppendAllText($Path, $Text, (New-Object System.Text.UTF8Encoding($false)))
}
function To-Fwd([string]$p) { return ($p -replace '\\', '/') }
function Join3([string]$a, [string]$b, [string]$c) { return (Join-Path (Join-Path $a $b) $c) }

# ---- home + surface roots ----
$HomeDir = ''
if ($env:USERPROFILE) { $HomeDir = $env:USERPROFILE }
elseif ($env:HOME)    { $HomeDir = $env:HOME }
else                  { $HomeDir = [Environment]::GetFolderPath('UserProfile') }
$Zipball = "https://github.com/$Owner/$RepoName/archive/refs/heads/main.zip"

# ===================================================================
# 1. locate the source (local clone vs download zip)
# ===================================================================
$SelfDir = ''
try { if ($PSScriptRoot) { $SelfDir = $PSScriptRoot } } catch { }
if (-not $SelfDir -and $PSCommandPath) { $SelfDir = Split-Path -Parent $PSCommandPath }

$Src = ''
if ($SelfDir -and (Test-Path (Join3 (Join-Path $SelfDir $Skill) '.claude-plugin' 'plugin.json'))) {
  $Src = $SelfDir
} elseif (Test-Path (Join3 $Skill '.claude-plugin' 'plugin.json')) {
  $Src = (Get-Location).Path
}

$Tmp = ''
function Invoke-Cleanup {
  if ($Tmp -and (Test-Path $Tmp)) { try { Remove-Item -Recurse -Force $Tmp -ErrorAction SilentlyContinue } catch { } }
}

if (-not $Src) {
  Head "Downloading $Skill$Ell"
  $Tmp = Join-Path ([System.IO.Path]::GetTempPath()) ("aads." + [guid]::NewGuid().ToString('N'))
  New-Item -ItemType Directory -Force -Path $Tmp | Out-Null
  $ZipFile = Join-Path $Tmp 'skill.zip'
  try {
    try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch { }
    Invoke-WebRequest -Uri $Zipball -OutFile $ZipFile -UseBasicParsing
  } catch {
    Bad "download failed ($Zipball): $($_.Exception.Message)"
    Invoke-Cleanup; exit 1
  }
  try {
    Expand-Archive -Path $ZipFile -DestinationPath (Join-Path $Tmp 'x') -Force
  } catch {
    Bad "extract failed: $($_.Exception.Message)"
    Invoke-Cleanup; exit 1
  }
  $found = Get-ChildItem -Path (Join-Path $Tmp 'x') -Recurse -Filter 'plugin.json' -File -ErrorAction SilentlyContinue |
    Where-Object { $_.DirectoryName -match ('[\\/]' + [regex]::Escape($Skill) + '[\\/]\.claude-plugin$') } |
    Select-Object -First 1
  if (-not $found) { Bad "could not find the skill in the downloaded archive"; Invoke-Cleanup; exit 1 }
  # <root>/anti-ai-design-style/.claude-plugin/plugin.json -> <root>
  $Src = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $found.FullName))
  Ok "downloaded"
}
$SkillSrc = Join-Path $Src $Skill
$Version = ''
try {
  $pj = Get-Content -Raw -Path (Join3 $SkillSrc '.claude-plugin' 'plugin.json') -ErrorAction SilentlyContinue
  if ($pj) {
    $m = [regex]::Match($pj, '"version"\s*:\s*"([^"]*)"')
    if ($m.Success) { $Version = $m.Groups[1].Value }
  }
} catch { }
Detail "source: $SkillSrc"

# ===================================================================
# 2. platform and runtime
# ===================================================================
$OsName = 'Windows'
try { if (-not ($env:OS -eq 'Windows_NT')) { $OsName = [System.Environment]::OSVersion.Platform.ToString() } } catch { }

function Test-PythonExe([string]$exe) {
  if (-not $exe -or -not (Test-Path $exe)) { return $false }
  # The Microsoft Store alias stub is not a Python; it opens the Store instead.
  if ($exe -like '*\WindowsApps\python*.exe' -and (Get-Item $exe).Length -eq 0) { return $false }
  $r = Invoke-Native $exe @('-c', 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)')
  return ($r.Code -eq 0)
}
function Find-Python {
  foreach ($c in @('python', 'python3')) {
    try {
      $g = Get-Command $c -ErrorAction SilentlyContinue
      if ($g -and $g.Source -and (Test-PythonExe $g.Source)) { return $g.Source }
    } catch { }
  }
  # The py launcher knows about installs that are not on PATH yet.
  if (Have 'py') {
    $r = Invoke-Native 'py' @('-3', '-c', 'import sys; print(sys.executable)')
    if ($r.Code -eq 0 -and $r.Out.Count -gt 0 -and (Test-PythonExe $r.Out[-1].Trim())) { return $r.Out[-1].Trim() }
  }
  # Fresh installs land here before PATH refreshes in this session.
  if ($env:LOCALAPPDATA) {
    $base = Join-Path $env:LOCALAPPDATA 'Programs\Python'
    if (Test-Path $base) {
      foreach ($d in (Get-ChildItem -Path $base -Directory -ErrorAction SilentlyContinue | Sort-Object Name -Descending)) {
        $p = Join-Path $d.FullName 'python.exe'
        if (Test-PythonExe $p) { return $p }
      }
    }
  }
  return ''
}
$script:Py = Find-Python
$PyLabel = 'missing'; if ($script:Py) { $PyLabel = $script:Py }
$VerLabel = ''; if ($Version) { $VerLabel = " $Version" }
Head "$Skill$VerLabel installer  $Dot  $OsName  $Dot  python: $PyLabel"

function Show-PythonHint {
  # No bootstrap: this installer does not install software you did not ask for.
  Dim "Install it with:  winget install Python.Python.3.12"
  Dim "Or get Python 3.8 or newer from https://python.org (tick 'Add python.exe to PATH')."
}

# ===================================================================
# 3. surfaces
# ===================================================================
# Two, both of them this skill in a place that reads skills. No editor
# plugins, no third-party CLI: an editor install is one command, printed at
# the end, so you run it knowingly rather than having it happen to you.
$ClaudeHome   = Join-Path $HomeDir '.claude'
$CodexHome    = Join-Path $HomeDir '.codex'
$AgentsSkills = Join-Path $HomeDir '.agents\skills'

function Test-Wants([string]$id) {
  if ($Only -and -not (Test-InList $Only $id)) { return $false }
  if ($Skip -and (Test-InList $Skip $id)) { return $false }
  return $true
}

# ===================================================================
# 4. plan
# ===================================================================
$Act = 'install'; if ($Uninstall) { $Act = 'uninstall' }
Head "Here's what I found (and will ${Act}):"
$PlanClaude = $false; $PlanCodex = $false

if (Test-Wants 'claude-code') {
  if ((Test-Path $ClaudeHome) -or (-not $Uninstall)) {
    $PlanClaude = $true
    Ok "Claude Code / Cowork  $Em  the skill, 3 commands, 2 hooks  (~/.claude)"
  }
}
if ((Test-Wants 'codex') -and (Test-Path $CodexHome)) {
  $PlanCodex = $true
  Ok "Codex  $Em  the skill only, no hooks  (~/.agents/skills)"
}
if (-not $PlanClaude -and -not $PlanCodex) { Skip "nothing to do (no matching surface found)" }
if (-not $script:Py -and -not $Uninstall) {
  Skip "python 3.8+ is missing. Files will still install; the two hooks need it."
  Show-PythonHint
}

if ($DryRun) { Head "Dry run $Em nothing installed."; Invoke-Cleanup; exit 0 }
$Interactive = $true
try { if ([Console]::IsInputRedirected) { $Interactive = $false } } catch { }
if (-not $Yes -and $Interactive) {
  Say ""
  $ans = Read-Host "Proceed? [Y/n]"
  if ($ans -match '^[nN]') { Say "Cancelled."; Invoke-Cleanup; exit 0 }
}

# ===================================================================
# 5. install helpers
# ===================================================================
$HookDefs = @(
  @{ event = 'PostToolUse'; matcher = 'Write|Edit|MultiEdit'; script = 'hook_scan.py';  timeout = 30 },
  @{ event = 'Stop';        matcher = '*';                    script = 'stop_check.py'; timeout = 60 }
)
function Test-OurHookBlock($block) {
  # True when any command in this block points at our scripts folder (either slash style).
  try {
    foreach ($hk in @(Get-Prop $block 'hooks')) {
      $cmd = Get-Prop $hk 'command'
      if ($cmd -and (("$cmd" -like "*$Skill/scripts/*") -or ("$cmd" -like "*$Skill\scripts\*"))) { return $true }
    }
  } catch { }
  return $false
}
function Read-JsonFile([string]$Path) {
  # {} on absent/empty/malformed; the caller took a backup first.
  if (-not (Test-Path $Path)) { return [pscustomobject]@{} }
  $raw = Get-Content -Raw -Path $Path -ErrorAction SilentlyContinue
  if ([string]::IsNullOrWhiteSpace($raw)) { return [pscustomobject]@{} }
  $obj = $raw | ConvertFrom-Json
  if ($null -eq $obj -or -not ($obj -is [pscustomobject])) { throw "not a JSON object" }
  return $obj
}
function Register-Hooks([string]$JsonPath, [string]$ScriptsDir) {
  if (-not $script:Py) { return $false }
  $pyCmd = To-Fwd $script:Py
  if ($pyCmd -match '\s') { $pyCmd = "`"$pyCmd`"" }
  $dirFwd = To-Fwd $ScriptsDir

  $settings = Read-JsonFile $JsonPath
  $hooksObj = Get-Prop $settings 'hooks'
  if ($null -eq $hooksObj -or -not ($hooksObj -is [pscustomobject])) {
    $hooksObj = [pscustomobject]@{}
    $settings | Add-Member -NotePropertyName 'hooks' -NotePropertyValue $hooksObj -Force
  }
  foreach ($h in $HookDefs) {
    $ev = $h.event
    # Only entries that are ours are removed, so other tools' hooks survive.
    $keep = @()
    foreach ($block in @(Get-Prop $hooksObj $ev)) {
      if ($null -eq $block) { continue }
      if (-not (Test-OurHookBlock $block)) { $keep += $block }
    }
    $entry = [ordered]@{}
    if ($h.matcher -ne '*') { $entry['matcher'] = $h.matcher }
    $entry['hooks'] = @([pscustomobject]@{ type = 'command'; command = "$pyCmd `"$dirFwd/$($h.script)`""; timeout = $h.timeout })
    $keep += [pscustomobject]$entry
    $hooksObj | Add-Member -NotePropertyName $ev -NotePropertyValue ([object[]]$keep) -Force
  }
  Write-Utf8NoBom $JsonPath (ConvertTo-Json -InputObject $settings -Depth 20)
  return $true
}
function Remove-Hooks([string]$JsonPath) {
  if (-not (Test-Path $JsonPath)) { return }
  try {
    $settings = Read-JsonFile $JsonPath
    $hooksObj = Get-Prop $settings 'hooks'
    if ($null -eq $hooksObj -or -not ($hooksObj -is [pscustomobject])) { return }
    foreach ($ev in @($hooksObj.PSObject.Properties.Name)) {
      $keep = @()
      foreach ($block in @(Get-Prop $hooksObj $ev)) {
        if ($null -eq $block) { continue }
        if (-not (Test-OurHookBlock $block)) { $keep += $block }
      }
      $hooksObj | Add-Member -NotePropertyName $ev -NotePropertyValue ([object[]]$keep) -Force
    }
    Write-Utf8NoBom $JsonPath (ConvertTo-Json -InputObject $settings -Depth 20)
  } catch { }
}
function Copy-SkillFolder([string]$Dest) {
  # A clean replace, never a merge, so a file a newer version removed does not linger.
  New-Item -ItemType Directory -Force -Path (Split-Path -Parent $Dest) | Out-Null
  if (Test-Path $Dest) { Remove-Item -Recurse -Force $Dest }
  Copy-Item -Recurse -Force -Path $SkillSrc -Destination $Dest
  Get-ChildItem -Path $Dest -Recurse -Directory -Filter '__pycache__' -ErrorAction SilentlyContinue |
    ForEach-Object { Remove-Item -Recurse -Force $_.FullName -ErrorAction SilentlyContinue }
}
function Copy-Commands([string]$SrcDir, [string]$DestDir, [string]$InstalledSkill) {
  # ${CLAUDE_PLUGIN_ROOT} is unset outside a plugin; unsubstituted, the
  # command would call nothing at all.
  # Forward slashes: the path sits inside python "..." and Python accepts either on Windows.
  $fwd = To-Fwd $InstalledSkill
  New-Item -ItemType Directory -Force -Path $DestDir | Out-Null
  foreach ($c in (Get-ChildItem -Path $SrcDir -Filter '*.md' -File -ErrorAction SilentlyContinue)) {
    $text = Get-Content -Raw -Path $c.FullName
    $text = $text.Replace('${CLAUDE_PLUGIN_ROOT}', $fwd).Replace('<skill-path>', $fwd)
    Write-Utf8NoBom (Join-Path $DestDir $c.Name) $text
  }
}
function Test-ClaudeProof([string]$InstalledSkill) {
  # A copied file is not a working install.
  if (-not $script:Py) { return $false }
  $r = Invoke-Native $script:Py @((Join3 $InstalledSkill 'scripts' 'verify_all.py'), (Join3 $InstalledSkill 'examples' 'fixed-example.html'))
  if ($r.Out.Count -eq 0) { return $false }
  return ("$($r.Out[-1])" -like 'PASS:*')
}

# ---- Claude Code / Cowork (they share ~/.claude) ----
function Install-Claude([string]$Dir) {
  $dest = Join3 $Dir 'skills' $Skill
  Copy-SkillFolder $dest
  Copy-Commands (Join-Path $SkillSrc 'commands') (Join-Path $Dir 'commands') $dest
  $scriptsDir = Join-Path $dest 'scripts'
  if ($scriptsDir -match '\s') {
    Bad "hook path contains a space ($scriptsDir) $Em hooks not registered, because a hook command with a space breaks tool use"
    Ok "Claude Code / Cowork $Em skill and 3 commands (no hooks)"
    return
  }
  if (-not $script:Py) {
    Ok "Claude Code / Cowork $Em skill and 3 commands"
    Skip "hooks not registered: python 3.8+ is missing. Re-run this installer once it is there."
    return
  }
  $settingsPath = Join-Path $Dir 'settings.json'
  $backup = "$settingsPath.bak.aads"
  if (Test-Path $settingsPath) { try { Copy-Item -Force -Path $settingsPath -Destination $backup } catch { } }
  else { Write-Utf8NoBom $settingsPath '{}' }
  $registered = $false
  try { $registered = Register-Hooks $settingsPath $scriptsDir } catch {
    if (Test-Path $backup) { try { Copy-Item -Force -Path $backup -Destination $settingsPath } catch { } }
  }
  if ($registered) { Ok "Claude Code / Cowork $Em skill, 3 commands, 2 hooks registered" }
  else { Bad "hook registration failed; your settings.json is unchanged (backup: settings.json.bak.aads)" }
  if (Test-ClaudeProof $dest) {
    Ok "verified: the installed skill printed PASS on its own example"
  } else {
    Bad "installed, but its own check did not print PASS. Run by hand:"
    Dim "`"$script:Py`" `"$(Join3 $dest 'scripts' 'verify_all.py')`" `"$(Join3 $dest 'examples' 'fixed-example.html')`""
  }
}
function Uninstall-Claude([string]$Dir) {
  $dest = Join3 $Dir 'skills' $Skill
  if (Test-Path $dest) { Remove-Item -Recurse -Force $dest -ErrorAction SilentlyContinue }
  foreach ($n in @('design-check.md', 'design-fix.md', 'design-brief.md')) {
    $p = Join3 $Dir 'commands' $n
    if (Test-Path $p) { Remove-Item -Force $p -ErrorAction SilentlyContinue }
  }
  Remove-Hooks (Join-Path $Dir 'settings.json')
  Ok "Claude Code / Cowork $Em removed (skill, commands, hooks)"
}

# ---- Codex ----
# Codex reads skills from the .agents/skills convention, which is also what
# this skill's own scripts/install.py --codex writes for a single project.
# No hooks: Codex hook wiring is not something this installer can verify, so
# it does not claim it.
function Install-Codex {
  $dest = Join-Path $AgentsSkills $Skill
  Copy-SkillFolder $dest
  Ok "Codex $Em skill copied to ~/.agents/skills/$Skill"
  $agentsMd = Join-Path $CodexHome 'AGENTS.md'
  if (Test-Path $agentsMd) {
    $existing = ''
    try { $existing = Get-Content -Raw -Path $agentsMd -ErrorAction SilentlyContinue } catch { }
    if ($null -eq $existing) { $existing = '' }
    if (-not ($existing -like "*$Skill*")) {
      $note = "`n## Design checks`n`nBefore presenting any web or mobile UI, load the ``$Skill`` skill from ``~/.agents/skills/`` and quote the line ``verify_all.py`` prints.`n"
      Add-Utf8NoBom $agentsMd $note
      Ok "Codex $Em noted the skill in ~/.codex/AGENTS.md"
    }
  }
  $pyName = 'python'; if ($script:Py) { $pyName = "`"$(To-Fwd $script:Py)`"" }
  Dim "For one project instead: $pyName `"$(To-Fwd (Join3 $dest 'scripts' 'install.py'))`" --codex <project>"
}
function Uninstall-Codex {
  $dest = Join-Path $AgentsSkills $Skill
  if (Test-Path $dest) { Remove-Item -Recurse -Force $dest -ErrorAction SilentlyContinue }
  Ok "Codex $Em removed (~/.agents/skills/$Skill; the AGENTS.md note, if any, is left for you to delete)"
}

# ===================================================================
# 6. run and summarise
# ===================================================================
$HardFail = $false
function Invoke-Surface([string]$label, [scriptblock]$body) {
  # One surface failing never aborts the other.
  try { & $body } catch {
    $script:HardFail = $true
    Bad "$label failed: $($_.Exception.Message)"
  }
}

try {
  Head "${Act}ing..."
  if ($Uninstall) {
    if ($PlanClaude) { Invoke-Surface 'Claude Code' { Uninstall-Claude $ClaudeHome } }
    if ($PlanCodex)  { Invoke-Surface 'Codex' { Uninstall-Codex } }
    Head "Uninstalled. Restart Claude Code to clear the loaded skill."
    if ($HardFail) { exit 1 } else { exit 0 }
  }

  if ($PlanClaude) { Invoke-Surface 'Claude Code' { Install-Claude $ClaudeHome } }
  if ($PlanCodex)  { Invoke-Surface 'Codex' { Install-Codex } }

  Head "Done."
  Say ""
  $installedSkill = To-Fwd (Join3 $ClaudeHome 'skills' $Skill)
  $pyName = 'python'; if ($script:Py) { $pyName = "`"$(To-Fwd $script:Py)`"" }
  Write-C "Next: open Claude Code and type /design-check <a page> $Em or just build a page; the hooks run on their own." 'Cyan'
  Say ""
  Write-C "Two things this installer deliberately leaves to you:" 'Cyan'
  Say "  1. The five warning rules load only from the folder you work in. Inside a project:"
  Say "     $pyName `"$installedSkill/scripts/install.py`" ."
  Say "  2. For Cursor, VS Code and other editors, one command adds the skill."
  Say "     It needs Node and downloads a third-party tool, so it is yours to run:"
  Say "     npx -y skills@latest add $Owner/$RepoName --global --agent cursor --copy"
  Say ""
  Dim "Re-run with -Uninstall to remove everything above. -DryRun shows the plan and writes nothing."
  if ($HardFail) { exit 1 }
}
finally {
  Invoke-Cleanup
}
