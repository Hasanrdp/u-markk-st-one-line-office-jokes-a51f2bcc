#!/usr/bin/env python3
"""One-Line Office Jokes entry: a single office joke, written to /output/entry.txt.

The program writes one original one-line joke about office life (111
characters, inside the 1-199 character gate) and nothing else. It is fully
deterministic: the same bytes on every run, no network, no randomness, no
input read, no environment read.

The joke was picked from six original candidates written for this bounty.
Every free judge route was tried and all were blocked at build time
(OpenRouter paid: HTTP 402 balance exhausted; OpenRouter :free proxy:
Cloudflare 403/1010; Apinex free: HTTP 402 allowance exhausted; Gemini
free: HTTP 429 quota; AMD TokenLab: HTTP 429), so no model verdict ranked
them — the pick was made by hand against the kit's published brief: a
single-line joke about office life, a real office detail, the laugh
landing in the last few words, clear on one reading, fresh wording.
The plant line won on the brief: the office plant, three rounds of
layoffs, HR, a performance review, and the final beat — a parking space.

Before the program prints anything it checks the joke against its pinned
SHA-256 and byte count, writes it, reads the file back, and checks the
bytes on disk against the same pinned hash and count. Any mismatch stops
the run with an error instead of writing a wrong entry.
"""

import hashlib
import os

JOKE = "Our office plant has outlasted three rounds of layoffs, so HR gave it a performance review and a parking space."

EXPECTED_SHA256 = "60ed6cdbb40106e4c764d4ec2e7d0ff8dcd0c651932468ac80f603b76f7f430f"
EXPECTED_BYTES = 111
MAX_CHARS = 199

OUTPUT_PATH = "/output/entry.txt"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify(path: str, data: bytes) -> None:
    """Check bytes just written: length, hash, and the gate's character cap."""
    if len(data) != EXPECTED_BYTES:
        raise SystemExit(
            f"entry is {len(data)} bytes, expected {EXPECTED_BYTES}"
        )
    if digest(data) != EXPECTED_SHA256:
        raise SystemExit("entry hash does not match the pinned SHA-256")
    if not 1 <= len(data.decode("utf-8")) <= MAX_CHARS:
        raise SystemExit("entry is outside the 1-199 character gate")
    with open(path, "rb") as f:
        on_disk = f.read()
    if on_disk != data:
        raise SystemExit("read-back mismatch: entry.txt is not the joke")


def main() -> None:
    joke = JOKE
    if not joke.strip():
        raise SystemExit("joke must not be blank")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("joke must be a single line")
    data = joke.encode("utf-8")
    verify_bytes_only(data)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    verify(OUTPUT_PATH, data)


def verify_bytes_only(data: bytes) -> None:
    """Check the joke bytes before anything is written to disk."""
    if len(data) != EXPECTED_BYTES:
        raise SystemExit(
            f"joke is {len(data)} bytes, expected {EXPECTED_BYTES}"
        )
    if digest(data) != EXPECTED_SHA256:
        raise SystemExit("joke hash does not match the pinned SHA-256")


if __name__ == "__main__":
    main()
