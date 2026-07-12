class Account:
    def __init__(self):
        self._balance=0

    def deposit(self,value):
        self._balance+=value
        return self._balance

    def withdraw(self,value):
        self._balance-=value
        return self._balance

    @property
    def balance(self):
        return self._balance
    
    
    @balance.setter
    def balance(self,value):
        self._balance=value

def main():
    account=Account()
    account.deposit(1000)
    account.withdraw(60)
    print(f"Account balance:{account.balance}")

if __name__=="__main__":
    main()