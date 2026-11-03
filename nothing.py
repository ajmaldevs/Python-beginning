#Sum of Digits
import sys
try:
    num:int=int(input("Enter a number: "))
    sum=0
    Asum=0
    temp=num
    while num>0:
        r=num%10
        Asum=r*r*r
        sum+=num%10
        num//=10

    print(f"Sum of Digits = {sum}")
    if temp==Asum:
        print(f"Armstrong number")
    else:
      print(f"Not an Armstrong number")
except ValueError:
    sys.exit(f"Value Entered is not an Integer")


        
