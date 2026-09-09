#!/usr/bin/env python3
"""Run trigger evals for one or more skills against the Anthropic API.

claude.ai has no command-line harness, so this reproduces the triggering
decision the model makes there: it sees the plugin's skill list (name plus
description, exactly as claude.ai presents it) and a user message, and must
say which skill, if any, it would open first.

Usage:
    pip install anthropic
    export ANTHROPIC_API_KEY=...
    python evals/run_trigger.py                      # all skills, 3 runs each
    python evals/run_trigger.py --skill brief        # one skill
    python evals/run_trigger.py --runs 5 --model claude-sonnet-4-6

Exit code is 1 when any query misses its target on any run, so it can gate
a CI job.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
TRIGGER_DIR = ROOT / "evals" / "trigger"
PLUGIN_NAME = "corpus"

FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---", re.S)


def read_skill_meta(skill_dir: Path) -> dict[str, str]:
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    m = FRONTMATTER.match(text)
    if not m:
        raise SystemExit(f"{skill_dir}: SKILL.md has no frontmatter")
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta


def available_skills_block(skills: list[dict[str, str]]) -> str:
    # Mirrors the shape claude.ai uses when it lists installed plugin skills.
    parts = ["<available_skills>"]
    for s in skills:
        parts.append(
            "<skill>\n<name>\n"
            f"{PLUGIN_NAME}:{s['name']}\n"
            "</name>\n<description>\n"
            f"{s['description']}\n"
            "</description>\n</skill>"
        )
    parts.append("</available_skills>")
    return "\n".join(parts)


SYSTEM = """You are Claude in claude.ai. The user's organization has installed a plugin whose skills are listed below. Before answering a request you decide whether to open one of these skills first.

{skills}

Answer with a single line of JSON and nothing else:
{{"skill": "<plugin:skill name>" or null, "reason": "<under 15 words>"}}

Open a skill when its description covers the request. Answer null when no listed skill applies, or when the request is better handled directly. Do not open a skill only because it shares a word with the request."""


def decide(client: anthropic.Anthropic, model: str, skills_block: str, query: str) -> str | None:
    resp = client.messages.create(
        model=model,
        max_tokens=100,
        system=SYSTEM.format(skills=skills_block),
        messages=[{"role": "user", "content": query}],
    )
    text = "".join(b.text for b in resp.content if b.type == "text").strip()
    text = text.replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(text).get("skill")
    except json.JSONDecodeError:
        return f"<unparseable: {text[:60]}>"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", action="append", help="skill name(s) to evaluate; default all with a trigger file")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--model", default="claude-sonnet-4-6")
    args = ap.parse_args()

    skills = [read_skill_meta(d) for d in sorted(SKILLS_DIR.iterdir()) if (d / "SKILL.md").exists()]
    skills_block = available_skills_block(skills)
    client = anthropic.Anthropic()

    targets = args.skill or [p.stem for p in sorted(TRIGGER_DIR.glob("*.json"))]
    failed = 0
    for name in targets:
        cases = json.loads((TRIGGER_DIR / f"{name}.json").read_text(encoding="utf-8"))
        full = f"{PLUGIN_NAME}:{name}"
        print(f"\n== {full}  ({len(cases)} queries x {args.runs} runs)")
        for case in cases:
            hits = defaultdict(int)
            for _ in range(args.runs):
                hits[decide(client, args.model, skills_block, case["query"])] += 1
            rate = hits.get(full, 0) / args.runs
            want = case["should_trigger"]
            ok = (rate == 1.0) if want else (rate == 0.0)
            failed += 0 if ok else 1
            mark = "ok " if ok else "MISS"
            others = {k: v for k, v in hits.items() if k != full}
            print(f"  {mark} {'T' if want else 'F'} {rate:.2f}  {case['query'][:70]!r}"
                  + (f"  others={dict(others)}" if others and not ok else ""))
    print(f"\n{failed} query(ies) missed target" if failed else "\nall queries on target")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
