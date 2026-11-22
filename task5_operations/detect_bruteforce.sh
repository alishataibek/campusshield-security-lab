#!/bin/bash
LOG=${1:-/var/log/auth.log}
THRESHOLD=3

echo "=== Failed SSH login report: $(date) ==="
RESULTS=$(grep "Failed password" "$LOG" | grep -oE "from [0-9.]+" | awk '{print $2}' | sort | uniq -c)

if [ -z "$RESULTS" ]; then
  echo "No failed SSH logins found."
  exit 0
fi

echo "$RESULTS" | while read count ip; do
  if [ "$count" -ge "$THRESHOLD" ]; then
    echo "ALERT: $count failed SSH logins from $ip (possible brute force)"
  else
    echo "ok: $count failed login(s) from $ip"
  fi
done
