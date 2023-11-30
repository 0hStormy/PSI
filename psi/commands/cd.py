# cd.py

# Packages
import os
import json
import time

# Read config file
f = open("psi/config.json", "r")
tmp_j = f.read()

cfginfo = json.loads(tmp_j)
welcome_message = (cfginfo["welcome_message"])
usercwd = (cfginfo["usercwd"])
version = (cfginfo["version"])
path = (cfginfo["path"])

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

if argslen == 1:
    print("No provided directory")

configcontents = {
    "welcome_message": welcome_message,
    "usercwd": usercwd,
    "version": version,
    "path": path,
}

cfgdump = json.dumps(configcontents, indent=4)
f = open("psi/config.json", "w+")
f.write(cfgdump)
f.close()