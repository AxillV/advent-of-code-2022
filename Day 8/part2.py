import os

import readline
# perhaps implement biggest number for all 5 directions in each node?
# takes more space but less time..

def checkScore(row, column):
    checkTree=forest[row][column]
    score1=0
    score2=0
    score3=0
    score4=0

    #i represents the row, so we are checking vertically
    for i in range(row-1, -1, -1):
        if forest[i][column]>=checkTree: 
            score1+=1
            break
        score1+=1    

    for i in range(row+1,len(forest)):
        if forest[i][column]>=checkTree: 
            score2+=1
            break
        score2+=1

    for i in range(column-1, -1, -1):
        if forest[row][i]>=checkTree: 
            score3+=1
            break
        score3+=1
   

    for i in range(column+1,len(forest[row])):
        if forest[row][i]>=checkTree: 
            score4+=1
            break
        score4+=1

    return score1*score2*score3*score4
    
    

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

bestScore=0
for i in range(len(forest)):
    for j in range(len(forest[i])):
        tempScore=checkScore(i,j)
        if tempScore>bestScore: 
            bestScore = tempScore 
print(bestScore)