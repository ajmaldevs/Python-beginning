
#integer addition calculator
x=int(input("enter first number:"))
y=int(input("enter second number:"))

z=x+y

print(z)

#floating point addition calculator
a=float(input("Whats a:"))
b=float(input("whats b:"))
#this is used to round the output to the nearest digit a
z=round(a+b)
#if i want the value to be something like 1,000 instead of 1000 i can use format function
print(f"{z:,}")
#this statement will print output as i desired


