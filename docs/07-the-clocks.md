# 07 — the clocks: no time zone anywhere, and a readme that turns out to be right

*Measure: `python tools/mtimes.py _work/members --waves` for the twelve, and
the `date` and `time` columns of `notes/setup1-toc.tsv` — produced by `python
tools/isz.py list _work/members/_SETUP.1 --tsv` — for the 256 inside.*

---

## What kind of clock this is, before any of it is used

Every timestamp in this object is a **DOS timestamp**: a `u16` date and a `u16`
time, two-second granularity, local time, **no time zone and no offset field**.
The twelve members' file-system mtimes were restored onto the extracted files
from the ZIP's central directory, so they are the ZIP's numbers and not this
machine's, and that is a derivation and is said here rather than assumed.

The previous object derived UTC+9 to the second from a compiler banner paired
with a COFF link stamp. **There is nothing here to derive.** The 256 entries
inside `_SETUP.1` carry DOS timestamps too, and the six PE files carry COFF
`TimeDateStamp` fields that Borland's linker filled with values like
`0xA6812284` — which is 2058 — so they cannot be paired with anything. `pecensus`
reports `impossible mtimes : 0 of 0 datable binaries`, which is the correct
answer for a population where nothing is datable.

This chapter therefore reports local times with no zone attached, and says so
once here instead of hedging in every row.

---

## The seven waves, on twelve files

```
python tools/mtimes.py _work/members --waves

wave 1  1995-09-07 19:22:40                     1 file      8,192   0.11 %
wave 2  1996-09-30 08:06:54                     1 file      6,128   0.08 %
wave 3  1996-11-04 13:04:12                     1 file     44,928   0.61 %
wave 4  1996-11-05 16:17:32                     1 file    320,276   4.35 %
wave 5  1996-12-19 17:19:56                     1 file     66,661   0.91 %
wave 6  1999-07-12 00:12:50 .. 00:24:28         2 files     2,367   0.03 %
wave 7  1999-07-12 01:27:34 .. 01:29:08         5 files 6,906,176  93.90 %
```

Ten distinct timestamps over twelve members. Waves 1 to 5 are InstallShield's
toolkit shipped as it stood — one file each, fourteen months apart at the
extremes. Waves 6 and 7 are the translator's, **seventy-four minutes apart on
one night**, and wave 7 is the build: the script library, the ini stub, the
6.6-megabyte archive, the manifest and the disk id, written in **ninety-four
seconds**.

---

## The archive's own clock, which agrees three ways and then does not

Each Z archive carries a DOS date at `+0x0E` and a DOS time at `+0x10`.

```
             header date   ZIP date     header time  ZIP time
_SETUP.1     1999-07-12    1999-07-12   01:27:38     01:29:08
_SETUP.LIB   1999-07-12    1999-07-12   01:27:34     01:27:34
SETUP.INS    1996-12-19    1996-12-19   12:02:24     17:19:56
```

**The date agrees on 3 of 3. The time agrees on 1 of 3.** Those are two
different results and they are reported apart, because folding them together
would turn one confirmation into three.

The time field is legible enough for the two 1999 files to make sense: the
header is stamped when the packer starts and the ZIP when the file is closed,
and `_SETUP.1` took ninety seconds to write 6.6 megabytes while `_SETUP.LIB`
started and finished inside the same two-second tick. `SETUP.INS` is five hours
and seventeen minutes out and no story here accounts for it. **One of three is
one of three.**

---

## Thirty-one more dates, which the pre-briefing could not see

Every entry in `_SETUP.1` carries its own date and time. That is 256 clocks
that did not exist as measurements until the archive opened:

```
distinct dates : 31    range 1995-07-11 .. 1999-07-12

by year:   1995   1        the most common dates:
           1996  52          1996-11-20   52     1997-02-01  19
           1997 116          1999-06-21   47     1997-03-01  17
           1998   2          1997-01-31   21     1997-02-08  10
           1999  85          1999-06-29   20     1997-01-18   9
                             1997-01-19   19     1999-07-12   6
```

