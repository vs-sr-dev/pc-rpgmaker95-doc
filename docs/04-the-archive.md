# 04 — the archive: 94.7453 % of the object, no specification, and it closes at residue 0 in four places

*Measure: `python tools/isz.py selftest` — 13 checks, three accepted specimens
and ten rejected ones — then `python tools/isz.py list`, `verify` and `extract`
against the three Z archives, and against Microsoft FrontPage 98's `DATA.Z` in
`pc-clic11-doc`, which this repository did not make and cannot have tuned
itself to.*

---

## The starting position

One magic number, `13 5d 65 8c` at offset 0, on three of the twelve members —
`_SETUP.1` (6,621,095), `_SETUP.LIB` (280,502) and `SETUP.INS` (66,661),
6,968,258 bytes between them, **94.7453 % of the members**. Entropy 7.9384,
7.9744 and 7.9424. No published specification. No vendor string anywhere
inside. Nothing in `tools\` that could read a byte of it.

And two integers that behaved: a count at `+0x0C` reading 256 / 11 / 1, and a
DOS date at `+0x0E` agreeing with each member's own ZIP date on 3 of 3.

**That is the position `pc-iamsetsuna-doc/docs/16` said to price on** — not *is
it documented*, but *does it state a quantity the reader does not control*. It
stated two before anything was opened. It turned out to state seven.

---

## The header, derived

```
python tools/isz.py header _work/members/_SETUP.1

+0x0C file count: 256
+0x0E date      : 0x26EC  1999-07-12
+0x10 time      : 0x0B73  01:27:38
+0x12 arch size : 6621095   (file is 6621095)
+0x16 unnamed   : 18821193
+0x1A           : 255
+0x29 toc at    : 6607566
+0x2D toc len   : 207
+0x31 dir count : 12
+0x33 entries at: 6607773
+0x37 entry len : 13322
first data at   : 255
```

The two tables and the two lengths were found by the only method available: a
`u32` inside the first sixty bytes that lands inside the file and near its end
is an offset, and the byte it lands on is either a plausible record or it is
not. The one at `+0x29` lands on `05 00 11 00 06 00 "Group1"` — a count of 5,
a chunk size of 17, a name length of 6, and a name the manifest also uses. From
there everything followed.

```
directory record :  u16 file count, u16 chunk size, u16 name length,
                    name, NUL, padding to the chunk size
entry record     :  u8 volume, u16 index, u32 expanded size, u32 STORED size,
                    u32 offset, u16 DOS date, u16 DOS time, u32 attributes,
                    u16 chunk size, 4 unnamed bytes, u8 name length,
                    name, NUL, 12 unnamed bytes -- total = the chunk size
```

Nine of twelve directory chunks are 17 bytes and three are 18: `Group1`..`Group9`
are six characters and `Group10`..`Group12` are seven, and 9 × 17 + 3 × 18 =
**207**, which is what `+0x2D` declares. The entry records are 43 bytes plus the
name; the 256 names run to 2,314 characters; 256 × 43 + 2,314 = **13,322**,
which is what `+0x37` declares.

**The first derivation was wrong and the tool said so on the first run.** The
record was built as 31 fixed bytes plus the name and an assertion in the
specimen builder fired with `AssertionError: (48, 49)` before a single real
byte was read. The name length sits at `+0x1D`, not `+0x1E`
([13](13-corrections.md)).

---

## The thirteen thousand seven hundred and eighty-four bytes

This was the pre-briefing's first hard question: `SETUP.PKG` declares
6,607,311 bytes of content and `_SETUP.1` weighs 6,621,095, and the difference
is 13,784. It is one subtraction, and the answer is that it is three additions:

```
python tools/zaccount.py --zip … --members _work/members

_SETUP.1   256 members  255 + 6607311 + 207 + 13322 = 6621095, file 6621095
    _SETUP.1 closes at residue 0    ok
```

```
       255   the header, and the first member's data begins there
 6,607,311   the members, laid end to end -- exactly the manifest's total
       207   the directory table, 12 records
    13,322   the entry table, 256 records
 ---------
 6,621,095   the archive, which is what +0x12 declares and what the file weighs

       255 + 207 + 13,322 = 13,784
```

**The manifest's `u32` size field is the member's STORED size, not its expanded
one.** That had to be true before it was checked: the ZIP finds only 3 % on
`_SETUP.1`, so its contents are already compressed, and a body of MIDI, bitmaps
and executables cannot be both compressed and 13,784 bytes short of its own
expanded total. The archive's entry table settles it — the offsets chain from
255 by the stored sizes and land on the directory table to the byte, and those
stored sizes are the manifest's numbers, all 256 of them.

The expanded total is a different number and the archive declares that too:

```
+0x16 = 18,821,193 = the sum of the 256 expanded fields
```

**A field the pre-briefing listed as unnamed is the archive's own uncompressed
size.** The readme, written by a man who never saw this field, says the
installation needs *"18 Mb of free space at your HDD"*. 18,821,193 bytes is
17.95 MiB.

---

## The seven closures

```
python tools/isz.py list _work/members/_SETUP.1

  the members' offsets chain with no gap and no overlap  ok  256 of 256
  the last member ends exactly at the directory table    ok  6607566 = 6607566
  header + data + both tables = the archive, residue 0   ok  residue 0
  the directory file counts sum to the file count        ok  256 against 256
