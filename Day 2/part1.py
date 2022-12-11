import os 

# ABC opponent
# XYZ me
# 1    2     3
# rock paper sciscor
# 0lose 3draw 6win

def gameCalc(pairPlayed):
    winPairs = [['A', 'Y'],['B', 'Z'],['C', 'X']]
    drawPairs = [['A', 'X'],['B', 'Y'],['C', 'Z']]
    losePairs = [['A', 'Z'],['B', 'X'],['C', 'Y']]
    pointsWon = 0

    match pairPlayed[1]:
        case 'X':
            pointsWon +=1
        case 'Y':
            pointsWon +=2
        case 'Z':
            pointsWon +=3
    if pairPlayed in winPairs: pointsWon += 6
    elif pairPlayed in drawPairs: pointsWon += 3
    return pointsWon

f = open(os.getcwd()+"\Day 2\input.txt", "r")
pointsWon = 0

for line in f:
    currentPair = [line[0], line[2]]
    pointsWon += gameCalc(currentPair)

print("You've won:", pointsWon)

