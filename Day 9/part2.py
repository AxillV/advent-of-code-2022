import os
AMOUNT_OF_KNOTS=10

def updateKnot(knots, index, visited):
    if(index==AMOUNT_OF_KNOTS-1):
        return updateTail(knots, visited)
    
    #Positive: Knot in front is Up/Right
    dHorizontal = knots[index-1][0]-knots[index][0]
    dVertical = knots[index-1][1]-knots[index][1]

    #touching
    if(abs(dHorizontal)<2 and abs(dVertical)<2):
        return updateKnot(knots, index+1, visited)

    #Not touching but same column or row
    if(dHorizontal==0): 
        knots[index][1]+= int(dVertical/2)
        return updateKnot(knots, index+1, visited)
        

    if(dVertical==0): 
        knots[index][0]+= int(dHorizontal/2)
        return updateKnot(knots, index+1, visited)

    #L-shape,
    #so +-1 in each cardinal direction
    knots[index][0]+= 1 if dHorizontal>0 else -1
    knots[index][1]+= 1 if dVertical>0 else -1
    return updateKnot(knots, index+1, visited)

def updateHead(knots, axis:int, value:int, visited):
    uniques=0
    #step for +- and abs for value
    step=int(value/abs(value))
    for i in range(abs(value)):
        knots[0][axis]+=step
        uniques+=updateKnot(knots, 1, visited)
    #render(knots)
    return uniques
    
def updateTail(knots, visited):
    index = AMOUNT_OF_KNOTS-1
    dHorizontal = knots[index-1][0]-knots[index][0]
    dVertical = knots[index-1][1]-knots[index][1]

    #touching
    if(abs(dHorizontal)<2 and abs(dVertical)<2):
        return 0

    #Not touching but same column or row
    if(dHorizontal==0): 
        knots[index][1]+= int(dVertical/2)
        return checkUnique(knots, visited)

    if(dVertical==0): 
        knots[index][0]+= int(dHorizontal/2)
        return checkUnique(knots, visited)

    #L-shape,
    #so +-1 in each cardinal direction
    knots[index][0]+= 1 if dHorizontal>0 else -1
    knots[index][1]+= 1 if dVertical>0 else -1
    return checkUnique(knots, visited)

def checkUnique(knots, visited):
    index = AMOUNT_OF_KNOTS-1
    if(knots[index] not in visited):
            visited.append([knots[index][0],knots[index][1]])
            return 1
    return 0
    
#TODO: MAKE RENDER ACTUALLY WORK
def render(knots):
    tail=AMOUNT_OF_KNOTS-1
    os.system('cls')
    for i in range(4,-1,-1):
        for j in range(6):
            if(j==knots[0][0] and i==knots[0][1]):
                print('H', end='')
                continue
            for k in range(1,tail):
                if(j==knots[k][0] and i==knots[k][1]):
                    print(k, end='')
                    if(knots[k][0]==knots[k+1][0] and knots[k][1]==knots[k+1][1]):
                        break
                continue
            if(j==knots[tail][0] and i==knots[tail][1]):
                print('T', end='')
                continue
            if(i==0 and j==0):
                print('s', end='')
                continue
            print('.', end='')
        print()
    print()

def main():
    f = open(os.getcwd()+'\\input.txt', 'r')

    #column, row
    knots=[]
    for i in range(AMOUNT_OF_KNOTS):
        knots.append([0,0])
    visited=[[0,0]]
    uniques=1

    #render(knots)
    for line in f:
        line=line.split()
        match line[0]:
            case 'R':
                axis=0
                value=int(line[1])
            case 'L':
                axis=0
                value=-int(line[1])
            case 'U':
                axis=1
                value=int(line[1])
            case 'D':
                axis=1
                value=-int(line[1])
        uniques += updateHead(knots, axis, value, visited)
    print(uniques)

if __name__ == "__main__":
    main()
