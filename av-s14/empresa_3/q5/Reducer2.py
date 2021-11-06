#!/usr/bin/env python
import sys

occurrence = {}
result = 0

for line in sys.stdin:
    key, value = line.split('\t', 1)

    try:
        value = int(value)
    except:
        continue
    try:
        occurrence[key] = occurrence[key] + value
    except:
        occurrence[key] = value

for occ in occurrence.keys():
    result = occurrence[occ] + result

print(result)


