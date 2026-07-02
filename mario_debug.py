def main():
    height=int(input("Enter height: "))
    pyramid(height)

def pyramid(h):
    for i in range(h+1):
        print("#"*i)

main()