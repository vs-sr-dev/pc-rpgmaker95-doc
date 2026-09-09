# 12 — the tools: the box had nothing for 94.7453 % of the object, and that was the good news

*Measure: `ls -1 tools/*.py | wc -l` — **522** — and `python tools/toolscan.py
tools .py`, which scans all 522 and reports 0 forbidden control bytes with all
three positive controls firing.*

---

## The starting position, which was better than it looked

**514 Python files inherited from `pc-iamsetsuna-doc`, and not one of them could
read an InstallShield anything.** Not the Z archive, not `_INST32I.EX_`, not the
`.PKG` manifest. `unityarc.py`, `lbarc.py`, `mtarc.py`, `criutf.py` and
`jstore.py` are all a different problem.

The last two sessions each spent a chapter dismantling a tool that answered a
question it had not been asked. `unityfs.py` reported nineteen terabytes;
`kfaccount.py` reported 100 % coverage out of a catch-all bucket. **Both
happened because a reader existed for the right family and the wrong
generation.** Here nothing existed, so nothing could quietly close on the wrong
object — and that is a measurement about the box rather than about the object,
which is why it is stated first.

Two general readers did apply and needed no change at all:

* **`zipdir.py`** read the object cold: end-of-central-directory at 7,120,031,
  12 entries of 12 declared, central directory 667 bytes at 7,119,364, no
  ZIP64, comment 0 bytes;
* **`ne.py`** read all three sixteen-bit executables cold: linker 5.60, segment
  and module tables, resident and non-resident name tables, expected Windows
  3.10 and 3.0.

---

## What was written here — eight tools

| tool | what it does | selftest |
|---|---|---|
| `ispkg.py` | InstallShield `.PKG` manifest: 12 groups, 256 records, three self-checking quantities | 9 checks, 1 accepted specimen, 8 rejected |
| `isz.py` | InstallShield 3 Z archive, **and a PKWARE DCL implode decoder** | 13 checks, 3 accepted, 10 rejected |
| `is32.py` | the `_INST32I` bootstrap container; imports `blast` from `isz` rather than copying it | 7 checks, 1 accepted, 4 rejected |
| `cptext.py` | high-byte census and side-by-side codepage decode | 6 checks |
| `runexpect.py` | how many printable runs chance predicts at a file's own entropy | 7 checks |
| `redact.py` | removes routable contacts, counts them, fails loudly at zero | 13 checks |
| `zaccount.py` | the four-layer accounting and the cross-layer closures | 4 checks |
| `coverage.py` | published / derived / neither, over a named denominator | 8 checks |

**Sixty-seven checks across eight selftests, every one of them on specimens
constructed in memory**, and forty of the sixty-seven assert that something is
**rejected** or **not** touched. A reader that only ever says yes has not been
tested.

### Four defects the selftests caught

**One, in `isz.py`, and it was a wrong derivation.** The entry record was built
as 31 fixed bytes plus the name. The specimen builder's own assertion fired:

```
AssertionError: (48, 49)
```

The name length sits at `+0x1D` and the name at `+0x1E`, not `+0x1E` and
`+0x1F`. Had the reader been pointed at `_SETUP.1` with that layout it would
have walked one byte off and produced 256 records of garbage that still summed
to something.

**Two, in `isz.py`'s selftest itself.** The specimen for "a back-reference
before the start of the stream" used a distance of one into two bytes of
output, which is perfectly legal. The check reported FAIL, the specimen was
wrong rather than the reader, and it was rebuilt to emit a distance of ten into
two bytes.

**Three, in `runexpect.py`'s selftest, and this one passed for the wrong
reason.** The check "plain text gives a ratio far above 1" used a specimen of
pure ASCII, where the probability of a printable byte is 1, the whole file is a
single run, and the expectation equals the observation. It passed through an
escape clause reading `or p == 1.0`. **A check that cannot fail is not a check.**
The specimen is now thirty NUL bytes followed by ten letters, repeated: `p` is
0.25, chance predicts 7.32 runs of six and there are 1,000, and the ratio is
136.5.

