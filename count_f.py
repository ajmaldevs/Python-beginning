from pathlib import Path
print(f"PWD: {Path.home()} ")
directory:str=input("Enter a Folder: ").strip()
folder=Path.home() / directory

for files in folder.iterdir():
    print(files.name)
    