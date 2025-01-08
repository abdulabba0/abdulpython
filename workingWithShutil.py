import os
import shutil
from datetime import datetime

# os.mkdir("TextFolder")
# os.mkdir("folder2")

# Deleting a file
# for files in os.listdir():
#     if files.endswith(".txt"):
#         shutil.move(files, "TextFolder")

# # copy a file to a file
# shutil.copy(index.txt, output.txt)


# index_createDate = datetime.fromtimestamp(os.stat("index.txt").st_atime)
# output_createDate = datetime.fromtimestamp(os.stat("output.txt").st_atime)

# print(f"index.txt file stat + {index_createDate}")
# print(" ")
# print("=" * 10)
# print(f"output.txt file stat + {output_createDate}")

# #moving a file
# shutil.move("output.txt", "TextFolder")

# # removing a file
# os.remove("output.txt")

# # removing a file
# try :
#     os.remove("output.txt")
# except Exception as e :
#     print("error removing this file {}".format(e))

# removing a directory
# try :
#     os.mkdir("TextFolder2")
# except Exception as e :
#     print("error creating this directory {}".format(e))
# else :
#     print("Directory removed successfully")

# try :
#     shutil.rmtree("TextFolder2")
# except Exception as e :
#     print("error removing this directory {}".format(e))
# else :
#     print("Folder removed removed using shutil")

# Check Available sapace on your pc
# print(f"Total space : {shutil.disk_usage("/").total / 2**30)
# print(f"Used space : {shutil.disk_usage("/").total / 2**30)
# print(f"Free space : {shutil.disk_usage("/").total / 2**30)

#archving a Folder

# shutil.make_archive("abdulArchive", "zip", "../abdulpython")

# Unpacking a archived file
# shutil.unpack_archive("abdulArchive.zip", "abdulPython", "zip")

print(dir(shutil))
shutil.make_archive("abdulArchive", "zip", "../abdulpython")
