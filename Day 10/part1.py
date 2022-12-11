import os

f = open(os.getcwd()+'/input.txt')
clock=0
register=1
signal=0

for line in f:
    line=line.split()
    match line[0]:
        case 'noop':
            clock+=1
            signal+=clock*register if clock in [20,60,100,140,180,220] else 0
        case 'addx':
            clock+=1
            signal+=clock*register if clock in [20,60,100,140,180,220] else 0
            clock+=1
            signal+=clock*register if clock in [20,60,100,140,180,220] else 0
            register+=int(line[1])

print(signal)