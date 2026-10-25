from pathlib import Path
folder=Path.home()/"Downloads"
if folder.exists() and folder.is_dir():
    for file in folder.iterdir():
        print(file.name)

        