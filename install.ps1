<#
.SYNOPSIS
  anti-ai-design-style universal installer (PowerShell core) - Windows.

.DESCRIPTION
  Zero prerequisites: needs only Windows PowerShell 5.1+ (or PowerShell 7+) and
  Invoke-WebRequest, both OS defaults. The hooks run on Python 3.8+; if it is
  missing, the installer offers to fetch it with winget / choco / scoop.
  Auto-detects Claude Code, Claude Cowork, Codex, and your editors, installs to
  each, verifies with the skill's own proof line, and self-troubleshoots. Reads
  installer/manifest.json semantics when run from a clone; otherwise downloads
  the repository zip.

  Run directly:
    irm https://raw.githubusercontent.com/ahmedbenaw/anti-ai-design-skill/main/install.ps1 | iex

  Or from a clone:
    powershell -ExecutionPolicy Bypass -File .\install.ps1

  Flags: -Yes -DryRun -Only <ids> -Skip <ids> -Owner <name> -Details -Uninstall -Help

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
$Surfaces = @('claude-code', 'claude-cowork', 'codex', 'cursor', 'vscode', 'windsurf', 'zed', 'cline', 'roo', 'continue', 'gemini-cli', 'aider', 'opencode', 'amp')

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
function Write-C([string]$Text, [string]$Color) {
  if ($script:UseColor -and $Color) { Write-Host $Text -ForegroundColor $Color } else { Write-Host $Text }
}
function Say   ([string]$m) { Write-Host $m }
function Ok    ([string]$m) { Write-C ("  " + [char]0x2713 + " $m") 'Green' }   # ✓
function Skip  ([string]$m) { Write-C ("  " + [char]0x2013 + " $m") 'Yellow' }  # –
function Bad   ([string]$m) { Write-C ("  " + [char]0x2717 + " $m") 'Red' }     # ✗
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
function To-Fwd([string]$p) { return ($p -replace '\\', '/') }
function Join3([string]$a, [string]$b, [string]$c) { return (Join-Path (Join-Path $a $b) $c) }

# ---- home + surface roots ----
$HomeDir = ''
if ($env:USERPROFILE) { $HomeDir = $env:USERPROFILE }
elseif ($env:HOME)    { $HomeDir = $env:HOME }
else                  { $HomeDir = [Environment]::GetFolderPath('UserProfile') }
$ClaudeHome = Join-Path $HomeDir '.claude'
$CodexHome  = Join-Path $HomeDir '.codex'
$Zipball    = "https://github.com/$Owner/$RepoName/archive/refs/heads/main.zip"

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
  Head "Downloading $Skill..."
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
  if (-not $found) { Bad "could not find the skill in the zip"; Invoke-Cleanup; exit 1 }
  # <root>/anti-ai-design-style/.claude-plugin/plugin.json -> <root>
  $Src = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $found.FullName))
  Ok "downloaded"
}
$SkillSrc = Join-Path $Src $Skill
Detail "source: $SkillSrc"

# ===================================================================
# 2. detect platform + runtime
# ===================================================================
$OsName = 'Windows'
try { if (-not ($env:OS -eq 'Windows_NT')) { $OsName = [System.Environment]::OSVersion.Platform.ToString() } } catch { }
$Pm = ''
foreach ($c in @('winget', 'choco', 'scoop')) { if (Have $c) { $Pm = $c; break } }

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
$Py = Find-Python
$PmLabel = 'none'; if ($Pm) { $PmLabel = $Pm }
$PyLabel = 'missing'; if ($Py) { $PyLabel = $Py }
Head "$Skill installer   .   $OsName   .   package manager: $PmLabel   .   python: $PyLabel"

