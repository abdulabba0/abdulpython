import os
import shutil
from datetime import datetime
import subprocess
import zipfile
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
def sync_directories(source_dir, dest_dir):
    """
    Synchronize files between source_dir and dest_dir.

    :param source_dir: Path to the source directory.
    :param dest_dir: Path to the destination directory.
    """
    try:
        # Check if source and destination directories exist
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)  # Create destination directory if it doesn't exist

        # Get the set of files in both directories
        source_files = {file for file in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, file))}
        dest_files = {file for file in os.listdir(dest_dir) if os.path.isfile(os.path.join(dest_dir, file))}

        # Copy files from source to destination
        for file in source_files:
            src_file = os.path.join(source_dir, file)
            dst_file = os.path.join(dest_dir, file)

            if file not in dest_files or os.path.getmtime(src_file) > os.path.getmtime(dst_file):
                shutil.copy2(src_file, dst_file)
                print(f"Copied: {file}")

        # Delete files in dest_dir that are not in source_dir
        for file in dest_files - source_files:
            os.remove(os.path.join(dest_dir, file))
            print(f"Deleted: {file}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print(f"Error: Permission denied when accessing directories.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


"""
Question 2: System Resource Monitor
Create a script monitor_resources.py that:
1.	Uses the subprocess module to run system commands like top (Linux/macOS) or tasklist (Windows) to list running processes.
2.	Parses the output to:
o	Display the top 5 processes consuming the most memory.
o	Display the top 5 processes consuming the most CPU.
3.	Write this information into a log file resource_log.txt.
Bonus: Schedule the script to run every minute using the os module to manipulate file timestamps as markers.
"""
# LOG_FILE = "resource_log.txt"
# INTERVAL = 60  # Time interval in seconds


# def get_process_info():
#     """
#     Get process information using platform-specific commands.
#     Returns:
#         processes (list of dict): List of process information containing PID, CPU, memory, and command.
#     """
#     processes = []
#     try:
#         # Determine the platform and execute appropriate command
#         if os.name == "nt":  # Windows
#             result = subprocess.run(
#                 ["tasklist", "/fo", "csv", "/v"],
#                 capture_output=True,
#                 text=True,
#                 check=True,
#             )
#             lines = result.stdout.splitlines()[1:]  # Skip the header
#             for line in lines:
#                 fields = line.split(",")
#                 # Memory and CPU usage are parsed for display, converting as necessary
#                 processes.append(
#                     {
#                         "pid": fields[1].strip('"'),
#                         "cpu": "N/A",  # CPU usage unavailable in tasklist
#                         "memory": int(fields[4].strip('"').replace(",", "")) * 1024,
#                         "command": fields[0].strip('"'),
#                     }
#                 )
#         else:  # Unix-based (Linux/macOS)
#             result = subprocess.run(
#                 ["ps", "-eo", "pid,pcpu,pmem,comm", "--sort=-%mem"],
#                 capture_output=True,
#                 text=True,
#                 check=True,
#             )
#             lines = result.stdout.splitlines()[1:]  # Skip the header
#             for line in lines:
#                 fields = line.split(None, 3)
#                 processes.append(
#                     {
#                         "pid": fields[0],
#                         "cpu": float(fields[1]),
#                         "memory": float(fields[2]),
#                         "command": fields[3],
#                     }
#                 )
#     except subprocess.SubprocessError as e:
#         print(f"Error executing system command: {e}")
#     return processes


# def log_top_processes():
#     """
#     Logs the top 5 processes consuming the most CPU and memory to a file.
#     """
#     processes = get_process_info()
#     if not processes:
#         return

#     # Sort processes by memory and CPU usage
#     top_memory = sorted(processes, key=lambda x: x["memory"], reverse=True)[:5]
#     top_cpu = sorted(processes, key=lambda x: x["cpu"], reverse=True)[:5]

#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     with open(LOG_FILE, "a") as log_file:
#         log_file.write(f"\n--- Resource Log at {timestamp} ---\n")
#         log_file.write("\nTop 5 Memory Consuming Processes:\n")
#         for proc in top_memory:
#             log_file.write(
#                 f"PID: {proc['pid']}, Memory: {proc['memory']} MB, Command: {proc['command']}\n"
#             )

#         log_file.write("\nTop 5 CPU Consuming Processes:\n")
#         for proc in top_cpu:
#             log_file.write(
#                 f"PID: {proc['pid']}, CPU: {proc['cpu']}%, Command: {proc['command']}\n"
#             )
#         log_file.write("\n")


# def main():
#     """
#     Main function to monitor system resources periodically.
#     """
#     print("Monitoring system resources. Press Ctrl+C to stop.")
#     try:
#         while True:
#             log_top_processes()
#             time.sleep(INTERVAL)
#     except KeyboardInterrupt:
#         print("\nMonitoring stopped.")


# if __name__ == "__main__":
#     main()

"""
Question 3: Create a File Backup System
Write a Python program backup_system.py that:
1.	Accepts a directory path to back up (source_dir) and a target directory for storing backups (backup_dir).
2.	Creates a zipped backup of source_dir in backup_dir with the current timestamp as the filename.
o	Example: backup_2024-11-11_10-30-00.zip
3.	Automatically deletes backups older than 7 days in backup_dir.
4.	Use shutil for file operations and the os module for cleanup.
Bonus: Use subprocess to run a command to check disk space before creating a backup.
"""

# def check_disk_space(target_dir):
#     """
#     Check available disk space for the target directory.
#     :param target_dir: Directory to check disk space.
#     :return: Available disk space in bytes.
#     """
#     try:
#         if os.name == 'nt':  # Windows
#             result = subprocess.run(['dir', target_dir], shell=True, capture_output=True, text=True)
#             lines = result.stdout.splitlines()
#             for line in lines:
#                 if 'bytes free' in line:
#                     return int(line.split()[0].replace(',', ''))
#         else:  # Linux/macOS
#             result = subprocess.run(['df', target_dir], capture_output=True, text=True, check=True)
#             lines = result.stdout.splitlines()
#             available_space = int(lines[1].split()[3]) * 1024  # Convert blocks to bytes
#             return available_space
#     except subprocess.SubprocessError as e:
#         print(f"Error checking disk space: {e}")
#         return 0

# def create_backup(source_dir, backup_dir):
#     """
#     Creates a zipped backup of the source directory in the backup directory.
#     :param source_dir: Path to the source directory to back up.
#     :param backup_dir: Path to the backup directory.
#     """
#     if not os.path.exists(source_dir):
#         print(f"Error: Source directory '{source_dir}' does not exist.")
#         return
#     if not os.path.exists(backup_dir):
#         os.makedirs(backup_dir)

#     # Check available disk space
#     available_space = check_disk_space(backup_dir)
#     required_space = sum(
#         os.path.getsize(os.path.join(root, file))
#         for root, _, files in os.walk(source_dir)
#         for file in files
#     )
#     if available_space and available_space < required_space:
#         print("Error: Not enough disk space for backup.")
#         return

#     # Create the backup file
#     timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#     backup_filename = f"backup_{timestamp}.zip"
#     backup_path = os.path.join(backup_dir, backup_filename)

#     try:
#         with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
#             for root, dirs, files in os.walk(source_dir):
#                 for file in files:
#                     file_path = os.path.join(root, file)
#                     arcname = os.path.relpath(file_path, start=source_dir)
#                     backup_zip.write(file_path, arcname)
#         print(f"Backup created: {backup_path}")
#     except Exception as e:
#         print(f"Error creating backup: {e}")

# def cleanup_old_backups(backup_dir, retention_days=7):
#     """
#     Deletes backups in the backup directory older than the specified retention period.
#     :param backup_dir: Path to the backup directory.
#     :param retention_days: Number of days to retain backups.
#     """
#     try:
#         cutoff_time = datetime.now() - timedelta(days=retention_days)
#         for file in os.listdir(backup_dir):
#             file_path = os.path.join(backup_dir, file)
#             if os.path.isfile(file_path) and file.startswith("backup_") and file.endswith(".zip"):
#                 file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
#                 if file_time < cutoff_time:
#                     os.remove(file_path)
#                     print(f"Deleted old backup: {file_path}")
#     except Exception as e:
#         print(f"Error cleaning up old backups: {e}")

# def main():
#     source_dir = input("Enter the source directory to back up: ").strip()
#     backup_dir = input("Enter the backup directory: ").strip()

#     print("\nStarting backup process...")
#     create_backup(source_dir, backup_dir)
#     print("Cleaning up old backups...")
#     cleanup_old_backups(backup_dir)
#     print("Backup process complete.")

# if __name__ == "__main__":
#     main()

"""
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
"""

# LOG_FILE = "rename_log.txt"

# def batch_rename(directory_path, prefix, reverse=False):
#     """
#     Renames or reverses renaming of all files in a directory.

#     :param directory_path: Path to the directory containing files.
#     :param prefix: Prefix to add to filenames.
#     :param reverse: If True, reverses the renaming operation using the log file.
#     """
#     if not os.path.exists(directory_path):
#         print(f"Error: Directory '{directory_path}' does not exist.")
#         return

#     if reverse:
#         reverse_rename(directory_path)
#         return

#     try:
#         with open(LOG_FILE, "a") as log_file:
#             for file in os.listdir(directory_path):
#                 file_path = os.path.join(directory_path, file)
#                 if os.path.isfile(file_path):  # Skip directories
#                     name, ext = os.path.splitext(file)
#                     new_name = f"{prefix}_{name}{ext}"
#                     new_file_path = os.path.join(directory_path, new_name)

#                     # Handle name collisions
#                     counter = 1
#                     while os.path.exists(new_file_path):
#                         new_name = f"{prefix}_{name}_{counter}{ext}"
#                         new_file_path = os.path.join(directory_path, new_name)
#                         counter += 1

#                     # Rename the file
#                     os.rename(file_path, new_file_path)
#                     log_file.write(f"{new_file_path},{file_path}\n")  # Log the renaming
#                     print(f"Renamed: {file} -> {new_name}")
#     except Exception as e:
#         print(f"Error during renaming: {e}")


# def reverse_rename(directory_path):
#     """
#     Reverses the renaming of files based on the log file.

#     :param directory_path: Path to the directory containing files.
#     """
#     if not os.path.exists(LOG_FILE):
#         print(f"Error: Log file '{LOG_FILE}' not found.")
#         return

#     try:
#         with open(LOG_FILE, "r") as log_file:
#             lines = log_file.readlines()

#         updated_lines = []
#         for line in lines:
#             new_path, original_path = line.strip().split(",")
#             if os.path.exists(new_path):
#                 os.rename(new_path, original_path)
#                 print(f"Reversed: {os.path.basename(new_path)} -> {os.path.basename(original_path)}")
#             else:
#                 updated_lines.append(line)  # Keep entries for files not found

#         # Update log file
#         with open(LOG_FILE, "w") as log_file:
#             log_file.writelines(updated_lines)
#     except Exception as e:
#         print(f"Error during reverse renaming: {e}")


# Example Usage:
# Forward renaming:
# batch_rename("/path/to/directory", "prefix")

# Reverse renaming:
# batch_rename("/path/to/directory", "prefix", reverse=True)

"""
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
# LOG_FILE = "git_log.txt"

# def log_message(message):
#     """Logs a message with a timestamp to the log file."""
#     timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     with open(LOG_FILE, "a") as log_file:
#         log_file.write(f"[{timestamp}] {message}\n")
#     print(message)

# def run_command(command, cwd=None):
#     """
#     Runs a shell command and captures the output.
#     :param command: List of command arguments.
#     :param cwd: Directory to execute the command.
#     :return: Output of the command.
#     """
#     try:
#         result = subprocess.run(
#             command, cwd=cwd, capture_output=True, text=True, check=True
#         )
#         log_message(f"Command succeeded: {' '.join(command)}")
#         return result.stdout.strip()
#     except subprocess.CalledProcessError as e:
#         log_message(f"Command failed: {' '.join(command)}")
#         log_message(f"Error: {e.stderr.strip()}")
#         raise


# def clone_repository(repo_url, target_dir):
#     """
#     Clones a Git repository to the specified directory.
#     :param repo_url: URL of the repository.
#     :param target_dir: Directory to clone into.
#     """
#     try:
#         if os.path.exists(target_dir):
#             log_message(f"Directory {target_dir} already exists. Skipping clone.")
#         else:
#             run_command(["git", "clone", repo_url, target_dir])
#             log_message(f"Repository cloned from {repo_url} to {target_dir}")
#     except Exception as e:
#         log_message(f"Failed to clone repository: {e}")


# def switch_branch(repo_dir, branch_name):
#     """
#     Checks the current branch and switches to a new branch if specified.
#     :param repo_dir: Path to the repository directory.
#     :param branch_name: Name of the branch to switch to.
#     """
#     try:
#         current_branch = run_command(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo_dir)
#         log_message(f"Current branch: {current_branch}")

#         if branch_name and branch_name != current_branch:
#             run_command(["git", "checkout", "-b", branch_name], cwd=repo_dir)
#             log_message(f"Switched to new branch: {branch_name}")
#     except Exception as e:
#         log_message(f"Failed to switch branch: {e}")


# def stage_and_commit(repo_dir, commit_message):
#     """
#     Stages and commits all changes in the repository.
#     :param repo_dir: Path to the repository directory.
#     :param commit_message: Commit message to use.
#     """
#     try:
#         run_command(["git", "add", "."], cwd=repo_dir)
#         run_command(["git", "commit", "-m", commit_message], cwd=repo_dir)
#         log_message(f"Changes committed with message: {commit_message}")
#     except subprocess.CalledProcessError as e:
#         if "nothing to commit" in e.stderr:
#             log_message("No changes to commit.")
#         else:
#             raise


# def push_changes(repo_dir, remote="origin", branch=None):
#     """
#     Pushes changes to the remote repository.
#     :param repo_dir: Path to the repository directory.
#     :param remote: Name of the remote (default is 'origin').
#     :param branch: Name of the branch to push (default is current branch).
#     """
#     try:
#         if not branch:
#             branch = run_command(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo_dir)

#         run_command(["git", "push", remote, branch], cwd=repo_dir)
#         log_message(f"Changes pushed to {remote}/{branch}")
#     except Exception as e:
#         log_message(f"Failed to push changes: {e}")


# def main():
#     repo_url = input("Enter the repository URL: ").strip()
#     target_dir = input("Enter the target directory to clone into: ").strip()
#     branch_name = input("Enter the branch name (leave blank to skip branch switch): ").strip()
#     commit_message = input("Enter the commit message: ").strip()

#     try:
#         # Clone the repository
#         clone_repository(repo_url, target_dir)

#         # Switch to the specified branch
#         if branch_name:
#             switch_branch(target_dir, branch_name)

#         # Stage and commit changes
#         stage_and_commit(target_dir, commit_message)

#         # Push changes to the remote repository
#         push_changes(target_dir)
#     except Exception as e:
#         log_message(f"An error occurred: {e}")


# if __name__ == "__main__":
#     main()
