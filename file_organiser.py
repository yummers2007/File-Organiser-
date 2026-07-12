from pathlib import Path
import shutil
import os
import re

#  directory path
path = "/storage/emulated/0"

#  target directory
directory = Path(path)

#  creating directories
if not Path(path + "/" + "Python").is_dir():
    os.mkdir("Python")
    
if not Path(path + "/" + "C++").is_dir():
    os.mkdir("C++")
    
if not Path(path + "/" + "Java").is_dir():
    os.mkdir("Java")
    
if not Path(path + "/" + "JavaScript").is_dir():
    os.mkdir("JavaScript")

#  file extensions match
python = r".py\b"
cpp = r".cpp\b"
java = r".java\b"
javascript = r".js\b"

#  files list 
files = []

#  append filenames to files list
for file in directory.iterdir():
    if file.is_file():
        files.append(file.name)

#  appending files to thier directories
for file in files:
    
    #  source file
    source = Path(path + "/" + file)
    
    #  file extension match
    python_match = re.search(python, file)
    cpp_match = re.search(cpp, file)
    java_match = re.search(java, file)
    js_match = re.search(javascript, file)
    
    if python_match:
        destination = Path(path + "/" + "Python")
        shutil.move(source, destination)
        
    elif cpp_match:
        destination = Path(path + "/" + "C++")
        shutil.move(source, destination)
        
    elif java_match:
        destination = Path(path + "/" + "Java")
        shutil.move(source, destination)
        
    elif js_match:
        destination = Path(path + "/" + "Javascript")
        shutil.move(source, destination)

#  displays files appended 
print("  File(s) appended : ")

if len(files) != 0:
    for file in files:
        print("  " + file)
        
else:
    print("  " + "None")
    
#  no. of files appended
print("\n  No. of files appended : " + str(len(files)))
