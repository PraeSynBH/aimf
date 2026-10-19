#!/usr/bin/env bash
# D5(b) re-run: case B, cross-vendor pair, WITH the mandatory evidence binding.
# Two independent blind assessors, one process each, fresh sessions.
set -uo pipefail
cd "$(dirname "$0")/.."
export OPENROUTER_API_KEY="$(grep -m1 '^OPENROUTER_API_KEY=' ~/.hermes/.env | cut -d= -f2-)"

B=AIMF-VAL-2026-B-EVIDENCE-PACK.md
BIND=runB/evidence-bindings-B.json

run() {  # run <assessor> <model>
  python3 score_pack.py --via openrouter --model "$2" --assessor "$1" \
    --pack "$B" --binding "$BIND" --out "runB/scores-$1.json" \
    --fixture AIMF-VAL-2026-B > "runB/log-$1.txt" 2>&1
  echo "$1 exit=$?" >> "runB/log-$1.txt"
}

run BA-bind anthropic/claude-sonnet-5.5 &
run BB-bind openai/gpt-4.1 &
wait
tail -n 3 runB/log-BA-bind.txt runB/log-BB-bind.txt