function Install-Python {
  if ($script:Py) { return $true }
  if (-not $Pm) {
    Skip "Python 3.8+ is missing and no package manager was found. Get it from https://www.python.org/downloads/windows/ (tick 'Add python.exe to PATH'), then re-run."
    return $false
  }
  Dim "python not found - bootstrapping via $Pm..."
  try {
    switch ($Pm) {
      'winget' { Invoke-Native 'winget' @('install', '-e', '--id', 'Python.Python.3.12', '--accept-source-agreements', '--accept-package-agreements') | Out-Null }
      'choco'  { Invoke-Native 'choco'  @('install', 'python3', '-y') | Out-Null }
      'scoop'  { Invoke-Native 'scoop'  @('install', 'python') | Out-Null }
    }
  } catch { }
  $script:Py = Find-Python
  if ($script:Py) { Ok "python installed: $script:Py"; return $true }
  Skip "couldn't bootstrap Python via $Pm. Get it from https://www.python.org/downloads/windows/ and re-run."
  return $false
}

# ---- Node helpers (only the editor surfaces need npx) ----
function Get-NodeBin {
  $cand = @()
  try { $g = Get-Command node -ErrorAction SilentlyContinue; if ($g) { $cand += $g.Source } } catch { }
  $cand += (Join-Path $HomeDir '.local\node-current\node.exe')
  $cand += (Join-Path $HomeDir '.local\node-current\bin\node.exe')
  foreach ($c in $cand) { if ($c -and (Test-Path $c)) { return $c } }
  return $null
}
function Get-NpxBin {
  $nb = Get-NodeBin
  if ($nb) {
    $dir = Split-Path -Parent $nb
    foreach ($n in @('npx.cmd', 'npx.exe', 'npx')) {
      $p = Join-Path $dir $n
      if (Test-Path $p) { return $p }
    }
  }
  if (Have 'npx') { return (Get-Command npx).Source }
  return $null
}
function Install-Node {
  if (Get-NpxBin) { return $true }
  if (-not $Pm) { return $false }
  Dim "Node not found (only editors need it) - bootstrapping via $Pm..."
  try {
    switch ($Pm) {
      'winget' { Invoke-Native 'winget' @('install', '-e', '--id', 'OpenJS.NodeJS.LTS', '--accept-source-agreements', '--accept-package-agreements') | Out-Null }
      'choco'  { Invoke-Native 'choco'  @('install', 'nodejs-lts', '-y') | Out-Null }
      'scoop'  { Invoke-Native 'scoop'  @('install', 'nodejs-lts') | Out-Null }
    }
  } catch { return $false }
  return [bool](Get-NpxBin)
}

# ===================================================================
# 3. detect surfaces
# ===================================================================
function Test-App([string[]]$names) {
  # Installed apps: the uninstall registry keys, then per-user Programs folders.
  $keys = @(
    'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
    'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall',
    'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'
  )
  foreach ($k in $keys) {
    try {
      if (-not (Test-Path $k)) { continue }
      $items = Get-ItemProperty -Path (Join-Path $k '*') -ErrorAction SilentlyContinue
      foreach ($it in @($items)) {
        $dn = Get-Prop $it 'DisplayName'
        if (-not $dn) { continue }
        foreach ($n in $names) { if ("$dn" -like "$n*") { return $true } }
      }
    } catch { }
  }
  if ($env:LOCALAPPDATA) {
    $programs = Join-Path $env:LOCALAPPDATA 'Programs'
    $folders = @{ 'Visual Studio Code' = @('Microsoft VS Code'); 'Microsoft Visual Studio Code' = @('Microsoft VS Code'); 'VSCodium' = @('VSCodium'); 'Cursor' = @('cursor', 'Cursor'); 'Windsurf' = @('Windsurf'); 'Zed' = @('Zed') }
    foreach ($n in $names) {
      $cands = @($n)
      if ($folders.ContainsKey($n)) { $cands += $folders[$n] }
      foreach ($f in $cands) { try { if (Test-Path (Join-Path $programs $f)) { return $true } } catch { } }
    }
  }
  return $false
}
function Test-VsExt([string]$id) {
  foreach ($root in @('.vscode\extensions', '.vscode-oss\extensions')) {
    $dir = Join-Path $HomeDir $root
    try {
      if ((Test-Path $dir) -and (Get-ChildItem -Path $dir -Directory -Filter "$id*" -ErrorAction SilentlyContinue | Select-Object -First 1)) { return $true }
    } catch { }
  }
  return $false
}
function Test-Editor([string]$id) {
  switch ($id) {
    'cursor'     { return ((Test-App @('Cursor')) -or (Have 'cursor')) }
    'vscode'     { return ((Test-App @('Microsoft Visual Studio Code', 'Visual Studio Code', 'VSCodium')) -or (Have 'code') -or (Have 'codium')) }
    'windsurf'   { return ((Test-App @('Windsurf')) -or (Have 'windsurf')) }
    'zed'        { return ((Test-App @('Zed')) -or (Have 'zed')) }
    'cline'      { return (Test-VsExt 'saoudrizwan.claude-dev') }
    'roo'        { return (Test-VsExt 'rooveterinaryinc.roo-cline') }
    'continue'   { return (Test-Path (Join-Path $HomeDir '.continue')) }
    'gemini-cli' { return ((Have 'gemini') -or (Test-Path (Join-Path $HomeDir '.gemini'))) }
    'aider'      { return (Have 'aider') }
    'opencode'   { return (Have 'opencode') }
    'amp'        { return (Have 'amp') }
    default      { return $false }
  }
}
function Get-AgentFor([string]$id) {
  switch ($id) {
    'vscode' { return 'github-copilot' }
    'aider'  { return 'aider-desk' }
    default  { return $id }
  }
}
$Editors = @('cursor', 'vscode', 'windsurf', 'zed', 'cline', 'roo', 'continue', 'gemini-cli', 'aider', 'opencode', 'amp')

