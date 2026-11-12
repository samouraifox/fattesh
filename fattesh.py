#!/usr/bin/env -S python3 -I 
# fattesh : static scanner for Claude skills. Reads the files, never runs them.
#
# 1. Imports
import argparse
import sys
from pathlib import Path 

VERSION = "0.1.0"

# 2. Read the command line
ap = argparse.ArgumentParser(prog="fattesh")
ap.add_argument("targets", nargs="+")           # One or more folders to scan 
ap.add_argument("--json", action="store_true")  # flag: JSON report instead of text 
ap.add_argument("--version", action="version", version="fattesh " + VERSION)
args = ap.parse_args()

# 3. Check every target is a folder
for target in args.targets:
    root = Path(target)
    if not root.is_dir():
        print("fattesh: not a folder: " + target, file=sys.stderr) # errors go to stderr, exit 2 = tool failed
        sys.exit(2)
    print("scanning " + str(root))

