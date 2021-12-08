#!/usr/bin/env python
#day2a.py


exercise='2a'

with open("day"+exercise+".input","r") as f:
    readings = f.read().splitlines()

horizontal = 0
depth = 0 

for i in readings:
    for j, k in (list(i.split(" ")),):
        if j == 'forward':
            horizontal += int(k)
        if j == 'down':
            depth += int(k)
        elif j == 'up':
            depth = depth - int(k)
        
print(horizontal, depth)
print(horizontal*depth)