#!/usr/bin/env python
import sys

for line in sys.stdin:
    fields = line.split(';')

    country = fields[0]
    year = fields[1]
    code = fields[2]
    commodity = fields[3]
    flow = fields[4]
    trade = fields[5]
    weight = fields[6]
    unit = fields[7]
    quantity = fields[8]
    category = fields[9]

    print '%s\t%s' % (year, "1")

