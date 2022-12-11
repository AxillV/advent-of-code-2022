import os

import readline
# perhaps implement biggest number for all 5 directions in each node?
# takes more space but less time..

def checkVisiblity(row, column):
    checkTree=forest[row][column]

    #i represents the row, so we are checking vertically
    visible=1
    for i in range(row):
        if forest[i][column]>=checkTree: 
            visible=0

    if visible: return 1
    visible=1

    for i in range(row+1,len(forest)):
        if forest[i][column]>=checkTree: 
            visible=0
    
    if visible: return 1
    visible=1

    for i in range(column):
        if forest[row][i]>=checkTree: 
            visible=0
        
    if visible: return 1
    visible=1

    for i in range(column+1,len(forest[row])):
        if forest[row][i]>=checkTree: 
            visible=0
    
    if visible: return 1
    return 0
        
        # if i!=row and forest[i][column]>=checkTree: 
        #     visible=0
        # #if reached from one side, continue to the other
        # if i==row or i==len(forest)-1:
        #     if visible:
        #         return 1
        #     else:
        #         visible=1
        #         continue

    #i represents the column, so we are checking horizontally
    # for i in range(len(forest[row])):
    #     if i!=column and forest[row][i]>=checkTree: 
    #         visible=0

    #     if i==len(forest[row])-1:
    #         if visible: 
    #             return 1
    #         if i==column:
    #             return 1
    #         else: 
    #             return 0

    #     if i==column:
    #         if visible:
    #             return 1
    #         else:
    #             visible=1
    #             continue


f = open(os.getcwd()+'/input.txt', 'r')

forest=[]
line = f.readline()
i=0
while line:
    forest.append([])
    for c in line:
        if c=='\n': continue
        forest[i].append(int(c))
    i+=1
    line = f.readline()

count=0
for i in range(len(forest)):
    for j in range(len(forest[i])):
        count+=checkVisiblity(i,j)

print(count)