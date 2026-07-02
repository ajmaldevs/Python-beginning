while True:
    try:
        x=int(input("Whats X? "))
    except ValueError:
        print("X is not an Integer")
    else:
        break

print(f"x is {x}")

# this programs asks the user the value of x if ots right it gives the user the value
# else it keeps running the program until the user inputs correct x value
# so by this program tells the user what's wrong ?
# and gives the oppurtunity to continue