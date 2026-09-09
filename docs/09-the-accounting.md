# 09 — the accounting: four totals, no shop, and residue 0 in six places

*Measure: `python tools/zaccount.py selftest` — 4 checks, including a ZIP this
tool did not write and a file whose end record has been corrupted — then
`python tools/zaccount.py --zip rpgmaker95-dist/RPG-Maker-95_Win_EN_RPG-Maker-95-v102.zip
--members _work/members`. The full output is `notes/account.txt`.*

---

## What replaces the shop

The last three objects this collection documented were Steam installations, and
each arrived with an external witness: an `appmanifest_NNNNNN.acf` declaring a
byte total, a build id, a depot list and a `LastPlayed`. The accounting chapter
compared two numbers written by two parties and reported the difference.

**There is none of that here.** No store, no manifest from a publisher, no
`installdir`, no depot, no `SizeOnDisk`. There is one downloaded file and
whatever it says about itself.

So the closure has to be built out of the object, and it turns out the object
is unusually good at it: **every container here states its own size, and one of
them states the total size of its contents as well.**

---

## Layer 1 — the object, against PKWARE's published structure

```
LAYER 1 -- THE OBJECT, denominator 1 file
  local file headers                      475
  member data                         7118889
  central directory                       667
  end-of-central-directory                 22
  TOTAL                               7120053
  the file on disk                    7120053

  the ZIP closes against PKWARE's structure              ok  residue 0
  the central directory is the length the EOCD declares  ok  667 = 667
```

Every term is counted out of the records, not read from a stored total: 30
bytes plus the name for each of twelve local headers, the compressed size out
of each central-directory record, 46 bytes plus the name for each of twelve
central records, and the 22-byte end record. **Residue 0 on the whole object,
with no external witness of any kind.**

It is a stronger result than any shop total this collection has reported,
because every term is a field somebody had to write correctly for the archive
to open at all — and the archive opens.

**And the archiver does not name itself.** `create_system` 0 (MS-DOS/FAT) on 12
of 12, `create_version` 2.0 on 12 of 12, `extract_version` 2.0 on 10 and **1.0
on 2** — the two stored members, which need no deflate support. Zero extra-field
bytes on all twelve, empty comment, no Info-ZIP signature, no `UT`. A 1999 PKZIP
2.04g would look exactly like this and so would several other programs, and
this repository does not guess which.

---

## Layer 2 — the members

```
LAYER 2 -- THE MEMBERS, denominator 12 files
  extracted bytes                     7354728
  stored inside the ZIP               7118889
  every member the ZIP declares is on disk               ok  12 of 12
```

7,120,053 on the wire against 7,354,728 inside: the ZIP saves **3.21 %**,
because ten of the twelve members were already compressed by InstallShield
before PKZIP ever saw them.

---

## Layer 3 — the four containers, each against its own header

```
LAYER 3 -- THE CONTAINERS, denominator 4 of those 12 members
  _SETUP.1        256 members  255 + 6607311 + 207 + 13322 = 6621095, file 6621095
  _SETUP.LIB       11 members  255 +  279651 +  11 +   585 =  280502, file  280502
  SETUP.INS         1 members  255 +   66343 +  11 +    52 =   66661, file   66661
  _INST32I.EX_      4 members  268 +  320008              =  320276, file  320276
```

**Four containers, four residues of 0.** Each one is header plus data plus
whatever tables it carries, and each total is also a number the container
declares about itself at a fixed offset — `+0x12` on the three Z archives, and
in `_INST32I.EX_`'s case the record table's own end meeting the first member's
offset.

`_SETUP.1`'s 255 + 207 + 13,322 = **13,784**, which is the entire content of
the pre-briefing's third open question ([04](04-the-archive.md)).

---

## Layer 4 — the product

```
LAYER 4 -- THE PRODUCT, denominator 272 recovered files
  bytes the entries declare            20442049
```

272 files: 256 in `_SETUP.1`, 11 in `_SETUP.LIB`, 1 in `SETUP.INS`, 4 in
`_INST32I.EX_`. Every one of them was decompressed and every one matched the
expanded length its own entry declares — **272 of 272**.

---

## The cross-checks between layers

```
  SETUP.PKG's 256 sizes equal _SETUP.1's stored sizes         6607311 = 6607311
  SETUP.PKG names the same 256 files, in the same order       256 of 256
  _SETUP.1's header declares the sum of its expanded sizes   18821193 = 18821193
  SETUP.PKG's group counts equal _SETUP.1's directory counts  12 of 12
```

Four agreements between two files that were read by two entirely separate
readers in `tools\`. The third is the one worth pausing on: `+0x16` of the
archive header is a `u32` the pre-briefing listed as unnamed, and it is the sum
of 256 fields sitting 6.6 megabytes away.

---

## The four totals, which are never added together

```
  the object                      7120053 over  1 file
  the members                     7354728 over 12 files
  the manifest declares           6607311 over 256 names
  the product, expanded          20442049 over 272 recovered files
```

**Four numbers, three of them larger or smaller than the object for different
reasons, and no two of them measure the same thing.** 7,120,053 is what was
downloaded. 7,354,728 is what comes out of it. 6,607,311 is how much of that
is one member's payload. 20,442,049 is what all four containers would write to
a disc.

Every percentage in this repository names which of these it is over, and the
one figure that would be meaningless — a share of "the object" computed over
the members — appears nowhere.

The one number that spans layers legitimately is **18,821,193**, `_SETUP.1`'s
declared expanded total, because it is the only figure in the object that a
human also wrote down: the readme asks for *"18 Mb of free space at your HDD (6
Mb at your C: drive and 12 Mb at others)"*. 18,821,193 bytes is 17.95 MiB, and
6 + 12 is 18.

---

## What has no residue and what has no number

**Six residues of 0**: the ZIP against PKWARE, and four containers against their
own headers, and the manifest against the archive's entry table.

**And two things with no number at all.** The object's own provenance — when it
was downloaded, from where, by whom — has one witness, this machine's file
system, saying 2026-09-09, and this repository does not build a story on a
single unverified mtime. And `SETUP.INS`'s 206,269-byte compiled script came out
whole and was not parsed: it is **1.0090 % of the recovered bytes** and it is
the only thing in the object that was opened and then set down again.
