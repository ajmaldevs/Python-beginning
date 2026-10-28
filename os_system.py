#OS library in python
import os
import sys
folder=""
directory=""
try:
    os.chdir(r"C:\Users\ajumu\Downloads")
    print(f"Current Working Directory: {os.getcwd()}")
    directory:str=input("Enter the Directory: ")
    os.chdir(fr"{os.getcwd()}\{directory}")
    folder:str=input("Enter the folder name: ")
    os.mkdir(folder)
    print("Folder made successfully..")
    os.chdir(fr"{os.getcwd()}\{folder}")
    file_name:str=input("Enter the file name: ")
    with open(file_name,"w") as f:
        data:str=input("Enter Data inside the file: ")
        f.write(data)
except Exception:
    print("Some Kind of Error Occured")
    sys.exit()
else:
    print(f"Program Executed Successfully..")