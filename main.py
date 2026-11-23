#!/usr/bin/env python3
"""news-image-20261123 entrypoint: "The World in One Day - Monday, 23 November 2026".

The entry is a single image, entry.png: a newspaper front page drawn by
draw.py (kept in this repository) and committed next to this file. This
program uses only the standard library and copies that image into the
output directory - /output in the grader's container, or
$MAKEFUN_OUTPUT_DIR when set - so the two graded runs produce exactly
the same bytes.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
