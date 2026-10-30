import re
email:str=input("Enter Your Email ID: ").strip().lower()
pattern=r"^([\w.-]+)"
res=re.search(pattern,email)
if res:
    print(f"Username= {res.group(1)}")
else: 
    print(f"Invalid Username")