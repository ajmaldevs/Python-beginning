import sys
def meow(n)->str:
    """
    Meow n times

    :param:n
    :n:integer
    :return type:string 
    """
    return f"meow\n"*(n)

def main():
    try:
        number=int(input("Enter a number: "))
        print(meow(number),end="")
    except ValueError:
        sys.exit("This Not an integer 😤")
        

if __name__=="__main__":
    main()