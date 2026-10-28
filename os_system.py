#OS library in python
import os
os.system("cd ..")
print(f"Current Working Directory: {os.getcwd()}")
directory:str=input("Enter the Directory: ")
os.chdir(f"{os.getcwd()}/{directory}")