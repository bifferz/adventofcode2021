#!/usr/bin/env python
#day2a.py


exercise='2a'

with open("day"+exercise+".input","r") as f:
    readings = f.read().splitlines()

horizontal = 0
depth = 0
aim = 0

for i in readings:
    for j, k in (list(i.split(" ")),):
        if j == 'forward':
            if aim == 0:
                horizontal += int(k)
            else:
                horizontal += int(k)
                depth += (int(k) * int(aim))
        if j == 'down':
            aim += int(k)
        if j == 'up':
            aim = aim - int(k)
        
print(horizontal*depth)