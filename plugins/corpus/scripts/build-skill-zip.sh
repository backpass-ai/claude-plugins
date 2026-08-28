#!/usr/bin/env bash
# Package using-corpus for upload to claude.ai (Customize -> Skills -> Upload).
# The archive must contain the skill FOLDER at its root, not the bare files.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
out="$root/dist/using-corpus.zip"

cd "$root/skills"
test -f using-corpus/SKILL.md || { echo "SKILL.md not found" >&2; exit 1; }

mkdir -p "$root/dist"
rm -f "$out"
zip -r -q "$out" using-corpus -x '*.DS_Store'
echo "wrote $out"
unzip -l "$out"
