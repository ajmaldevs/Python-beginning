try:
    x=int(input("Whats X? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")