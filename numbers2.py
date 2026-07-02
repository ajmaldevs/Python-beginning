try:
    x=int(input("Whats X? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

#here the program tries a code except if its a value error 
#if its a value error it prints "x ix not an integer"
#if no error is oocured it moves to the else function and contibue with code
