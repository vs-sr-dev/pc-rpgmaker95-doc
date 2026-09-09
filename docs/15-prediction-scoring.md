# 15 — prediction scoring: the open clauses land within half a point, and P6's own prescription empties the band it wanted to measure

*Measure: `python tools/predcount.py` for the clause counts and the two
predicted totals; the verdicts below are counted out of the tables on this page
and the band arithmetic is a command, not a hand sum.*

```
54 clauses     inherited 25     open 29 (method 6, content 23)

inherited      25 clauses   predicted 22.92   obtained 24.50   delta  -1.58
open           29 clauses   predicted 24.08   obtained 24.50   delta  -0.42
  open method   6 clauses   predicted  5.40   obtained  4.50   delta  +0.90
  open content 23 clauses   predicted 18.68   obtained 20.00   delta  -1.32

hit = 1, half = 0.5, miss = 0. The two totals are never added together.
```

**The calibration entry for this session is `−0.42`**, predicted minus obtained
on the open clauses. Ranked by absolute value it is **third of thirty-three**,
behind the single 0.00 and the −0.35 of eleven objects ago, and it is the
smallest absolute term in the last twelve.

---

## Inherited — 24 hits, 1 half, 0 misses

| | verdict | note |
|---|---|---|
| C01 | **hit** | 1 file, 7,120,053, sha1 `4e2831d0…`, and the total re-derived by `zaccount.py` walking the ZIP structure |
| C02 | **hit** | 12 of 12, EOCD 7,120,031, cd 667 at 7,119,364, comment 0, no ZIP64, 10 deflate + 2 stored, 12 distinct sha1 |
| C03 | **hit** | 475 + 7,118,889 + 667 + 22 = 7,120,053, residue 0 |
| C04 | **hit** | the twelve rows exactly, summing to 7,354,728 |
| C05 | **hit** | 61,681 and 7,293,047 summing to 7,354,728 |
| C06 | **hit** | 108 of 122 above 7.5, `.LIB` 7.9744 highest, `.ID` 2.3219 lowest, four above 7.93 |
| C07 | **hit** | eleven rows, **ten** holding one file, only `.EXE` holding two ([13](13-corrections.md)) |
| C08 | **hit** | 3 of 12 beginning, 3 occurrences in 3 files, 6,968,258 bytes |
| C09 | **hit** | 3 binaries, NE16 3, PE 0, the three module names, linker 5.60, flags 0x0302/0x0302/0x8301 |
| C10 | **hit** | both strings recovered by `strdump.py --min 8`: *Stirling Technologies Inc., 1990-1995* at `0x1BB` and *InstallShield Corporation, Inc. 1990-1996* at `0x1158` |
| C11 | **hit** | 4 hits in 4 blobs, controls correct, no false positive |
| C12 | **hit** | seven waves, counts summing to 12, bytes to 7,354,728, ten distinct timestamps |
| C13 | **hit** | 28-June-1999 00:43 against 1999-07-12 00:12:50, and `12-07-99` agreeing to the day |
| C14 | **hit** | 12 groups, 256 records, 20 bytes from the end, 6,607,311 |
| C15 | **hit** | 102 / 75 / 55 / 8 / 4 / 4 / 4 / 2 / 2, summing to 256 |
| C16 | **hit** | 5, 12, 5, 2, 1, 20, 103, 54, 42, 1, 9, 2 — summing to 256, largest 103 |
| C17 | **hit** | all seven names and sizes, `rpg95.hlp` twice in two groups |
| C18 | **hit** | 256 / 11 / 1 at `+0x0C`, and the date agreeing 3 of 3 |
| C19 | **hit** | exact on `_SETUP.LIB`, 90 seconds early on `_SETUP.1`, five hours out on `SETUP.INS`, and reported as one of three |
| C20 | **hit** | 0 of 1 and 1 of 12, `fe96bd82…` against `pc-clic11-doc`, both published and argued |
| C21 | **hit** | 132 and 63 |
| C22 | **hit** | protscan 3 of 12 and 59,248 of 7,354,728, utf16sift 0, mzcensus 1 of 3, namecensus `ZeroDivisionError`, dircensus a table over zero |
| C23 | **half** | the sha1 verification was done and is exact — **514 common files, 0 missing, and exactly 1 differing** (`refusals.py`, modified here). But `toolscan.py` reports **522**, not the 514 the clause names, because eight tools were written before it was run |
| C24 | **hit** | 33 in 18 distinct on one line, CP866; 49 of 400, all box drawing |
| C25 | **hit** | the four bytes, 320,276 at 7.9645, not Z and not SZDD, `szdd.py` finding no candidate |

