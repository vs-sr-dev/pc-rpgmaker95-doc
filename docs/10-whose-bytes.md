# 10 — whose bytes: a man who signed his work in three places, and the one thing this repository takes out

*Measure: `python tools/sift.py _work/members --group personal --show` and the
same on `_work/product`; `python tools/utf16sift.py _work/members`; `python
tools/redact.py selftest` — 13 checks — and `python tools/redact.py
notes/sift-personal.txt --in-place --expect 1`.*

---

## The decision, first, because everything below depends on it

This repository's standing rule is *redact what identifies a person, publish
third-party build roots and company details.* That rule was written for account
names left in build paths by accident. **It has never met a contact address
whose author printed it in a readme and asked people to use it.**

Deciding it required knowing what was actually in the object, and the pre-briefing
could not know, because four of the six occurrences were inside a container
nobody had opened. Here is the population:

```
python tools/sift.py _work/product --group personal --show
=== e-mail shape ===
    000_readme.txt     x1
    000_rpg95.exe      x1
    000_rpg95.hlp      x1
    004_rpg95.hlp      x1
```

| token | occurrences | where |
|---|---:|---|
| the e-mail address | **6** | `readme.txt` ×3 (ZIP, `_SETUP.1`, `_SETUP.LIB`), `rpg95.exe` ×1, `rpg95.hlp` ×2 |
| ICQ UIN `#2444691` | 3 | the three readmes |
| `http://www.chat.ru/~rpgmaker` | 4 | the three readmes and `rpg95.exe` |
| "Don Miguel", in some spelling | 17 | across all four layers |
| **"Miguel Bratous"** | 1 | inside `rpg95.exe` |
| `(847) 240-9111`, `(708) 240-9111` | 3 | `SETUP.EXE`, `_SETUP.DLL`, `_ISDEL.EXE` |
| "You Ito", "Tsuneari Okumoto" | in 3 version resources | `rpg95.exe`, `game.exe`, `game_engl_123.exe` |

Inside `rpg95.exe`, at offset `0x09FEF1`, the About box reads:

```
[ http://www.chat.ru/~rpgmaker ] Created by Miguel Bratous aka Don Miguel!!
... E-mail me your suggestions!  <address>   Thank You!!!   It's for free!!!
```

**He did not leave this behind; he put it in the program.** The address is not
in a build path, not in a debug symbol and not in a stray configuration file.
It is in the About window of the software he distributed, beside his name, next
to a sentence asking to be written to.

### The rule this repository adopts

> **In a signature block its author wrote in order to be credited and
> contacted, publish what claims credit and redact what routes a message.**
>
> Credit is authorship: names, handles, the studio, the thanks, the project
> page. Routing is anything a stranger can use **today** to reach a private
> individual: an e-mail address, an account on a service that is still running,
> a private person's telephone number.
>
> A company's published support line is not a private individual's contact.

Applied to the four contacts in the same paragraph:

| | verdict | why |
|---|---|---|
| the e-mail address, at `mail.ru` | **redacted** | `mail.ru` is an operating consumer mail service; the address would still deliver |
| ICQ UIN `#2444691` | published | ICQ was shut down in June 2024; the identifier no longer routes |
| `http://www.chat.ru/~rpgmaker` | published | a defunct host, and a project page rather than a person |
| `(847) 240-9111` ×2, `(708) 240-9111` | published | a company's published support line, and also a clock ([06](06-the-installer.md)) |

And to the names: **"Don Miguel", the six aliases and "Miguel Bratous" are
published.** They are the authorship claim of the object, and the object is the
translation he is claiming. Redacting the name of the person whose work this
repository exists to describe, while publishing the work, would be incoherent.
The same goes for "You Ito" and "Tsuneari Okumoto" in ASCII's version resources
and for "TNomad of KanjiHack" in the readme's thanks.

### The limit, stated instead of hidden

**The address is trivially reconstructable from what is published**, because one
of the author's own aliases is its local part and this document publishes the
alias list. The redaction is against automated harvesting of the literal string,
not against a reader who wants it. A redaction that claimed more than that would
be a lie, and it is written into the tool's own docstring so nobody downstream
mistakes it for anonymisation.

