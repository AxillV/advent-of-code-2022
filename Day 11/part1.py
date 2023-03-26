import os
import operator
import math

#items for each monkey
monkeys=[]
monkeysCount=[]
#arg,op,arg,condition,true,false
monkeysInfo={}
operations={'+':operator.add, 
            '*':operator.mul}

f = open(os.getcwd()+'\\input.txt', 'r')

line=f.readline().replace(':', '').split()
while (line):
    if line[0]=='Monkey': 
        #line 1
        monkeys.append([])
        monkeysCount.append(0)
        index=int(line[1])
        
        #line 2
        line=f.readline().replace(',', '').split()
        for word in line[2:]:
            monkeys[index].append(int(word))

        #line 3
        line=f.readline().split()
        monkeyInfo=[]
        for word in line[3:]:
            monkeyInfo.append(word)

        #lines 4-6
        for __ in range(3):
            line=f.readline().split()
            monkeyInfo.append(int(line[-1]))

        monkeysInfo[index] = monkeyInfo
    
    f.readline()
    line=f.readline().replace(':', '').split()

for r in range(20):
    for monkeyIndex in range(len(monkeys)):
        for itemIndex in range(len(monkeys[monkeyIndex])):
            monkeysCount[monkeyIndex]+=1
            item = monkeys[monkeyIndex][itemIndex]
            op = monkeysInfo[monkeyIndex][1]
            arg = monkeysInfo[monkeyIndex][2]
            divisor = monkeysInfo[monkeyIndex][3]
            trueMonkey = monkeysInfo[monkeyIndex][4]
            falseMonkey = monkeysInfo[monkeyIndex][5]

            if(arg=='old'):
                item = operations[op](item, item)
            else:
                item = operations[op](item, int(arg))
            item=math.floor(item/3)
            monkeys[monkeyIndex][itemIndex] = item

            if (item%divisor==0):
                monkeys[trueMonkey].append(item)
            else:
                monkeys[falseMonkey].append(item)
        monkeys[monkeyIndex]=[]

first=max(monkeysCount)
monkeysCount.remove(first)
second=max(monkeysCount)
print('Monkey business level:', first*second)               
            
