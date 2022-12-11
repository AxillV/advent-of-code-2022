import os

f = open(os.getcwd()+"\Day 1\input.txt", "r")

tempCal = 0
maxCal = 0
for line in f:
    if(line=="\n"):
        if tempCal > maxCal: maxCal = tempCal
        tempCal = 0
    else:
        tempCal +=  int(line)
    
print(maxCal)
