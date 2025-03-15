import hashlib
import os
import json

def calculate_hash(file_path, algorithm='sha256'):
    """Calculate the hash of a file using the specified algorithm."""
    hasher = hashlib.new(algorithm)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

def save_hashes(directory, hash_file='hashes.json', algorithm='sha256'):
    """Save hashes of all files in a directory to a JSON file."""
    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path, algorithm)
            if file_hash:
                hashes[file_path] = file_hash
    with open(hash_file, 'w') as f:
        json.dump(hashes, f, indent=4)
    print("Hashes saved successfully.")

def check_integrity(hash_file='hashes.json', algorithm='sha256'):
    """Check the integrity of files by comparing their current hashes with saved hashes."""
    try:
        with open(hash_file, 'r') as f:
            saved_hashes = json.load(f)
        
        for file_path, old_hash in saved_hashes.items():
            new_hash = calculate_hash(file_path, algorithm)
            if new_hash is None:
                print(f"[MISSING] {file_path} has been deleted or moved.")
            elif new_hash != old_hash:
                print(f"[MODIFIED] {file_path} has been altered!")
            else:
                print(f"[UNCHANGED] {file_path} is intact.")
    except FileNotFoundError:
        print("Error: Hash file not found. Please generate hashes first.")

def main():
    """Main function to handle user input."""
    print("File Integrity Checker")
    print("1. Save hashes of files in a directory")
    print("2. Check file integrity")
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        directory = input("Enter the directory path: ")
        save_hashes(directory)
    elif choice == '2':
        check_integrity()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
