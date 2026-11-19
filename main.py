"""Copy the bundled news image to the make.fun output directory.

Standard library only. No network access. Deterministic: the same
bytes are written on every run.
"""

import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    destination = out_dir / "entry.png"
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
