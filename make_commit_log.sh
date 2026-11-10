#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
git log --reverse --date=iso --format='%h | %ad | %an | %s' > git_commit_log.txt
echo "Đã xuất Git commit log vào git_commit_log.txt"
