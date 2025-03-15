# FILE-INTEGRITY-CHECKER
 A TOOL TO MONITOR CHANGES  IN FILES BY CALCULATING AND  COMPARING HASH VALUES. 
 COMPANY: CODTECH IT SOLUTIONS 
 NAME : SHURAIM SHAKEEL BHAT
 INTERN  ID : CT08TPH
 DOMAIN : CYBER SECURITY AND ETHICAL HACKING
 DURATION : 4 WEEKS
 MENTOR : NEELA SANTOSH<br>
 


## Overview
The **File Integrity Checker** is a Python-based tool that monitors and verifies the integrity of files within a directory by computing and comparing hash values. It helps detect unauthorized modifications, accidental changes, or missing files. The tool leverages the `hashlib` library to generate cryptographic hashes (SHA-256 by default) and stores them in a JSON file for future integrity checks.

## Features
- **Hash Calculation**: Uses SHA-256 (or other specified algorithms) to generate unique hash values for files.
- **Save Hashes**: Stores computed hash values in a JSON file for future verification.
- **Integrity Checking**: Compares current file hashes with stored values to detect changes, deletions, or unauthorized modifications.
- **Easy-to-Use Interface**: Simple command-line interface for quick operation.
- **Recursive Directory Scanning**: Supports hashing all files within a given directory, including subdirectories.

## How It Works
The tool follows a simple workflow:
1. **Generate Hashes**: The script scans all files in a directory and calculates their hashes.
2. **Save Hashes**: These hashes are stored in a JSON file (`hashes.json`).
3. **Check Integrity**: The script compares stored hashes with newly computed hashes to identify modified or missing files.

## Installation
### Prerequisites
Ensure you have Python installed on your system (Python 3.x recommended).

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/file-integrity-checker.git
   cd file-integrity-checker
   ```
2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt  # Not required if using built-in Python libraries
   ```

## Usage
Run the script from the command line:

### 1. Saving Hashes
To generate and save hashes for files in a directory:
```bash
python file_integrity_checker.py
```
- Select option `1` when prompted.
- Enter the directory path to scan.
- The script will generate and store hashes in `hashes.json`.

### 2. Checking File Integrity
To verify the integrity of files:
```bash
python file_integrity_checker.py
```
- Select option `2` to check file integrity.
- The script will compare current hashes with stored values and notify you of any changes.

## Output Messages
- **[UNCHANGED]** – File is intact.
- **[MODIFIED]** – File content has been altered.
- **[MISSING]** – File has been deleted or moved.
- **[NEW]** – A new file has been added.

## Customization
- You can modify the default hashing algorithm (e.g., MD5, SHA-1, SHA-256) by updating the `calculate_hash` function in `file_integrity_checker.py`.
- Change the hash storage file (`hashes.json`) if needed.

## Why Use This Tool?
- **Security**: Detect unauthorized modifications to critical files.
- **Backup Verification**: Ensure backups have not been altered.
- **Data Integrity**: Prevent accidental changes in software projects.



