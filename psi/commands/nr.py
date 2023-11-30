# nitro.py

import json
import subprocess
import os

# Read config file
f = open("psi/config.json", "r")
tmp_j = f.read()

cfginfo = json.loads(tmp_j)
userdir = (cfginfo["usercwd"])
PATH = (cfginfo["path"])

# Read args file
f = open("psi/cmd.temp")
args = f.read()
f.close()
args = args.split()
argslen = len(args)

# Check for a directory arg
if argslen == 2:
    nitrofile = userdir + "/" + (args[1])
    f = open(nitrofile, "r")
    nitrocontents = f.readlines()
    f.close()
    
    scriptlen = len(nitrocontents)
    
    # Read each line of the file
    for x in range(scriptlen):
        filename = (nitrocontents[x])
        command = PATH + filename
    
        # Write command to temp file
        f = open("psi/cmd.temp", "w")
        f.write(command)
        f.close()
        
        command = command.split()
        command = (command[0] + ".py")

        
        if os.path.isfile(command):
            subprocess.run(["python", command])

        else:
            print("Command does not exist")

print("")    