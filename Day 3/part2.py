import os

f = open(os.getcwd()+"\Day 3\\input.txt", "r")

count=0
value=0
for line in f:
    count+=1
    match count%3:
        case 1:
            first = line[:-1]
        case 2:
            second = line[:-1]
        case 0:
            third = line[:-1]
            char = (set(first).intersection(second)).intersection(third)
            for c in char:
                value += ord(c[0])-38 if ord(c[0])<=90 else ord(c[0])-96
                break

    
   
print(value)