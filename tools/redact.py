#!/usr/bin/env python3
"""redact.py -- remove routable personal contacts from a text file, by
program, and fail loudly when it removes nothing.

THE RULE THIS TOOL IMPLEMENTS, which is argued in the personal-data chapter:

    In a signature block its author wrote in order to be credited and
    contacted, PUBLISH what claims credit and REDACT what routes a message.

    Credit is authorship: names, handles, the studio, the thanks, the version,
    the project page. Routing is anything a stranger can use TODAY to reach a
    private individual: an e-mail address, an account on a service that is
    still running, a private person's telephone number.

    A company's published support line is not a private individual's contact
    and is not redacted.

What that comes to on this object: one e-mail address is removed and
everything else in the same paragraph is published -- the six aliases, the
name, the ICQ number on a service that closed in 2024, and the URL of a host
that no longer exists.

THE LIMIT, STATED RATHER THAN HIDDEN. The address is reconstructable from what
this repository publishes, because one of the author's own aliases is its local
part. This redaction is against automated harvesting of the literal string, not
against a reader who wants it. A redaction that claimed more than that would be
a lie.

Failure is loud and is the point. `--expect N` makes the count part of the
contract, and a run that replaces nothing when something was expected returns
non-zero rather than quietly copying the file through.

    python tools/redact.py notes/sift-personal.txt --in-place --expect 1
    python tools/redact.py notes/sift-personal.txt --check
    python tools/redact.py selftest
"""
import argparse
import os
import re
import sys

# Deliberately narrow. A wide pattern would eat the vendor telephone numbers,
# the URL and the version strings, all of which this repository publishes.
EMAIL = re.compile(rb"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
TOKEN = b"[e-mail redacted: see docs on the personal data]"


def redact(data):
    """Returns (new_bytes, count). Bytes in, bytes out: the files this is
    pointed at hold CP437 and CP866 fragments and must not be decoded."""
    return EMAIL.subn(TOKEN, data)


def cmd_run(args):
    if not os.path.exists(args.path):
        raise SystemExit("redact: no such file: %s" % args.path)
    with open(args.path, "rb") as fh:
        data = fh.read()
    out, n = redact(data)
    print("file      : %s" % args.path)
    print("bytes     : %d" % len(data))
    print("addresses : %d replaced" % n)
    if args.expect is not None and n != args.expect:
        print("redact: FAILED -- expected %d and replaced %d"
              % (args.expect, n), file=sys.stderr)
        return 1
    if args.check:
        remaining = len(EMAIL.findall(data))
        print("check     : %d address-shaped strings remain in the file"
              % remaining)
        return 1 if remaining else 0
    if args.in_place:
        with open(args.path, "wb") as fh:
            fh.write(out)
        print("written   : %s" % args.path)
    else:
        sys.stdout.write(out.decode("latin-1"))
    return 0


def cmd_selftest(args):
    checks = []

    # This specimen used to be the real address this tool exists to
    # remove. `pc-rpgmaker2000-doc/docs/13` found it here and
    # `pc-rpgmaker2003-doc/docs/12` found it still here: the repository
    # redacted the address from every chapter and left it written out
    # twice inside the source of the tool that does the redacting -- a
    # file which is committed and published. It is now `.invalid`, a
    # top-level domain RFC 2606 reserves so that it can never resolve,
    # and the check below asserts that no address in this file is
    # anything else.
    body = b"ICQ UIN #2444691       E-mail: someone@example.invalid\n"
    out, n = redact(body)
    checks.append(("an address is replaced and the count is 1",
                   n == 1 and b"@" not in out, out.decode("latin-1").strip()))
    checks.append(("the ICQ number beside it survives",
                   b"2444691" in out, ""))

    survivors = [
        (b"http://www.chat.ru/~rpgmaker", "a project URL"),
        (b"(847) 240-9111", "a company support line"),
        (b"Don_Miguel aka BMV aka Mummy aka GrEeZlY", "the alias list"),
        (b"Created by Miguel Bratous aka Don Miguel", "the author's name"),
        (b"RPG Maker 95+ v 1.02", "a version string"),
        (b"C:\\Program Files\\RPG95", "a path with an @-free colon"),
    ]
    for text, label in survivors:
        out, n = redact(text)
        checks.append((label + " is NOT touched", n == 0 and out == text,
                       "" if n == 0 else "replaced %d" % n))

    # Things that must be caught, including shapes the object does not have.
    catches = [
        b"a@b.invalid", b"first.last+tag@sub.domain.example",
        b"SOMEONE@EXAMPLE.INVALID",
    ]
    for text in catches:
        out, n = redact(text)
        checks.append(("%s is caught" % text.decode(), n == 1, ""))

    # THE CHECK THAT WOULD HAVE CAUGHT THE LEAK. Every address-shaped
    # string in this file's own source must sit in a domain that cannot
    # resolve -- `.invalid` or `.example`, both reserved by RFC 2606 --
    # so that the tool which removes contacts can never itself be the
    # thing that publishes one.
    src = open(os.path.abspath(__file__), "rb").read()
    found = EMAIL.findall(src)
    leaked = [a for a in found
              if not a.lower().endswith((b".invalid", b".example"))]
    checks.append(("no address in this tool's own source is routable",
                   not leaked,
                   "LEAKED: %s" % b", ".join(leaked).decode("latin-1")
                   if leaked else "%d specimens, all reserved"
                   % len(found)))

    # A file with nothing to redact must be reported as zero, not as success.
    out, n = redact(b"no contacts here at all")
    checks.append(("a file with no address reports zero rather than one",
                   n == 0, ""))

    # Bytes in, bytes out: high bytes must survive untouched.
    high = bytes([0xE1, 0xE7, 0xA8]) + b" x@y.invalid " + bytes([0xCD, 0xB3])
    out, n = redact(high)
    checks.append(("high bytes either side of an address are preserved",
                   n == 1 and out.startswith(bytes([0xE1, 0xE7, 0xA8]))
                   and out.endswith(bytes([0xCD, 0xB3])), ""))

    width = max(len(c[0]) for c in checks)
    failed = 0
    for label, ok, note in checks:
        print("  %-*s  %s   %s" % (width, label, "ok  " if ok else "FAIL",
                                   note))
        if not ok:
            failed += 1
    print()
    print("%d checks, %d failures" % (len(checks), failed))
    return 1 if failed else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("path", help="a file, or the word selftest")
    ap.add_argument("--in-place", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--expect", type=int)
    args = ap.parse_args()
    if args.path == "selftest":
        return cmd_selftest(args)
    return cmd_run(args)


if __name__ == "__main__":
    sys.exit(main())
