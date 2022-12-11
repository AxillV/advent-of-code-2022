import os

f = open(os.getcwd()+"\Day 1\input.txt", "r")

tempCal = 0
calList = []
for line in f:
    if(line=="\n"):
        calList.append(tempCal)
        tempCal = 0
    else:
        tempCal += int(line)
    
calList.sort()
print(sum(calList[-3:]))
