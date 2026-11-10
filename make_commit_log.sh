#!/usr/bin/env bash
# Xuất Git commit log ra file text cho bài nộp.
# Chạy trong thư mục submission (đã `git init`):  ./make_commit_log.sh
set -euo pipefail
git log --reverse --date=iso --pretty=format:'%h | %ad | %an | %s' > git_commit_log.txt
echo "Đã ghi $(wc -l < git_commit_log.txt) commit vào git_commit_log.txt"
