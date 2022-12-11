import os
import math

f = open(os.getcwd()+"\Day 3\\input.txt", "r")

value = 0
for line in f:
    size = len(line)
    first = line[:math.floor(size/2)]
    second = line[math.floor(size/2):size-1]


    char = set(first).intersection(second)
    for c in char:
        value += ord(c[0])-38 if ord(c[0])<=90 else ord(c[0])-96

print(value)