**Four, and it was found by running all eight one last time with
`PYTHONIOENCODING` unset.** `cptext.py` prints Cyrillic and box drawing by
design and died with `UnicodeEncodeError` on a default Windows console — a tool
that worked only because an environment variable happened to be set for every
earlier run. It now reconfigures its own streams and falls back to replacement
characters. **The three earlier defects were caught by the specimens; this one
was caught by distrusting the environment**, which no specimen can do for you.

---

## The tool that did it again

The brief warned that `jstore.py` — which looks for a marker followed by a
count and fixed-width records — was dangerous here, and told this session to
read its output rather than its exit code. It was pointed at both files:

```
python tools/jstore.py _work/members/SETUP.PKG
index        : SETUP.PKG      bytes : 4513
lists        : 0     GUIDs : 0
arithmetic   : 5 x 0 + 16 x 0 + 4513 = 4513
residue      : 0
exit=0

python tools/jstore.py _work/members/_SETUP.1
index        : _SETUP.1       bytes : 6621095
lists        : 4     GUIDs : 288003
arithmetic   : 5 x 4 + 16 x 288003 + 2013027 = 6621095
residue      : 0
GUIDs repeated inside this index : 2865
exit=0
```

**Two hundred and eighty-eight thousand and three GUIDs, residue 0, exit 0.**
There are no GUIDs in `_SETUP.1`. There are 256 entry records of 43 bytes plus
a name, a directory table of 207 bytes and a 255-byte header, and the real
arithmetic is `255 + 6,607,311 + 207 + 13,322`.

On `SETUP.PKG` it does the other failure: zero lists, zero GUIDs, residue 0, and
a clean exit — a closure over a file it did not parse at all.

**Third consecutive object on which `jstore.py` returns residue 0 on something
it has not read.** The pattern is now well enough established to name: *a tool
whose closure is "everything I did not claim is filler" always closes.* The
residue is not evidence; the claim is, and it has to be checked against
something outside the tool.

---

## The tools that refused, and the ones that refused well

**`isaccount.py`**, written for the previous object's Unity and CRIWARE
directories, is the good failure mode:

```
python tools/isaccount.py check _work/members
files                       : 12
bytes, walked               : 7354728
bytes, summed by family     : 7354728   residue 0
unclaimed files             : 12
VERDICT                     : DOES NOT CLOSE
```

Its byte arithmetic closes and it still says no, because all twelve files fell
into `UNCLAIMED` and it counts that as a failure rather than as a bucket.
**That is the distinction `jstore.py` does not make.**

**`kfaccount.py`**, third appearance, in a new form: it now prints its usage
message and exits 0 with no arguments, with `--root`, and with a positional
path. It did nothing at all and reported success. The brief predicted it would
claim 100 % coverage from a catch-all bucket; it did not get that far.

**`verres.py`**, written for PE on the previous object, was pointed at the three
NE files as the brief asked. It refuses per file and then lies in its summary:

```
python tools/verres.py census _work/members            # exit 0
SETUP.EXE     _work/members\SETUP.EXE: no PE signature at 0xE00
_ISDEL.EXE    _work/members\_ISDEL.EXE: no PE signature at 0x80
_SETUP.DLL    _work/members\_SETUP.DLL: no PE signature at 0x80

PE files                       : 3
carrying a version resource    : 0
```

**`PE files : 3` when it has just printed three "no PE signature" lines.** The
per-file behaviour is right and the summary counts candidates as results. A
reader of the summary alone would conclude the object holds three PE binaries
with no version resources; it holds three NE binaries, two of which do have
version resources, and one of those is where the Stirling/InstallShield rename
shows up ([06](06-the-installer.md)).

Pointed at the 256 recovered files the same tool works perfectly and produces
the version-resource table in [05](05-the-product.md) — **6 of 6 PE, 6 carrying
a version resource** — which is how ASCII's 1997 copyright and
`game_engl_123.exe`'s `ver 1.23` were found. Same tool, same session, one
population it reads and one it miscounts.

**`szdd.py`** finds no candidate and is right: `_INST32I.EX_` is neither SZDD
nor KWAJ.

---

## The refusal harness, extended by ten and repaired

`refusals.py` points every reader written for the previous objects at this one
and records what it says. It was extended here by the ten written on
`pc-iamsetsuna-doc` — `sfv15.py`, `unityweb.py`, `criutf.py`, `crihca.py`,
`luac52.py`, `placement.py`, `unitytex.py`, `isaccount.py`, `verres.py`,
`sigcount.py` — and **its two-session-old defect was fixed**: the last entry
in its own table is itself, and the child inherited no guard, so every
invocation recursed until the 900-second timeout. The child is now given
`--harness-check` and prints one line.