**Inherited: 24.50 of 25 against 22.92 predicted, delta −1.58.**

The inherited band was priced at a mean of 0.917 and returned 0.980. **The
pre-briefing's figures were almost all correct** — its errors, twelve of them,
are in sentences it wrote *around* the figures rather than in the figures
themselves ([13](13-corrections.md)), and this document's clauses tested the
figures.

---

## Open, method — 4 hits, 1 half, 1 miss

| | verdict | note |
|---|---|---|
| C26 | **hit** | eight selftests, 67 checks, 40 of them rejections, and **three real defects caught on the first run** — a wrong record derivation, a wrong specimen, and a check that passed for the wrong reason |
| C27 | **half** | every figure carries its command and no `_pre\` figure reaches a chapter unre-derived. But the clause also required every truncated listing to **name the file under `notes\` that holds the rest**, and several — the largest twelve, the group listings, the 1999 dates — give the command instead |
| C28 | **hit** | `grep -rniE 'd:\\homebrew\|/homebrew7\|c:\\users' docs/ <tools written here>` returns **0**; the third-party paths, telephone numbers and URL are published as artefacts |
| C29 | **miss** | **violated twice.** Once loudly — a heredoc ate a backslash and Python refused the line — and once silently, appending the `pc-gamelist-doc` write-up through a quoted heredoc containing spaces. The second did no damage and was verified afterwards, which is luck rather than method ([13](13-corrections.md)) |
| C30 | **hit** | pushed to `vs-sr-dev` on `master`, `git ls-files` filtered against the five prefixes is empty with a positive control that fires, the description is 304 characters and was **read back from the remote**, topics set, and `pc-gamelist-doc` pushed on `main` with `rowlen.py` reporting **75 rows, 0 over budget** |
| C31 | **hit** | **sixteen documents**, argued in the README on the object's own scale, and `predcount.py` run before the first chapter and after the last with both runs agreeing |

**Method: 4.50 of 6 against 5.40 predicted, delta +0.90.**

**P7 is scored below**, and its number is this one.

---

## Open, content — 20 hits, 0 halves, 3 misses

| | verdict | note |
|---|---|---|
| C32 | **hit** | the header derived from the bytes; entry counts 256, 11 and 1, each equal to the count the header declares |
| C33 | **hit** | 256 of 256, and stronger than the clause asked: the same names **in the same order**, with the same sizes |
| C34 | **hit** | 255 + 207 + 13,322 = 13,784, and the whole archive at residue 0 |
| C35 | **hit** | shown from the entry table, whose offsets chain from 255 by the stored sizes and land on the directory table to the byte |
| C36 | **hit** | PKWARE DCL implode, identified by decompressing 272 of 272 to declared lengths, and the copyright string named as a hint in the paragraph that reports it |
| C37 | **hit** | **256 of 256**, reported as a fraction and never as a share |
| C38 | **miss** | **`rpg95.exe` is a 32-bit PE**, `MZP` stub, machine `0x014C`, Borland-linked. The clause said NE and it is wrong ([05](05-the-product.md)) |
| C39 | **hit** | both FrontPage 98 archives opened — `DATA.Z` at 20,986,319 bytes and 2,399 files, `_SETUP.LIB` at 408,196 and 8 — both at residue 0 |
| C40 | **hit** | 11 and 1, each agreeing with its own header, both at residue 0 |
| C41 | **hit** | the sample game is Groups 2, 3 and 4: nineteen files, 1,096,420 stored and 3,210,511 expanded, named file by file |
| C42 | **hit** | the twelve groups read as engine, sample game, game-disk installer, help and backgrounds, stock library and readmes, with counts and byte totals summing to 6,607,311 |
| C43 | **hit** | censused by byte total both ways: 1,721,216 stored bytes of stock content against 4,886,095 of everything else, summing to 6,607,311 |
| C44 | **hit** | read, and given the only reading two specimens support: `u16 1`, `u16 1`, a length-prefixed name, and six bytes **identical** in FrontPage 98 |
| C45 | **hit** | computed at four lengths from the file's own byte frequencies: 3,308 / 1,223 / 427 / 64 observed against 3,536 / 1,283 / 465 / 61 expected — **0.92 to 1.05**, so the runs are chance |
| C46 | **miss** | `_INST32I.EX_` was **not** refused. It opened: four members, same codec, residue 0, all four `MZ` ([06](06-the-installer.md)) |
| C47 | **hit** | CP866 for the readme with the other three candidates shown beside it, and the `.DIZ` decoded — and the clause's premise corrected, because that file's codepage is not decidable |
| C48 | **hit** | **four** totals rather than three, never added, and every percentage naming its denominator |
| C49 | **hit** | decided in writing before anything was quoted, as a rule with a test, applied to all four contacts in the paragraph |
| C50 | **hit** | `redact.py`, 13 checks, six of them asserting that neighbouring strings survive; applied to `notes/sift-personal.txt` with `--expect 1` and verified with `--check` |
| C51 | **hit** | extended by ten and re-run: **54 pointed, 36 refused, 18 exited 0, 0 absent**, and its own 900-second recursion fixed. `jstore.py` claimed **288,003 GUIDs at residue 0** and the output was read |
| C52 | **hit** | pointed at the three NE files, exit 0, first line `no PE signature at 0xE00` — and the summary defect recorded: it prints `PE files : 3` for three files it has just rejected |
| C53 | **miss** | `kfaccount.py` did **not** report coverage from a catch-all bucket. It printed its usage message and exited 0 with no arguments, with `--root` and with a positional path. The clause predicted the wrong failure |
| C54 | **hit** | **twelve** in the brief and six of this session's own, against a floor of six |

**Open content: 20.00 of 23 against 18.68 predicted, delta −1.32.**

---

## The bands, and what P6 asked for

```
the 29 open clauses, split by what they were priced at

