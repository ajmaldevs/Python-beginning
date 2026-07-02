import re

name = input("What's Your name : ").strip().title()

macthes = re.search("^(.+), *(.+)$", name)
if macthes:
    last, first = macthes.groups()
    name = f"{first} {last}"

print(f"Hello {name}")

#i could also do this by specifying the required groups like matches.group(n) or something like that 
