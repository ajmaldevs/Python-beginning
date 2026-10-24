from file import fadd
import sys

def main():
    name:str=input("Enter a name: ").title()
    n:int=int(input("Enter a number: "))
    fadd(name,n)
    print(f"Program Saved to {sys.argv[1]} file")

if __name__=="__main__":
    try:
        main()
    except ValueError:
        sys.exit("You entered Value wrong")
