# 05 — the product: the most interesting question in the object had the wrong answer

*Measure: `python tools/isz.py extract _work/members/_SETUP.1 --all --out
_work/product` for the 256 files, then `python tools/pecensus.py`, `python
tools/verres.py dump _work/product` and `python tools/isz.py list … --tsv
notes/setup1-toc.tsv` for what they are. `_work\` is not committed: this
chapter publishes measurements of the product, not the product.*

---

## `rpg95.exe` is thirty-two bit

The pre-briefing called this "the single most interesting unanswered question
in this object", and it is:

> 16-bit would make the translation a resource edit of a Windows 3.1 binary,
> 32-bit would make it something else.

This repository predicted **NE**, in writing, at 0.70
([00](00-predictions.md), C38), on the reasoning that RPG Maker 95 is a 1995
Japanese application whose installer is entirely 16-bit. That reasoning was
about the wrapper and the wrapper is not the program.

```
python tools/isz.py extract _work/members/_SETUP.1 --name rpg95.exe --out _work/product
rpg95.exe                  493551 stored ->  1213440 expanded

od -A d -t x1z -N 16 _work/product/000_rpg95.exe
0000000 4d 5a 50 00 02 00 00 00 04 00 0f 00 ff ff 00 00  >MZP.............<

e_lfanew    : 256
signature   : 'PE'
bytes there : 50 45 00 00 4c 01 06 00 84 22 81 a6 00 00 00 00
```

**`MZP`, `e_lfanew` 256, `PE\0\0`, machine `0x014C`, six sections.** A 32-bit
Windows executable, and the `MZP` stub plus a linker version of 2.25 plus the
string `Borland C++ - Copyright 1994 Borland Intl.` plus an import of
`BWCC32.DLL` put it on Borland's 32-bit toolchain, not Microsoft's.

The clause is a miss and it stays in the document. What makes it worth the
half-page is *why* it was wrong: the object presents three sixteen-bit
executables and zero PE files before anything is opened, and every one of them
belongs to InstallShield. **The installer's bitness is a fact about
InstallShield's 1996 toolkit and carries no information at all about what it
installs.**

---

## The inversion, in one table

```
python tools/pecensus.py _work/members --by-magic          NE16 3   PE 0
python tools/pecensus.py _work/product --by-magic          NE16 0   PE 6
```

| layer | NE | PE |
|---|---:|---:|
| the twelve ZIP members | **3** | **0** |
| inside `_INST32I.EX_` | 2 | 2 |
| inside `_SETUP.LIB` | 0 | 5 |
| inside `_SETUP.1`, the product | **0** | **6** |
| **the object, all layers** | **5** | **13** |

The pre-briefing's headline — *zero PE in the whole object* — was true of the
twelve members and false of the object by thirteen.

---

## The six programs, and their version resources

```
python tools/verres.py dump _work/product
```

| file | expanded | CompanyName | FileVersion | ProductVersion |
|---|---:|---|---|---|
| `rpg95.exe` | 1,213,440 | **ASCII** | **1.02** | *(overwritten, unreadable)* |
| `game.exe` | 504,832 | *(empty)* | 97.02.28 | `ver 1.03` |
| `game_engl_123.exe` | 408,064 | *(empty)* | 97.02.28 | **`ver 1.23`** |
| `SETUP.EXE` | 225,280 | **ASCII** | 1.0 | 1.0 |
| `unlha32.dll` | 151,552 | *(empty)* | 0.71.0.5 | 0.71.0.5 |
| `USER32.DLL` | 44,544 | **Microsoft Corporation** | **4.00.950** | 4.00.950 |

**`rpg95.exe` says `FileVersion 1.02`** — the version the ZIP's file name, the
readme, `SETUP.INI` and `FILE_ID.DIZ` all claim, now confirmed from the
program's own resource rather than from four pieces of prose.

**`game_engl_123.exe` says `ProductVersion "ver 1.23"`.** The pre-briefing
flagged this as an open question and told the next session not to assume it:
the readme says the translator had just obtained version 1.23 and had not
finished with it, and a file *name* containing "123" is not a version. It is
one. The resource agrees with the name, the file is 408,064 bytes, and it is
the record the packer appended last ([03](03-the-manifest.md)).

**`LegalCopyright` on `rpg95.exe` is:**

```
Copyright (c) 1997 by ASCII Corporation
Copyright (c) 1997 by You Ito/Tsuneari Okumoto.
```

`game.exe` and `game_engl_123.exe` carry the same, shortened to *You & Tsune*.
**Two more named people**, and unlike everybody else in this object they are
the ones who wrote the program ([10](10-whose-bytes.md)).

**`USER32.DLL` at 44,544 bytes is Microsoft's.** The pre-briefing reasoned that
it could not be Windows 95's, "which is around 40 times that", and concluded it
was a thunk, a stub or a mistake. Its version resource says *Microsoft
Corporation, Win32 USER32 core component, 4.00.950, Microsoft Windows Operating
System* — `4.00.950` is Windows 95's retail build, and Windows 95's `USER32.DLL`
really is about forty kilobytes, because on that system it thunks down to the
16-bit `USER.EXE` and holds little code of its own. It is exactly what its name
says, shipped by a Japanese publisher into an installer as a redistributable
([13](13-corrections.md)).

`unlha32.dll` is Micco's freeware LHA library, `0.71.0.5`, copyright
1995-97 — and `rpg95.exe` imports it and builds command lines like
`u -jn0 %srpgtmp.lzh`. **RPG Maker 95 keeps a user's project inside an LHA
archive**, which is why a game-making tool ships a compression library.

---

## What the 256 files are

```
python tools/coverage.py product

