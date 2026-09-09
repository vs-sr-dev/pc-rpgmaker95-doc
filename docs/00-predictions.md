# 00 — predictions: what you measure when the object is the wrapper and the contents are only a list of names

*Measure: `python tools/predcount.py` — the clause count and the two totals
below are that command's output and not a hand sum. This header was written
from the first run, before the first chapter, and regenerated from a second run
after the last chapter; both runs agree. The verdicts are in the last chapter of
this repository.*

```
document      : docs/00-predictions.md
clauses        : 54
  inherited    : 25
  open         : 29
  method       : 6
  content      : 48

the cross-tabulation, which is the one that matters:
  inherited method  : 0
  inherited content : 25
  open      method  : 6
  open      content : 23

TWO TOTALS, NEVER SUMMED TOGETHER:
  inherited predicted : 22.92 of 25
  open      predicted : 24.08 of 29

content share of the open clauses : 23 of 29 = 79.3 %
```

This document was written after `prompt.txt` and the eight files of `_pre\`
were read; after `pc-iamsetsuna-doc/docs/16` and its **P6** and **P7** were read
in the original; after `pc-clic11-doc/docs/13` was read for what its
InstallShield objects turned out to be; after the collection's two directory
counts were re-derived with `ls`; and **before** one byte of any of the three Z
archives past the sixteen the pre-briefing published, before `SETUP.PKG` was
walked by this session's own code, before `_INST32I.EX_` was looked at past its
first eight bytes, and before any of the 256 names in the manifest was resolved
to a single byte of content.

Everything in §A is the pre-briefing's work and scores nothing. §B is the
calibration series, re-derived here by command. Everything from C01 on is priced
from the brief and is scored in the last chapter whether it was right or not.

**The prescription that governs the pricing of every clause below** has two
halves, and they come from different places.

From `pc-academagia-doc/docs/18`, still in force and followed literally:

> Never quote a percentage inside a clause. State the byte count and the
> denominator, and let the share be computed.

From `pc-iamsetsuna-doc/docs/16`, replacing the one that broke there:

> The correct predictor is not *is there a specification* but *does the format
> state a quantity the reader does not control*.

**This object was chosen to test the second one and the test is fair.** There
are three undocumented containers here and two of them display a self-checking
quantity before anything is opened: the Z archive's DOS date agrees with the
ZIP's on 3 of 3, and a count of 256 is declared by two files that do not know
about each other. The clauses about those containers are therefore priced in the
same band as the clauses about ZIP and NE, and if that is wrong the series will
say so.

**And P7 is followed.** The previous three sessions wrote thirteen discipline
clauses at 0.95 each and the delta went −0.65, −0.65, +1.35. This document
writes **six**, each at **0.90**, on the six things that can fail
independently: the selftests, the commands on the page, the absolute paths, the
rule-0 violations, the push, and the document count. Nothing else is priced as
discipline.

---

## §A — the pre-briefing, which is worth zero points

**The object is one file.** `rpgmaker95-dist\RPG-Maker-95_Win_EN_RPG-Maker-95-v102.zip`,
**7,120,053 bytes**, sha1 `4e2831d0098c8aa11220ef746fc29955b9cbc164`. It is
**RPG Maker 95+ v1.02**, the unauthorised English translation Don Miguel made in
1999 of ASCII Corporation's Japanese *RPG Maker 95*. It is a downloaded
distribution archive, not a copy of a live installation, and there is no
original on this machine to verify it against. `_work/copyverify.py` has nothing
to do and reporting "1 of 1" would be a vacuous number.

**Six denominators, not four:** 1 file on disk; 12 ZIP members; 3 executables,
all NE and zero PE; 7 mtime waves; **256 files the manifest names and none of
them opened**; 12 groups the manifest declares.

**The members.** 12 of 12 parsed, 12 distinct sha1, 7,354,728 bytes
uncompressed against 7,118,889 stored: `_SETUP.1` 6,621,095; `_INST32I.EX_`
320,276; `_SETUP.LIB` 280,502; `SETUP.INS` 66,661; `SETUP.EXE` 44,928;
`_ISDEL.EXE` 8,192; `_SETUP.DLL` 6,128; `SETUP.PKG` 4,513; `readme.txt` 1,967;
`FILE_ID.DIZ` 400; `SETUP.INI` 61; `DISK1.ID` 5. Ten deflated, **two stored**,
and the two stored are the 61-byte and the 5-byte members.

**The free coverage is 61,681 bytes of 7,354,728** — three NE executables at
59,248 and four text files at 2,433 — and that is the lowest this collection has
started from, after 2.1516 % and 15.5825 %.

**The ZIP closes on itself at residue 0:** 475 bytes of local headers plus
7,118,889 of member data plus 667 of central directory plus 22 of
end-of-central-directory is 7,120,053, and the file on disk is 7,120,053. No
external witness of any kind — no shop, no depot, no `SizeOnDisk`.

**One magic opens 94.7453 % and has no specification.** `0x8C655D13`, the
InstallShield 3 Z archive, begins `_SETUP.1`, `_SETUP.LIB` and `SETUP.INS` —
6,968,258 bytes — and occurs nowhere else. Its sixteen-byte header shows a count
at `+0x0C` reading 256 / 11 / 1 and a DOS date at `+0x0E` that **agrees with the
ZIP's own stored date on 3 of 3**. The time-shaped field at `+0x10` agrees on
one of three.

**The manifest is in the clear.** `SETUP.PKG`, 4,513 bytes, entropy 5.2521,
declares 12 groups named `Group1`..`Group12` and 256 files as `(u32 size, u8
name length, name, NUL, u16 group)`; 256 of 256 records parse, the walk ends 20
bytes from the end on a trailer reading `01 00 01 00 08 00 "_SETUP.Z" 01 01 0a
00 00 00`, and the declared sizes sum to **6,607,311**. By extension: MID 102,
BMP 75, WAV 55, DAT 8, EXE 4, TXT 4, ATR 4, DLL 2, HLP 2. By group: 5, 12, 5, 2,
1, 20, 103, 54, 42, 1, 9, 2. It names `rpg95.exe` (493,551), `rpg95.hlp`
(890,048, twice), `game.exe` (241,493), `game_engl_123.exe` (182,094),
`unlha32.dll` (98,281), `MONSTPIC.DAT` (358,271) and `USER32.DLL` (21,223).
**6,607,311 against `_SETUP.1`'s 6,621,095 is a difference of 13,784.**

**Three executables, all sixteen-bit, none of them the product.** `SETUP.EXE`
(module `ISSET_SE`), `_ISDEL.EXE` (`_DELIS`) and `_SETUP.DLL` (`_SETUP`), all
linker 5.60, two segments each, **zero PE files in the object**. `_SETUP.DLL`
carries *Stirling Technologies* in its NE description and *InstallShield
Corporation* in its version resource, and the company renamed itself in 1996.
`_ISDEL.EXE` (1995-09-07) prints **(708) 240-9111**; `SETUP.EXE` (1996-11-04)
and `_SETUP.DLL` (1996-09-30) print **(847) 240-9111**, and Illinois assigned
847 in January 1996.

**Seven waves, all from DOS timestamps restored out of the ZIP central
directory** — two-second granularity, local time, **no time zone anywhere**:
1995-09-07 19:22:40 (1 file, 8,192); 1996-09-30 08:06:54 (1, 6,128); 1996-11-04
13:04:12 (1, 44,928); 1996-11-05 16:17:32 (1, 320,276); 1996-12-19 17:19:56 (1,
66,661); 1999-07-12 00:12:50..00:24:28 (2, 2,367); 1999-07-12
01:27:34..01:29:08 (5, 6,906,176). `readme.txt` dates itself **28-June-1999**
and is stamped 12 July; `FILE_ID.DIZ` dates itself `12-07-99` and agrees with
its own stamp.

**Four text files, 2,433 bytes, carry the whole provenance.** `SETUP.INI` names
the product and the translator; `DISK1.ID` is five bytes reading `DML`;
`FILE_ID.DIZ` is a CP437 box-drawing BBS descriptor of which 49 of 400 bytes are
`>= 0x80`; `readme.txt` names the chain of custody — ASCII made it, KanjiHack
ripped it from CD and translated it roughly, Don Miguel finished it — and 33 of
its 1,967 bytes are `>= 0x80` in 18 distinct values and are one line of CP866
Cyrillic. The readme says "CD-RIP", "I almost cracked it now" and "I'm working
hard for UnlimitedTilesets crack!".

**One crossing.** `crossall.py` reports **0 of 1** on the object's own sha1 and
**1 of 12** on the members', over 102 repositories, 448 list files and 155,217
hash tokens; the crossing is `_ISDEL.EXE`, sha1 `fe96bd82…`, 8,192 bytes, also
in `pc-clic11-doc`. The collection holds **132** `-doc` directories and **63**
`pc-*-doc`, both including this one.

**Fifteen tools of 514 were run.** `zipdir.py` and `ne.py` read this object with
no change at all; `sigcount.py` finds the Z magic on 3 of 12; `sift.py --group
personal` fires 4 times with no false positives; `utf16sift.py` finds **0**;
`protscan.py` searches 3 files of 12 and 59,248 bytes of 7,354,728;
`mzcensus.py` finds 1 of 3; `namecensus.py` raises `ZeroDivisionError`;
`dircensus.py` prints a full table over zero and exits 0; `toolscan.py` reports
514 files and 0 forbidden bytes. **There is no reader in the box for
InstallShield of any kind**, and the pre-briefing says that is a better position
than the last two sessions had.

**The personal data is a man who signed his own work.** One e-mail address in
`readme.txt`, three telephone numbers that are a vendor's support line, and
nothing else. The e-mail sits beside an ICQ number, a URL and six aliases, in a
paragraph asking to be written to.

---

## §B — the calibration series, re-derived

```
python - <<the thirty-two terms, in order>>
+10.50  +7.50  +5.00  +2.00 -14.00  -2.00  +9.00   0.00 +19.75
 +5.25  -4.10  -3.40  +9.30  +1.05  -2.50  -3.57  -2.50  -0.35
 -3.85  -4.95  -4.70  +0.70  -2.40  -2.12  -3.57  -3.88  -3.87
 -2.92  -8.89  -5.93  +0.51  -7.57

