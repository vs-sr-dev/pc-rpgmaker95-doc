# 01 — the object: one file, six denominators, and a coverage figure that has to say which layer it is over

*Measure: `python tools/hashall.py rpgmaker95-dist` for the object,
`python tools/hashall.py _work/members` for the members, and
`python tools/coverage.py members` and `python tools/coverage.py product` for
the two coverage tables. The lists behind them are `notes/sha1-all.txt` and
`notes/sha1-members.txt`.*

---

## What it is

```
python tools/hashall.py rpgmaker95-dist
4e2831d0098c8aa11220ef746fc29955b9cbc164       7120053  RPG-Maker-95_Win_EN_RPG-Maker-95-v102.zip
files 1  bytes 7120053  distinct sha1 1  unreadable 0  excluded 0
```

**RPG Maker 95+ v1.02**, the English translation Don Miguel made without
permission in 1999 of ASCII Corporation's Japanese *RPG Maker 95*. One
downloaded ZIP file, 7,120,053 bytes, and nothing else.

Eleven of the previous twelve objects in this collection were copies of a live
installation on the owner's machine, verified against the original on size,
mtime to the 100-nanosecond tick, sha1 and the directory tree. **This one has
no original.** The download *is* the object. `_work/copyverify.py` was carried
over with the tools and has nothing to check; running it and reporting "1 of 1"
would be a number with no content, and this chapter says so instead of
producing one.

That makes the placement claim the weakest this repository has made: the file
is where it says it is and hashes to what it says it hashes to, and there is no
second witness for where it came from beyond what the bytes themselves say —
which, as it turns out, is a great deal ([08](08-the-text.md)).

---

## Six denominators, and the fifth stopped biting

The pre-briefing counted six populations and warned that the fifth would be the
problem: *256 files the manifest names, and none of them opened.* By the end of
this session every one of them is open, so the six have become seven and the
awkward one is now the last:

| | population | what it is |
|---:|---|---|
| 1 | **1 file** | the object as downloaded |
| 2 | **12 members** | what the ZIP holds |
| 3 | **4 containers** | the InstallShield files among those twelve |
| 4 | **272 files** | what those four containers hold, recovered here |
| 5 | **256 names** | what `SETUP.PKG` declares — the same set as the 256 in `_SETUP.1` |
| 6 | **12 groups** | the manifest's own partition of those 256 |
| 7 | **18 executables** | 5 NE and 13 PE, across all layers ([06](06-the-installer.md)) |

Every percentage in this repository names which of these it is over. The
temptation this object creates is to quote a share of "the object" when the
figure is a share of the members, and they differ by 234,675 bytes.

---

## The coverage, before and after

The pre-briefing measured the free coverage at **61,681 bytes of 7,354,728**,
the lowest this collection has ever started from — three NE executables and
four text files, and nothing else. That figure is re-derived here and it holds
exactly:

```
python tools/coverage.py members

denominator : 12 files, 7354728 bytes -- the twelve files the ZIP holds
  published     7 files        61681 bytes     0.8387 % of 7354728
  derived       5 files      7293047 bytes    99.1613 % of 7354728
  neither       0 files            0 bytes     0.0000 % of 7354728
  SUM          12 files      7354728 bytes
```

**The 0.8387 % is unchanged and the rest of the row is the session.** Five files
— three Z archives, one `_INST32I` container and one `.PKG` manifest — hold
99.1613 % of the members' bytes in three formats nobody has published, and all
three were worked out of the bytes here and all five files close at residue 0
([04](04-the-archive.md), [09](09-the-accounting.md)).

**`derived` is kept in its own column and is never added to `published`.** A
format this session reverse-engineered from four specimens is a weaker claim
than a format PKWARE or Microsoft wrote down, and merging the two would hide
that. What the two columns together support is a different sentence: *no byte of
the twelve members is unaccounted for.*

Underneath, the picture inverts:

```
python tools/coverage.py product

denominator : 272 files, 20442049 bytes
  published   257 files     17050056 bytes    83.4068 % of 20442049
  derived       0 files            0 bytes     0.0000 % of 20442049
  neither      15 files      3391993 bytes    16.5932 % of 20442049
```

**Inside the undocumented containers is almost nothing undocumented.** 102
Standard MIDI files, 78 Windows bitmaps, 55 RIFF WAVEs, fifteen PE and NE
binaries and five text files — 83.4068 % of the recovered bytes are in formats
with published specifications. What is left is WinHelp 3.x (2 files,
1,700,484 bytes), RPG Maker's own `.DAT` and `.ATR` (12 files, 1,485,240) and
one compiled InstallShield script (206,269).

The object is a locked box holding ordinary things.

---

## The redundancy, which is a formality twice over

```
python tools/hashall.py _work/members
files 12  bytes 7354728  distinct sha1 12  unreadable 0
```

**Twelve distinct hashes over twelve members**, which on a population of twelve
is not evidence of anything. But one layer down the redundancy is real and it
is a control rather than waste:

**`readme.txt` exists three times in this object, byte for byte.** Once as a ZIP
member, once inside `_SETUP.1` and once inside `_SETUP.LIB` — sha1
`260e355d3d8dec82a3bee081002f748c5352096c`, 1,967 bytes, all three. The two
inside were recovered by decompressing a format with no specification, and they
reproduce exactly the file `deflate` produced from a different compressed
stream. **That is the strongest check this session performed and it was free**
([04](04-the-archive.md)).

`rpg95.hlp` is likewise stored twice inside `_SETUP.1`, at 890,048 stored bytes
each, in two different groups; `NOSOUND.WAV` twice; `README.TXT` four times at
four different sizes. 256 records, **251 distinct names**.

---

## Entropy, and the row that is not a mean

```
python tools/entropy.py _work/members --tree --by-ext
files 12   bytes 7354728   blocks above 7.5 : 108 of 122

.1   7.9384    .EX_ 7.9645   .LIB 7.9744   .INS 7.9424
.EXE 6.2578    .DLL 5.7149   .PKG 5.2521   .TXT 5.2969
.DIZ 3.4963    .INI 4.9244   .ID  2.3219
```

Four files above 7.93 and all four are the InstallShield containers; the
`.PKG` at 5.2521 is the manifest, and its entropy is the reason anybody looked
at it.

**The table has eleven rows over twelve files, so ten of the eleven rows
contain exactly one file.** The only row with two is `.EXE`. A "mean entropy"
over one file is that file's entropy, and nine of these numbers are not means
at all. The briefing for this session said nine rows held one file; it is ten
([13](13-corrections.md)).

---

## What this object is, in one sentence

**A 1999 ZIP holding a 1996 InstallShield installer holding a 1997 Japanese
program that a Russian translated into English, downloaded in 2026 by somebody
who has never run it.** Every clause of that is in the bytes except the last,
which is the file system's — and the pre-briefing's version of the same
sentence said *1995* for the program, because the only place the program's real
year appears is in a version resource inside a container nobody had opened
([07](07-the-clocks.md)).