function Test-Wants([string]$id) {
  if ($Only -and -not (Test-InList $Only $id)) { return $false }
  if ($Skip -and (Test-InList $Skip $id)) { return $false }
  return $true
}
function Test-Cowork {
  # Cowork shares ~/.claude with Claude Code; it is covered by claude-home, never installed twice.
  $dirs = @()
  if ($env:APPDATA) { $dirs += (Join-Path $env:APPDATA 'Claude') }
  $dirs += (Join-Path $HomeDir '.config\Claude')
  foreach ($d in $dirs) { try { if ($d -and (Test-Path $d)) { return $true } } catch { } }
  return $false
}

# ===================================================================
# 4. plan
# ===================================================================
$Act = 'install'; if ($Uninstall) { $Act = 'uninstall' }
Head "Here's what I found (and will ${Act}):"
$PlanClaude = $false; $PlanCodex = $false; $PlanEditors = @()

if (Test-Wants 'claude-code') {
  if ((Test-Path $ClaudeHome) -or (-not $Uninstall)) {
    $PlanClaude = $true
    $coworkNote = ''; if (Test-Cowork) { $coworkNote = ' + Cowork detected' }
    Ok "Claude Code / Cowork  (~/.claude)$coworkNote"
  }
}
if ((Test-Wants 'codex') -and (Test-Path $CodexHome)) { $PlanCodex = $true; Ok "Codex  (~/.codex)" }
foreach ($e in $Editors) {
  if (-not (Test-Wants $e)) { continue }
  if (Test-Editor $e) { $PlanEditors += $e; Ok "$e  (via skills CLI)" }
  elseif ($Details) { Skip "$e (not found)" }
}
if (-not $PlanClaude -and -not $PlanCodex -and $PlanEditors.Count -eq 0) {
  Skip "no supported surfaces detected"
  Say ""
  Say "Manual per-surface commands:"
  Say "  Claude Code : re-run this script (installs to ~/.claude)"
  Say "  Codex       : re-run once ~/.codex exists"
  Say "  Editors     : npx -y skills@latest add $Owner/$RepoName --global --agent <agent> --copy --full-depth"
}
if (-not $Py -and -not $Uninstall) {
  $via = 'a package manager'; if ($Pm) { $via = $Pm }
  Skip "python 3.8+ is missing; the hooks need it. I will try to install it via $via."
}

