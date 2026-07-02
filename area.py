def area(length,breadth):
    print(str(length*breadth)+"Square feet")
    return length*breadth

def main():
    length=int(input("Enter the length"))
    breadth=int(input("Enter the breadth"))
    ar=area(length,breadth)
    print(str(ar)+"area")

main()
          
