# lsdir.py

# Packages
import json

# Read config file
f = open("psi/config.json", "r")
tmp_j = f.read()

cfginfo = json.loads(tmp_j)
usercwd = (cfginfo["usercwd"])

print("You are in -*" + usercwd)