if ($DryRun) { Head "Dry run - nothing installed."; Invoke-Cleanup; exit 0 }
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
  # ${CLAUDE_PLUGIN_ROOT} is unset outside a plugin; the commands would call nothing.
  # Forward slashes: the path sits inside python3 "..." and Python accepts either on Windows.
  $fwd = To-Fwd $InstalledSkill
  New-Item -ItemType Directory -Force -Path $DestDir | Out-Null
  foreach ($c in (Get-ChildItem -Path $SrcDir -Filter '*.md' -File -ErrorAction SilentlyContinue)) {
    $text = Get-Content -Raw -Path $c.FullName
    $text = $text.Replace('${CLAUDE_PLUGIN_ROOT}', $fwd).Replace('<skill-path>', $fwd)
    Write-Utf8NoBom (Join-Path $DestDir $c.Name) $text
  }
}
function Test-ClaudeProof([string]$InstalledSkill) {
  if (-not $script:Py) { return $false }
  $r = Invoke-Native $script:Py @((Join3 $InstalledSkill 'scripts' 'verify_all.py'), (Join3 $InstalledSkill 'examples' 'fixed-example.html'))
  if ($r.Out.Count -eq 0) { return $false }
  return ("$($r.Out[-1])" -like 'PASS:*')
}

# ---- install: claude-home (Claude Code + Cowork share ~/.claude) ----
function Install-Claude([string]$Dir) {
  $dest = Join3 $Dir 'skills' $Skill
  New-Item -ItemType Directory -Force -Path (Join-Path $Dir 'commands') | Out-Null
  Copy-SkillFolder $dest
  Copy-Commands (Join-Path $SkillSrc 'commands') (Join-Path $Dir 'commands') $dest
  $scriptsDir = Join-Path $dest 'scripts'
  if ($scriptsDir -match '\s') {
    Bad "hook path has a space ($scriptsDir) - skipping hook registration (a hook path with a space breaks tool use)"
    return
  }
  if (-not (Install-Python)) { Skip "Claude files installed; the hooks need python 3.8+ (install it, then re-run)"; return }
  $settingsPath = Join-Path $Dir 'settings.json'
  $backup = "$settingsPath.bak.aads"
  if (Test-Path $settingsPath) { try { Copy-Item -Force -Path $settingsPath -Destination $backup } catch { } }
  else { Write-Utf8NoBom $settingsPath '{}' }
  $registered = $false
  try { $registered = Register-Hooks $settingsPath $scriptsDir } catch {
    Bad "hook registration failed: $($_.Exception.Message) - settings.json restored from backup (settings.json.bak.aads)"
    if (Test-Path $backup) { try { Copy-Item -Force -Path $backup -Destination $settingsPath } catch { } }
  }
  if ($registered) { Ok "Claude Code / Cowork - skill, 3 commands, 2 hooks registered" }
  else { Bad "hook registration failed; settings.json left as it was (backup: settings.json.bak.aads)" }
  $py = $script:Py
  if (Test-ClaudeProof $dest) { Ok "verified: the installed skill printed PASS on its own example" }
  else { Bad "installed, but the skill's own proof line did not print PASS. Run: `"$py`" `"$(Join3 $dest 'scripts' 'verify_all.py')`" `"$(Join3 $dest 'examples' 'fixed-example.html')`"" }
}
function Uninstall-Claude([string]$Dir) {
  $dest = Join3 $Dir 'skills' $Skill
  if (Test-Path $dest) { Remove-Item -Recurse -Force $dest -ErrorAction SilentlyContinue }
  foreach ($n in @('design-check.md', 'design-fix.md', 'design-brief.md')) {
    $p = Join3 $Dir 'commands' $n
    if (Test-Path $p) { Remove-Item -Force $p -ErrorAction SilentlyContinue }
  }
  Remove-Hooks (Join-Path $Dir 'settings.json')
  Ok "Claude Code / Cowork - removed (skill, commands, hooks)"
}

