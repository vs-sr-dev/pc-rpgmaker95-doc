# 14 — leftovers: what was not settled, and the expansions with their sources named

*Measure: everything here is stated as unmeasured or as derived from a named
source. Nothing in this chapter is used anywhere else in this repository as
evidence.*

---

## What was asked and answered

The pre-briefing listed six things that were "actually unknown". Five closed:

| | asked | answer |
|---|---|---|
| 1 | what is inside a Z archive, and is it PKWARE DCL | 256 / 11 / 1 files, and **yes**, shown by decompressing 272 of 272 to declared lengths ([04](04-the-archive.md)) |
| 2 | is `rpg95.exe` 16-bit or 32-bit | **32-bit PE**, Borland-linked ([05](05-the-product.md)) |
| 3 | what the 13,784 bytes are | 255 header + 207 directory table + 13,322 entry table, residue 0 |
| 4 | what `_INST32I.EX_` is | a four-member container, same codec, residue 0 ([06](06-the-installer.md)) |
| 5 | is `SETUP.INS` stock or the translator's | **stock**: it holds one 206,269-byte member, dated 1996-12-19 17:19:54, two seconds before its own ZIP stamp and two and a half years before the translator's work |
| 6 | what to do about the e-mail address | decided, argued and implemented ([10](10-whose-bytes.md)) |

---

## What is left

**The compiled setup script.** `SETUP.INS`'s single member, 206,269 bytes,
**1.0090 % of the recovered bytes**, is InstallShield's compiled script
language. It came out of the Z archive whole and at its declared length and was
not parsed. It is the only thing in the object that was opened and then set
down. What would settle it is a grammar for InstallShield 3's compiled `.INS`,
which nobody has published either.

**`RPGMakr95-409`.** At offset `0x0B747D` of `rpg95.exe`, a name followed by
forty-two hyphens. `0x0409` is Microsoft's language identifier for English
(United States), which is a tempting reading — and the same file's version
resource declares `0x0411`, Japanese, so the object contradicts it. Not settled.

**The version of the translation.** The readme says *"Version of Translation is
in the About Window (in GAME.EXE too!!!)"* and gives it as `1.0b`. The literal
string appears **three times in the object and all three are the readme**. Not
one of the 272 recovered files contains it. Either the dialogue builds the
string from pieces or it says something else, and settling it means
disassembling a resource dialogue, which this session did not do.

**The six bytes after the archive's name.** `SETUP.PKG`'s trailer ends
`01 01 0a 00 00 00`, and Microsoft FrontPage 98's ends **identically**. Two
specimens, one constant. That is not a field whose meaning has been recovered;
it is a constant observed twice, and it is written down as that.

**The unnamed integers.** The Z archive header has legible fields at `+0x0C`,
`+0x0E`, `+0x10`, `+0x12`, `+0x16`, `+0x1A`, `+0x29`, `+0x2D`, `+0x31`, `+0x33`
and `+0x37`, and unnamed ones at `+0x04` (314 on 4 of 4 specimens), `+0x06`
(2 on 4 of 4) and `+0x1A` (255 on 4 of 4, and it equals the first member's
offset on all four, which may be causation or may be a constant that happens to
be the header length). Each entry record has 4 unnamed bytes at `+0x19` and 12
at its tail. `is32.py`'s records have 8 unnamed bytes. All of them are printed
by the tools as integers and none is used to decide anything.

**The 1997 dates and their time zone.** 116 of the 256 entries carry 1997 dates
from ASCII's build. They are DOS timestamps and carry no zone. They are almost
certainly Japanese local time and "almost certainly" is not a measurement
([07](07-the-clocks.md)).

**Whether `pc-clic11-doc`'s InstallShield is the same *version*.** Two
byte-identical `_ISDEL.EXE` prove the same toolkit family. FrontPage's `DATA.Z`
needed the sixteen-bit table-length repair and this object's three did not,
which is a difference in scale rather than in format. The version numbers of the
two toolkits were not compared.

---

## The expansions, and which are demonstrated

The brief asked for the abbreviations, with each one marked by how it is known.
**Demonstrated from the object** means a byte in this object shows it;
**derived** means it follows from measurements here; **attributed** means a
public fact named with its holder; **not demonstrated** means neither.

