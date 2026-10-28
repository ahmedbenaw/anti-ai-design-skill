<#
.SYNOPSIS
  Installs the skill on Windows, checks what landed, then removes it.

.DESCRIPTION
  The whole round trip, in the order a user would hit it:

    1. A dry run must write nothing.
    2. An install must land on user-profile paths, with the repo's version.
    3. The installed copy's selftests must pass.
    4. A second install must add no new references. That is the 3.2.2
       single-registration fix.
    5. An uninstall must remove every file it added and every reference it
       wrote, and leave settings.json as valid JSON.

  Step 4 counts references before and after rather than asserting a fixed
  number, because the point is that a repeat install changes nothing. An
  absolute count would encode a guess about how many an install should write,
  and would fail for the wrong reason the day that number legitimately
  changes.

  Run it on a throwaway machine or a CI runner: it installs into, and then
  deletes from, the current user profile.

.PARAMETER RepoRoot
  The clone to install from. Defaults to this script's parent's parent.
#>
[CmdletBinding()]
param(
  [string]$RepoRoot = (Split-Path -Parent (Split-Path -Parent $PSCommandPath))
)

$ErrorActionPreference = 'Stop'

$skill = 'anti-ai-design-style'
$home_ = $env:USERPROFILE
if (-not $home_) {
  Write-Host "USERPROFILE is not set; this script is for Windows"
  exit 1
}

$skillDir = Join-Path $home_ ('.claude\skills\' + $skill)
$codexDir = Join-Path $home_ ('.agents\skills\' + $skill)
$settings = Join-Path $home_ '.claude\settings.json'
$installer = Join-Path $RepoRoot 'install.ps1'
$repoPlugin = Join-Path $RepoRoot ($skill + '\.claude-plugin\plugin.json')

foreach ($p in @($installer, $repoPlugin)) {
  if (-not (Test-Path $p)) { Write-Host "not found: $p"; exit 1 }
}

function Count-Ours {
  if (-not (Test-Path $settings)) { return 0 }
  return ([regex]::Matches((Get-Content $settings -Raw), 'anti-ai-design')).Count
}

function Fail([string]$why) {
  Write-Host ""
  Write-Host "ROUND TRIP: FAIL - $why"
  exit 1
}

Push-Location $RepoRoot
try {
  # --- 1. dry run -----------------------------------------------------------
  if (Test-Path $skillDir) { Fail "the skill was already installed before we started" }
  & $installer -Yes -DryRun
  if ($LASTEXITCODE -ne 0) { Fail "dry run exited $LASTEXITCODE" }
  if (Test-Path $skillDir) { Fail "the dry run installed something" }
  Write-Host "  ok   dry run wrote nothing"

  # --- 2. install -----------------------------------------------------------
  & $installer -Yes
  if ($LASTEXITCODE -ne 0) { Fail "install exited $LASTEXITCODE" }

  # USERPROFILE, not HOME. Native backslashes, not forward slashes.
  foreach ($p in @($skillDir, $codexDir)) {
    if (-not (Test-Path $p)) { Fail "missing after install: $p" }
  }
  $installedPlugin = Join-Path $skillDir '.claude-plugin\plugin.json'
  if (-not (Test-Path $installedPlugin)) { Fail "missing after install: $installedPlugin" }

  $want = (Get-Content $repoPlugin -Raw | ConvertFrom-Json).version
  $got = (Get-Content $installedPlugin -Raw | ConvertFrom-Json).version
  if ($want -ne $got) { Fail "installed version $got but the repo says $want" }
  Write-Host "  ok   installed $got on user-profile paths"

  # --- 3. the installed copy's own selftests --------------------------------
  $runner = Join-Path $RepoRoot 'installer\ci-run-selftests.ps1'
  & $runner -ScriptsDir (Join-Path $skillDir 'scripts')
  if ($LASTEXITCODE -ne 0) { Fail "the installed copy's selftests failed" }
  Write-Host "  ok   the installed copy's selftests pass"

  # --- 4. installing twice registers once -----------------------------------
  $before = Count-Ours
  & $installer -Yes
  if ($LASTEXITCODE -ne 0) { Fail "the second install exited $LASTEXITCODE" }
  $after = Count-Ours
  if ($after -ne $before) {
    Fail "a second install changed our references from $before to $after"
  }
  Write-Host "  ok   a second install added nothing (references stayed at $after)"

  # --- 5. uninstall ---------------------------------------------------------
  & $installer -Yes -Uninstall
  if ($LASTEXITCODE -ne 0) { Fail "uninstall exited $LASTEXITCODE" }
  foreach ($p in @($skillDir, $codexDir)) {
    if (Test-Path $p) { Fail "still present after uninstall: $p" }
  }
  if (Test-Path $settings) {
    $left = Count-Ours
    if ($left -ne 0) { Fail "$left of our references left in settings.json" }
    try {
      Get-Content $settings -Raw | ConvertFrom-Json | Out-Null
    } catch {
      Fail "settings.json is no longer valid JSON: $($_.Exception.Message)"
    }
  }
  Write-Host "  ok   uninstall removed every file and reference, JSON still valid"
} finally {
  Pop-Location
}

Write-Host ""
Write-Host "ROUND TRIP: PASS"
exit 0
