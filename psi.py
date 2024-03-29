# psi.py

# Packages
import os
import json
import subprocess

# Define Functions

# Make config
def psi_makecfg():
    configcontents = {
        "welcome_message": "Python Shell Interface (PSI)",
        "usercwd": os.path.expanduser('~'),
        "version": "0.1.0-dev",
        "path": "psi/commands/",
        "non_psi_cmds": False,
        "color": True,
    }

    cfgdump = json.dumps(configcontents, indent=4)
    f = open("psi/config.json", "w+")
    f.write(cfgdump)
    f.close()

# Make tempfile
def psi_tempfile():
    tmpcontents = {
        "cwd": os.getcwd(),
    }

    cfgdump = json.dumps(tmpcontents, indent=4)
    f = open("psi/psi.temp", "w+")
    f.write(cfgdump)
    
if os.path.isfile('psi/config.json') == False:
    psi_makecfg()

# Create tempfile
psi_tempfile()

subprocess.run(["python", "psi/core/prompt.py"])
