#!/usr/bin/env python3

import os, sys, re
from glob import glob
from pathlib import Path

def main(argc, argv):
    logs = glob("*-*-*.log")

    for f in logs:
        # Strip IPs
        with open(f, "r+") as fp:
            out = ""
            for l in fp:
                out += re.sub(r"(Quits|Joins|Parts): (\S+?) \(.*?@.*?\)", r"\1: \2", l)
            fp.seek(0)
            fp.truncate()
            fp.write(out)

        old_path = Path(f)
        new_path = Path("/".join(old_path.stem.split("-")) + ".log")
        print(f"Moving {old_path} to {new_path}")

        new_path.parent.mkdir(parents=True, exist_ok=True)
        old_path.replace(new_path)

if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))
