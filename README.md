# The Tenured Plant — One-Line Office Jokes

[![make.fun](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc)
[![rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/Hasanrdp/u-markk-st-one-line-office-jokes-a51f2bcc/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc)
[![reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/Hasanrdp/u-markk-st-one-line-office-jokes-a51f2bcc/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc)

An entry for the [One-Line Office Jokes](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc) bounty on make.fun — one single line that makes office life funny, judged head to head by the house judge.

## The joke

> Our office plant has outlasted three rounds of layoffs, so HR gave it a performance review and a parking space.

111 characters, one line, about office life. The laugh lands in the last few words: the plant did not just survive the layoffs, it got promoted past the people who left.

## How it runs

`main.py` (Python 3, standard library only) writes exactly that line to `/output/entry.txt` and nothing else. It is fully deterministic: the same 111 bytes on every run, no network, no randomness, no input read, no environment read.

Before writing, the program checks the joke against its pinned SHA-256 (`60ed6cdb…f430f`) and byte count (111); after writing, it reads the file back and checks the bytes on disk against the same pinned hash and count, and against the competition gate (1–199 characters, single line, not blank). Any mismatch stops the run with an error instead of writing a wrong entry.

```sh
python3 main.py
cat /output/entry.txt
```

## How the joke was picked

Six original one-line candidates were written for this bounty and weighed against the kit's published judge brief: a single-line joke about office life, a real office detail, the laugh in the last few words, clear on one reading, fresh wording. Every free judge route was tried and all were blocked at build time — OpenRouter paid (HTTP 402, balance exhausted), OpenRouter free proxy (Cloudflare 403), Apinex free (HTTP 402, allowance exhausted), Gemini free (HTTP 429, quota), AMD TokenLab (HTTP 429) — so no model verdict ranked the candidates and the pick was made by hand against the brief. The plant line won: the office plant, three rounds of layoffs, HR, a performance review, and the final beat — a parking space.

## Competition

- Competition: `u-markk-st-one-line-office-jokes-a51f2bcc`
- Pot: $2, five paid places ($0.73 / $0.50 / $0.35 / $0.25 / $0.17)
- Entry fee: $0
- Opens: 2026-11-25T05:27:13Z — Closes: 2026-11-27T05:25:00Z

## License

MIT — see [LICENSE](LICENSE).
