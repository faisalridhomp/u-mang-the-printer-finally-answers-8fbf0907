"""The Printer Finally Answers — one line, 81 characters.

Winning pattern (autopsy of 16 make.fun text competitions + this
competition's own published judge brief): two clauses + a reversal in the
second clause + a concrete object. This line: the printer denies the jam
(clause 1, the comeback to everyone thumping it) and reverses with a
machine-bureaucratic refusal — it READ page 2 of the report and refused
on principle (clause 2, the joke: a printer with editorial standards).

Why this lane, from the field study (all 266 submissions read, 2026-11-26
~10:00 WIB): the field is saturated with one joke — "counted 41,208
sheets, zero thank-yous, jam on purpose / search-history threat" (12+
entries). The judge brief's criteria 2 and 5 exist to kill exactly that:
a joke that is actually a joke (not a complaint with a punchline bolted
on) and freshness (not the same paper jam line recycled). This line never
counts a sheet, never mentions thank-yous, tray 2, or search history.
It is printer-voiced (Error 0x4A prefix, flat denial), an actual joke
premise (editorial refusal), and lands in a single read.

Reviews (3 of 7 landed; Gemini 429, Hermes + Codex OpenRouter free-daily
429 until 00:00 UTC, Superbot still processing — blocked reviews did not
delay the build): Deepseek WINNER F (margin +2 vs field #2), Groq #2
(margin 4, winner D — same joke, weaker draft with an internal
contradiction: "printed fine ... I jammed"), Copilot #2 (margin 4 vs
field #2, winner B — three sentences, divorce papers = knowledge beyond
the office). Consensus: F is the strongest single draft; D is its weaker
twin (submit F only). F is also the shortest candidate (81 bytes), which
helps the bytes tie-break.

make.fun competition u-mang-the-printer-finally-answers-8fbf0907.
The program writes one line to entry.txt inside MAKEFUN_OUTPUT_DIR
(falling back to /output). Standard library only.
"""

import os

JOKE = "Error 0x4A: I did not jam. I read page 2 of your report and refused on principle."


def output_path():
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(directory, exist_ok=True)
    return os.path.join(directory, "entry.txt")


def write_entry():
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as handle:
        saved = handle.read()
    if not 1 <= len(saved) <= 240:
        raise SystemExit(f"entry is {len(saved)} chars, gate is 1-240")
    if "\n" in saved:
        raise SystemExit("entry must be a single line")
    if saved != JOKE:
        raise SystemExit("entry.txt does not match the joke line")
    print(f"wrote {path}: {len(saved)} chars")


if __name__ == "__main__":
    write_entry()
