#Armstrong number or not
n:int=int(input("Enter a number : "))
sum=0
temp=n
while(n>0):
    r=n%10
    sum+=r*r*r
    n//=10

if temp==sum:
    print(f"{temp} is an Armstrong Number")
else:
    print(f"{temp} is not an Armstrong number")
    
