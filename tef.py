
import sys
def main():
    """
    this is just a function to take an integer,String,Floating point, list datatypes
    and pass it to a function to print its types
    """
    n:int=int(input("Enter a number: "))
    name:str=input("Enter a String: ")
    point:float=float(input("Enter a floating point: "))
    print("Data for a list : ")
    l:list=[]
    for _ in range(n):
        val:str=input("Enter a name: ")
        l.append(val)
    print(l)
    stype(n,name,point,l)

def stype(n,name,point,l):
    print(type(n))
    print(type(name))
    print(type(point))
    print(type(l))

if __name__=="__main__":
    try:
        main()
    except ValueError:
        print("Value Error You entered wrong type of data")
    finally:
        sys.exit("program Executed Successfully")