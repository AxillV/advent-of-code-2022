import os
import re
import math
from collections import deque

ROW_COUNT = 8
COL_COUNT = 9

def moveCrates (amount, fromCrate, toCrate):
    for i in range(amount):
        crates[toCrate-1].append(crates[fromCrate-1].pop())


f = open(os.getcwd()+"\Day 5\\input.txt", "r")

crates=[]
for i in range(COL_COUNT):
    crates.append(deque())

for i in range(ROW_COUNT):
    line = f.readline()
    line = line.replace('\n', '')
    j=0
    for c in line:
        j+=1
        if (c not in {' ', '[', ']'} and j%4==2):
            crates[math.floor(j/4)].appendleft(c)

f.readline() #skip empty lines
f.readline()
line=f.readline()
while(line):
    temp = re.sub("[^0-9 ]", "", line).lstrip().split('  ')
    moveCrates(int(temp[0]), int(temp[1]), int(temp[2]))
    line=f.readline()

for i in range(ROW_COUNT):    
    for j in range(COL_COUNT):
        try:
            print(crates[j].pop(), end=" ")
        except IndexError: 
            print("-", end=" ")
    print()
    