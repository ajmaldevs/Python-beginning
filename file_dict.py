from pathlib import Path
import sys
print(f"PWD : {Path.home()}")
directory:str=input("Enter The folder: ").strip()
if directory:
    folder=Path.home() / directory
else:
    folder=Path.home()
if folder.is_dir():
    pass
else:
    sys.exit("Not a Folder ")

data={}
num=0
direc=0
for file in folder.rglob("*"):
    if file.is_file():
        num+=1
    if file.is_dir():
        direc+=1

print(f"Number of Files: {num}")
print(f"Number of Folder: {direc}")
