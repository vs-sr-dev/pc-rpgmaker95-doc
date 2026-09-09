# 06 — the installer: eighteen executables, five of them sixteen-bit, and a company that renamed itself inside one file

*Measure: `python tools/pecensus.py _work/members --by-magic` and `python
tools/ne.py` per file for the three visible ones; `python tools/is32.py list
_work/members/_INST32I.EX_` and `python tools/isz.py list
_work/members/_SETUP.LIB` for the other fifteen.*

---

## What the object shows before anything is opened

```
python tools/pecensus.py _work/members --by-magic
binaries : 3     NE16 3     PE : 0

SETUP.EXE   ISSET_SE  linker 5.60  segs 2  flags 0x0302  expects Windows 3.10
   "InstallShield Launcher SE v2.1 (C) InstallShield Corporation, Inc. 1990-1996"
_ISDEL.EXE  _DELIS    linker 5.60  segs 2  flags 0x0302  expects Windows 3.10
   "Deleter Process (c) Stirling Technologies, 1990-1995"
_SETUP.DLL  _SETUP    linker 5.60  segs 2  flags 0x8301  expects Windows 3.0
   "InstallSHIELD Resource DLL (c) Stirling Technologies Inc., 1990-1995"
```

Three files, 59,248 bytes, **0.8055 % of the members**, and until this session
they were the only code in the object anybody could read. The previous object
had seventeen PE and zero NE; this one shows three NE and zero PE, and both are
one command.

**All three belong to InstallShield.** Not one byte of RPG Maker is reachable
without opening a container.

---

## And what it holds

`_INST32I.EX_` is InstallShield's bootstrap. Its first eight bytes are `2a ab
79 d8 00 01 00 00`, and then, uncompressed, a copyright banner and a record
table:

```
python tools/is32.py list _work/members/_INST32I.EX_

banner      : Copyright (c) 1990-1995 Stirling Technologies, Inc. All Rights Reserve
            (70 bytes, no terminator, and it stops mid-word)
members     : 4

  rec at  installed as   shipped as         offset     stored   expanded
  82      INSTALL.EXE    _INS0432._MP          268     289709     674816
  129     LZWSERV.EXE    _INZ0432._MP       289977      11534      20656
  176     WUTL95i.DLL    _WUTL95.DLL        301511      16148      36864
  222     BOOT16.EXE     _INJ0432._MP       317659       2617       7168

  the record table ends where the first member's data begins  ok  268 = 268
  the members' offsets chain with no gap and no overlap       ok  4 of 4
  first offset + stored sizes = the file, residue 0           ok  320276 = 320276
```

**Each record carries two names**: what the file is called once installed and
what it is called on the disc. `_INS0432._MP`, `_INZ0432._MP`, `_INJ0432._MP` —
the three twelve-character strings that survive in a file of entropy 7.9645.

The payload is the **same PKWARE DCL implode** as the Z archive, and `blast` is
imported from `isz.py` rather than written twice. All four members expand to
their declared lengths and all four begin `MZ`:

```
python tools/is32.py extract _work/members/_INST32I.EX_ --out _work/inst32
INSTALL.EXE      289709 stored ->   674816 expanded   first two bytes MZ
LZWSERV.EXE       11534 stored ->    20656 expanded   first two bytes MZ
WUTL95i.DLL       16148 stored ->    36864 expanded   first two bytes MZ
BOOT16.EXE         2617 stored ->     7168 expanded   first two bytes MZ
4 of 4 members expanded to their declared length
```

| | bytes | format | |
|---|---:|---|---|
| `INSTALL.EXE` | 674,816 | **PE**, linker 3.0 | the 32-bit installer proper |
| `WUTL95i.DLL` | 36,864 | **PE**, linker 3.0 | |
| `LZWSERV.EXE` | 20,656 | **NE**, linker 5.60, expects Windows 3.0 | |
| `BOOT16.EXE` | 7,168 | **NE**, linker 5.60, expects Windows 3.10 | |

**The container that made the object look purely sixteen-bit is itself half
thirty-two.** A 16-bit `SETUP.EXE` starts, unpacks this, and hands over to a
32-bit `INSTALL.EXE`; `BOOT16.EXE` and `LZWSERV.EXE` are the sixteen-bit half of
the handover. That is the whole reason a 1996 installer looks like a Windows
3.1 program and installs a Windows 95 one.

`_SETUP.LIB` holds five more, all PE:

```
python tools/isz.py list _work/members/_SETUP.LIB

      #     stored   expanded     offset  date       time     name
      0       4384      19963        255  1999-07-12 01:27:30 SETUP.INI
      1      18333      91136       4639  1996-10-07 16:01:36 _ISRES.DLL
      2      10981      28160      22972  1996-07-22 15:54:36 _ISUSER.DLL
      3      25509      52736      33953  1996-12-19 17:34:34 _ISREG32.DLL
      4     124799     299008      59462  1996-11-05 16:13:22 UNINST.EXE
      5       4376      16259     184261  1996-09-30 13:23:14 CORECOMP.INI
      6      13634      27136     188637  1995-07-13 18:46:26 CTL3D32.DLL
      7       6592      12118     202271  1999-06-20 20:19:10 Logo.bmp
      8       1302       1967     208863  1999-07-12 00:12:50 readme.txt
      9      33356      49622     210165  1999-07-12 00:50:42 title.bmp
     10      36385      76978     243521  1999-07-12 01:13:06 setup1.bmp
