# 08 — the text: two thousand four hundred and thirty-three bytes that carry the whole provenance, and one line in a Russian DOS codepage

*Measure: `python tools/cptext.py selftest` — 6 checks — then `census` and
`decode` on each of the four text members. The e-mail address quoted from these
files is redacted; the decision and the rule behind it are
[10](10-whose-bytes.md).*

---

## Four files, 2,433 bytes

| file | bytes | ≥ 0x80 | distinct | what it is |
|---|---:|---:|---:|---|
| `readme.txt` | 1,967 | 33 | 18 | the document |
| `FILE_ID.DIZ` | 400 | 49 | 7 | a BBS file description |
| `SETUP.INI` | 61 | 0 | 0 | the bootstrap's two lines |
| `DISK1.ID` | 5 | 0 | 0 | `DML` and a CRLF |

They are 0.0331 % of the members and they contain every fact about where this
object came from.

---

## `SETUP.INI` and `DISK1.ID`

```
[Startup]
AppName=RPG Maker 95+ (Translated by Don Miguel)
```

```
DML
```

**Where a commercial product puts a serial number, this one puts three
letters.** `DISK1.ID` is InstallShield's disk identifier and its contents are
the packager's initials. Five bytes, and one of them is a carriage return.

(The 61-byte `SETUP.INI` in the ZIP is the bootstrap stub. The real one, 19,963
bytes, is inside `_SETUP.LIB` — see [06](06-the-installer.md).)

---

## `FILE_ID.DIZ`, and a codepage the object cannot decide

```
python tools/cptext.py decode _work/members/FILE_ID.DIZ --cp cp437 --whole

┌────═══[ Don Miguel Presents ]═══───┐
│                                    │
│  ASCII's RPG Maker 95+ (1.02 beta) │
│                                    │
│      Translated by  Don Miguel     │
│                                    │
│   CD-RIP and basic translation by  │
│             KanjiHack              │
│                                    │
└─[12-07-99]──────────────[wIN95/98]─┘
```

A `FILE_ID.DIZ` is what a bulletin board displayed beside a file, and its
presence dates the distribution channel as surely as the timestamps date the
build.

**But the codepage is not decidable from the bytes, and the pre-briefing said
CP437 as though it were:**

```
python tools/cptext.py census _work/members/FILE_ID.DIZ

bytes >= 0x80  : 49
distinct values: 7
  0xb3 0xbf 0xc0 0xc4 0xcd 0xd9 0xda
all of them in the CP437/CP866 shared box-drawing range 0xB0..0xDF : YES
   -- the two codepages cannot be told apart here
```

CP437 and CP866 are **identical** on `0xB0`..`0xDF`, which is the whole
box-drawing block, and all forty-nine of this file's high bytes are in it. The
picture above is the same picture under either. Given that the same author's
readme is CP866, CP866 is at least as likely as CP437 — and it does not matter,
which is exactly why the claim should not be made. What the bytes support is
*box drawing in the range the two codepages share* ([13](13-corrections.md)).

---

## `readme.txt`, and the line that is decidable

```
python tools/cptext.py census _work/members/readme.txt

bytes >= 0x80  : 33
distinct values: 18
  0x84 0x90 0x93 0x97 0xa0 0xa3 0xa5 0xa7 0xa8 0xa9 0xaa 0xad
  0xe1 0xe2 0xe3 0xe7 0xeb 0xef
all of them in the shared box-drawing range : no
lines carrying a high byte : 1 of 51
  line 48   33 high bytes
```

**Thirty-three bytes on one line of fifty-one**, none of them in the shared
range, so this file's codepage *is* decidable — and the tool shows the four
candidates rather than asserting one:

```
python tools/cptext.py decode _work/members/readme.txt

line 48, 33 high bytes:
  cp437    *** ôτ¿ΓÑ Éπßß¬¿⌐ ∩ºδ¬!!! ù¿Γá⌐ΓÑ ¬¡¿ú¿! äáπ¡δ!!! ***
  cp866    *** Учите Русский язык!!! Читайте книги! Дауны!!! ***
  cp1251   *** “зЁвҐ ђгббЄЁ© п§лЄ!!! —Ёв ©вҐ Є­ЁЈЁ! „ г­л!!! ***
  latin-1  *** ç¨â¥ ãááª¨© ï§ëª!!! ¨â ©â¥ ª­¨£¨!  ã­ë!!! ***
```

**CP866**, and only CP866. *"Learn Russian!!! Read books! Morons!!!"*

A file that is ASCII for fifty lines and one sentence of Cyrillic in a DOS
codepage tells you who wrote it and what he assumed his readers had installed.
It is one `.decode('cp866')` and it is the only place in 7.3 megabytes where
the author writes in his own language — to insult the audience he is doing the
favour for.

