# File Organiser
import sys
import time
from pathlib import Path

def main():
    word="Welcome to File Organiser"
    for w in word:
        print(f"{w}",flush=True,end="")
        time.sleep(0.25)
    print()
    time.sleep(0.2)
    print(f"Current Directory = {Path.home()}")
    directory:str=input("Enter The Folder You Want: ")
    folder=Path.home() / directory
    data=[]
    suffix(folder,data)
    create(folder,data)
    time.sleep(2)
    print("File Organised Successfully")


def suffix(folder,data):
    for file in folder.iterdir():
        suf=file.suffix
        data.append(suf)

def create(folder,data):
    file_extensions = [
    ".txt", ".doc", ".docx", ".pdf", ".rtf", ".odt", ".ods",
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg",
    ".mp3", ".mp4", ".avi", ".wav", ".flac", ".aac", ".mkv",
    ".exe", ".py", ".js", ".java", ".html", ".htm", ".css",
    ".zip", ".rar", ".7z", ".tar", ".gz",
    ".dll", ".sh", ".bat",
    ".cfg", ".conf", ".xml", ".json", ".sql", ".bak",
    ".csv", ".xlsx", ".xls", ".pptx", ".ppt",
    ".md", ".log", ".ini", ".yml", ".yaml",
    ".ico", ".tiff", ".heic", ".webm", ".ogg",
    ".c", ".cpp", ".h", ".cs", ".go", ".rs", ".rb",
    ".php", ".swift", ".kt", ".m",
    ".iso", ".img", ".vhd",
    ".apk", ".jar", ".class",
    ".db", ".sqlite", ".mdb",
    ".eps", ".ai", ".psd", ".sketch",
    ".srt", ".vtt",
    ".wasm", ".bin",
    ] 
    
    for i in set(data):
            if i in file_extensions:
                folder_name=i.replace(".","").title()
            else:
                folder_name=f"No/{i.replace('.','').title()}"
                
            directory=folder / f"{folder_name}"
            directory.mkdir(exist_ok=True,parents=True)

            for file in folder.iterdir():
                 if file.is_file() and file.suffix in [i]:
                    file.rename(directory/file.name)
         



    
if __name__=="__main__":      
    try:
        main()
    except FileNotFoundError:
        sys.exit("File is not founded")
