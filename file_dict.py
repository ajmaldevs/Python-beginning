from pathlib import Path
directory:str=input("Enter The folder: ").strip()
print(f"PWD : {Path.home()}")
folder=Path.home() / directory
data={}
num=0
for file in folder.iterdir():
    if file.is_file():
        num+=1
    else:
        print(file)
