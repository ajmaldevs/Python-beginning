a=float(input("Enter a number:"))
b=float(input("Enter another number:"))

#c=round(a/b,2)
#what this does is converts the ouput to two decimal points instead of 0.66666 it will be 0.67
#another way to convert this intto two decimal points is using format function
print(f"{a/b:0.2f}")
#this is the another way to convert this into two decimal points we can also do this by converting or declaring this to a variable and later print the variable
