#!/usr/bin/env python3
"""Entry point for make.fun news-image-20261120 (FRONT PAGE variant).

Copies the pre-built front-page image ``entry.png`` (1024x1024, drawn with
PIL by build_image.py) to the output directory as ``entry.png``.

The output directory is taken from the ``MAKEFUN_OUTPUT_DIR`` environment
variable and defaults to ``/output``.  The copy is byte-for-byte identical
on every run: no network, no randomness, no timestamps are involved.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def _sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    dest = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(SOURCE):
        print("error: entry.png not found next to main.py", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    if _sha256(SOURCE) != _sha256(dest):
        print("error: copied file differs from source", file=sys.stderr)
        return 1
    print("wrote", dest, os.path.getsize(dest), "bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
