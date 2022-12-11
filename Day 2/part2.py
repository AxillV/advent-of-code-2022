import os

# A     B       C opponent
# X     Y       Z me
# 1     2        3
# rock paper sciscor
# 0lose 3draw 6win

def gameCalc(pairPlayed):
    winPairs = {'A':'Y', 'B':'Z', 'C':'X'}
    drawPairs = {'A':'X', 'B':'Y', 'C':'Z'}
    losePairs = {'A':'Z', 'B':'X', 'C':'Y'}
    pointsWon = 0

    match pairPlayed[1]:
        case 'X':
            pick = losePairs[pairPlayed[0]]
        case 'Y':
            pick = drawPairs[pairPlayed[0]]
            pointsWon += 3
        case 'Z':
            pick = winPairs[pairPlayed[0]]
            pointsWon += 6
    
    match pick:
        case 'X':
            pointsWon +=1
        case 'Y':
            pointsWon +=2
        case 'Z':
            pointsWon +=3
            
    return pointsWon

f = open(os.getcwd()+"\Day 2\input.txt", "r")
pointsWon = 0

for line in f:
    currentPair = [line[0], line[2]]
    pointsWon += gameCalc(currentPair)

print("You've won", pointsWon, "points!")

