import sys

if len(sys.argv)<2:
    sys.exit("Too less arguments")
elif len(sys.argv)>2:
    sys.exit("too many arguments")
else:
    pass

def main():
    try:
        res=meow(int(sys.argv[1]))
        print(res,end="")
    except ValueError:
        sys.exit("Not an integer")


def meow(n:int):
    return "meow\n"*n 

if __name__=="__main__":
    main()