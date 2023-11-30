# prompt.py

# Packages
import os
import subprocess
import json

# Declare variables
working = True

# Clear Screen
os.system("cls")

# Read config file
f = open("psi/config.json", "r")
tmp_j = f.read()

cfginfo = json.loads(tmp_j)

welcomemsg = (cfginfo["welcome_message"])
psiversion = (cfginfo["version"])
PATH = (cfginfo["path"])

# Welcome message
print(welcomemsg)
print("Licenced under GNU GPL 2.0")
print("Version " + psiversion)
print("")

# Prompt loop
while working:
    
    # Read config file
    f = open("psi/config.json", "r")
    tmp_j = f.read()

    cfginfo = json.loads(tmp_j)
    usercwd = (cfginfo["usercwd"])
    
    command = input(usercwd + "$ ")
    
    #Checks if Exit command
    if command == 'exit':
        working = False
        exit(0)
    
    command = 'psi/commands/' + command
    
    
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