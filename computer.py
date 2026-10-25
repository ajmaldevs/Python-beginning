import os
folder=input("Enter the folder: ").strip()
path=fr"C:\Users\ajumu\{folder}"
ftype=input('Enter the type of the file: ').lower().strip()
for file in os.listdir(path):
    if file.endswith(ftype):
        print(f"{file}")
