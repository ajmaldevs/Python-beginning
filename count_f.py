from pathlib import Path
print(f"PWD: {Path.home()} ")
directory:str=input("Enter a Folder: ").strip()
folder=Path.home() / directory
data=[]
for files in folder.iterdir():
    data.append(files.suffix)

updated_data=set(data)
variables={}
for x in updated_data:
    name=x.lstrip(".")
    variables[name]=1

    for files in folder.iterdir():
        ch=files.suffix.lstrip(".")
        if ch == name:
            variables[name]+=1
        print(variables[name])

    
    