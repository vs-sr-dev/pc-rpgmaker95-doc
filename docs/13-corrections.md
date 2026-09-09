# 13 — corrections: twelve in the brief and seven of this session's own

*Measure: each entry names the file and the line that is wrong and the command
that produces the right figure. The pre-briefing flagged no corrections of its
own, which is why they had to be found rather than read.*

---

## In `prompt.txt` and `_pre\`

**1. The entropy table has ten single-file rows, not nine.**
`prompt.txt` warns against "una tabella per estensione su popolazioni di uno —
nove delle undici righe dell'entropia hanno un solo file dentro". The table has
eleven rows over twelve files and only `.EXE` holds two, so **ten** rows hold
exactly one. The warning is right and its arithmetic is not.

```
python tools/entropy.py _work/members --tree --by-ext
.1 1   .EX_ 1   .LIB 1   .INS 1   .EXE 2   .DLL 1
.PKG 1   .TXT 1   .DIZ 1   .INI 1   .ID 1
```

**2. `USER32.DLL` is Windows 95's `USER32.DLL`.**
`_pre/executable.txt` says it "is **not** Windows 95's `USER32.DLL`, which is
around 40 times that", and calls the 21,223-byte entry "either a 16-bit thunk,
a stub, or a mistake". Its version resource says otherwise:

```
python tools/verres.py dump _work/product
000_USER32.DLL
    CompanyName        Microsoft Corporation
    FileDescription    Win32 USER32 core component
    FileVersion        4.00.950
    ProductName        Microsoft Windows Operating System
```

`4.00.950` is Windows 95's retail build. On Windows 95 `USER32.DLL` thunks down
to the 16-bit `USER.EXE` and holds little code of its own, so forty-odd
kilobytes is its right size — 44,544 expanded, from 21,223 stored. The
briefing's reasoning was about Windows NT.

**3. `_INST32I.EX_`'s signature is stated in a different convention from the Z
archive's, and the two are given as though they matched.**
The brief writes the Z archive as `0x8C655D13` — the little-endian `u32` of the
bytes `13 5d 65 8c` — and `_INST32I.EX_` as `0x2AAB79D8`, which is the bytes
`2a ab 79 d8` read left to right. As a `u32` the second is `0xD879AB2A`. Both
appear in the same table in `_pre/formats.txt` and only one is a `u32`.

```
python tools/is32.py list _work/members/_INST32I.EX_
signature   : 2a ab 79 d8   as a little-endian u32 0xD879AB2A
              as the bytes read left to right 0x2AAB79D8
```

**4. `SETUP.PKG`'s first four bytes are not a magic number.**
`_pre/formats.txt` gives `u32 magic 0x118BA34A`. FrontPage 98's manifest begins
`0xC068A34A`. Only the low half is constant, and the high half is the value at
`+0x0A` plus 14 on both specimens ([03](03-the-manifest.md)).

**5. `FILE_ID.DIZ`'s codepage is not decidable from the bytes.**
The brief calls it CP437 four times. All 49 of its high bytes lie in
`0xB0`..`0xDF`, where CP437 and CP866 are identical, so the object cannot
distinguish them — and given the author's readme is CP866, CP866 is at least as
likely.

```
python tools/cptext.py census _work/members/FILE_ID.DIZ
all of them in the CP437/CP866 shared box-drawing range 0xB0..0xDF : YES
```

**6. The e-mail address is not "on a service that no longer exists".**
`prompt.txt` frames the personal-data decision around an address published
"ventisette anni fa, su un servizio che non esiste più". The service that no
longer exists is `chat.ru`, which hosted the URL. `mail.ru` is an operating
consumer mail service, and that difference is the whole basis of the decision
in [10](10-whose-bytes.md) — the address would still deliver.

**7. The four `.TXT` files in the manifest are four copies of one name.**
`_pre/formats.txt` reports "TXT 4" and names `readme.txt` once. All four records
are called `README.TXT`, at 1,302 / 172 / 73 / 163 bytes in groups 2, 11, 12 and
12, and the manifest holds **251 distinct names over 256 records** — a figure the
brief does not give.

