from tabulate import tabulate
from pathlib import Path
folder=Path.home()/"Downloads"
data=[]
if folder.exists() and folder.is_dir():
    for file in folder.iterdir():
        data.append(
            [file.name,file.suffix or "No Extension"]
        )
head=["File name","File type"]
print(tabulate(data,headers=head,tablefmt="grid"))
        

        