import os
import math

def updateHead(head, direction:str, amount:int, visited):
    #axis is index for accessing head
    #value>0 means up/right 
    uniques=0
    match direction:
        case 'R':
            axis=0
            value=1
        case 'L':
            axis=0
            value=-1
        case 'U':
            axis=1
            value=1
        case 'D':
            axis=1
            value=-1
        
    for i in range(amount):
        head[axis]+=value
        updateTail(head, tail)
        if(tail not in visited):
            visited.append([tail[0],tail[1]])
            uniques+=1
        #render(head,tail)
    return uniques

def updateTail(head, tail):
    #Positive: Head is Up/Right
    dHorizontal = head[0]-tail[0]
    dVertical = head[1]-tail[1]

    #touching
    if(abs(dHorizontal)<2 and abs(dVertical)<2): 
        return

    #Not touching but same column or row
    if(dHorizontal==0): 
        tail[1]+= int(dVertical/2)
        return
    if(dVertical==0): 
        tail[0]+= int(dHorizontal/2)
        return

    #L-shape,
    #so +-1 in each cardinal direction
    tail[0]+= 1 if dHorizontal>0 else -1
    tail[1]+= 1 if dVertical>0 else -1
    
#5 height, 6 length
def render(head, tail):
    for i in range(50,-51,-1):
        for j in range(-50,51):
            if(j==head[0] and i==head[1]):
                print('H', end='')
                continue
            if(j==tail[0] and i==tail[1]):
                print('T', end='')
                continue
            if(i==0 and j==0):
                print('s', end='')
                continue
            print('.', end='')
        print()
    print()

f = open(os.getcwd()+'\\input.txt', 'r')

#column, row
head=[0,0]
tail=[0,0]
visited=[[0,0]]
uniques=1

#render(head,tail)
for line in f:
    line=line.split()
    uniques += updateHead(head, line[0], int(line[1]), visited)

print(uniques)