balance=0

def main():
    try:
        deposit(100)
        withdraw(50)
        print("Balance=",balance)
    except ValueError:
        pass
    finally:
        print(f"....................Program worked Successfully.................")

def deposit(value):
    global balance
    balance=balance+value

def withdraw(money):
    global balance
    balance=balance-money


if __name__=="__main__":
    main()
    