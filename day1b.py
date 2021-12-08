#!/usr/bin/env python
#day1b.py

with open("day1.input","r") as f:
    readings = [int(line) for line in f.read().splitlines()]

def count_decreases(depths, neighbor=1):
    return sum(1 for reading1, reading2 in zip(depths, depths[neighbor:]) if reading1 < reading2)

print(count_decreases(readings, neighbor=3))