| | expansion | how |
|---|---|---|
| `IS` | InstallShield | **demonstrated** — the NE descriptions and version resources spell it |
| `ISZ` / `.Z` | the archive's own extension; the manifest's trailer names the file `_SETUP.Z` | **demonstrated** |
| `.1` | **volume number**, not an ordinal or a part | **derived** — every entry in `_SETUP.1` carries volume 1 and all 2,419 entries in every other Z archive carry 0 ([03](03-the-manifest.md)) |
| `PKG` | package — the file manifest | **derived** — it is a manifest; the word is not in the object |
| `INS` | the compiled setup script | **derived** — the Z archive named `SETUP.INS` holds one member also named `SETUP.INS` |
| `LIB` | library — the installer's own support files | **derived** — its 11 members are `_ISRES.DLL`, `_ISUSER.DLL`, `_ISREG32.DLL`, `UNINST.EXE`, `CTL3D32.DLL` and the translator's bitmaps |
| `DIZ` | *description in zip*, the BBS file-description convention | **attributed** — a convention of the period, not stated in the object |
| `NE` | New Executable | **attributed** to Microsoft's format documentation; `ne.py` reads it |
| `PE` | Portable Executable | **attributed**, same |
| `DCL` | Data Compression Library, PKWARE's | **derived** — the codec is identified by decompressing, and PKWARE's name is in `SETUP.EXE` as a hint only ([04](04-the-archive.md)) |
| `LHA` | the Japanese archive format | **demonstrated** — `unlha32.dll`'s `FileDescription` is *LZH file extracting library*, and `rpg95.exe` builds `u -jn0 %srpgtmp.lzh` |
| `RTP` | Run Time Package | **not demonstrated** — the string does not occur in this object at all |
| `ATR` | attributes, of a map chip | **derived** — `MCHIP0.ATR`..`MCHIP3.ATR` are 256 bytes each and sit beside `MCHIP0.BMP`..`MCHIP3.BMP`; 256 is one byte per tile |
| `MCHIP` | map chip | **derived** — from the pairing above and from RPG Maker's tile-based editor, which the readme calls *Map/Area Definition* |
| `EPARTY` | the party — `EPARTY.DAT`, 604 stored bytes, Group2 | **not demonstrated** |
| `EVE` | event — `EVE99999.DAT` | **demonstrated** — the readme says *"Just delete EVExxxx.DAT file!"* under a bug about the *"If then... branch event"* |
| `DML` | the packager's initials, in `DISK1.ID` | **derived** — five bytes reading `DML` where a serial would go, beside an author who signs himself *Don Miguel* |
| `BMV` | the local part of the address, and the third alias in the signature | **demonstrated** — *Don_Miguel aka BMV aka …* |
| `SE` in *Launcher SE* | not established | **not demonstrated** |
| `ISSET_SE` | the NE module name of `SETUP.EXE` | **demonstrated** as a name; its expansion is **not demonstrated** |
| `_DELIS` | the NE module name of `_ISDEL.EXE`, and it is `ISDEL` reversed around the underscore | **derived** |
| `_MP` in `_INS0432._MP` | not established | **not demonstrated** |
| `KH` | KanjiHack | **demonstrated** — the readme uses both *"the KH translation"* and *"KanjiHack"* |
| `UIN` | the ICQ user identification number | **attributed** — a term of that service, not spelled out in the object |
| `409` | not established, and contradicted by `0x0411` in the same file | **not demonstrated** |

**Twenty-five expansions: six demonstrated from the object, nine derived, four
attributed to a public source, and six not demonstrated**, and the four counts
sum to twenty-five. `pc-iamsetsuna-doc/docs/15` had eight, six, three and
eleven, which sums to **twenty-eight** and is the number of rows in its table;
`prompt.txt` reports that split as being out of twenty-five
([13](13-corrections.md)).

Against twenty-eight rows this session is proportionally better on the
demonstrated end and much better on the not-demonstrated end — 24 % against
39 % undemonstrated — and the reason is that the containers opened: `.1`,
`ATR`, `EVE`, `LHA` and `_DELIS` all needed a byte that was not visible before.

---

## Sources named

Everything attributed above rests on public knowledge held outside the object,
and it is named here rather than smuggled into a chapter:

* **PKWARE's APPNOTE** for the ZIP structure, and the PKWARE Data Compression
  Library for the implode codec — the algorithm was implemented from its
  published description, not from any file here;
* **Microsoft's NE and PE documentation** for the executable formats, and
  Microsoft's language identifiers for `0x0411` and `0x0409`;
* **the Illinois area-code split of January 1996**, for the 708/847 clock;
* **Stirling Technologies' rename to InstallShield Corporation in 1996**;
* **ICQ's shutdown in June 2024**, which is load-bearing for the personal-data
  decision in [10](10-whose-bytes.md), and **`mail.ru`'s continued operation**,
  which is load-bearing for the other half of it.

**No network was used.** The URL inside the object was not visited and neither
was the mail domain.

---

## And the one thing the object cannot tell anybody

Whether it works. Rule 4 of this pipeline is that nothing is executed,
installed or emulated, and on an object that is an installer the temptation is
larger than it has ever been. **Nothing here was run.** Every statement about
what `rpg95.exe` does is a statement about strings, imports and resources in a
file that was decompressed and read.
