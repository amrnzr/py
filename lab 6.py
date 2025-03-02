#Python Directories and Files exercises
import os
import shutil
#Task 1
def lfd(path):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return dirs, files
path = 'C:\\Users'
print(lfd(path))