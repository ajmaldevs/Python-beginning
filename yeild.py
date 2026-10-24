
import sys
def main():
    n:int=int(input("Enter a number: "))
    name:str=input("Enter a name: ")
    for res in loop(n,name):
        print(res)


def loop(n:int,name:str):
    for _ in range(n):
        yield name

if __name__=="__main__":
    try:
        main()
    except ValueError:
        sys.exit("ValueError")

    