```

plus the declared archive size against the file length, the two table lengths
against the records that fill them, and — from `verify` — every member's
expanded length against the field its own entry declares. **Seven quantities
the format states about itself, and a reader that lands on all seven.**

`_SETUP.LIB` and `SETUP.INS` close the same way:

```
_SETUP.LIB   11 members  255 + 279651 + 11 + 585 = 280502, file 280502
SETUP.INS     1 members  255 +  66343 + 11 +  52 =  66661, file  66661
```

Both have **one** directory whose name is the empty string — an 11-byte chunk,
which is the 11 bytes a zero-length name leaves. `SETUP.INS` holds one member,
itself called `SETUP.INS`, 206,269 bytes expanded: the compiled InstallShield
script, which this session did not open and does not claim to have.

---

## The compression, identified by decompressing rather than by quoting

`SETUP.EXE` contains the string `Copyright 1990-92 PKWARE Inc. All Rights
Reserved.` That is a hint about which compressor InstallShield licensed. **It is
not a measurement, and it is not the evidence used here.** The evidence is that
a PKWARE Data Compression Library *implode* decoder, written from the algorithm
and not from any file in this object, expands every member to the length the
archive independently declares for it:

```
python tools/isz.py verify _work/members/_SETUP.1 --all

members tried  : 256 of 256
EXPANDED LENGTH MATCHES THE DECLARED FIELD : 256 of 256
refused or mismatched                      : 0 of 256

first two bytes of the expanded members:
  'MT'   MT     102        'MZ'   MZ       6
  'BM'   BM      75        '?_'   ?_       2
  'RI'   RI      55        others         16
```

**256 of 256**, and the magic numbers of the output match the manifest's
extension census exactly: 102 files named `.MID` and 102 beginning `MThd`, 75
named `.BMP` and 75 beginning `BM`, 55 named `.WAV` and 55 beginning `RIFF`, 6
named `.EXE` or `.DLL` and 6 beginning `MZ`. Two censuses, one from names in a
manifest and one from bytes out of a decompressor, over the same 256 files.

### And the check that cost nothing

`readme.txt` is a ZIP member at 1,967 bytes, sha1
`260e355d3d8dec82a3bee081002f748c5352096c`. It is **also** the fifth member of
`_SETUP.1` and the ninth member of `_SETUP.LIB`:

```
readme.txt in the ZIP        : 1967 bytes  260e355d3d8dec82a3bee081002f748c5352096c
000_readme.txt (_SETUP.1)    : 1967 bytes  260e355d3d8dec82a3bee081002f748c5352096c
000_readme.txt (_SETUP.LIB)  : 1967 bytes  260e355d3d8dec82a3bee081002f748c5352096c
```

**The output of an undocumented decompressor is byte-identical, twice, to the
output of `deflate` on a different stream.** No length check, no plausibility
argument, no eyeballing: a hash. That is the single strongest piece of evidence
in this repository and it was sitting there for free.

---

## The control that this repository did not build

A reader that only ever meets the object it was written for has proved
nothing about the format. `pc-clic11-doc` holds an entirely different
InstallShield 3 product — **Microsoft FrontPage 98**, packaged by Microsoft in
July 1997, twenty-one megabytes:

```
python tools/isz.py list ../pc-clic11-doc/_work/iso/FP98/DATA.Z

declared    : 2399 files in 108 directories
  the members' offsets chain with no gap and no overlap  ok  2399 of 2399
  the last member ends exactly at the directory table    ok  20852252 = 20852252
  header + data + both tables = the archive, residue 0   ok
      255 + 20851997 + 2852 + 131215 = 20986319 against 20986319, residue 0
  the directory file counts sum to the header's count    ok  2399 against 2399

python tools/isz.py verify ../pc-clic11-doc/_work/iso/FP98/DATA.Z -n 40
EXPANDED LENGTH MATCHES THE DECLARED FIELD : 40 of 40
```

**Two thousand three hundred and ninety-nine files, residue 0, no change to the
reader.** And FrontPage's own `SETUP.PKG` declares 20,851,997 stored bytes —
which is the same number `DATA.Z`'s entry table produces, in a product this
session had no hand in.

`pc-clic11-doc/docs/13` reported its two InstallShield `.Z` files as
*"21,394,515 bytes, not declared"* and said what was inside them was unknown.
It is 2,399 files in 108 directories with paths like `themes\global` and
`pages\feedback.tem`, and it was one command away the whole time.

### The refusal that came first, and the field that is sixteen bits

`DATA.Z` did **not** open on the first attempt:

```
isz: REFUSED: entry record at 20855214 declares a chunk of 55, which does not
     hold a 12-byte name inside the table
```

The entry table is declared by a `u16` at `+0x37`, and FrontPage's entry table
is 131,215 bytes:

```
archive_size - entry_offset = 131215      declared u16 = 143
131215 mod 65536 = 143
```

**The field overflowed, twice.** The reader now uses the length the archive size
fixes, and only when the declared value is congruent to it modulo 65,536 —
which is exactly what a truncated 16-bit field looks like and is not a licence
to ignore the field. On all three of this object's archives the two agree
exactly, and the repair changes nothing here; on FrontPage's it is the
difference between a refusal and 2,399 files.

**A format whose file count is a `u16` and whose entry-table length is also a
`u16` can hold about 1,500 files before it can no longer describe itself.**
InstallShield shipped past that, and the extractor presumably walks by count
rather than by length, so nobody noticed.

---

## What is still shut

`SETUP.INS`'s single 206,269-byte member is InstallShield's compiled setup
script. It came out of the Z archive intact and at the declared length, and
this session did not parse it. That is 206,269 bytes of the 20,442,049
recovered — **1.0090 %** — and it is the only container-shaped thing here that
was opened and then left alone ([14](14-leftovers.md)).
