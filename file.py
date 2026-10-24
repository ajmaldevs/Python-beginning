import sys

def main():
    name:str=input("Enter your Name: ").title()
    n:int=int(input("Enter a number: "))
    fadd(name,n)

def fadd(name,n):
    if sys.argv[1]:
        with open(sys.argv[1],'a') as file:
            file.write(f"Name = {name} Number = {n} ")

if __name__=="__main__":
    try:
        main()
    except ValueError:
        sys.exit("you Entered a value wrong name:str number:int")
    except IndexError:
        sys.exit("You did not enter command line Argument")


