import re
name:str=input("Enter Your name: ").title()
pattern=r"^([\w]+)\s([\w]+)"
res = re.search(pattern,name)
if res:
    print(f"First Name : {res.group(1)}")
    print(f"Last Name : {res.group((2))}")
else:
    pass

