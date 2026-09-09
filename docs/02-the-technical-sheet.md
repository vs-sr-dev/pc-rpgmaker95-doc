# 02 — the technical sheet: every figure in this repository, with the command that makes it again

*Measure: this page. Every row is a command that can be run from the repository
root against `rpgmaker95-dist\` and `_work\members\`; neither directory is
committed, and the chapter that uses each figure is linked beside it.*

---

## The object

| what | value | command |
|---|---|---|
| the file | `RPG-Maker-95_Win_EN_RPG-Maker-95-v102.zip` | `ls rpgmaker95-dist` |
| bytes | 7,120,053 | `python tools/hashall.py rpgmaker95-dist` |
| sha1 | `4e2831d0098c8aa11220ef746fc29955b9cbc164` | same |
| ZIP members | 12 declared, 12 parsed | `python tools/zipdir.py rpgmaker95-dist/RPG-Maker-95_Win_EN_RPG-Maker-95-v102.zip` |
| end-of-central-directory at | 7,120,031 | same |
| central directory | 667 bytes at 7,119,364 | same |
| archive comment | 0 bytes | same |
| ZIP64 locator | absent | same |
| structural closure | 475 + 7,118,889 + 667 + 22 = 7,120,053, **residue 0** | `python tools/zaccount.py --zip rpgmaker95-dist/RPG-Maker-95_Win_EN_RPG-Maker-95-v102.zip --members _work/members` |

## The twelve members

| member | bytes | stored | method | what it is |
|---|---:|---:|---|---|
| `_SETUP.1` | 6,621,095 | 6,421,170 | deflate | Z archive, 256 members |
| `_INST32I.EX_` | 320,276 | 319,518 | deflate | `_INST32I` container, 4 members |
| `_SETUP.LIB` | 280,502 | 278,097 | deflate | Z archive, 11 members |
| `SETUP.INS` | 66,661 | 65,837 | deflate | Z archive, 1 member |
| `SETUP.EXE` | 44,928 | 24,228 | deflate | NE, InstallShield Launcher SE v2.1 |
| `_ISDEL.EXE` | 8,192 | 3,775 | deflate | NE, Deleter Process |
| `_SETUP.DLL` | 6,128 | 3,026 | deflate | NE, resource library |
| `SETUP.PKG` | 4,513 | 1,827 | deflate | the manifest, in the clear |
| `readme.txt` | 1,967 | 1,169 | deflate | text, one CP866 line |
| `FILE_ID.DIZ` | 400 | 176 | deflate | text, box drawing |
| `SETUP.INI` | 61 | 61 | **stored** | text |
| `DISK1.ID` | 5 | 5 | **stored** | text, `DML` |
| | **7,354,728** | **7,118,889** | | 12 distinct sha1 |

`python tools/hashall.py _work/members` — 12 files, 7,354,728 bytes, 12 distinct
sha1, 0 unreadable.

## The formats

| family | files | bytes | command |
|---|---:|---:|---|
| InstallShield Z archive | 3 | 6,968,258 | `python tools/sigcount.py _work/members --hex 135d658c` |
| InstallShield `_INST32I` | 1 | 320,276 | `python tools/is32.py list _work/members/_INST32I.EX_` |
| NE, 16-bit Windows | 3 | 59,248 | `python tools/pecensus.py _work/members --by-magic` |
| InstallShield manifest | 1 | 4,513 | `python tools/ispkg.py walk _work/members/SETUP.PKG` |
| text | 4 | 2,433 | `python tools/cptext.py census _work/members/readme.txt` |

`sigcount` reports **3 of 12** files beginning with `13 5d 65 8c` and **3
occurrences anywhere in 3 files** — the magic appears at offset 0 of those three
and nowhere else in the object.

## The four containers, each closing on its own header

`python tools/zaccount.py --zip … --members _work/members`

| container | members | header | data | dir table | entry table | total | file |
|---|---:|---:|---:|---:|---:|---:|---:|
| `_SETUP.1` | 256 | 255 | 6,607,311 | 207 | 13,322 | 6,621,095 | 6,621,095 |
| `_SETUP.LIB` | 11 | 255 | 279,651 | 11 | 585 | 280,502 | 280,502 |
| `SETUP.INS` | 1 | 255 | 66,343 | 11 | 52 | 66,661 | 66,661 |
| `_INST32I.EX_` | 4 | 268 | 320,008 | — | — | 320,276 | 320,276 |

**Residue 0 on all four.** `_SETUP.1`'s 255 + 207 + 13,322 = **13,784**, which is
the difference the pre-briefing could not explain ([04](04-the-archive.md)).

## The manifest

`python tools/ispkg.py walk _work/members/SETUP.PKG --explain --tsv notes/setup-pkg.tsv`

| what | value |
|---|---|
| leading `u32` | `0x118BA34A` — low half `0xA34A` constant, **high half is not a magic** |
| `+0x0A` | 4,477 = end of the record table minus the 16-byte header |
| groups | 12, named `Group1`..`Group12` |
| files | 256 declared, 256 parsed |
| walk ends | 20 bytes from the end |
| declared bytes | **6,607,311** |
| trailer | `01 00 01 00 08 00` `_SETUP.Z` `01 01 0a 00 00 00` |
| by extension | MID 102, BMP 75, WAV 55, DAT 8, EXE 4, TXT 4, ATR 4, DLL 2, HLP 2 |
| by group | 5, 12, 5, 2, 1, 20, 103, 54, 42, 1, 9, 2 |
| distinct names | 251 of 256 |

## The archive's own table of contents

`python tools/isz.py list _work/members/_SETUP.1 --tsv notes/setup1-toc.tsv`

| closure | result |
|---|---|
| declared archive size = file length | 6,621,095 = 6,621,095 |
| directory records fill the declared table | 207 bytes, 12 records |
| entry records fill the entry table | 13,322 bytes, 256 records |
| directory file counts sum to the file count | 256 = 256 |
| members' offsets chain with no gap | 256 of 256 |
| last member ends at the directory table | 6,607,566 = 6,607,566 |
| header + data + tables = the archive | residue 0 |
| `+0x16` = the sum of the expanded sizes | 18,821,193 = 18,821,193 |
| `SETUP.PKG` names the same 256, in order | 256 of 256 |
| `SETUP.PKG`'s sizes = the stored sizes | 6,607,311 = 6,607,311 |

## Decompression

`python tools/isz.py verify _work/members/_SETUP.1 --all`

```
members tried  : 256 of 256
EXPANDED LENGTH MATCHES THE DECLARED FIELD : 256 of 256
refused or mismatched                      : 0 of 256

