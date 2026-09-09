#!/usr/bin/env python3
"""coverage.py -- what share of an object is in a format somebody published,
stated over a named denominator.

This repository's coverage figure has always been a share of bytes whose
format has a published specification. On this object that figure is different
at every layer, so the tool takes the layer as an argument and prints the
denominator on the same line as the share. A coverage number without its
denominator is not a measurement.

    members  the twelve files the ZIP holds
    product  the files the four InstallShield containers hold, by the expanded
             size each container's own entry table declares

A format counts as PUBLISHED when a specification exists outside this
repository: PKWARE's APPNOTE for ZIP, Microsoft's NE and PE, the MIDI
Manufacturers Association's Standard MIDI File, Microsoft's BMP and RIFF WAVE,
and plain text. It counts as DERIVED when this session worked it out of the
bytes: InstallShield's Z archive, its `_INST32I` container and its `.PKG`
manifest. It counts as NEITHER when nobody here opened it and nobody outside
has written it down: WinHelp 3.x, and RPG Maker's own `.DAT` and `.ATR`.

The three buckets are printed separately and are never merged, because
"derived by this session" is a weaker claim than "published by a vendor" and
folding them together would hide that.

    python tools/coverage.py members --members _work/members
    python tools/coverage.py product --members _work/members
    python tools/coverage.py selftest
"""
import argparse
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import is32                                      # noqa: E402
import isz                                       # noqa: E402

PUBLISHED = {
    "MID": "Standard MIDI File (MMA RP-001)",
    "BMP": "Windows bitmap (Microsoft)",
    "WAV": "RIFF WAVE (Microsoft and IBM)",
    "EXE": "NE and PE (Microsoft)",
    "DLL": "NE and PE (Microsoft)",
    "TXT": "plain text",
    "INI": "plain text",
    "DIZ": "plain text; CP437 and CP866 render it identically",
    "ID": "plain text",
}
DERIVED = {
    "1": "InstallShield Z archive, derived here",
    "LIB": "InstallShield Z archive, derived here",
    "INS": "InstallShield Z archive, derived here",
    "EX_": "InstallShield _INST32I container, derived here",
    "PKG": "InstallShield manifest, derived here",
}
NEITHER = {
    "HLP": "WinHelp 3.x, no published specification",
    "DAT": "RPG Maker's own, no published specification",
    "ATR": "RPG Maker's own, no published specification",
    "INS_product": "InstallShield compiled setup script, not opened here",
}


def ext_of(name):
    base = name.rsplit("\\", 1)[-1]
    if "." in base[1:]:
        return base.rsplit(".", 1)[-1].upper()
    return "(none)"


def bucket(ext, mode="members"):
    # `.INS` is a Z archive at the member layer and a compiled setup script
    # at the product layer. Same three letters, two different things, and
    # one table must not silently claim the other was opened.
    if ext == "INS" and mode == "product":
        return "neither", NEITHER["INS_product"]
    if ext in PUBLISHED:
        return "published", PUBLISHED[ext]
    if ext in DERIVED:
        return "derived", DERIVED[ext]
    if ext in NEITHER:
        return "neither", NEITHER[ext]
    return "neither", "not identified in this session"


def population(mode, members):
    rows = []
    if mode == "members":
        for n in sorted(os.listdir(members)):
            rows.append((n, os.path.getsize(os.path.join(members, n))))
        return rows, "the twelve files the ZIP holds"
    for name in ("_SETUP.1", "_SETUP.LIB", "SETUP.INS"):
        p = os.path.join(members, name)
        for e in isz.parse(open(p, "rb").read(), p)["entries"]:
            rows.append((e["name"], e["expanded"]))
    p = os.path.join(members, "_INST32I.EX_")
    for r in is32.parse(open(p, "rb").read())["records"]:
        rows.append((r["name"], r["expanded"]))
    return rows, "the files the four containers hold, at their declared " \
                 "expanded sizes"


def report(rows, label, mode="members"):
    total = sum(s for _, s in rows)
    cnt = collections.Counter()
    byt = collections.Counter()
    for n, s in rows:
        e = ext_of(n)
        cnt[e] += 1
        byt[e] += s
    print("denominator : %d files, %d bytes -- %s" % (len(rows), total, label))
    print()
    print("  %-8s %6s %12s  %-10s %s"
          % ("ext", "files", "bytes", "bucket", "format"))
    for e, c in cnt.most_common():
        b, why = bucket(e, mode)
        print("  %-8s %6d %12d  %-10s %s" % (e, c, byt[e], b, why))
    print()
    sums = collections.Counter()
    counts = collections.Counter()
    for e in cnt:
        b, _ = bucket(e, mode)
        sums[b] += byt[e]
        counts[b] += cnt[e]
    for b in ("published", "derived", "neither"):
        print("  %-10s %4d files %12d bytes   %8.4f %% of %d"
              % (b, counts[b], sums[b], 100.0 * sums[b] / total if total else 0,
                 total))
    print("  %-10s %4d files %12d bytes"
          % ("SUM", sum(counts.values()), sum(sums.values())))
    if sum(sums.values()) != total:
        print("  THE BUCKETS DO NOT SUM TO THE DENOMINATOR", file=sys.stderr)
        return 1
    return 0


def selftest():
    checks = []
    checks.append(("every extension falls in exactly one bucket",
                   len(set(PUBLISHED) & set(DERIVED)) == 0
                   and len(set(PUBLISHED) & set(NEITHER)) == 0
                   and len(set(DERIVED) & set(NEITHER)) == 0, ""))
    checks.append(("an unknown extension is not counted as published",
                   bucket("QQQ")[0] == "neither", str(bucket("QQQ"))))
    checks.append(("INS is derived at the member layer and neither at the "
                   "product layer",
                   bucket("INS")[0] == "derived"
                   and bucket("INS", "product")[0] == "neither", ""))
    checks.append(("a name with a path separator takes the last component",
                   ext_of("themes\\global\\a.BMP") == "BMP", ""))
    checks.append(("a dotfile is not given an extension",
                   ext_of(".profile") == "(none)", ext_of(".profile")))
    checks.append(("a name with no dot is not given an extension",
                   ext_of("README") == "(none)", ""))
    checks.append(("HLP is NOT counted as published",
                   bucket("HLP")[0] == "neither", ""))
    checks.append(("the Z archive is derived and not published",
                   bucket("1")[0] == "derived", ""))
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
    ap.add_argument("mode", choices=("members", "product", "selftest"))
    ap.add_argument("--members", default="_work/members")
    args = ap.parse_args()
    if args.mode == "selftest":
        return selftest()
    rows, label = population(args.mode, args.members)
    return report(rows, label, args.mode)


if __name__ == "__main__":
    sys.exit(main())
