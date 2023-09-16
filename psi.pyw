# psi.py

# Packages
import sys
import os
import json

# Define Variables


# Define Functions

def psi_makecfg():

    configcontents = {
    "version": "0.1.0-DEV",
    "welcome_message": "Welcome to PSI Version",
    }

    cfgdump = json.dumps(configcontents)
    print(cfgdump)

psi_makecfg()