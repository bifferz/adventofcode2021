#!/usr/bin/env python
#day1.py

with open("day1.input","r") as f:
    readings = f.read().splitlines()
old = 0
count = 0
for new in readings:
    if new > old:
        count += 1
    else:
        count = count
    old = new
print(count)