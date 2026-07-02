import re

email = input("Whats Your Email: ").strip()

if re.search(r"^\w+@\w+\.(edu|com|org)$",email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
