r'''

This is an alternative to "pip install -r requirements.txt"* that do not will
stop running if a package cannot be installed.

From CMD run:  
> pip-try.py "path\to\your\requirements.txt"

*The requirementes.txt file have the name and version of the installed python
packages. Is usually obtained running in CMD "pip freeze > requirements.txt"

'''

import subprocess
import sys
import os.path

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# -----------------------------------------------------------------------------
# Get requirements.txt path
# -----------------------------------------------------------------------------

if len(sys.argv) == 2:
    req = sys.argv[-1]
else:
    req = input('Insert the path to requirements txt file: ')

if not os.path.isfile(req):
    err = '\n  Error: '+f'"{req}" is not a file.'
    sys.exit(err) 

if not req.endswith('.txt'): 
    err = '\n  Error: '+f'"{req}" is not a txt file'
    sys.exit(err)

# -----------------------------------------------------------------------------
# Install packages
# -----------------------------------------------------------------------------

f = open(req,'r')

not_installed = []
for package in f:
    try:
        install(package)    
    except Exception:
        not_installed.append(package)    

f.close()

# -----------------------------------------------------------------------------
# Print results
# -----------------------------------------------------------------------------

if len(not_installed)>0:
    print('\n'+'-'*79)
    print('Failed to install the following packages:')
    print('-'*79+'\n')
    for n in not_installed:
        print(package.replace('\n',''))
else:
    print('\n'+'-'*79)
    print('Ok')
    print('-'*79)


