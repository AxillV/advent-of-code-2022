import os 

f = open(os.getcwd()+"\Day 6\\input.txt", "r")
input = f.readline()

flag=[0,0]
for i in range(len(input)):
    if(len(set(input[i:i+4]))==4 and not flag[0]):
        print("First start-of-packet marker in position",i+4)
        flag[0]=1
    if(len(set(input[i:i+14]))==14 and not flag[1]):
        print("First start-of-message marker in position",i+14)
        flag[1]=1 
    if flag[0] and flag[1]: break