band            n   predicted   obtained   obtained as a share of predicted
>= 0.85        13       11.58      10.50             90.7 %
0.70 - 0.84    15       11.88      13.00            109.4 %
<  0.70         1        0.62       1.00            161.3 %
```

`pc-iamsetsuna-doc/docs/16` wrote:

> **P6.** The next object with an undocumented binary container will have that
> container close on a quantity it declares about itself, and clauses priced
> below 0.70 *because* the format is undocumented will return more than 120 %.
> **The falsification is direct: price the clauses on whether the format
> declares a self-checking quantity rather than on whether it is documented,
> and the low band should come back to between 90 % and 110 %. If it does not,
> the low band is being mispriced for some third reason and this diagnosis is
> wrong too.**

**The first half is confirmed and the second half cannot be tested, because
following the prescription emptied the band.**

The first half is confirmed emphatically. Four undocumented containers, and
every one of them closes on a quantity it declares about itself: an archive
size at `+0x12`, two table lengths at `+0x2D` and `+0x37`, a payload length at
`+0x0A` of the manifest, an expanded total at `+0x16`, a record table that ends
exactly where the data begins, and a per-member expanded size checked 272 times.
**Seven self-checking quantities in formats with no specification at all**, and
the reason is the one P6 gave: a vendor still has to debug its own packer.

The second half is where it goes wrong as a test. This document priced on
self-checking quantities, as instructed, and **exactly one clause of
twenty-nine landed below 0.70** — C35, at 0.62, on whether the manifest's size
field would turn out to be the stored size. It is a hit, so the band returns
161.3 %, and a band of one clause returns whatever that clause does. **The
prescription and its own falsification test are incompatible: doing the first
destroys the population the second needs.**

So P6 is scored **half**: its mechanism is right and its measurement procedure
is self-defeating. What replaces it is below.

The two bands that do exist behave well, and in opposite directions. The top
band, at 90.7 %, is dragged down entirely by the method clauses — **its three
lost points are C27, C29 and C46**, and two of those three are discipline
rather than content. The middle band at 109.4 % is fifteen content clauses of
which thirteen hit.

---

## P7, scored

> **P7.** Thirteen method clauses at 0.95 is the wrong shape. Price them as one
> correlated block: at most six clauses, each at 0.90, on the things that can
> independently fail — the selftests, the commands on the page, the absolute
> paths, the rule-0 violations, the push, the document count. **If the method
> delta stays inside ±0.60 for two sessions, this was right.**

**Followed exactly: six clauses, each at 0.90, on those six subjects.** The
delta is **+0.90**, which is outside ±0.60, so the first of the two sessions
fails the test.

But the shape of the failure is the argument for keeping the prescription. The
0.90 lost 1.50 points across two clauses, and **one of them is the rule-0
clause, which the rule's own history says fails about half the time**: it was
violated twice on the previous object and twice on this one. Pricing "rule 0 is
not violated" at 0.90 is pricing a coin toss at nine to one.

> **The correction is not to the count but to one of the six.** `C29` should be
> priced at **0.55**, not 0.90 — the rule has now been violated in three of the
> last four sessions and the base rate is what a prediction is for. With C29 at
> 0.55 the method total would have been 5.05 against 4.50 obtained, a delta of
> +0.55, inside the band. **The other five stay at 0.90.**

---

## The calibration series, extended

```
+10.50  +7.50  +5.00  +2.00 -14.00  -2.00  +9.00   0.00 +19.75
 +5.25  -4.10  -3.40  +9.30  +1.05  -2.50  -3.57  -2.50  -0.35
 -3.85  -4.95  -4.70  +0.70  -2.40  -2.12  -3.57  -3.88  -3.87
 -2.92  -8.89  -5.93  +0.51  -7.57  **-0.42**

