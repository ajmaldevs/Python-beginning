#OS library in python
import os
print(f"Current Working Directory: {os.chdir(r"C:\Users\ajumu\Downloads")}")
directory:str=input("Enter the Directory: ")
os.chdir(fr"{os.getcwd()}\{directory}")
print(os.getcwd())