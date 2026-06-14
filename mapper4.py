#!/usr/bin/env python3
import sys

TARGET_CATEGORIES = {"Computers", "Cameras", "Video Games"}

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    if len(fields) == 6:
        category = fields[3]
        amount = fields[4]
        if category in TARGET_CATEGORIES:
            print(f"{category}\t{amount}")
