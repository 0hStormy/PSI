# lsdir.py

# Packages
from termcolor import cprint
import json

# Read config file
f = open("psi/config.json", "r")
tmp_j = f.read()

cfginfo = json.loads(tmp_j)
usercwd = (cfginfo["usercwd"])

cprint("You are in -*" + usercwd, 'light_green')