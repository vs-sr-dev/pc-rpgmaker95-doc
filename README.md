# pc-rpgmaker95-doc

**RPG Maker 95+ v1.02** — the unauthorised English translation Don Miguel made
in 1999 of ASCII Corporation's Japanese *RPG Maker 95*, as one downloaded ZIP
file. Not an installation, not a copy of a live tree: an archive, and whatever
it says about itself.

```
RPG-Maker-95_Win_EN_RPG-Maker-95-v102.zip
7,120,053 bytes    sha1 4e2831d0098c8aa11220ef746fc29955b9cbc164
12 members, 12 distinct sha1, 7,354,728 bytes uncompressed

free coverage at the start :     61,681 of 7,354,728 = 0.8387 %
after this session         :  7,354,728 of 7,354,728 accounted for
                              (0.8387 % published, 99.1613 % derived here)
```

**Ninety-four point seven per cent of it was one undocumented container.** Three
InstallShield 3 "Z" archives, an `_INST32I` bootstrap and a `.PKG` manifest —
five files, three formats, no published specification for any of them, and
nothing in a box of 514 inherited tools that could read a byte.

They are all open now, and every one of them closes at **residue 0** on a
quantity it states about itself.

| | |
|---|---|
| the object | 7,120,053 bytes, closing against PKWARE's structure at residue 0 |
| the members | 12 files, 7,354,728 bytes |
| the containers | 4, holding **272 files**, all decompressed to their declared lengths |
| the manifest | 256 names, 12 groups, agreeing with the archive's own table **256 of 256, in order** |
| the executables | **5 NE and 13 PE** — and only the 5 were visible before |
| the crossings | 0 of 1 on the object, **1 of 12** on the members |
| the personal data | 4 hits, 0 false positives, and **one deliberate redaction** |
| the calibration | inherited 23.50 of 25 against 22.92; open 27.50 of 29 against 24.08 |

**The headline is a prediction that was wrong.** This repository wrote down, in
advance, that `rpg95.exe` would be a sixteen-bit NE binary, because the
installer around it is entirely sixteen-bit. It is a **32-bit PE**, linked by
Borland, with a version resource that still declares its language as Japanese
while its strings are English. The wrapper's bitness said nothing about what it
wrapped, and the clause is left where it was written.

Along the way the reader was pointed at Microsoft FrontPage 98's installer in a
neighbouring repository, which it opened unchanged: **2,399 files, residue 0**,
in a column that repository had published as *not declared*.

---

## The chapters

| | |
|---|---|
| [00](docs/00-predictions.md) | **predictions** — 54 clauses, written before anything was opened |
| [01](docs/01-the-object.md) | **the object** — one file, six denominators, coverage at two layers |
| [02](docs/02-the-technical-sheet.md) | **the technical sheet** — every figure, with the command that makes it again |
| [03](docs/03-the-manifest.md) | **the manifest** — 4,513 bytes naming a product nobody had opened |
| [04](docs/04-the-archive.md) | **the archive** — 94.7453 %, no specification, seven closures |
| [05](docs/05-the-product.md) | **the product** — the most interesting question had the wrong answer |
| [06](docs/06-the-installer.md) | **the installer** — eighteen executables and a company that renamed itself inside one file |
| [07](docs/07-the-clocks.md) | **the clocks** — no time zone anywhere, and a readme that turns out to be right |
| [08](docs/08-the-text.md) | **the text** — 2,433 bytes of provenance, one line of CP866, and a crime |
| [09](docs/09-the-accounting.md) | **the accounting** — four totals, no shop, residue 0 in six places |
| [10](docs/10-whose-bytes.md) | **whose bytes** — a man who signed his work, and the one thing taken out |
| [11](docs/11-against-the-collection.md) | **against the collection** — one crossing, two denominators |
| [12](docs/12-the-tools.md) | **the tools** — the box had nothing, and that was the good news |
| [13](docs/13-corrections.md) | **corrections** — twelve in the brief and six of this session's own |
| [14](docs/14-leftovers.md) | **leftovers** — what was not settled, with sources named |
| [15](docs/15-prediction-scoring.md) | **prediction scoring** — and the answer to the question the brief asked |

**Sixteen documents**, for an object of twelve members. The count is not a
target: five of the sixteen exist because five containers opened and each one
needed its own arithmetic on the page, and there is no chapter here that would
survive being asked what it measures.

---

## What is in the repository and what is not

`docs/` the chapters, `notes/` the raw output of every command they cite,
`tools/` 522 Python files — 514 inherited, one of them repaired, and **eight
written here**:

| | |
|---|---|
| `isz.py` | InstallShield 3 Z archive, and a **PKWARE DCL implode decoder** |
| `ispkg.py` | the `.PKG` manifest, with three self-checking quantities |
| `is32.py` | the `_INST32I` bootstrap container |
| `cptext.py` | high-byte census and side-by-side codepage decode |
| `runexpect.py` | how many printable runs chance predicts at a file's own entropy |
| `redact.py` | removes routable contacts, counts them, fails loudly at zero |
| `zaccount.py` | the four-layer accounting |
| `coverage.py` | published / derived / neither, over a named denominator |

Sixty-seven selftest checks across the eight, forty of them asserting that
something is **rejected**.

**The object itself is not committed**, and neither is anything extracted from
it. `rpgmaker95-dist\`, `_work\` and `_pre\` are ignored. This repository
publishes measurements of a piece of unlicensed software, not the software.

---

## The question the brief asked

> *A file, twelve members, two hundred and fifty-six names and no content; at
> what point does a list of names stop being a measurement of the contents and
> start being a measurement of the wrapper?*

The answer this object gives is that **it never stops being both, and the way to
tell which you have is whether anything outside the list agrees with it.**
`SETUP.PKG` was a list of 256 names and sizes and it looked like a measurement
of the contents. It was — but nothing could show that until a second file,
written by the same packer and read by different code, produced the same 256
names in the same order with the same sizes. Before that agreement the manifest
was a measurement of the wrapper: a statement about what the installer intended
to write, which is not the same as a statement about what it holds.

The four counts that made the difference were all things the format states about
itself and the reader does not control — an archive size, two table lengths, and
a total of expanded sizes sitting 6.6 megabytes from the files it describes.
None of them is documented anywhere. **A vendor with no public specification
still has to debug its own format**, and every check it writes for itself is
available to anybody who reads the bytes.
