"""Write one single-line joke excusing a missed deadline to entry.txt.

The program writes exactly one line, no trailing newline, using only the
standard library. The output directory comes from MAKEFUN_OUTPUT_DIR.
"""

import os
import stat

LINE = "I delegated the deadline to my future self, and he has left me on read ever since."


def main():
    if not LINE or not LINE.strip():
        raise ValueError("entry line must not be empty")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise RuntimeError("MAKEFUN_OUTPUT_DIR is not set")
    path = os.path.join(out_dir, "entry.txt")
    try:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
        os.chmod(path, 0o644)
    except OSError as exc:
        raise RuntimeError(f"failed to write entry.txt: {exc}") from exc


if __name__ == "__main__":
    main()
