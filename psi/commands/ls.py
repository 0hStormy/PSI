# ls.py

# Packages
import os
import json

# Read config file
f = open("psi/config.json", "r")
tmp_j = f.read()

cfginfo = json.loads(tmp_j)
usercwd = (cfginfo["usercwd"])

# Read args file
f = open("psi/cmd.temp")
args = f.read()
f.close()
args = args.split()
argslen = len(args)

# Check for a directory arg
if argslen == 2:
    if os.path.isdir((args[1])) == True:
        usercwd = (args[1])
    else:
        print("Invalid Directory")
        exit(1)

# Read file names
filelist = os.listdir(usercwd)
filelistlength = (len(filelist))

print("")
print("Files in " + usercwd)
print("------------------------")

for x in range(filelistlength):
    filename = (filelist[x])
    
    if '.' in filename:
        if filename.startswith('.'):
            print(filename)
        else:
            print(filename)
            
    else:
        print(filename)
        
        
        
print("------------------------")
print("")