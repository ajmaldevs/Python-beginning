import os
path=r"C:\Users\ajumu\Downloads"
ftype=input('Enter the type of the file: ')
for file in os.listdir(path):
    if file.endswith(ftype):
        print(f"{file}")
