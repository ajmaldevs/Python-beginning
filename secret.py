import secrets
import sys

password=""

try:
    n=int(input("Enter a limit: "))
except ValueError:
    sys.exit("Input was not a Integer")

for i in range(n):
    letter=secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*=+")
    password+=letter

with open("Password.txt","a") as file:
    file.write(f"{password}\n")

print(password)