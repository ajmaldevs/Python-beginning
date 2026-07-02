def main():
    x=int(input("What's X? "))
    if is_even(x):
        print("Even number")
    else:
        print("Odd number")
    
# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False        
# Here instead of a four line code function what we ca do is we can compress it to one line its only possible on python like:
def is_even(n):
    return True if n%2==0 else False
#Also here we dont use : on if or else statement keep that in mind
# Or we can use one other method
#def is_even(n):
#   return(n%2==0)
#Because its a boolean expression returning the question itself will work also 
    
main()

# here we made a function is_even to check if a number is even or not by this we can do the program infinite number of times
# the value retuened from the function here is not integer or string or other its called BOOL its True/False