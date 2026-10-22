#!/usr/bin/env bash
set -euo pipefail

CHECK_URL="${1:-https://httpbin.org/status/200}"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

echo "=========================================="
echo "  System Health Check: $TIMESTAMP"
echo "=========================================="

echo "Checking endpoint: $CHECK_URL"
HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$CHECK_URL" || echo "000")

if [ "$HTTP_STATUS" -eq 200 ]; then
    echo " [SUCCESS] Endpoint reachable (HTTP $HTTP_STATUS)"
else
    echo " [FAILURE] Endpoint error! Status code: $HTTP_STATUS"
fi
echo "=========================================="

