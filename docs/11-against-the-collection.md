# 11 — against the collection: one crossing, two denominators, and a neighbour's twenty-one megabytes that opened on the way past

*Measure: `python tools/crossall.py notes/sha1-all.txt --collection .. --skip
pc-rpgmaker95-doc` and the same with `notes/sha1-members.txt`; both runs are in
`notes/crossall.txt`. The directory counts are `ls -1d ../*-doc/ | wc -l` and
`ls -1d ../pc-*-doc/ | wc -l`.*

---

## The denominators, counted

```
ls -1d ../*-doc/    | wc -l      132
ls -1d ../pc-*-doc/ | wc -l       63

crossall's own report:
  repositories swept          : 102
  list files swept            : 448
  hash tokens read            : 155217
```

Both directory counts include this repository, which already existed when they
were taken. **132 does not move after this session**, and 63 does not either.

---

## The trap that was not in the brief

The pre-briefing reported **0 of 1** on the object. The first run here reported
**1 of 1**, and the crossing was the object matching itself:

```
sha1 4e2831d0098c8aa11220ef746fc29955b9cbc164   7120053 bytes
   mine : RPG-Maker-95_Win_EN_RPG-Maker-95-v102.zip
   also : pc-rpgmaker95-doc     notes/sha1-all.txt
   also : pc-rpgmaker95-doc     docs/00-predictions.md
```

`crossall.py` sweeps the collection root, and this repository is in it. The
pre-briefing's run predated `notes/`, so there was nothing of its own to find
and the omission never showed. **`--skip pc-rpgmaker95-doc` is required and the
brief does not say so**, and a session that published its notes first and swept
afterwards would have reported a crossing rate of 100 % against itself
([13](13-corrections.md)).

With the skip in place both figures reproduce exactly.

---

## Two runs, two questions, and the repository has to say which it means

```
python tools/crossall.py notes/sha1-all.txt --collection .. --skip pc-rpgmaker95-doc
    my distinct sha1 : 1     CROSSINGS : 0 of 1

python tools/crossall.py notes/sha1-members.txt --collection .. --skip pc-rpgmaker95-doc
    my distinct sha1 : 12    CROSSINGS : 1 of 12
```

**Both are correct and they answer different questions.** This is the first
object in this collection where the crossing denominator is a choice rather
than a fact, and the choice has to be argued rather than made quietly.

*0 of 1* asks: **has anybody else in the collection downloaded this file?** The
answer is no, and it will stay no unless somebody documents the same
distribution archive. It is a true statement about a population of one, which
is to say it is almost content-free.

*1 of 12* asks: **does any file inside this distribution appear in another
object?** That is the question the collection has always been asking of trees,
and it is the one worth answering.

> **This repository means `notes/sha1-members.txt`, and that is the list the
> collection should use to compare itself with this object.**
>
> `notes/sha1-all.txt` is published beside it because the brief asked for both
> and because the object-level answer is a real, if empty, one. Anybody sweeping
> the collection should read the members list; anybody asking whether this exact
> download is elsewhere should read the other.

And the honest caveat, because 1 of 12 is **8.3333 %** and that would be the
fourth-highest rate in the collection's table: **one file out of twelve is a
rate a small denominator manufactures.** `pc-iamsetsuna-doc` crossed 10 of 962
and reported 1.0395 %; the difference between the two figures is mostly the
size of the tree, not the amount of sharing. The rate is published with its
fraction beside it and never on its own.

There is now a third population — the 272 recovered files — and it is
**deliberately not published as a hash list**. Two reasons, and only the second
is load-bearing: the crossing question is about the object as distributed, not
about what falls out of it; and a hash list of 256 files of unlicensed software
is a checklist for verifying a copy of it, which is not what this repository is
for.

---

## The one crossing

```
sha1 fe96bd82d167f50cb8cd9c9a32d72b77f45f8002   8192 bytes
   mine : _ISDEL.EXE
   also : pc-clic11-doc          notes/sha1-all.txt
```

**`_ISDEL.EXE`, InstallShield's "Deleter Process", byte-identical in an
unauthorised Russian translation of a Japanese game-making tool and in
`pc-clic11-doc`**, where it sits at `FP98/_ISDEL.EXE` on a cover disc, inside
Microsoft FrontPage 98's installer.

**What that measures is InstallShield, not RPG Maker**, and the sentence that
reports it has to say so in the same breath. Two identical 8,192-byte
uninstaller stubs prove that two packagers used the same toolkit family, and
nothing else. The other eleven members cross nothing, including all three Z
archives — which is expected, because `_SETUP.1` was built on one night in 1999
for one product.

**Two objects in a row have crossed on the plumbing.** `pc-iamsetsuna-doc`
crossed ten of 962 and all ten were a Mono configuration file no Unity game
reads; this one crosses one of twelve and it is an uninstaller nobody runs on
purpose. The collection's crossings have stopped being about content.

### And the dates disagree, which is the interesting part

| | `_ISDEL.EXE` | dated |
|---|---|---|
| here | ZIP central directory | **1995-09-07 19:22:40** |
| `pc-clic11-doc` | ISO directory record | **1997-07-29 14:50:56** |

Same 8,192 bytes, same sha1, and two containers two years apart stamping them
differently. The ZIP preserved the file's own 1995 mtime; the ISO recorded when
FrontPage's disc was mastered. **Neither date is the file's, and the crossing is
the only reason either could be checked.**

---

## What this session gives back to `pc-clic11-doc`

`pc-clic11-doc/docs/13` censused its disc's containers and reported:

| | files | bytes on disc | declared inside |
|---|---:|---:|---|
| InstallShield `.Z` | 2 | 21,394,515 | **not declared** |

It said the contents of those two files were unknown, and it was right that
nothing in the box could read them. `isz.py` reads them now, unchanged:

```
python tools/isz.py list ../pc-clic11-doc/_work/iso/FP98/DATA.Z
declared    : 2399 files in 108 directories
255 + 20851997 + 2852 + 131215 = 20986319 against 20986319, residue 0

python tools/isz.py list ../pc-clic11-doc/_work/iso/FP98/_SETUP.LIB
declared    : 8 files in 1 directories
255 + 407496 + 11 + 434 = 408196 against 408196, residue 0
```

**2,407 files and 21,259,493 declared bytes, in a repository that published "not
declared" in that column.** The directory names are real paths — `themes\global`,
`pages\feedback.tem`, `_vti_bin\_vti_adm` — and FrontPage's own `SETUP.PKG`
declares 20,851,997 stored bytes, which is the same number `DATA.Z`'s entry
table produces.

That neighbour is not modified by this session. The result is recorded here, and
the tool that produces it is in `tools\` where the next session that meets an
InstallShield disc will find it.

**And the neighbour paid this session back first**: `DATA.Z` is where the
sixteen-bit entry-table length was caught overflowing, which this object could
never have shown, because 13,322 fits in a `u16` and 131,215 does not
([04](04-the-archive.md)).

---

## The rate table

This object enters at **1 of 12 = 8.3333 %** on the members and **0 of 1 =
0.0000 %** on the object. Both are in `notes/crossall.txt` with their
denominators printed above them, and the members figure is the one this
repository stands behind.