```

`_ISRES.DLL`, `_ISUSER.DLL`, `_ISREG32.DLL`, `UNINST.EXE` and `CTL3D32.DLL` are
InstallShield's and Microsoft's; **`Logo.bmp`, `title.bmp`, `setup1.bmp` and the
19,963-byte `SETUP.INI` are the translator's**, stamped between 20 June and 12
July 1999. The 61-byte `SETUP.INI` in the ZIP is not this file: it is the
bootstrap's two-line stub, and the real one is 19,963 bytes and lives in here.

The eighteenth executable is `SETUP.EXE` at 112,888 stored bytes inside
`_SETUP.1`, which belongs to ASCII rather than to either installer
([03](03-the-manifest.md)).

---

## The company that renamed itself, inside one file

```
_SETUP.DLL   NE module description : InstallSHIELD Resource DLL
                                     (c) Stirling Technologies Inc., 1990-1995
_SETUP.DLL   version resource      : Copyright InstallShield Corporation, Inc.
                                     1990-1996
```

Stirling Technologies became InstallShield Corporation in 1996. **This one
6,128-byte file carries both names at once**: the NE description is written at
link time and was not regenerated, the version block was. One file, two names,
one company, and a year between the halves.

Across the object the two names split cleanly by date: `_ISDEL.EXE` (1995) and
`_INST32I.EX_`'s banner (1990-1995) say *Stirling*; `SETUP.EXE` (1996) says
*InstallShield Corporation*.

---

## The clock that is a telephone number

```
python tools/sift.py _work/members --group personal --show
telephone shape : 3 hits in 3 blobs

SETUP.EXE    (847) 240-9111    dated 1996-11-04
_SETUP.DLL   (847) 240-9111    dated 1996-09-30
_ISDEL.EXE   (708) 240-9111    dated 1995-09-07
```

The same seven digits behind two area codes. Illinois split 708 and gave the
northern suburbs — Schaumburg among them — **847**, effective January 1996. The
1995 file has the old code and the two 1996 files have the new one, and the
ordering is consistent.

**The area code dates the string, not the file.** A 1996 build could easily have
carried a stale 708 and this one does not; that is a fact about one vendor's
release discipline in one year, and it would be worth nothing as a rule. It is
reported here as a third clock that agrees with the other two, and no date is
derived from it.

---

## The banner that stops mid-word

`_INST32I.EX_`'s 70-byte banner reads `Copyright (c) 1990-1995 Stirling
Technologies, Inc. All Rights Reserve` — no terminator, and no `d`. The field
runs from `+0x08` to `+0x4D`, seventy bytes, and the member count begins at
`+0x4E`; the sentence it was meant to hold ends `Reserved.` and is seventy-two
characters. It is the smallest thing in the object and it is the only place
where somebody at the vendor counted wrong.