first two bytes of the expanded members:
  'MT' 102     'BM' 75     'RI' 55     'MZ' 6     others 18
```

The codec is **PKWARE Data Compression Library implode**. The 102 / 75 / 55
here are magic numbers; the 102 / 75 / 55 in the manifest table above are file
name extensions; the two censuses were produced by different code from
different bytes and agree.

## The executables, at every layer

`python tools/pecensus.py _work/members --by-magic`, then the same on the
recovered directories.

| layer | NE | PE |
|---|---:|---:|
| the twelve ZIP members | **3** | **0** |
| inside `_INST32I.EX_` | 2 | 2 |
| inside `_SETUP.LIB` | 0 | 5 |
| inside `_SETUP.1`, the product | **0** | **6** |
| **the object** | **5** | **13** |

## The version resources

`python tools/verres.py dump _work/product`

| file | CompanyName | FileVersion | LegalCopyright |
|---|---|---|---|
| `rpg95.exe` | ASCII | **1.02** | Copyright (c) **1997** by ASCII Corporation / You Ito, Tsuneari Okumoto |
| `game.exe` | — | 97.02.28 | Copyright (c) 1997 by ASCII Corporation / You & Tsune |
| `game_engl_123.exe` | — | 97.02.28 | as above; **ProductVersion `ver 1.23`** |
| `SETUP.EXE` (112,888) | ASCII | 1.0 | Copyright (c) 1996 |
| `unlha32.dll` | — | 0.71.0.5 | (C)Micco 1995-97 |
| `USER32.DLL` | Microsoft Corporation | **4.00.950** | Copyright Microsoft Corp. 1991-1995 |

## The clocks

`python tools/mtimes.py _work/members --waves`

| wave | when | files | bytes |
|---|---|---:|---:|
| 1 | 1995-09-07 19:22:40 | 1 | 8,192 |
| 2 | 1996-09-30 08:06:54 | 1 | 6,128 |
| 3 | 1996-11-04 13:04:12 | 1 | 44,928 |
| 4 | 1996-11-05 16:17:32 | 1 | 320,276 |
| 5 | 1996-12-19 17:19:56 | 1 | 66,661 |
| 6 | 1999-07-12 00:12:50 .. 00:24:28 | 2 | 2,367 |
| 7 | 1999-07-12 01:27:34 .. 01:29:08 | 5 | 6,906,176 |

Ten distinct timestamps over twelve members. All of them DOS timestamps
restored from the ZIP central directory: two-second granularity, local time,
**no time zone**. The 256 entries inside `_SETUP.1` carry 31 further distinct
dates spanning 1995-07-11 to 1999-07-12 ([07](07-the-clocks.md)).

## Text and codepages

| file | bytes | bytes ≥ 0x80 | distinct | verdict |
|---|---:|---:|---:|---|
| `readme.txt` | 1,967 | 33 | 18 | **CP866**, all on line 48 of 51 |
| `FILE_ID.DIZ` | 400 | 49 | 7 | box drawing; **CP437 and CP866 are indistinguishable here** |
| `SETUP.INI` | 61 | 0 | 0 | ASCII |
| `DISK1.ID` | 5 | 0 | 0 | ASCII |

`python tools/cptext.py census _work/members/readme.txt` and
`python tools/cptext.py decode _work/members/readme.txt`.

## Personal data and protection

| what | value | command |
|---|---|---|
| personal hits in the members | 4 in 4 blobs, 0 false positives | `python tools/sift.py _work/members --group personal --show` |
| hits only a UTF-16 pass finds | **0** | `python tools/utf16sift.py _work/members` |
| e-mail occurrences, all layers | **6** in 3 layers | [10](10-whose-bytes.md) |
| protection markers, members | 0 of 11, over 3 files / 59,248 bytes | `python tools/protscan.py _work/members` |
| protection markers, product | 0 of 11, over 6 files | `python tools/protscan.py _work/product` |
| the CD check | 1 string, still linked in `rpg95.exe` | [08](08-the-text.md) |

## Against the collection

| what | value | command |
|---|---|---|
| `-doc` directories | 132 | `ls -1d ../*-doc/ \| wc -l` |
| `pc-*-doc` directories | 63 | `ls -1d ../pc-*-doc/ \| wc -l` |
| crossings, denominator 1 | **0 of 1** | `python tools/crossall.py notes/sha1-all.txt --collection .. --skip pc-rpgmaker95-doc` |
| crossings, denominator 12 | **1 of 12** | `python tools/crossall.py notes/sha1-members.txt --collection .. --skip pc-rpgmaker95-doc` |
| repositories swept | 102 | same |
| list files swept | 448 | same |
| hash tokens read | 155,217 | same |

## The tools

| what | value | command |
|---|---|---|
| Python files in `tools\` | **522** | `ls -1 tools/*.py \| wc -l` |
| forbidden control bytes | 0 of 522 scanned | `python tools/toolscan.py tools .py` |
| written this session | 8 | [12](12-the-tools.md) |
