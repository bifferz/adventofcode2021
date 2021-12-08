#!/usr/bin/env python
#day3a.py
from collections import Counter

exercise='3'

with open("day"+exercise+".input","r") as f:
    readings = f.read().splitlines()

def most_common(file, digit):
    a.append((Counter([i[digit] for i in file]).most_common(1)[0][0]))
    return a

def least_common(file, digit):
    b.append((Counter([i[digit] for i in file]).most_common(2)[1][0]))
    return b

def bin_to_dec(string):
    dec = int(string, 2)
    return dec

a = []
b = []
for i in range(len(readings[0])):
    most_common(readings, i)
for i in range(len(readings[0])):
    least_common(readings, i)

gamma = int(bin_to_dec("".join(a)))
epsilon = int(bin_to_dec("".join(b)))

print("Power is: ")
print(gamma * epsilon)