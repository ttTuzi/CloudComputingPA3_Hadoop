#!/usr/bin/env python3
import sys

# read each line in cvs
for line in sys.stdin:
    # remove the white space for each line
    line = line.strip()

    # analysis the cvs
    try:
        date, instance_type, os, region, price = line.split(',')
        # use only region at "eu-central-1"
        if region.startswith('eu-central-1'):
            # print the data
            print(f'{instance_type},{os},{region}\t{price},{date}')
    except ValueError as e:
        continue
