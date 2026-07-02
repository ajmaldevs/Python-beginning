def main():
    a=use_int()
    print(f"X is {a}")

def use_int():
    while True:
        try:
            x=int(input("Whats x? "))
            return x
        except ValueError:
            print("X is not an integer")

main()
# what return does is it breaks the program and also returns x
# there are multiple ways to do this we can use else statement to return the function too
# or to make more lengthier code we can use else to break the code and then return x in another line