
# detected errors in the path or existing files

# import os

# path = "C:\\Users\\Oleksii\\Desktop\\text"

# if os.path.exists(path):
#     print("That location exists!")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory!")
# else:
#     print("That location not find!")

# ---------------------------------------------------------------

# try:
#     with open('test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not fund!")

# -------------------------------------------------------------------

# text = "\nThis one more string"

# with open ('test1.txt', 'w') as file:
#     file.write(text)

#--------------------------------------------------------------------

# copyfile() = copies contents of a file
# copy()     = copyfile() + permission mode + destination can be a derectory
# copy2()    = copy() + copies metadata (file's creatiion and modification times)

# import shutil

# shutil.copyfile('test.txt', 'copy.txt') # src, destination
# shutil.copy('test.txt', 'C:\\Users\\Oleksii\\Desktop\\copy.txt') # copy to the desktop

# -------------------------------------------------------------------
# how to move file

# import os

# source = "test.txt"
# destination = "C:\\Users\\Oleksii\\Desktop\\text\\test.txt"

# try:
#     if os.path.exists(destination):
#         print("There is already a file there")
#     else:
#         os.replace(source, destination)
#         print(source, "was moved")
# except FileNotFoundError:
#         print(source, "was not found")

# -------------------------------------------------------------------

# delete file

import os
import shutil

path = "folder"
try:
    # os.remove(path)       #delete a file 
    # os.rmdir(path)        #delete an empty directory
    shutil.rmtree(path)   #delete a directory containing files

except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path, "was deleted")