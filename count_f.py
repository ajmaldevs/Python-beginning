from pathlib import Path
print(f"PWD: {Path.home()} ")
directory:str=input("Enter a Folder: ").strip()
folder=Path.home() / directory
varble={}
for file in folder.iterdir():
    if file.is_file():
        ext=file.suffix
        if ext:
            varble[ext]=varble.get(ext,1)+1

print(*varble)


    
    