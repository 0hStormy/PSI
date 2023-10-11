# ls.py

# Packages
import os
import json
from termcolor import colored, cprint

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
        cprint("Invalid Directory", "red")
        exit(1)

# Read file names
filelist = os.listdir(usercwd)
filelistlength = (len(filelist))

print("")
cprint("Files in " + usercwd, "yellow")
print("------------------------")

for x in range(filelistlength):
    filename = (filelist[x])
    
    if '.' in filename:
        if filename.startswith('.'):
            cprint(filename, 'magenta')
        else:
            cprint(filename, 'light_green')
            
    else:
        cprint(filename, 'light_blue')
        
        
        
print("------------------------")
print("")