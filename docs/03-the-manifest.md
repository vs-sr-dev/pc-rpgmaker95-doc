# 03 — the manifest: four and a half kilobytes that name a product nobody had opened

*Measure: `python tools/ispkg.py walk _work/members/SETUP.PKG --explain --tsv
notes/setup-pkg.tsv`, and the same tool pointed at Microsoft FrontPage 98's
manifest in `pc-clic11-doc`. `python tools/ispkg.py selftest` first — 9 checks,
one accepted specimen and eight rejected ones.*

---

## Why this was the first thing done

The pre-briefing had walked `SETUP.PKG` and published its results, and the
instruction for this session was to walk it again by hand before trusting a
line of it, because everything else would use it as a second witness. That was
the right order: the manifest turned out to be correct in every figure it
published and to contain three things it did not notice.

`SETUP.PKG` is 4,513 bytes at entropy 5.2521 — the only member of the twelve
that is neither compressed nor an executable, which is why anybody looked at
it at all.

---

## The layout, derived twice

The pre-briefing read the first four bytes as a magic number, `0x118BA34A`.
**They are not a magic number.** FrontPage 98's manifest, in
`pc-clic11-doc/_work/iso/FP98/SETUP.PKG`, begins `4a a3 68 c0` — the low half
`0xA34A` is shared, the high half is not:

```
python tools/ispkg.py walk ../pc-clic11-doc/_work/iso/FP98/SETUP.PKG --explain

leading u32     : 0xC068A34A   (low half 0xA34A is constant; high
                  half 49256 is +0x0A plus 14 on both specimens: yes)
header unknowns : 0 2 0 49242 0
group count     : 108   (declared and parsed)
file count      : 2399  (declared and parsed)
record table    : offsets 2008 .. 49258
walk ended      : 18 bytes from the end of the file
declared bytes  : 20851997
```

Two specimens fix the header:

```
0x00  u16   0xA34A, the same on both
0x02  u16   the value at +0x0A plus 14, on both
0x04  u16   0        0x06  u16   2        0x08  u16   0
0x0A  u16   THE LENGTH OF THE BODY -- the end of the record table minus 16
0x0C  u16   0
0x0E  u16   GROUP COUNT
      then  group-count records of (u16 length, name, NUL)
      then  u16 FILE COUNT, u16 0
      then  file-count records of (u32 size, u8 length, name, NUL, u16 group)
      then  the trailer
```

**The format states its own payload length and the walk lands on it**, on both
specimens: 4,493 − 16 = 4,477 here, 49,258 − 16 = 49,242 there. That is the
third self-checking quantity in a file the pre-briefing described as having
none, and it is the one that made the reader's bounds checkable rather than
hopeful.

---

## The trailer, which took two specimens

```
ours   01 00  01 00  08 00  "_SETUP.Z"  01 01 0a 00 00 00
FP98   01 00  01 00  06 00  "data.z"    01 01 0a 00 00 00
```

`u16 1`, `u16 1`, `u16` name length, the archive's own name **with no
terminator**, and then **six bytes that are byte-identical across two unrelated
products two years apart**. That is everything the object can say about them:
they are a constant, and a constant observed twice is not a field whose meaning
has been recovered. The pre-briefing listed "the six bytes after `_SETUP.Z`" as
an open question; the honest answer is *a constant*, and it is written here as
that and not as a guess ([14](14-leftovers.md)).

**But the name is not a constant, and it explains the object's oddest file
name.** The manifest calls the archive `_SETUP.Z`; the file that ships is
`_SETUP.1`. FrontPage's manifest calls it `data.z` and the file that ships is
`DATA.Z`. The difference is in the archive's own entry records:

```
_SETUP.1          256 entries   volume byte: {1: 256}
_SETUP.LIB         11 entries   volume byte: {0: 11}
SETUP.INS           1 entries   volume byte: {0: 1}
FP98 DATA.Z      2399 entries   volume byte: {0: 2399}
FP98 _SETUP.LIB     8 entries   volume byte: {0: 8}
```

**Every entry in `_SETUP.1` carries volume 1; all 2,419 entries in every other
Z archive here carry volume 0.** `_SETUP.Z` is the archive's name; `.1` is the
volume number of a set that could have spanned floppy disks and did not. The
readme confirms the intent from the other side — it advertises that the
translated GAMEDISK Maker can now write to 1.44-inch floppies.

---

## What it declares

```
group count     : 12   (declared and parsed)
file count      : 256  (declared and parsed)
walk ended      : 20 bytes from the end of the file
declared bytes  : 6607311   (the sum of 256 u32 size fields)
```

```
by extension, in stored bytes:       by group, in stored bytes:
  MID  102      137063                 Group1    5   1685197
  BMP   75     2393372                 Group2   12    367610
  WAV   55      778175                 Group3    5    429213
  DAT    8      367081                 Group4    2    299597
  EXE    4     1030026                 Group5    1    112888
  TXT    4        1710                 Group6   20   1991354
  ATR    4         284                 Group7  103    214666
  DLL    2      119504                 Group8   54    775534
  HLP    2     1780096                 Group9   42    182314
  TOTAL256     6607311                 Group10   1      7404
                                       Group11   9    541298
                                       Group12   2       236
                                       TOTAL   256   6607311
```