### And it is implemented

The previous object's `steamacf.py` redacts by program. There was no equivalent
here, so `tools/redact.py` was written: it removes address-shaped strings,
counts what it removes, and **fails loudly when the count is not what was
expected**.

```
python tools/redact.py selftest
  an address is replaced and the count is 1              ok
  the ICQ number beside it survives                      ok
  a project URL is NOT touched                           ok
  a company support line is NOT touched                  ok
  the alias list is NOT touched                          ok
  the author's name is NOT touched                       ok
  ... 13 checks, 0 failures

python tools/redact.py notes/sift-personal.txt --in-place --expect 1
addresses : 1 replaced
python tools/redact.py notes/sift-personal.txt --check
check     : 0 address-shaped strings remain in the file
```

Six of the thirteen checks assert that things beside the address are **not**
touched, because a redaction pattern wide enough to catch a vendor telephone
number would have destroyed the clock in [06](06-the-installer.md).

---

## What the sweep found, and it is all real

```
python tools/sift.py _work/members --group personal --show
blobs searched : 12   bytes : 7,354,728

e-mail shape        1        1
telephone shape     3        3
P.O. Box            0        0
home dir            0        0
Documents and Settings 0     0
Copyright <name>    0        0
positive control fired : YES (1253)   negative control quiet : YES
```

**Four hits, four blobs, and not one false positive** — the first time in this
collection. The previous object fired sixty times and one of the sixty was a run
of compressed texture with an at-sign in it.

```
python tools/utf16sift.py _work/members
hits that only a UTF-16 pass finds : 0
```

**Zero.** `sift.py`'s eight-bit-only sweep is a defect this collection has
recorded repeatedly, and on a 1996 object in CP437 and CP866 it is **correct**.
A defect is a property of a tool against a population, and this is the
measurement that proves it rather than the assertion that assumes it
([12](12-the-tools.md)).

The build-path sweep finds exactly one drive-letter path in the whole object:

```
python tools/sift.py _work/members --group buildpath --show
=== drive-letter path ===
    _ISDEL.EXE    x1    c:\stopthis.now
```

**A sentinel file name inside InstallShield's uninstaller stub**, not a build
root and not anybody's directory.

---

## Nine named parties, and where each of them is

| | what | where it is |
|---|---|---|
| **ASCII Corporation** | the publisher | `readme.txt`, `FILE_ID.DIZ`, six version resources |
| **You Ito**, **Tsuneari Okumoto** | the programmers | the `LegalCopyright` of `rpg95.exe`, `game.exe`, `game_engl_123.exe` |
| **Don Miguel** / Miguel Bratous | the translator | everywhere, 17 times, and in the About box |
| **KanjiHack**, **TNomad** | the previous translators | `readme.txt`, `FILE_ID.DIZ` — credited and blamed |
| **Aspetra** | thanked | `readme.txt` |
| **Micco** | wrote `unlha32.dll` | that file's `LegalCopyright` |
| **Stirling Technologies** | the installer, before 1996 | 3 binaries |
| **InstallShield Corporation** | the same company, after | 3 binaries |
| **PKWARE**, **Microsoft**, **Borland** | the compressor, the OS, the compiler | `SETUP.EXE`, `USER32.DLL`, `rpg95.exe` |

**Twelve parties, not nine**, and three of the extra ones — You Ito, Tsuneari
Okumoto and Micco — were unreachable until an undocumented container came apart.
The previous object had a studio that named itself three times in 1.4 gigabytes;
this one names everyone who touched it, in 2,433 bytes of text and six version
resources.

---

## And nothing of the owner's

No path from this machine, no account name, no save file, no configuration, no
registry fragment. The only thing here that belongs to whoever downloaded it is
the file's mtime, 2026-09-09, and it has no second witness.

**The rule against publishing this machine's absolute paths costs nothing on
this object, which is exactly why it is stated rather than assumed.** No `.md`
in this repository and no default argument in any tool written here contains a
path from this machine.