**One hundred and sixteen files from 1997 and eighty-five from 1999.** The 1997
block is ASCII's build of the program — and this is the only place in the object
where the *program's* year appears, which is why the pre-briefing's one-sentence
summary said 1995 and this repository's says 1997 ([01](01-the-object.md)).

The single 1995 file is `USER32.DLL`, 1995-07-11 09:50:00 — Windows 95 shipped
in August of that year, and a Japanese publisher was redistributing a
pre-release build of one of its DLLs.

The fifty-two files stamped **1996-11-20 18:06:36**, all within the same tick,
are the sound library: `ARROWHIT.WAV`, `ARRRG.WAV` and fifty more. A whole
resource library copied in one operation.

---

## The readme is not two weeks wrong

The pre-briefing's sharpest observation was that `readme.txt` dates itself

```
Don_Miguel aka BMV aka Mummy aka GrEeZlY aka Debilkuz aka Miguello
28-June-1999 00:43
```

while its ZIP timestamp says **1999-07-12 00:12:50** — fourteen days apart —
and that this is the only place in the object where a clock inside a file can be
checked against a clock outside it. It called it a check rather than a
discrepancy, and it was right to, because the archive settles it:

```
awk -F'\t' '$10=="game.exe"' notes/setup1-toc.tsv
index  stored  expanded   offset  vol  date        time      attrib chunk name
22     241493    504832  2358285    1  1999-06-28  00:32:20      32    51 game.exe
```

**`game.exe` is stamped 1999-06-28 00:32:20 and the readme is signed 28 June
1999 at 00:43.** Ten minutes and forty seconds apart, the same night, and the
readme is the later of the two. He finished the runtime, wrote the readme, and
packaged it a fortnight afterwards.

Fourteen days is not an error in a text file. It is the gap between finishing
the work and shipping it, and the object contains a second witness for the
earlier date that nobody could see until 6.6 megabytes came apart.

`FILE_ID.DIZ` dates itself `12-07-99` inside its frame and agrees with its own
ZIP stamp to the day. **Two text files, two self-declared dates, and both are
now corroborated by something other than themselves.**

---

## The translator's own working week

Filtering the 256 entries to 1999 gives the shape of the job:

```
1999-06-20 20:19:10   Logo.bmp        (in _SETUP.LIB)
1999-06-21 22:57:54   MCHIP0.BMP .. MCHIP3.BMP        47 files this day
1999-06-28 00:32:20   game.exe
1999-06-29 22:17:24   BG01.BMP .. BG19.BMP            20 files this day
1999-07-10 23:57:00   MCHIP0.ATR .. MCHIP3.ATR
1999-07-11 22:17:24   chara.bmp
1999-07-11 22:38:26   STRINGS.DAT
1999-07-11 22:55:28   ITEM.DAT
1999-07-11 22:59:36   MAGIC.DAT
1999-07-11 23:01:38   EVE99999.DAT
1999-07-12 00:12:50   readme.txt
1999-07-12 00:45:58   rpg95.exe
1999-07-12 01:23:46   rpg95.hlp
1999-07-12 01:27:34   the build begins
1999-07-12 01:29:08   the build ends
```

**Eighty-five of the 256 files carry a 1999 date**, and they are almost all
evenings and nights: 20:19, 22:57, 22:17, 23:57, 00:32, 01:23. The last hour is
continuous — the readme at 00:12, the editor at 00:45, the help file at 01:23,
the archive closed at 01:29 — and then it was over.

**And the two files everything else waited for are `rpg95.exe` and
`rpg95.hlp`**, written 00:45:58 and 01:23:46, thirty-eight minutes apart, on the
last night. The executable and its help text are the translation.

---

## What the clocks still cannot say

* **when the object was downloaded.** The file's own mtime on this machine is
  2026-09-09 and there is no second witness for it. It is not reported as a
  fact about the object;
* **any time zone.** Every date above is local to a machine whose location the
  object never states. The CP866 line in the readme and a `mail.ru` address
  make a guess available and this repository does not make it;
* **whether ASCII's 1997 dates are Japanese local time.** They almost certainly
  are, and "almost certainly" is not a measurement.