---

## The chain of custody, in the translator's words

The readme is the object's real documentation and it says everything:

> This is a full installation of RPG Maker 95+ / 100% English Version
> (translated by Don Miguel) / (Version of Translation: 1.0b)

> 1) The 100% English version! (RPG95.EXE, GAME.EXE, RPG95.HLP)
> 2) Fixed SOME!!! context mistakes in the KH translation
> 3) Full translation of EventEditor, MonstrEditor, ItemEditor, Map/Area
> Definition, GAMEDISK Maker (You can make GD on the 1.44" floppy disks
> now!!!), MagicEditor, TextEditor, Default Strings, Character's Names, etc.

> Known bugs:
> 1) Wrong property window for "Play Movie" (KanjiHack did it when translating
> the RPG95.EXE ver 6. It've not been in old untranslated jap. file)

> Big Thanx to ASCii Co, TNomad of KanjiHack, Aspetra!

**Three parties, in a hierarchy of credit and blame.** ASCII Corporation made
it. KanjiHack ripped it from CD and did a rough translation — and introduced a
bug, which is attributed to them by name. Don Miguel finished it. *"the KH
translation"* and *"RPG95.EXE ver 6"* are two more references to a prior
version this object does not contain.

Every clause of that is corroborated elsewhere in the object:

| the readme says | the bytes say |
|---|---|
| RPG95.EXE, GAME.EXE, RPG95.HLP were translated | all three are in the manifest; `rpg95.exe` carries `FileVersion 1.02` |
| "Version of Translation: 1.0b" | **not corroborated** — see below |
| "get the translated STRINGS.DAT" | `STRINGS.DAT`, 1,057 stored bytes, Group3 |
| "Just delete EVExxxx.DAT file!" | `EVE99999.DAT`, 306 expanded bytes, Group2 |
| "18 Mb of free space at your HDD" | `_SETUP.1` declares **18,821,193** expanded bytes at `+0x16` |
| "I got a new version (ver 1.23)" | `game_engl_123.exe`, `ProductVersion "ver 1.23"`, appended as record 255 |
| ASCII made it | six version resources say *ASCII Corporation, 1997* |
| dated 28-June-1999 00:43 | `game.exe` stamped 1999-06-28 **00:32:20** |

**Eight claims in a text file, seven of them confirmed by something that is not
a text file**, and most of that confirmation was inside an undocumented
container.

**The eighth is the one the readme is loudest about.** It says *"Version of
Translation is in the About Window (in GAME.EXE too!!!)"*, and the string is not
there:

```
occurrences of '1.0b' across every recovered layer : 3 in 3 files
   _work/product    000_readme.txt   1
   _work/lib        000_readme.txt   1
   _work/members    readme.txt       1
```

Three hits and all three are the same 1,967-byte readme in its three copies.
Not one of the 272 recovered files contains the literal `1.0b`. Either the About
box builds it from pieces, or it says something else; this session did not
disassemble the dialogue and does not know which ([14](14-leftovers.md)).

---

## There is no protection here; there is a crime

```
python tools/protscan.py _work/members
files searched : 3 of 12   bytes : 59,248 of 7,354,728
0 hits on eleven markers; the positive control fires on 3

python tools/protscan.py _work/product
0 hits on eleven markers; the positive control fires on 6
```

Fourteenth appearance of `protscan.py`'s filtered denominator, and the worst
ratio it has had: on the members it examines **0.8055 %** of the object. Pointed
at the recovered product it examines six files of 256 and still finds nothing,
which is the right answer for eleven pre-2010 optical-media schemes aimed at a
1997 Japanese application.

**The object is not protected. It is the output of removing somebody else's
protection, and it says so in its own documentation:**

> CD-RIP and basic translation by KanjiHack

> P.S. I got a new version of RPG Maker 95 (ver 1.23). **I almost cracked it
> now.** And may be I'll translate it too.
> P.P.S. **I'm working hard for UnlimitedTilesets crack!**

And the disc check it was ripped from is still in the program, in the clear, at
a byte offset:

```
Please Insert RPG Maker 95 CD-ROM, While holding the Shift key down.
```

A string a program keeps and never prints. Every protection chapter this
collection has written measures a scheme that was working; this one measures
the message the scheme would have shown, preserved inside the thing that no
longer shows it.

---

## The one thing outside the object

```
http://www.chat.ru/~rpgmaker
```

A tilde-user page on a Russian free-hosting service that closed years ago. It
appears four times across three layers — in the readme, inside `rpg95.exe`, and
in the copies of the readme in both containers. **No network was used and none
should be**: the URL is evidence about 1999, not an address to visit.
