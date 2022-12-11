import os 
import collections.abc

def printFiles(dir, level):
    tempFiles=[]
    try:
        throughFiles  = files[dir][1:]
    except KeyError:
        throughFiles = None

    for item in throughFiles:
        try:
            throughFile  = files[item][1:]
        except KeyError:
            throughFile = None

        if not isinstance(throughFile, collections.abc.Sequence):
            tempFiles.append(item) 
        else: 
            print(' '*level+'-'+item)
            printFiles(item, level+1)

    for file in tempFiles:
            print(' '*level+'-'+file)    

def updateSize(upDir, sizeDifference):
    files[upDir][0][1]+=sizeDifference

    
    if files[upDir][0] == '/' and upDir == '/':
        return
    updateSize(files[upDir][0][0], sizeDifference)


f = open(os.getcwd()+"\Day 7\\input.txt", "r")
f.readline()
line = f.readline()
workingDir = '/'
files={'/':[['/', 0]]} 

while line:
    #parse command
    match line[2:4]:
        case 'cd':
            # dir = line[5:-1]
            # #add dir
            # if dir not in files:
            #     files[dir] = '-'
            # if workingDir == None: 
            #     line = f.readline()
            #     workingDir = dir  
            #     continue
            # if (files[workingDir] == '-'):
            #     files[workingDir] = dir
            #     line = f.readline()
            #     workingDir = dir  
            #     continue
            # else:
            #     files[workingDir].append(dir)
            #     line = f.readline()
            #     workingDir = dir
            if line[5:7]=='..':
                workingDir=files[workingDir][0]
            else:
                workingDir = line[5:-1]
            line = f.readline()

        case 'ls':
            line = f.readline()
            while line and line[0]!='$':
                #directory
                if line[0:3]=='dir':
                    dir = line[4:-1]
                    #add dir
                    if dir not in files:
                        #first item is always the parent dir, second size
                        files[dir] = [[workingDir, 0]]
                    # if workingDir == None: 
                    #     line = f.readline()
                    #     #workingDir = dir  
                    #     continue
                    files[workingDir].append(dir)
                    line = f.readline()
                    #workingDir = dir  

                #file
                else:
                    line=line.split()
                    size = int(line[0])
                    name = line[1]
                    #add file
                    files[workingDir].append([name, size])

                    # if (files[workingDir] == '-'):
                    #     files[workingDir] = [name]
                    #     line = f.readline()
                    #     #workingDir = dir  
                    #     continue
                    # else:
                    #     files[workingDir].append(name)
                    #     line = f.readline()
                    #     #workingDir = dir  
                    
                    updateSize(workingDir, size)
                    line = f.readline()

f.close()
count=0
for item in sizes:
    if item in files and sizes[item]<= 100000:
        count+=sizes[item]
printFiles('/',0)
