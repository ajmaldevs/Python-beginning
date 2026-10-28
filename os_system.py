#OS library in python
import os
os.chdir(r"C:\Users\ajumu\Downloads")
print(f"Current Working Directory: {os.getcwd()}")
directory:str=input("Enter the Directory: ")
os.chdir(fr"{os.getcwd()}\{directory}")
folder:str=input("Enter the folder name: ")
os.mkdir(folder)
print("Folder made successfully..")
os.chdir(fr"{os.getcwd()}\{folder}")
file_name:str=input("Enter the file name: ")
name=os.path.join(folder,file_name)
with open(name,"w") as f:
    data:str=input("Enter Data inside the file: ")
    f.write(data)

print(f"Program Executed Successfully..")