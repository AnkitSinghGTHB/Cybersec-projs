import hashlib
import os
import json
import sys
from datetime import datetime

# File to store baseline hashes
BASELINE_FILE = "baseline.json"

def calculate_hash(file_path, algorithm='sha256'):
    #Calculate hash of a file using specified algorithm
    try:
        if algorithm == 'sha256':
            hash_obj = hashlib.sha256()
        elif algorithm == 'md5':
            hash_obj = hashlib.md5()
        elif algorithm == 'sha1':
            hash_obj = hashlib.sha1()
        else:
            hash_obj = hashlib.sha256()
        
        with open(file_path, 'rb') as f:
            # Read file in 64KB chunks for memory efficiency
            while True:
                data = f.read(65536)
                if not data:
                    break
                hash_obj.update(data)
        
        return hash_obj.hexdigest()
    except Exception as e:
        print(f"Error calculating hash for {file_path}: {e}")
        return None

def create_baseline(directory_path):
    #Scan directory and create baseline of file hashes
    baseline = {}
    print(f"\n[*] Creating baseline for directory: {directory_path}")
    print("[*] Scanning files...\n")
    
    file_count = 0
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            
            # Calculate hash
            file_hash = calculate_hash(file_path)
            if file_hash:
                baseline[file_path] = {
                    'hash': file_hash,
                    'size': os.path.getsize(file_path),
                    'modified': os.path.getmtime(file_path)
                }
                file_count += 1
                print(f"  [+] Added: {file_path}")
    
    # Save baseline to JSON file
    with open(BASELINE_FILE, 'w') as f:
        json.dump(baseline, f, indent=4)
    
    print(f"\n[✓] Baseline created successfully!")
    print(f"[✓] Total files monitored: {file_count}")
    print(f"[✓] Baseline saved to: {BASELINE_FILE}\n")

def monitor_files(directory_path):
    #Compare current files against baseline
    if not os.path.exists(BASELINE_FILE):
        print(f"\n[!] Error: Baseline file '{BASELINE_FILE}' not found!")
        print("[!] Please create a baseline first.\n")
        return
    
    # Load baseline
    with open(BASELINE_FILE, 'r') as f:
        baseline = json.load(f)
    
    print(f"\n[*] Monitoring directory: {directory_path}")
    print("[*] Checking for changes...\n")
    
    modified_files = []
    new_files = []
    deleted_files = []
    unchanged_files = 0
    
    # Check existing files
    current_files = set()
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            current_files.add(file_path)
            
            # Calculate current hash
            current_hash = calculate_hash(file_path)
            if not current_hash:
                continue
            
            if file_path in baseline:
                # File exists in baseline - check if modified
                if current_hash != baseline[file_path]['hash']:
                    modified_files.append(file_path)
                    print(f"  [!] MODIFIED: {file_path}")
                else:
                    unchanged_files += 1
            else:
                # New file not in baseline
                new_files.append(file_path)
                print(f"  [+] NEW FILE: {file_path}")
    
    # Check for deleted files
    for file_path in baseline.keys():
        if file_path not in current_files:
            deleted_files.append(file_path)
            print(f"  [-] DELETED: {file_path}")
    
    # Summary
    print(f"\n{'='*60}")
    print("INTEGRITY CHECK SUMMARY")
    print(f"{'='*60}")
    print(f"  Unchanged files: {unchanged_files}")
    print(f"  Modified files:  {len(modified_files)}")
    print(f"  New files:       {len(new_files)}")
    print(f"  Deleted files:   {len(deleted_files)}")
    print(f"{'='*60}\n")
    
    if modified_files or new_files or deleted_files:
        print("[!] WARNING: Changes detected!")
    else:
        print("[✓] All files verified - No changes detected!")
    print()

def main(): #user interface    
    print("\n" + "="*60)
    print("         FILE INTEGRITY CHECKER")
    print("="*60)
    
    # Get directory path
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = input("\nEnter directory path to monitor (or press Enter for current directory): ").strip()
        if not directory:
            directory = os.getcwd()
    
    # Validate directory
    if not os.path.exists(directory):
        print(f"\n[!] Error: Directory '{directory}' does not exist!\n")
        return
    
    if not os.path.isdir(directory):
        print(f"\n[!] Error: '{directory}' is not a directory!\n")
        return
    
    # Menu
    print("\nSelect an option:")
    print("  1. Create new baseline")
    print("  2. Monitor files (check integrity)")
    print("  3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == '1':
        create_baseline(directory)
    elif choice == '2':
        monitor_files(directory)
    elif choice == '3':
        print("\nExiting...\n")
    else:
        print("\n[!] Invalid choice!\n")

if __name__ == "__main__":
    main()

# Example usage:
# create_baseline("path/to/directory", "baseline.json")
# verify_integrity("path/to/directory", "baseline.json")

#inputs:
#directory path - folder to monitor
#user choice - new baseline or mointor
#hash algo (optional) - default SHA-256, choices - SHA-1, MD5 or SHA-256

#outputs:
#baseline file - JSON file with file paths and their hashes
''' eg:
{
  "/path/to/file1.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41...",
  "/path/to/file2.pdf": "d41d8cd98f00b204e9800998ecf8427e..."
}
'''
#monitoring report - console output of modified, new, or deleted files
#modified files: List of files whose hashes changed (with old and new hash values)
#new files: Files that exist now but weren't in the baseline
#deleted files: Files in the baseline that no longer exist
#status messages: "OK" for unchanged files or "FAILED" for modified ones​
#console alerts or a report file summarizing all detected changes
'''eg: file1.txt: OK, file2.pdf: FAILED - Hash mismatch detected.'''