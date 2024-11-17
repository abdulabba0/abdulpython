import os
import shutil

os.mkdir("TextFolder")
# os.mkdir("folder2")

# Deleting a file
for files in os.listdir():
    if files.endswith(".txt"):
        shutil.move(files, "TextFolder")