denominator : 272 files, 20442049 bytes
  MID  102       986405   published   Standard MIDI File
  BMP   78     11152730   published   Windows bitmap
  WAV   55      1084902   published   RIFF WAVE
  EXE    8      3353264   published   NE and PE
  DAT    8      1484216   neither     RPG Maker's own
  DLL    7       432128   published   NE and PE
  TXT    5         4405   published   plain text
  ATR    4         1024   neither     RPG Maker's own
  HLP    2      1700484   neither     WinHelp 3.x
  INI    2        36222   published   plain text
  INS    1       206269   neither     compiled InstallShield script
```

By group, in expanded bytes, aligned record for record against the manifest:

| | files | expanded | |
|---|---:|---:|---|
| Group1 | 5 | 2,667,842 | the engine |
| Groups 2, 3, 4 | 19 | 3,210,511 | **a complete sample game** |
| Group5 | 1 | 225,280 | ASCII's game-disk installer |
| Group6 | 20 | 6,707,524 | the help file again and 19 battle backgrounds |
| Groups 7–11 | 209 | 6,009,761 | the stock resource library |
| Group12 | 2 | 275 | two readmes |
| | **256** | **18,821,193** | |

---

## The sample game, which is in the object

The owner said the package "also ships a sample game, which we are not
analysing here", and the pre-briefing said the sample game was not in this
object and that whether any of the 256 entries was one had never been asked.

**It is in the object, it is nineteen files, and it is 3,210,511 expanded bytes
of the 18,821,193.** Groups 2, 3 and 4 hold a complete RPG Maker project and
the runtime that plays it:

```
Group2   CHARA.DAT  EPARTY.DAT  EVE99999.DAT  ITEM.DAT  MAGIC.DAT
         MONSTPIC.DAT  PARAM.DAT  MCHIP0.ATR .. MCHIP3.ATR  readme.txt
Group3   STRINGS.DAT  chara.bmp  MCHIP0.BMP  MCHIP1.BMP  MCHIP2.BMP
Group4   MCHIP3.BMP  game.exe
```

Characters, a party, an event file, items, magic, a monster picture bank of
1,423,248 expanded bytes, parameters, four map-chip attribute files of 256
bytes each, the bitmaps those chips index, and `game.exe`. `EVE99999.DAT` is
306 bytes — and the readme's second known bug says *"Just delete EVExxxx.DAT
file!"*, so the naming convention is confirmed by the man who shipped it.

This is the one question in the object that could be answered without opening
anything, and it took the manifest and a `grep`.

---

## The largest twelve

```
awk -F'\t' 'NR>1' notes/setup1-toc.tsv | sort -t$'\t' -k3,3nr | head -12

  stored ->  expanded   name
  358271 -> 1423248   MONSTPIC.DAT
  493551 -> 1213440   rpg95.exe
  890048 ->  850242   rpg95.hlp
  890048 ->  850242   rpg95.hlp
  241493 ->  504832   game.exe
   82602 ->  451638   ENEMY4.BMP
   72451 ->  451638   ENEMY5.BMP
   44195 ->  451638   ENEMY6.BMP
   84996 ->  431158   ENEMY0.BMP
   95503 ->  431158   ENEMY2.BMP
  182094 ->  408064   game_engl_123.exe
   67984 ->  388150   ENEMY1.BMP
```

**Seven of the 256 entries declare an expanded size BELOW their stored size** —
the packer made them bigger:

```
       890048 ->     850242  rpg95.hlp        (twice)
        11194 ->      10366  ARRRG.WAV
        27599 ->      26136  GLSMASH.WAV
        42494 ->      40748  MAGIC.WAV
         5478 ->       5266  NINJAHIT.WAV
           73 ->         68  readme.txt
```

A WinHelp file and a WAV are already compressed inside; DCL implode found
nothing to take out and stored them with the codec's own overhead on top, and a
68-byte readme is too short to pay for its Huffman tables. That is not a defect
in the reader: the decompressor produces exactly the declared length on all
seven, and on the other 249.

---

## The resource block still says Japanese

`rpg95.exe`'s version resource has readable English strings — *ASCII*, *RPG
Maker 95*, *1.02* — and its `VarFileInfo\Translation` entry reads:

```
raw 00 00 11 04   langid 0x0411   codepage 932
StringFileInfo block name : 041103A4
```

**Language `0x0411` is Japanese and codepage 932 is Shift-JIS.** The translator
overwrote the strings inside the block and left the block's own declared
language alone, so the file announces itself as a Japanese resource containing
English text. It is also why `verres.py` prints `ProductVersion` as `ÒW`: those
are Shift-JIS bytes being read as Latin, in a field the resource edit did not
reach.

**That mismatch is the translation, visible as a structure rather than as
prose** — and it is the only place in the object where the Japanese original
shows through.

---

## And the string that says what was done to it

`rpg95.exe` still contains, in the clear:

```
Please Insert RPG Maker 95 CD-ROM, While holding the Shift key down.
```

The readme says the package began as a **CD-RIP** by KanjiHack. **The message
the disc check would have printed is still linked into the binary**, in a
program that no longer asks for the disc. It is the only trace of the
protection in an object whose documentation describes removing it
([08](08-the-text.md)).

And at offset `0x0B747D`, verbatim:

```
RPGMakr95-409--------------------------------------------
```

`409` is a tempting three digits — Microsoft's language identifier for English
(United States) is `0x0409` — but **the version resource of this same file
declares `0x0411`, Japanese**, so the object contradicts that reading and this
chapter does not make it. What the string is has not been established here
([14](14-leftovers.md)).
