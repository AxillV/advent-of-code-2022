import os

f = open(os.getcwd()+"\Day 4\\input.txt", "r")

length=[-1,-1]
start=[-1,-1]
count=0
lines=0

for line in f:
    if(line[-1]=='\n'): 
        current = line[:-1].split(',')
    else:
        current = line.split(',')

    for i in range(0,2):
        nums = current[i].split('-')
        length[i] = int(nums[1])-int(nums[0])
        start[i] = int(nums[0])
    
    diff = abs(start[0]-start[1])
    if(start[0]<=start[1] and length[0]>=diff):
        count += 1
    elif(start[0]>=start[1] and diff<=length[1]):
        count += 1

print(count)

f = open(os.getcwd()+"\Day 4\\input.txt", "r")
finish=[-1,-1]
start=[-1,-1]
count=0
lines=0
for line in f:
    if(line[-1]=='\n'): 
        current = line[:-1].split(',')
    else:
        current = line.split(',')

    for i in range(0,2):
        nums = current[i].split('-')
        finish[i] = int(nums[1])
        start[i] = int(nums[0])
    
    if(start[0]<=start[1] and finish[0]>=start[1]):
        count += 1
    elif(start[0]>=start[1] and start[0]<=finish[1]):
        count += 1

print(count)