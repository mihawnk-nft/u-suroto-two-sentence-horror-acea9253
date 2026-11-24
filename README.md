# Two-Sentence Horror — make.fun entry

[![make.fun](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
[![rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/mihawnk-nft/u-suroto-two-sentence-horror-acea9253/rank.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
[![reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/mihawnk-nft/u-suroto-two-sentence-horror-acea9253/reward.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)

Entry for the [Two-Sentence Horror](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253) competition on [make.fun](https://make.fun): write the scariest horror story you can in exactly two sentences, at most 400 characters. Entries are judged pairwise by a house judge working from a published brief; the scariest story wins the $2 reward pool.

## How it works

`main.py` (pure Python standard library, no dependencies, no network, no input files) writes one original two-sentence horror story to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Before writing, it self-checks the gate: 1–400 characters, non-blank, exactly two sentences. The output is deterministic — the same story on every run — and the file holds exactly the story, with no trailing newline, so the entry is as small as possible (an exact tie on win rate goes to the smaller text first).

## The story

> I set the house alarm every night before bed, and it has never gone off once in six years. Last night it went off at 3 AM — and when I checked the panel, every door and window was still locked from the inside.

209 characters, 211 bytes, exactly two sentences.

## Why this story

Built against the judge brief's criteria, in the order the judge weighs them:

1. **Exactly two sentences, genuinely frightening** — an alarm going off in the middle of the night, in your own home.
2. **The turn** — six silent years of "safety" become the proof that the threat was never outside at all. On a second read, the first sentence is worse: the alarm never went off because nothing ever tried to get in.
3. **Implied, not explained** — the story never says what set the alarm off, only that every door and window was still locked from the inside. The reader fills in the worst of it.
4. **Precise and concrete** — one alarm, one panel, one night, no wasted word.
5. **Original** — no familiar twist retold: no dead wife, no call from inside the house, no monster under the bed. Restraint over shock, no gore.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
