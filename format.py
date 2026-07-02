import re

name = input("What's Your name : ").strip().title()

macthes = re.search("^(.+), (.+)$", name)
if macthes:
    last, first = macthes.groups()
    name = f"{first} {last}"

print(f"Hello {name}")
