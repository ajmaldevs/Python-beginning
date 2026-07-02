def main():
    x=int(input("What's X? "))
    if is_even(x):
        print("Even number")
    else:
        print("Odd number")
    
def is_even(n):
    if n%2==0:
        return True
    else:
        return False        
    
main()

# here we made a function is_even to check if a number is even or not by this we can do the program infinite number of times
# the value retuened from the function here is not integer or string or other its called BOOL its True/False