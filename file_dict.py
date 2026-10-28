from pathlib import Path
directory:str=input("Enter The folder: ").strip()
print(f"PWD : {Path.home()}")
folder=Path.home() / directory
data={}
for file in folder.iterdir():
    for i in file.name:
        print(i)
