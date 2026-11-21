"""Entry for news-image-20261121: "The World Today — 21 November 2026".

The entry image is a newspaper front page summing up the world's news of
Saturday 21 November 2026. It is stored in this repository as entry.png and
this program copies it, byte for byte, to the output directory. It uses only
the Python standard library and needs no network, so every run writes the
exact same bytes.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    if not source.is_file():
        print(f"missing entry image: {source}", file=sys.stderr)
        raise SystemExit(1)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)
    # Confirm the copy is complete and identical to the stored image.
    if hashlib.sha256(destination.read_bytes()).hexdigest() != hashlib.sha256(
        source.read_bytes()
    ).hexdigest():
        print("copied image does not match entry.png", file=sys.stderr)
        raise SystemExit(1)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
