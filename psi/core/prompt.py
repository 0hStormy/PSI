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
AllowNonPSICMDS = (cfginfo["non_psi_cmds"])
ColorExist = (cfginfo["color"])

# Read temp file
with open('psi/psi.temp', 'r') as f:
    tmp_j = f.read()

    cfginfo = json.loads(tmp_j)
    CommandCwd = (cfginfo["cwd"])

# Welcome message
print(welcomemsg)
print("Licenced under GNU GPL 2.0")
print("Version " + psiversion)
print("")

# Checks if color is enabled
if ColorExist == True:
    from colorama import Fore, Back, Style
    cBlue = Fore.LIGHTBLUE_EX
    cGreen = Fore.LIGHTGREEN_EX
    cRed = Fore.LIGHTRED_EX
    cNone = Style.RESET_ALL
else:
    cBlue = ''
    cGreen = ''
    cRed = ''
    cNone = ''
        
# Prompt loop
while working:
    
    # Read config file
    f = open("psi/config.json", "r")
    tmp_j = f.read()

    cfginfo = json.loads(tmp_j)
    usercwd = (cfginfo["usercwd"])
    
    command = input(f'{cGreen}{usercwd}{cBlue}:{cNone}$ ')
    shellCommand = command
    
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
        if AllowNonPSICMDS == True:
            os.chdir(usercwd)
            os.system(shellCommand)
            os.chdir(CommandCwd)
        else:
            print(f"{cRed}The command {command.replace('psi/commands/', '')} does not seem to exist.")