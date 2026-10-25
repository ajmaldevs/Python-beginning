from tabulate import tabulate
from pathlib import Path
directory:str=input("Enter the Directory: ")
folder=Path.home()/f"{directory}"
data=[]
if folder.exists() and folder.is_dir():
    for file in folder.iterdir():
        data.append(
            [file.name,file.suffix or "No Extension"]
        )
head=["File name","File type"]
print(tabulate(data,headers=head,tablefmt="grid"))

        

        