#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    if len(fields) != 6:
        raise ValueError(f"Expected exactly 6 elements, got {len(fields)}: {line}")
    category = fields[3]
    amount = fields[4]
    print(f"{category}\t{amount}")
