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
        destination=folder/file
        file.rename(destination)
        num+=1

print(f"Number of Files: {num}")