"""
Question 1: Directory Synchronization
Write a Python function sync_directories that:
1.	Accepts two directory paths (source_dir and dest_dir).
2.	Copies all files from source_dir to dest_dir.
o	If a file in source_dir is newer than the one in dest_dir, overwrite it.
o	If a file exists in dest_dir but not in source_dir, delete it.
3.	Use the os and shutil modules to handle file operations.
Bonus: Add error handling to handle cases where directories do not exist or access is denied.
"""
import os
import shutil
from datetime import datetime

def sync_directories(source_dir, dest_dir):
    """
    Synchronize two directories by copying, overwriting, or deleting files.

    Args:
        source_dir (str): Path to the source directory.
        dest_dir (str): Path to the destination directory.
    """
    try:
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")
        if not os.path.exists(dest_dir):
            raise FileNotFoundError(f"Destination directory '{dest_dir}' does not exist.")
    except FileExistsError as e:
        print("Cannot locate destination directory '{dest_dir}")
    else :
        print("Both directory existed")

    # Listing filies and destination directories
    try :
        source_files = {f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))}
        dest_files = {f for f in os.listdir(dest_dir) if os.path.isfile(os.path.join(dest_dir, f))}
    except :
        print(f"There was an error {e}")
    finally :
        print("Listing files in source and destination directories")
        print("source files:", source_files)
        print("destination files:", dest_files) 

# Deleting files in the destination directory
    try :
        for file in dest_files :
            if file not in source_files :
                os.remove(os.path.join(dest_dir, file))
            print(f"Deleted: {file}")
    except Exception as e :
        print(f"Error deleting files {e}")
# Move files from the source directory to the destination directory
    try:
        for file in dest_files :
            src_file = os.path.kion(source_dir, file)
            dest_file = os.path.kion(dest_dir, file)
            print(src_file)

        if not os.path.exists(dest_file) or os.path.getmtime(src_file) > os.path.getmtime(dest_file):
            shutil.copy2(src_file, dest_file)
            print(f"Copied or updtaed: {file}")
    except Exception as e :
        print(f"Error copying files {e}")                                                                                    

source = input("Enter the source directory path: ")
dest = input("Enter the destination directory path: ")
sync_directories(source, dest)

"""
________________________________________
Question 2: System Resource Monitor
Create a script monitor_resources.py that:
1.	Uses the subprocess module to run system commands like top (Linux/macOS) or tasklist (Windows) to list running processes.
2.	Parses the output to:
o	Display the top 5 processes consuming the most memory.
o	Display the top 5 processes consuming the most CPU.
3.	Write this information into a log file resource_log.txt.
Bonus: Schedule the script to run every minute using the os module to manipulate file timestamps as markers.
________________________________________
Question 3: Create a File Backup System
Write a Python program backup_system.py that:
1.	Accepts a directory path to back up (source_dir) and a target directory for storing backups (backup_dir).
2.	Creates a zipped backup of source_dir in backup_dir with the current timestamp as the filename.
o	Example: backup_2024-11-11_10-30-00.zip
3.	Automatically deletes backups older than 7 days in backup_dir.
4.	Use shutil for file operations and the os module for cleanup.
Bonus: Use subprocess to run a command to check disk space before creating a backup.
________________________________________
Question 4: Batch File Renamer
Write a Python function batch_rename that:
1.	Accepts a directory path and a prefix.
2.	Renames all files in the directory to include the given prefix, maintaining the original file extension.
o	Example: file1.txt becomes prefix_file1.txt.
3.	Handles the following:
o	If a file already exists with the new name, append a unique number to avoid overwriting (e.g., prefix_file1_1.txt).
o	Skip directories in the specified path.
4.	Use the os module for directory traversal and renaming.
Bonus: Allow the script to reverse the renaming operation using a log file to track original names.
________________________________________
Question 5: Automating Git Operations
Write a script git_automation.py that:
1.	Automates common Git operations using the subprocess module.
2.	The script should:
o	Clone a repository from a given URL to a specified directory.
o	Check the current branch and switch to a new branch if specified.
o	Stage and commit all changes in the working directory with a custom commit message.
o	Push changes to the remote repository.
3.	Add error handling for common Git issues, such as:
o	Invalid repository URL.
o	Merge conflicts when switching branches or pushing changes.
o	Permission errors.
Bonus: Log all actions performed and errors encountered into a file git_log.txt.


"""