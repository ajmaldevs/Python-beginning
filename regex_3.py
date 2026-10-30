import re
import sys
try:
    phone_number:str=input("Enter the Phone Number: ")
    space=" "
    if not space in phone_number:
        raise ValueError
    pattern=r"^(\+[0-9]+)\s([0-9]+)"
    res = re.search(pattern,phone_number)
    if res:
        print(f"Country code : {res.group(1)}")
        print(f"Number : {res.group(2)}")
    else:
        pass
except ValueError:
    sys.exit("No Space between country code and Number")