**8. The fourth executable in the manifest is named.**
`_pre/formats.txt` says "The four executables are `rpg95.exe`, `game.exe`,
`game_engl_123.exe` and one more". It is `SETUP.EXE` at 112,888 bytes, alone in
Group5, and it is **ASCII's**, not InstallShield's — a different file from the
44,928-byte `SETUP.EXE` beside it in the ZIP.

**9. The sample game is in the object, and the error has a known provenance.**
`_pre/provenance.txt` states "It also ships a sample game, which is *not* part
of this object and is not analysed here", and `_pre/question.txt` says whether
any of the 256 entries is one "is a question the manifest can answer and nobody
has asked it". The manifest answers yes: Groups 2, 3 and 4, nineteen files,
3,210,511 expanded bytes ([05](05-the-product.md)). The first statement is an
assertion the second one contradicts.

**Where it came from is the useful part.** The abandonware page the object was
downloaded from lists a *Sample game* as a separate item beside the package,
and the owner reported that listing. **That observation is correct and it is
about a catalogue, not about a file.** Both things can be true at once — the
site may well offer some other sample project separately, and this package
contains one anyway — so the premise was never wrong. What was wrong was the
negation drawn from it.

**A negative claim about contents cannot be derived from a positive claim about
a distributor.** "There is a separate sample game" is a fact about a shop;
"which is not part of this object" is a fact about 6,607,311 bytes, and only the
bytes can settle it. This collection already applies exactly that rule to Steam:
an `appmanifest` says what the shop delivers and the files say what is there.
Here the shop was an abandonware index and it beat the object's own manifest for
a whole session, over a question that was one `awk` away in a file that had
already been walked end to end.

**The prescription is a label, not more work.** A pre-briefing carries the
owner's framing and that framing is load-bearing — two of this owner's three
statements are confirmed by the bytes, one of them three times over
([08](08-the-text.md)). What it lacks is a mark separating *what is known about
the object* from *what is known about where the object came from*, because the
two arrive in the same prose and the second one won.

**10. `crossall.py` needs `--skip` and the brief does not say so.**
The pre-briefing's `0 of 1` was obtained before this repository had a `notes/`
directory. Run afterwards without `--skip pc-rpgmaker95-doc`, the object matches
its own published hash list and the tool reports **1 of 1**
([11](11-against-the-collection.md)).

**11. The `+0x16` field of the Z archive header is not unnamed.**
`_pre/formats.txt` lists the sixteen-byte header and says two of its fields are
legible. `+0x16` is a `u32` holding **18,821,193**, which is the sum of the 256
expanded sizes 6.6 megabytes away — the third self-checking quantity, and the
one that matches the readme's "18 Mb".

**12. The previous session's expansion table has twenty-eight rows, not
twenty-five.** `prompt.txt` reports it as "su venticinque ne sono state
dimostrate otto dall'oggetto, sei derivate, tre attribuite a una fonte pubblica
e undici non dimostrate". Those four counts sum to 28, and 28 is what the
chapter holds:

