#Palindrome number or not
n:int=int(input("Enter a number : "))
rev=0
temp=n
while(n>0):
    r=n%10
    rev=rev*10+r
    n//=10

if temp==rev:
    print(f"{temp} is a palindrome Number")
else:
    print(f"{temp} is not a palindrome number")
    
