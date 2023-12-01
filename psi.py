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
        "usercwd": os.getcwd(),
        "version": "0.1.0-dev",
        "path": "psi/commands/ psi/extensions",
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
    
psi_makecfg()

# Create tempfile
psi_tempfile()

subprocess.run(["python", "psi/core/prompt.py"])
