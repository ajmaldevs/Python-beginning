def main():
    name=input("Whats your name :")
    hello(name)


def hello(to="world"):
    print("Hello,",to)

main()    
#the main function is the starting point of the program and it calls the hello function and passes the name variable as an argument    