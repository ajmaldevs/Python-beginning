

def main():
    n:int=int(input("Enter a number: "))
    name:str=input("Enter a name: ")
    print(loop(n,name))


def loop(n:int,name:str):
    for _ in range(n):
        yield name

if __name__=="__main__":
    main()
    

