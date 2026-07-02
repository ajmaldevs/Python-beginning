def main():
    while True:
        n=int(input("Enter number of times : "))
        if n>0:
            break
    meow(n)
    
def meow(n):
    for _ in range(n):
        print("meowww...")

main()


        