# echo.py

# Packages
import json

# Read config file
f = open("psi/config.json", "r")
tmp_j = f.read()

cfginfo = json.loads(tmp_j)
PATH = (cfginfo["path"])

# Read args file
f = open("psi/cmd.temp")
args = f.read()
f.close()
argscheck = args.split()
argslen = len(argscheck)

# Check for a directory arg
if argslen >= 2:
    echomsg = args.replace(PATH + 'math ', '')
    echomsg = eval(echomsg)
    print(echomsg)
       
else:
    print("Missing Args (Please add an equation)")