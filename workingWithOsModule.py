import os
import shutil
import subprocess

# print(dir(os))
# Get the list of files in the specified directory
# print(os.listdir("c://"))

# Check current working directory
# print(os.getcwd())

# Changing a directory
os.chdir("c://users/abdul abba/documents/abdulpython")

# Making a directory
# os.makedir("coding2/CodingClass", mode=511, exist_ok=True)

# Making  directories
# os.makedirs("coding2/CodingClass", mode=511, exist_ok=True)

# Removing a folder
# os.rmdir("coding2")

# Removing folders
# os.removedirs("coding2/CodingClass")

# Removing a file
# os.remove("index.txt")

# Display of CPU cores
# print(os.cpu_count())

# Checking if a file exists
# print(os.path.exists("pythonFile.py"))

# Checking information about a file
# print(os.stat("pythonFile.py"))

# Renaming a file
# os.rename("pythonFile.py", "pythonFiles.py")

# Listing the drives
# print(os.listdrives())

# Scanning through a directory
# with os.scandir() as dir :
#     for entry in dir :
#         if entry.is_file() :
#             print(entry.name)
            # print(entry.stat())

# using environment
# os.environ["HOME"] = "This is Great!"
# print(os.environ.get("HOME"))

# Working with the shell
# os.system("dir")
# os.system("ping www.google.com")

# Capturing the output of a commad on the shell implemented in python
# res = subprocess.run("dir", capture_output=True, shell=True, text=True)

# with open("index.txt", "w") as f :
#        f.write(res.stdout)

# for dirpath, directoryname, directoryfiles in os.walk("c://users/abdul abba/pictures") :
#     print(dirpath, directoryname, directoryfiles)
#     for filename in directoryfiles :
#         print(os.path.join(dirpath, filename))
#     for dirname in directoryname :
#         print(os.path.join(dirpath, dirname))

pdf = []
dirpath = "c://users/abdul abba/documents"
for files in os.listdir(dirpath):
    if files.endswith(".pdf"):
        pdf.append(os.path.join(dirpath,))

print(pdf)