import re
phone_number:str=input("Enter the Phone Number: ")
pattern=r"^(\+[0-9]+)\s([0-9]+)"
res = re.search(pattern,phone_number)
if res:
    print(f"Country code : {res.group(1)}")
    print(f"Number : {res.group(2)}")
else:
    pass