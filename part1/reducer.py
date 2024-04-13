#!/usr/bin/env python3
import sys

# read the variable
all_entries = []
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    price, date = value.split(',')
    all_entries.append((key, float(price), date))

# sort by date
all_entries.sort(key=lambda x: x[2])

# init the variable
current_key = None
current_prices = []
fluctuations = {}

# process the data after sort
for entry in all_entries:
    key, price, date = entry
    if key == current_key:
        current_prices.append(price)
    else:
        if current_key:
            # calculate the current diff and avg
            if len(current_prices) > 1:
                price_diffs = [abs(current_prices[i] - current_prices[i-1]) for i in range(1, len(current_prices))]
                avg_fluctuation = sum(price_diffs) / len(price_diffs)
                fluctuations[current_key] = avg_fluctuation
            current_prices = [price]
        current_key = key

# last key
if current_prices and len(current_prices) > 1:
    price_diffs = [abs(current_prices[i] - current_prices[i-1]) for i in range(1, len(current_prices))]
    avg_fluctuation = sum(price_diffs) / len(price_diffs)
    fluctuations[current_key] = avg_fluctuation

# find top 3 instance
top_three_fluctuations = sorted(fluctuations.items(), key=lambda x: x[1], reverse=True)[:3]

# print the result
for instance, fluctuation in top_three_fluctuations:
    print(f'{instance}\t{fluctuation}')

