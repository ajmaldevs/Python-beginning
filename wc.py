from pathlib import Path
wc=0
folder=Path.home() / "Downloads" / "My Python Projects"
if folder.exists() and folder.is_dir():
    for file in folder.iterdir():
        if file.suffix==".py":
            wc+=1

print(wc)
