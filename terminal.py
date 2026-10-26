import os 
command:str=input("Enter the Command to execute: ").lower()
print(os.system(f"{command}"))

