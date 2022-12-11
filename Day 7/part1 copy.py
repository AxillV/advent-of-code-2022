# import os 

# def addDir(newDir):
#     if newDir not in files:
#             files[newDir] = '-'
#             if workingDir == None: return
#             if (files[workingDir] == '-'):
#                 files[workingDir] = dir
#                 return
             
# #working directory, command
# def parseCommand(wd, cmd):
#     match cmd[2:4]:
#         case 'cd':
#             dir = cmd[5:-1]
#             addDir(dir)
#             cmd = f.readline()
#             return dir    

#         case 'ls':
#             cmd = f.readline()
#             while cmd[0]!='$':
#                 if cmd[0:4]=='dir':
#                     addDir(cmd[4:-1])

# f = open(os.getcwd()+"\Day 7\\input.txt", "r")
# line = f.readline()
# workingDir = None
# files={}
# sizes={}

# while line:
#     workingDir=parseCommand(workingDir, line)
# f.close()
