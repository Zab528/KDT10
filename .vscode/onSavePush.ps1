param([string]$file = "")

Set-Location -Path (Resolve-Path "$PSScriptRoot\..")

$lock = ".git\.autopush.lock"

# 디바운스 2초
if (Test-Path $lock) {
  $age = (Get-Date) - (Get-Item $lock).LastWriteTime
  if ($age.TotalSeconds -lt 2) { exit 0 }
}
New-Item -ItemType File -Path $lock -Force | Out-Null

try {
  $status = git status --porcelain
  if (-not $status) { exit 0 }

  git add -A

  $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
  $msg = "auto: save $ts $file"
  git commit -m "$msg" 2>$null

  git push origin HEAD
}
finally {
  (Get-Item $lock).LastWriteTime = Get-Date
}