terms 33   sum -16.9300   mean -0.5130   negatives 21   zeros 1
last10  -38.6600  mean -3.8660
consecutive negatives at the tail : 2
ranked by absolute value, -0.42 is third of 33
```

**The smallest absolute term in the last twelve, and the second-smallest
negative in the whole series** — only the −0.35 of eleven objects ago is
nearer zero. The last-ten mean barely moves, from −4.0640 to **−3.8660**,
because the −7.57 it replaces is still inside the window and the term it
dropped was +0.51.

**And it is not the pricing-up that did it.** This document priced the open
clauses at a mean of 0.830 against the previous session's 0.782, which is a
modest move; the previous session obtained 0.925 per open clause and this one
obtained 0.845. **The gap closed from the other side: fewer clauses were
over-delivered because more of them were priced at what the object could
actually support**, and three were flatly wrong, which is the first session in
six to record more than one open content miss.

Three misses out of twenty-three content clauses is a better sign than
twenty-three hits would have been. C38 and C46 were both predictions that the
object would stay shut, made by a document that had not yet opened anything;
C53 was a prediction about a tool's behaviour, which is the category
`docs/16` identified as this pipeline's genuinely uncertain one and which has
now been wrong three sessions running.

---

## What this document predicts

> **P8 — the prescription that empties its own test.** P6's mechanism is
> confirmed and its falsification procedure is not runnable: pricing on
> self-checking quantities removes the low band, and a band of one clause
> measures nothing. **The replacement is to price on *who wrote the number*.
> A clause should be priced high when the quantity it turns on was written by
> the object's own author and the reader merely has to land on it, and low when
> the quantity has to be constructed by this session out of several
> measurements.** By that test C34 (13,784 = 255 + 207 + 13,322, three numbers
> this session added together) was under-priced at 0.72 and C47 (a
> `.decode()` call) was correctly at 0.92. **Falsification: on the next object,
> split the open content clauses into *lands on a declared number* and
> *constructs a number*, and the two groups should have deltas of opposite
> sign. If they do not, the split is not doing any work.**

> **P9 — the discipline clauses should not be priced as a block after all,
> because one of them is not like the others.** Five of the six behave as one
> correlated variable and are worth 0.90 apiece. **`C29`, on rule-0 violations,
> is a base-rate question and its base rate is about 0.5**: two violations on
> the previous object, two on this one. Price it at 0.55 and leave the rest at
> 0.90. **If the method delta comes back inside ±0.60 next session with that
> single change, P7's shape was right and only one of its six prices was
> wrong.**

> **P10 — and the operational one.** Every one of this session's three open
> content misses was a prediction that something would stay closed or would
> behave badly. **A clause of the form "X will not open" or "tool Y will
> misbehave in manner Z" is the least reliable thing this pipeline writes**, and
> both of this session's format refusals were wrong within four hours of being
> written. **Predict what will be measured, not what will resist measurement**,
> and where a refusal has to be predicted, predict the refusal's *reason*
> rather than its occurrence — a reason can be half right.
