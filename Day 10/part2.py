import os

f = open(os.getcwd()+'/input.txt')
clock=0
register=1

for line in f:
    line=line.split()

    clock+=1
    if((clock-1)%40>=register-1 and (clock-1)%40<=register+1):
        print('#', end='')
    else: print('.', end='')
    if clock%40==0: print()

    if(line[0]=='noop'): continue

    clock+=1
    if ((clock-1)%40>=register-1 and (clock-1)%40<=register+1):
        print('#', end='')
    else: print('.', end='')

    register+=int(line[1])
    if clock%40==0: print()