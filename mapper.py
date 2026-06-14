#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    if len(fields) == 6:
        payment_type = fields[5]
        amount = fields[4]
        print(f"{payment_type}\t{amount}")
