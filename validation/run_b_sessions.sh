#!/usr/bin/env bash
# Run a set of blind assessor sessions in parallel; one process per session.
set -uo pipefail
cd "$(dirname "$0")"
export OPENROUTER_API_KEY="$(grep -m1 '^OPENROUTER_API_KEY=' ~/.hermes/.env | cut -d= -f2-)"
mkdir -p runB

run() {  # run <assessor> <model> <pack> <fixture> <outdir>
  python3 score_pack.py --via openrouter --model "$2" --assessor "$1" \
    --pack "$3" --out "$5/scores-$1.json" --fixture "$4" > "$5/log-$1.txt" 2>&1
  echo "$1 exit=$?" >> "$5/log-$1.txt"
}

B=AIMF-VAL-2026-B-EVIDENCE-PACK.md
A=AIMF-VAL-2026-A-EVIDENCE-PACK.md

case "${1:?set}" in
  b1)
    run BA  anthropic/claude-sonnet-5.5 "$B" AIMF-VAL-2026-B runB &
    run BB  openai/gpt-4.1             "$B" AIMF-VAL-2026-B runB &
    run BD1 deepseek/deepseek-chat     "$B" AIMF-VAL-2026-B runB &
    ;;
  b2)
    run BD2 deepseek/deepseek-chat     "$B" AIMF-VAL-2026-B runB &
    run AD1 deepseek/deepseek-chat     "$A" AIMF-VAL-2026-A runB &
    run AD2 deepseek/deepseek-chat     "$A" AIMF-VAL-2026-A runB &
    ;;
esac
wait
tail -n 2 runB/log-*.txt
