import re
email:str=input("Enter Your Email ID: ").strip().lower()
pattern=r"[/w.-+]"
res=re.findall(pattern,email)
print(res)