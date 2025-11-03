    # .vscode/onSavePush.ps1
    param([string]$file = "")

    # 0) 리포지토리 루트로 이동
    Set-Location -Path (Resolve-Path "$PSScriptRoot\..")

    # 1) 너무 잦은 실행 방지(디바운스 5초)
    $lock = ".git\.autopush.lock"
    if (Test-Path $lock) {
    $age = (Get-Date) - (Get-Item $lock).LastWriteTime
    if ($age.TotalSeconds -lt 5) { exit 0 }
    }
    New-Item -ItemType File -Path $lock -Force | Out-Null

    try {
    # 2) 변경사항 없으면 종료
    $status = git status --porcelain
    if (-not $status) { exit 0 }

    # 3) 커밋 & 푸시
    git add -A

    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $msg = "auto: save $ts $file"
    git commit -m "$msg" 2>$null  # 변경 없으면 조용히 스킵

    # (옵션) 리베이스 풀: 충돌 위험 있으면 주석처리
    # git pull --rebase origin HEAD

    git push origin HEAD
    }
    finally {
    # 4) 락 파일 타임스탬프 갱신(다음 실행 간격 측정용)
    (Get-Item $lock).LastWriteTime = Get-Date
    }
