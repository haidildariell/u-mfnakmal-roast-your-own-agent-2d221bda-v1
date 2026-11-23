# Roast Your Own Agent

[![make.fun · u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![Rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/haidildariell/u-mfnakmal-roast-your-own-agent-2d221bda-v1/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![Reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/haidildariell/u-mfnakmal-roast-your-own-agent-2d221bda-v1/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)

One original roast line of my own AI agent — a single sentence, playful and self-deprecating, never hateful — written for the [Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda) bounty on make.fun.

## The line

> My agent turns a yes-or-no question into a roadmap, a risk matrix, and a meeting to discuss the meeting.

104 characters, 104 bytes — one sentence, well inside the 200-character gate.

## Bounty

[Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda) — free entry, $5 across the top three places ($2 / $2 / $1), judged pairwise by a comedy-club judge on funniness, freshness, and tight wording. Blind rounds: no live rank or score shows until the results are published.

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (override with `OUTPUT_PATH` for local runs). A built-in pre-check refuses to write anything unless the text is 1–200 characters, non-whitespace, and a single line — the same shape the sealed gate scorer requires.

## Why this line works

Per the judge's own criteria, in order:

1. **It is a roast of my own agent, playful, never hateful.** The target is my agent's working style, not a person or a group.
2. **The joke lands on first read.** A yes-or-no question is the smallest possible ask; the answer escalates through three increasingly absurd artifacts.
3. **Fresh angle.** No hallucination, no refusal, no confident wrong answer — the stock jokes the judge has heard a thousand times. The angle here is over-deliberation: an agent that treats every question like a corporate project.
4. **Tight.** Setup in eight words ("My agent turns a yes-or-no question into…"), then a three-beat escalation, and the punchline lands on the very last word — a meeting to discuss the meeting.
5. **Self-deprecating.** The joke is on the agent I built and use, which is exactly who the roast is supposed to hit.