# ---- install: codex-home ----
function Install-Codex {
  $dest = Join3 $CodexHome 'plugins' $Skill
  Copy-SkillFolder $dest
  $scriptsDir = Join-Path $dest 'scripts'
  if ($scriptsDir -match '\s') { Bad "codex hook path has a space ($scriptsDir) - skipping hooks"; return }
  if (-not (Install-Python)) { Skip "Codex plugin copied; hooks need python 3.8+"; return }
  $hooksPath = Join-Path $CodexHome 'hooks.json'
  $backup = "$hooksPath.bak.aads"
  if (Test-Path $hooksPath) { try { Copy-Item -Force -Path $hooksPath -Destination $backup } catch { } }
  else { Write-Utf8NoBom $hooksPath '{}' }
  $registered = $false
  try { $registered = Register-Hooks $hooksPath $scriptsDir } catch {
    if (Test-Path $backup) { try { Copy-Item -Force -Path $backup -Destination $hooksPath } catch { } }
  }
  if ($registered) { Ok "Codex - plugin + 2 hooks" } else { Skip "Codex plugin copied; hook registration failed (hooks.json restored from backup)" }
  Dim "For a project Codex reads directly (.agents/skills/): `"$script:Py`" `"$(Join3 $dest 'scripts' 'install.py')`" --codex <project>"
}
function Uninstall-Codex {
  $dest = Join3 $CodexHome 'plugins' $Skill
  if (Test-Path $dest) { Remove-Item -Recurse -Force $dest -ErrorAction SilentlyContinue }
  Remove-Hooks (Join-Path $CodexHome 'hooks.json')
  Ok "Codex - removed"
}

# ---- install: editors via skills CLI (npx) ----
function Install-Editor([string]$e) {
  $ag = Get-AgentFor $e
  $manual = "npx -y skills@latest add $Owner/$RepoName --global --agent $ag --copy --full-depth"
  if (-not (Install-Node)) { Skip "$e - needs Node/npx (couldn't bootstrap). Manual: $manual"; return }
  $npx = Get-NpxBin
  if (-not $npx) { Skip "$e - npx unavailable. Manual: $manual"; return }
  $r = Invoke-Native $npx @('-y', 'skills@latest', 'add', "$Owner/$RepoName", '--global', '--agent', $ag, '--skill', '*', '-y', '--copy', '--full-depth')
  if ($r.Code -eq 0) { Ok "$e - installed (agent: $ag)" } else { Skip "$e - skills CLI failed; manual: $manual" }
}
function Uninstall-Editor([string]$e) {
  $ag = Get-AgentFor $e
  $npx = Get-NpxBin
  if ($npx) { Invoke-Native $npx @('-y', 'skills@latest', 'remove', $Skill, '--global', '--agent', $ag) | Out-Null }
  Ok "$e - remove attempted"
}

# ===================================================================
# 6-8. run, verify, summarise
# ===================================================================
$HardFail = $false
function Invoke-Surface([string]$label, [scriptblock]$body) {
  # One surface failing never aborts the others.
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
    foreach ($e in $PlanEditors) { Invoke-Surface $e { Uninstall-Editor $e } }
    Head "Uninstalled. Restart your editor to clear loaded skills."
    Dim "Backups kept: settings.json.bak.aads / hooks.json.bak.aads - copy one back over the original if you want the pre-install file."
    if ($HardFail) { exit 1 } else { exit 0 }
  }

  if ($PlanClaude) { Invoke-Surface 'Claude Code' { Install-Claude $ClaudeHome } }
  if ($PlanCodex)  { Invoke-Surface 'Codex' { Install-Codex } }
  foreach ($e in $PlanEditors) { Invoke-Surface $e { Install-Editor $e } }

  Head "Done."
  Say ""
  $installedSkill = To-Fwd (Join3 $ClaudeHome 'skills' $Skill)
  $pyName = 'python'; if ($Py) { $pyName = "`"$(To-Fwd $Py)`"" }
  Write-C "Next: open Claude Code and type /design-check <a page> - or just build a page; the hooks run by themselves." 'Cyan'
  Write-C "One thing this installer cannot do: the five hookify warning rules only load from the folder you work in." 'Cyan'
  Say "  Inside any project, run:  $pyName `"$installedSkill/scripts/install.py`" ."
  Dim "Tips: /design-fix (repair what the scan found)  .  /design-brief (before building)  .  re-run with -Uninstall to remove."
  if ($HardFail) { exit 1 }
}
finally {
  Invoke-Cleanup
}