```
grep -c '^| `' ../pc-iamsetsuna-doc/docs/15-leftovers.md
28
```

Another count of a table the source already printed
([14](14-leftovers.md)).

---

## And seven of this session's own

**A. Rule 0 was violated twice — once loudly, once silently.**
A throwaway analysis script was passed through a heredoc and the shell ate a
backslash:

```
  File "<stdin>", line 16
    b=n.rsplit('\',1)[-1]
               ^
SyntaxError: unterminated string literal
```

`.rsplit('\\', 1)` reached Python as `.rsplit('\', 1)`. It raised rather than
returning a number, which is luck and not method, and the work was redone with
`Write` into `tools/coverage.py`.

**The second was silent and did no damage, which is worse.** The
`pc-gamelist-doc` write-up was appended with a quoted heredoc — content full
of spaces and backticks, no backslashes. The quoting meant nothing was
expanded and the text landed byte-correct, and it was verified afterwards by
reading it back. **The rule says `Write` or `Edit` for anything containing a
backslash or a space, and it says so precisely because "it happened to be
fine" is not a check.** Two violations, one loud, one silent, on a session
that predicted zero ([15](15-prediction-scoring.md), C29).

**B. An inherited tool was overwritten.**
`tools/account.py` was created for this object's four-layer accounting without
checking whether the name was taken. It was: `pc-iamsetsuna-doc/tools/account.py`,
5,914 bytes, a single-denominator coverage tool for an object with no
containers. The `Write` result said *updated* rather than *created* and that
was the signal; it was noticed one step later, when `toolscan.py` reported 521
files where 522 were expected. The inherited file was restored from the
neighbour and verified by hash, and this session's tool is `zaccount.py`:

```
restored account.py sha1 : 93de3e992e6b9f516f0890b7f2f3e4790faaa41f
inherited account.py sha1: 93de3e992e6b9f516f0890b7f2f3e4790faaa41f
identical : True
```

**C. The Z entry record was derived one byte wrong**, and the specimen builder's
assertion caught it before a real byte was read: name length at `+0x1D`, not
`+0x1E` ([12](12-the-tools.md)).

**D. A selftest specimen was wrong rather than the reader.** `isz.py`'s
"back-reference before the start of the stream" specimen emitted a legal
distance. The check failed, the specimen was rebuilt.

**E. A selftest check passed for the wrong reason.** `runexpect.py`'s
"plain text gives a ratio far above 1" used a pure-ASCII specimen where `p` is
1 and the expectation equals the observation, and an escape clause `or p == 1.0`
let it through. **A check that cannot fail is not a check**; the specimen is now
text buried in binary at `p = 0.25`, ratio 136.5.

**F. `cptext.py` crashed on a default Windows console.** It prints Cyrillic
and box drawing by design, and with no `PYTHONIOENCODING` set its own selftest
died with `UnicodeEncodeError` partway through the table — a tool that works
only when an environment variable happens to be set. Found by running all eight
selftests one last time with the variable unset. It now reconfigures its own
streams to UTF-8 and falls back to replacement characters rather than raising.

**G. `coverage.py` classified two published text files as unclassifiable.**
The first version put `FILE_ID.DIZ` and `DISK1.ID` in the `neither` bucket
because the `.DIZ` codepage is ambiguous, which dropped the published figure to
0.8332 % and contradicted the pre-briefing's 0.8387 % for the wrong reason. The
ambiguity is *which* published codepage, not *whether* one exists; both were
moved to `published` and the figure agrees with the brief exactly.

---

## The count

**Twelve in the brief and seven here.** The last eight briefs carried nine, seven,
eight, eleven, twelve, eleven, eleven and nine, and the author is the same.
This one flagged none of its own and the twelve above are the answer to that.

**Only two of the twelve needed a container to be opened** — the `USER32.DLL`
identification and the `+0x16` field. The other ten were available to the
pre-briefing in files it had already read: the entropy table it printed, the
manifest it walked, the two text files it decoded, and the tool it ran.

That is the uncomfortable version and it is the true one. **The corrections are
not what the extra work bought; they are what a second pass over the same bytes
buys.** Seven of them come from asking one more question of a table that was
already on the page — how many rows have one file, are these four names the
same name, which one is the fourth executable, are these high bytes actually
decidable — which is precisely the failure mode
`pc-iamsetsuna-doc/docs/16` named at the end of its own scoring:

> **A figure in a brief that is a count of a table the tool already printed is
> the most likely thing in it to be wrong.**

Eleven briefs later that prescription has now caught its own author twice
running.

**But number 9 is a different species and it is the one worth carrying
forward.** The other eleven are counts and readings that a second pass over the
same page fixes. That one is an inference from **outside** the object — a
correct observation about a download site, turned into a negative claim about a
file's contents — and no amount of re-reading the brief would have caught it,
because the brief is where it entered. It needs a rule rather than a second
pass:

> **Mark every statement in a pre-briefing as being about the object or about
> the object's provenance, and never let the second kind produce a negation
> about the first.** A distributor's catalogue, a shop manifest, a filename on
> a web page and an owner's recollection are all evidence about how an object
> arrived. What is inside it is settled by what is inside it.