```
python tools/refusals.py _work/members

readers pointed              : 54
refused with a non-zero exit : 36
exited 0 anyway              : 18
absent from the box          : 0
```

**Eighteen exited 0**, and an exit 0 here is not a success — it means the tool
was willing to print a table. Two of the eighteen were expected to and did:
`sigcount.py` takes its signature on the command line and `verres.py` walks any
directory. The rest divide into tools that printed a table of zeroes
(`unityfs.py`, `sfv15.py`, `criutf.py`, `crihca.py`, `luac52.py`, `unitytex.py`,
`unityweb.py`, `unityarc.py`, `unityasset.py`, `clrmeta.py`, `utf16sift.py`,
`kultaccount.py`) and the three that are dangerous rather than merely
inapplicable: `steamacf.py`, `pdbpaths.py` and `kfaccount.py`, none of which
found anything here but none of which said so with a non-zero exit either.

**`isaccount.py` is the one that refused properly**, and it is the only
accounting tool in the box that treats an all-`UNCLAIMED` result as a failure.

---

## The defects carried, with their counts

| tool | defect | appearance |
|---|---|---|
| `namecensus.py` | `ZeroDivisionError` on an empty population | **nineteenth** |
| `dircensus.py` | a complete formatted table over zero containers, exit 0 | **twentieth** |
| `protscan.py` | eleven pre-2010 optical markers, and the filtered denominator | **fifteenth** |
| `mzcensus.py` | filters on the `.EXE` extension, so 1 of 3 — `_SETUP.DLL` is the same NE format | **eighth**, and the form is new |
| `refusals.py` | recursed into itself and blocked for its 900-second timeout | third, **fixed here** |
| `kfaccount.py` | exits 0 having done nothing | third, new form |
| `verres.py` | counts non-PE candidates as PE in its summary | **first** |
| `jstore.py` | residue 0 over a file it did not parse | third |
| `sift.py` | eight-bit only — **and here that is correct** | quiet, and measured |
| `crossall.py` | sweeps the collection root including this repository | **first**, and it is a trap ([11](11-against-the-collection.md)) |
| `pdbpaths.py`, `peimpexp.py`, `authenticode.py`, `buildroot.py`, `pe.py`, `langtab.py`, `strdump.py`, `magic_sweep.py`, `cga.py`, `fsb5.py`, `unityfs.py`, `unityarc.py`, `unityasset.py`, `bundlebudget.py` | carried, quiet here | |

### `sift.py`'s defect is right on this object, and the proof is a zero

`utf16sift.py` reports **0 hits that only a sixteen-bit pass finds**, over
7,354,728 bytes. A 1996 object in CP437 and CP866 has no UTF-16 in it. On the
previous object the same defect cost an entire chapter. **A defect is a property
of a tool against a population**, and the zero is the measurement that makes
that sentence a finding rather than an excuse.

### `mzcensus.py`, eighth appearance, and a new shape

It reports **1 of 3** on the members. It filters on the `.EXE` extension, so it
finds `SETUP.EXE`, misses `_ISDEL.EXE`'s sibling `_SETUP.DLL`, which is the same
NE format, and misses `_INST32I.EX_`, which contains four more executables under
an extension designed to hide that. The new shape is the third case: **an
extension filter on an object whose whole naming convention exists to disguise
what a file is.**

---

## What a later session should take from here

`isz.py` is the one worth keeping. It reads InstallShield 3 Z archives, closes
on seven quantities the format states about itself, decompresses PKWARE DCL
implode, and has been shown to work on **two products by two companies two
years apart** — 256 files here and 2,399 in `pc-clic11-doc`. `is32.py` and
`ispkg.py` complete the set; between them they open every InstallShield 3
installer this collection is likely to meet.

`runexpect.py` is the small one that generalises furthest: **before reporting
that strings survive inside a compressed file, compute how many chance
predicts.** It is one line of arithmetic, nobody in this collection had written
it down, and here it settled a question the pre-briefing raised and could not
answer ([14](14-leftovers.md)).
