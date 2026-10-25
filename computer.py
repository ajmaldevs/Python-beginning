import os
path=r"C:\Users\ajumu\Downloads"
for file in os.listdir(path):
    if file.endswith(".pdf"):
        print(f"{file}")
