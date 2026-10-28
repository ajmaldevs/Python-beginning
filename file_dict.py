from pathlib import Path
import sys
print(f"PWD : {Path.home()}")
directory:str=input("Enter The folder: ").strip()
folder=Path.home() / directory
if folder.is_dir():
    pass
else:
    sys.exit("Not a Folder ")

data={}
num=0
for file in folder.rglob("*"):
    if file.is_file():
        num+=1

print(f"Number of Files: {num}")