Both histograms are the pre-briefing's, re-derived, and both hold exactly.

---

## Three things the pre-briefing did not notice

**One: the four `.TXT` files are all the same name.** `README.TXT`, four times,
at 1,302 / 172 / 73 / 163 bytes, in groups 2, 11, 12 and 12. The briefing
reported "TXT 4" and named the readme once. There are also two `NOSOUND.WAV`
and two `RPG95.HLP`, so **251 distinct names over 256 records**.

**Two: the fourth executable is not the installer's.** The briefing found
`rpg95.exe`, `game.exe` and `game_engl_123.exe` and said "and one more". It is
`SETUP.EXE` at **112,888 bytes**, alone in Group5 — and it is not the 44,928-byte
InstallShield launcher that sits beside it in the ZIP. Its version resource
says *ASCII, Setup for Windows, Copyright (c) 1996*: it is ASCII's own
game-disk installer, the stub that RPG Maker stamps onto a floppy so somebody
else can install the game you made with it ([05](05-the-product.md)).

**Three: record 255 breaks the order.** Records 0 to 254 run in group order —
group 0 first, then group 1, and so on to group 11. The **last** record,
number 255, is `game_engl_123.exe` and it belongs to **group 0**:

```
awk -F'\t' '$3==0' notes/setup-pkg.tsv
0    493551  0  Group1  EXE  rpg95.exe
1     98281  0  Group1  DLL  unlha32.dll
2    890048  0  Group1  HLP  rpg95.hlp
3     21223  0  Group1  DLL  USER32.DLL
255  182094  0  Group1  EXE  game_engl_123.exe
```

**It was appended to a finished manifest.** The readme, written a fortnight
earlier, says *"I got a new version of RPG Maker 95 (ver 1.23). I almost
cracked it now."* The 1.23 runtime went into the package last, out of order,
after everything else was laid down — and its version resource, once the
archive is open, does say `ver 1.23` ([05](05-the-product.md)).

---

## What the groups are

The group table gives the product a shape that nothing else in the object does.
Adding the extension census per group:

| group | files | bytes | what it holds |
|---|---:|---:|---|
| `Group1` | 5 | 1,685,197 | **the engine** — `rpg95.exe`, `rpg95.hlp`, `unlha32.dll`, `USER32.DLL`, and `game_engl_123.exe` appended last |
| `Group2` | 12 | 367,610 | **a complete game project** — `CHARA.DAT`, `EPARTY.DAT`, `EVE99999.DAT`, `ITEM.DAT`, `MAGIC.DAT`, `MONSTPIC.DAT`, `PARAM.DAT`, `MCHIP0..3.ATR`, a readme |
| `Group3` | 5 | 429,213 | that project's graphics — `chara.bmp`, `MCHIP0..2.BMP`, `STRINGS.DAT` |
| `Group4` | 2 | 299,597 | `MCHIP3.BMP` and **`game.exe`**, the runtime |
| `Group5` | 1 | 112,888 | `SETUP.EXE`, ASCII's game-disk installer |
| `Group6` | 20 | 1,991,354 | `rpg95.hlp` again, and `BG01..BG19.BMP` — battle backgrounds |
| `Group7` | 103 | 214,666 | **the music library** — 101 MIDI, 1 BMP, 1 WAV |
| `Group8` | 54 | 775,534 | **the sound library** — 53 WAV, 1 MIDI |
| `Group9` | 42 | 182,314 | 41 BMP, 1 WAV — animation frames |
| `Group10` | 1 | 7,404 | `ANM41.BMP`, alone |
| `Group11` | 9 | 541,298 | `ENEMY0..7.BMP` and a readme |
| `Group12` | 2 | 236 | two readmes, 73 and 163 bytes |

**Groups 2, 3 and 4 are a game.** A character file, a party file, an event
file, items, magic, monsters, parameters, map-chip attributes, the graphics
those chips index, and the runtime that plays them. The owner said the package
"also ships a sample game" and treated it as outside the object; the manifest
says it is inside, it occupies **19 of the 256 files and 1,096,420 of the
6,607,311 stored bytes**, and nobody had checked.

**Groups 7, 8, 9, 10 and 11 are the stock library** — 209 files, 1,721,216
stored bytes, all of it MIDI, WAV and bitmap whose only purpose is to be put
into somebody else's game. The two sides of the product divide as
**1,721,216 stored bytes of stock content against 4,886,095 of editor, runtime,
help, sample game and backgrounds, and the two sum to 6,607,311** — the
manifest's own total, to the byte. That is what justifies a game-making tool appearing
in a game index, and it is an arithmetic justification rather than a rhetorical
one.

---

## And it is right about everything

The manifest's numbers were checkable only once `_SETUP.1` opened. All four
checks pass:

```
SETUP.PKG's 256 sizes equal _SETUP.1's stored sizes       6607311 = 6607311
SETUP.PKG names the same 256 files, in the same order     256 of 256
SETUP.PKG's group counts equal _SETUP.1's directory counts  12 of 12
```

**Two files, written by the same packer, read by two entirely separate code
paths in this repository, agreeing on a population of 256 in the same order.**
The manifest is not a summary of the archive; it is the same table written
twice.
