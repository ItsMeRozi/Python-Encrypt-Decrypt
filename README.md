# File Encryption and Decryption Program

## Overview
A program for crypting and decrypting files in the current and upwards directories. Uses the `cryptography` module for encryption and decryption using Fernet symmetric key cryptography.

## Features
- Automatic installation of required modules
- Check for administrator privileges and elevate if necessary
- Recursive retrieval of all files in a directory
- Exclude specific files from encryption and decryption
- Print the list of files to be encrypted or decrypted
- Generate a new encryption key for each encryption process
- Save the key to a file for decryption
- Remove the key file after decryption

## How to Use
1. Run `crypt.py` to encrypt files in the current and upwards directories.
2. Run `decrypt.py` to decrypt files previously encrypted by `crypt.py`.
3. Follow on-screen prompts and observe the console output for details.
4. Check the list of files to be encrypted or decrypted before confirming the process.

## Latest Update
- 14.12.2023: Implemented file encryption and decryption using the Fernet symmetric key cryptography. Added key generation and removal functionality.

Feel free to customize the script to meet your specific encryption and decryption needs. Ensure that sensitive keys and decrypted files are handled securely.
