from pathlib import Path
print(f"PWD: {Path.home()} ")
directory:str=input("Enter a Folder: ").strip()
folder=Path.home() / directory
data=[]
for files in folder.iterdir():
    data.append(files.suffix)

set(data)
print(data)
    
    