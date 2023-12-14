"""
Program for decrypting files in the current and upwards directories.
Latest update: 14.12.2023
"""

# Import necessary modules
import ctypes
import sys
import importlib
import subprocess
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
            print(f'Failed to install module {module}: {e}')

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

# Print the list of files to be decrypted
print(files)

# Read the encryption key from the key file
with open("key.key", "rb") as key_file:
    secret_key = key_file.read()

# Decrypt each file with the stored key
for file in files:
    with open(file, "rb") as the_file:
        contents = the_file.read()
    content_decrypted = Fernet(secret_key).decrypt(contents)
    with open(file, "wb") as the_file:
        the_file.write(content_decrypted)

# Remove the key file after decryption
os.remove("key.key")
