#!/usr/bin/env python3

import os, sys
from glob import glob
from pathlib import Path

def main(argc, argv):
    logs = glob("*-*-*.log")

    for f in logs:
        old_path = Path(f)
        new_path = Path("/".join(old_path.stem.split("-")) + ".log")
        print(f"Moving {old_path} to {new_path}")

        new_path.parent.mkdir(parents=True, exist_ok=True)
        old_path.replace(new_path)

if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))
