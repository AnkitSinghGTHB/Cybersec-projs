pip install -r requirements.txt

# What is a Baseline?

A baseline is a snapshot of your files in their trusted, unaltered state. It's essentially a reference point that captures what your files look like when everything is correct and safe. The baseline stores the cryptographic hash (unique fingerprint) of each file along with metadata like file size, permissions, and modification time.​

Think of it like taking a photograph of your files at a specific moment in time, this becomes your "known good" state that you'll compare against later.​

## How the Project Works

### Phase 1: Creating the Baseline

When you first run the program, it scans your chosen directory and calculates a hash for every file. These hashes are stored in a file (like baseline.json) along with file paths. This creates your trusted reference point showing what all files should look like when untampered.​

### Phase 2: Monitoring for Changes

Later, you run the verification function which recalculates hashes for the same files. The program compares the new hashes against your stored baseline. Any differences indicate the file has been modified, corrupted, or tampered with.​

### Phase 3: Detecting Changes

The checker identifies three types of changes:​

- Modified files: Hash differs from baseline (file content changed)
- New files: File exists now but wasn't in the baseline
- Deleted files: File was in baseline but is now missing

When discrepancies are detected, the program generates alerts or reports so you can investigate unauthorized changes.

# How to use?

- Run the file
- Select option 1 (create baseline) and enter director path to monitor
- Now run the file again, select option 2 to verify integrity of the file
