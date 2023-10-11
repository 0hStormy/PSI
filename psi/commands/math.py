# echo.py

# Packages
from termcolor import colored, cprint
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
    cprint(echomsg, 'light_green')
       
else:
    cprint("Missing Args (Please add an equation)", "red")