terms    : 32
sum      : -16.5100
mean     : -0.5159
negative : 20   positive : 11   zero : 1
last8    : -36.1200  mean -4.5150
last10   : -40.6400  mean -4.0640
consecutive negatives at the tail : 1
```

The brief's summary of the series is correct in every figure and the tail count
is **one**, not a run — `+0.51` sits two terms back. **The operative fact for
this document is the last ten: −4.0640 per session, and the sign says these
documents predict less than they obtain.** Eight of the last ten terms are
negative and the mechanism named in `docs/16` is caution about formats rather
than caution about tools.

**So this document prices upward, deliberately, and names the two places it
does it**: the Z archive clauses, which P6 says to price on the self-checking
quantity, and the manifest clauses, where a second file already agrees on a
count. If the term comes back deeply negative again after pricing up, the
correction is not "be braver" and this repository will have to look elsewhere.

---

## §C — the clauses

### Inherited — re-testing the pre-briefing's own figures

**C01** `content` `inherited` — `hashall.py` re-run on `rpgmaker95-dist\`
returns **1 file, 7,120,053 bytes, 1 distinct sha1, 0 unreadable**, the sha1 is
`4e2831d0098c8aa11220ef746fc29955b9cbc164`, and the byte total is re-derived by
a command that is not `hashall.py`. *Predicted: 0.97*

**C02** `content` `inherited` — `zipdir.py` re-run reports **12 entries declared
and 12 parsed**, end-of-central-directory at offset 7,120,031, a central
directory of 667 bytes at offset 7,119,364, an archive comment of 0 bytes, no
ZIP64 locator, **10 deflated and 2 stored**, 7,354,728 bytes uncompressed
against 7,118,889 stored, and **12 distinct sha1 over 12 members**.
*Predicted: 0.95*

**C03** `content` `inherited` — the object's structural closure re-derives to
**residue 0** from the ZIP specification alone: 12 local headers of 30 bytes
plus their names is 475, member data 7,118,889, 12 central directory records of
46 bytes plus their names is 667, the end record 22, total 7,120,053, and the
file on disk is 7,120,053. *Predicted: 0.95*

**C04** `content` `inherited` — the twelve-row member table holds exactly as
published — `_SETUP.1` 6,621,095, `_INST32I.EX_` 320,276, `_SETUP.LIB` 280,502,
`SETUP.INS` 66,661, `SETUP.EXE` 44,928, `_ISDEL.EXE` 8,192, `_SETUP.DLL` 6,128,
`SETUP.PKG` 4,513, `readme.txt` 1,967, `FILE_ID.DIZ` 400, `SETUP.INI` 61,
`DISK1.ID` 5 — and the twelve sum to 7,354,728. *Predicted: 0.96*

**C05** `content` `inherited` — the free coverage is **7 files and 61,681 bytes
of 7,354,728**, made of three NE executables at 59,248 and four text files at
2,433, and the not-derived side is 5 files and 7,293,047 bytes, and the two
sides sum to 7,354,728 exactly. *Predicted: 0.94*

**C06** `content` `inherited` — `entropy.py --tree --by-ext` re-run reports **12
files, 7,354,728 bytes and 108 of 122 blocks above 7.5**, with `.LIB` the
highest at 7.9744 and `.ID` the lowest at 2.3219, and the four values above 7.93
are the four InstallShield containers. *Predicted: 0.90*

**C07** `content` `inherited` — the by-extension entropy table has **eleven
rows** over twelve files, and therefore **ten of the eleven rows contain exactly
one file**; the only row with two is `.EXE`. Any statement that nine rows hold
one file is wrong by one. *Predicted: 0.88*

**C08** `content` `inherited` — `sigcount.py --hex 135d658c` re-run reports
**3 of 12 files beginning with the signature** — `_SETUP.1`, `_SETUP.LIB`,
`SETUP.INS`, 6,968,258 bytes between them — and **3 occurrences anywhere, in 3
files**, so the magic appears nowhere except at offset 0 of those three.
*Predicted: 0.94*

**C09** `content` `inherited` — `pecensus.py --by-magic` re-run reports **3
binaries, 3 NE16, 0 PE, 0 Authenticode**, with module names `ISSET_SE`,
`_DELIS` and `_SETUP`, linker 5.60 on all three, two segments each, and NE flags
0x0302, 0x0302 and 0x8301. *Predicted: 0.93*

**C10** `content` `inherited` — `_SETUP.DLL` carries **both company names at
once**: its NE module description says *Stirling Technologies* with a 1990-1995
range and its version resource says *InstallShield Corporation* with a 1990-1996
range, and both strings are recovered from the file by a command on the page.
*Predicted: 0.88*

**C11** `content` `inherited` — `sift.py --group personal` re-run finds **4 hits
in 4 blobs** and no others: one e-mail shape in `readme.txt` and three telephone
shapes, `(847) 240-9111` in `SETUP.EXE` and `_SETUP.DLL` and **`(708)
240-9111`** in `_ISDEL.EXE`; the positive control fires and the negative control
stays quiet; and none of the four is a false positive. *Predicted: 0.93*

**C12** `content` `inherited` — `mtimes.py --waves` re-run reports **seven
waves** with the counts and byte totals 1/8,192, 1/6,128, 1/44,928, 1/320,276,
1/66,661, 2/2,367 and 5/6,906,176, the seven counts sum to 12 and the seven byte
totals sum to 7,354,728, and there are **ten distinct timestamps** over the
twelve members. *Predicted: 0.90*

**C13** `content` `inherited` — `readme.txt` dates itself **28-June-1999 00:43**
in its own last line while its ZIP timestamp is **1999-07-12 00:12:50**, and
`FILE_ID.DIZ` dates itself **12-07-99** inside its box-drawing frame and agrees
with its own ZIP timestamp to the day. *Predicted: 0.93*

**C14** `content` `inherited` — `SETUP.PKG` re-walked by this session's own code
declares **12 groups** named `Group1`..`Group12` and **256 files**, all 256
records parse as `(u32 size, u8 name length, name, NUL, u16 group)`, the walk
stops **20 bytes** from the end of the file, and the 256 declared sizes sum to
**6,607,311**. *Predicted: 0.93*

**C15** `content` `inherited` — the manifest's extension histogram is MID 102,
BMP 75, WAV 55, DAT 8, EXE 4, TXT 4, ATR 4, DLL 2, HLP 2, and the nine rows sum
to 256. *Predicted: 0.92*

**C16** `content` `inherited` — the manifest's group histogram is 5, 12, 5, 2, 1,
20, 103, 54, 42, 1, 9, 2 across the twelve group indices, the twelve rows sum to
**256**, and the largest group holds 103 files. *Predicted: 0.90*

**C17** `content` `inherited` — the manifest names `rpg95.exe` at 493,551,
`rpg95.hlp` at 890,048 **twice, in two different groups**, `game.exe` at
241,493, `game_engl_123.exe` at 182,094, `unlha32.dll` at 98,281, `MONSTPIC.DAT`
at 358,271 and `USER32.DLL` at 21,223, and every one of those figures is read
out of the manifest by a command on the page. *Predicted: 0.90*

**C18** `content` `inherited` — the three Z archives carry a count at `+0x0C`
reading **256, 11 and 1** on `_SETUP.1`, `_SETUP.LIB` and `SETUP.INS`
respectively, and a DOS date at `+0x0E` that decodes to 1999-07-12, 1999-07-12
and 1996-12-19 and therefore **agrees with each member's own ZIP date on 3 of
3**. *Predicted: 0.90*

**C19** `content` `inherited` — the word at `+0x10` of the three Z archives does
**not** agree three ways: it matches `_SETUP.LIB`'s ZIP time exactly, is
ninety seconds earlier than `_SETUP.1`'s, and is hours away from
`SETUP.INS`'s, and this repository reports that as one of three rather than
folding it into the date's three of three. *Predicted: 0.85*

**C20** `content` `inherited` — `crossall.py` re-run reports **0 of 1** on the
object's own hash list and **1 of 12** on the members', the single crossing is
`_ISDEL.EXE` at sha1 `fe96bd82d167f50cb8cd9c9a32d72b77f45f8002` and 8,192 bytes
against `pc-clic11-doc`, and both denominators are published in this repository
with an argument for which one it means. *Predicted: 0.93*

**C21** `content` `inherited` — the collection holds **132** directories matching
`*-doc` and **63** matching `pc-*-doc`, both counts including this repository,
and both are re-derived by `ls` rather than quoted. *Predicted: 0.95*

**C22** `content` `inherited` — `protscan.py` re-run searches **3 files of 12
and 59,248 bytes of 7,354,728**, reports 0 hits on eleven markers, and its
positive control fires on 3; `utf16sift.py` reports **0 hits that only a
sixteen-bit pass finds**; `mzcensus.py` reports **1 of 3** because it filters on
the `.EXE` extension and `_SETUP.DLL` is the same NE format; `namecensus.py`
raises `ZeroDivisionError`; and `dircensus.py` prints a complete table over zero
containers and exits 0. *Predicted: 0.88*

**C23** `content` `inherited` — `toolscan.py` reports **514 Python files** in
`tools\` and **0 forbidden bytes**, all three of its positive controls fire, and
the 514 are `pc-iamsetsuna-doc/tools/` copied whole — verified file by file by
sha1, with the count of differing files reported. *Predicted: 0.90*

**C24** `content` `inherited` — `readme.txt` holds **33 bytes `>= 0x80` in 18
distinct values**, all of them in one line, and that line decodes under CP866 to
a Russian sentence; `FILE_ID.DIZ` holds **49 bytes `>= 0x80` of 400** and every
one of them is a CP437 line-drawing character. *Predicted: 0.88*

**C25** `content` `inherited` — `_INST32I.EX_` begins with the four bytes of
magic `0x2AAB79D8`, is 320,276 bytes at entropy 7.9645, is **not** the Z archive
and **not** SZDD or KWAJ — `szdd.py` finds no candidate in the object — and it
is the only member whose format appears exactly once. *Predicted: 0.92*

---

### Open, method — six clauses, priced as one correlated block per P7

**C26** `method` `open` — every reader written in this session ships a
`selftest` subcommand built on specimens constructed in memory, **most of them
rejected and at least one accepted**, and at least one of those selftests
catches a real defect in its own reader on the first run and the defect is
written down. *Predicted: 0.90*

**C27** `method` `open` — every figure in every chapter carries the command that
regenerates it on the same page, no figure from `_pre\` reaches a chapter
without being re-derived by this session's own run, and every truncated listing
says how many of how many and names the file under `notes\` that holds the rest.
*Predicted: 0.90*

**C28** `method` `open` — no absolute path of this machine appears in any `.md`
of this repository or in the default arguments of any tool written here, and the
third-party paths, telephone numbers and URLs recovered from the object are
published as the artefacts they are, with the single exception argued in the
personal-data chapter. *Predicted: 0.90*

**C29** `method` `open` — rule 0 is not violated: no heredoc carries a backslash,
a space or a non-ASCII byte, `Write` and `Edit` are used for every such file,
and every script that substitutes text counts its substitutions and exits
non-zero when the count is zero. *Predicted: 0.90*

**C30** `method` `open` — the repository is pushed to `vs-sr-dev` on branch
`master`, `git ls-files` filtered against the five permitted prefixes is empty
with a positive control that fires, the description is under 350 characters and
is **read back from the remote** rather than from the command that set it, the
topics are set, and `pc-gamelist-doc` is modified and pushed on `main` with
`rowlen.py` reporting 0 rows over budget. *Predicted: 0.90*

**C31** `method` `open` — the repository is **under twenty documents**, the count
is argued in the README on the object's own scale rather than padded to a
target, and `predcount.py` is run before the first chapter and after the last
with both runs agreeing. *Predicted: 0.90*

---

### Open, content — the work

**C32** `content` `open` — a reader for the InstallShield 3 Z archive is written
in this session, it derives the header layout from the bytes rather than from
any published description, and it recovers a **table of contents whose entry
count equals the count the header declares** — 256 for `_SETUP.1`, 11 for
`_SETUP.LIB`, 1 for `SETUP.INS`. *Predicted: 0.86*

**C33** `content` `open` — the names in `_SETUP.1`'s own table of contents match
the names in `SETUP.PKG` on **256 of 256**, as sets, so that two files written by
the same packer but read by two entirely different code paths agree on the whole
population. *Predicted: 0.80*

**C34** `content` `open` — the **13,784-byte difference** between `SETUP.PKG`'s
declared 6,607,311 and `_SETUP.1`'s 6,621,095 is explained exactly and closes at
residue 0: it is the archive's own header plus its table of contents, and the
sum of the header size, the directory table and the 256 entry records equals
13,784 with nothing left over. *Predicted: 0.72*

**C35** `content` `open` — the u32 size field in `SETUP.PKG` is shown, from the
bytes and not by assertion, to be the size of the member **as stored inside the
archive** rather than its expanded size, because the ZIP deflates `_SETUP.1` by
only 3 % and a 6.6-megabyte body of MIDI, bitmaps and executables cannot both be
compressed and be 13,784 bytes short of its own expanded total. *Predicted: 0.62*

**C36** `content` `open` — the compression inside the Z archive is identified as
**PKWARE's Data Compression Library implode**, and it is identified by
decompressing a member and matching a declared length, not by quoting the
`Copyright 1990-92 PKWARE Inc.` string that sits in `SETUP.EXE`; the chapter
says in the same paragraph that the copyright line is a hint and was not the
evidence. *Predicted: 0.78*

**C37** `content` `open` — at least one member of `_SETUP.1` is decompressed and
its expanded length matches a length the archive or the manifest declares for
it, and the number of members that close this way is reported as *n* of 256
rather than as a share. *Predicted: 0.76*

**C38** `content` `open` — **`rpg95.exe` is a sixteen-bit NE binary**, not PE:
its `e_lfanew` points at the two bytes `NE`, and this repository answers the
question by extracting the file rather than by reasoning from the product's
1995 date. *Predicted: 0.70*

**C39** `content` `open` — the Z archive reader is pointed at
`pc-clic11-doc`'s `FP98\DATA.Z` and `FP98\_SETUP.LIB` — an entirely different
product, packaged by a different company two years earlier — and opens at least
one of them, so that the format claim rests on more than one specimen; and the
result, whichever way it goes, is reported with the specimen's byte count.
*Predicted: 0.74*

**C40** `content` `open` — `_SETUP.LIB` opens and holds **11 members**, and
`SETUP.INS` opens and holds **1**, each agreeing with the count in its own
sixteen-byte header; and if either refuses, the refusal names the byte offset at
which it stopped. *Predicted: 0.80*

**C41** `content` `open` — the question the owner raised and nobody checked —
**whether a sample game is in the package** — is answered out of the manifest's
256 names, with the names and sizes of whatever supports the answer, and the
answer is stated as what the manifest shows rather than as what RPG Maker is
known to ship. *Predicted: 0.82*

**C42** `content` `open` — the twelve groups are given a reading from the
manifest's arithmetic alone: which group holds the engine, which holds the stock
resource library, and which are single-file groups, each backed by the group's
file count and byte total, and the twelve byte totals sum to 6,607,311.
*Predicted: 0.84*

**C43** `content` `open` — the manifest's 256 files are censused by byte total
as well as by count, so that the object can say what share of the *product's*
6,607,311 bytes is stock MIDI, bitmap and WAV content against what share is the
editor and its runtime, and the two sides sum to 6,607,311. *Predicted: 0.88*

**C44** `content` `open` — the six bytes that follow `_SETUP.Z` in the
manifest's twenty-byte trailer are read and given a reading, or a refusal is
written that says what was tried and what would settle it. *Predicted: 0.80*

**C45** `content` `open` — the number of printable runs to expect **by chance**
in 320,276 bytes at `_INST32I.EX_`'s measured byte distribution is computed and
compared with the 427 observed, using the file's own empirical byte frequencies
rather than a uniform model, and the comparison is what decides whether the runs
mean anything. *Predicted: 0.84*

**C46** `content` `open` — `_INST32I.EX_` is **not** opened, the refusal is
written down, and it carries a bound or a specific reason rather than a shrug.
*Predicted: 0.86*

**C47** `content` `open` — the CP866 line in `readme.txt` is decoded with
`.decode('cp866')` and reported in full, and `FILE_ID.DIZ` is decoded with
`.decode('cp437')` and reproduced with its box drawing intact, and both
chapters name the codepage they used and why that one. *Predicted: 0.92*

**C48** `content` `open` — the accounting chapter states **three totals at three
levels** — 7,120,053 for the object, 7,354,728 for the members, 6,607,311 for
the product the manifest declares — never adds two of them together, and every
percentage anywhere in this repository names which of the six denominators it is
over. *Predicted: 0.84*

**C49** `content` `open` — this repository decides in writing, in the
personal-data chapter and before quoting anything from `readme.txt`'s signature
block, what to do with the self-published e-mail address; the decision is stated
as a rule with a test that can be applied to the other three contacts in the same
paragraph — the ICQ number, the URL and the vendor telephone line — and each of
the four is disposed of by that test. *Predicted: 0.90*

**C50** `content` `open` — the decision of C49 is **implemented in code**, not
merely stated: a tool in `tools\` performs it, it is applied to the output that
lands in `notes\`, and it has a positive control that fails loudly if the
redaction stops matching. *Predicted: 0.80*

**C51** `content` `open` — `refusals.py` is extended by the ten readers written
on the previous object and re-run, and the outcome is recorded as *n* pointed,
*n* refused and *n* exited 0; and `jstore.py` in particular is pointed at
`SETUP.PKG` and at a Z archive header and its **output** is read rather than its
exit code, and what it claims is reported whether or not it is true.
*Predicted: 0.88*

**C52** `content` `open` — `verres.py`, written for PE on the previous object, is
pointed at the three NE files, and whether it reads them or refuses is recorded
with the exit code and the first line of its output. *Predicted: 0.88*

**C53** `content` `open` — `kfaccount.py` is pointed at this object and reports
substantially complete coverage from a catch-all bucket, for the third
consecutive session, and the chapter says which bucket. *Predicted: 0.82*

**C54** `content` `open` — `docs\NN-corrections.md` records **at least six**
errors, counting those found in `prompt.txt` and in `_pre\` together with this
session's own; the pre-briefing flags none, and the last eight briefs carried
nine, seven, eight, eleven, twelve, eleven, eleven and nine. *Predicted: 0.82*
