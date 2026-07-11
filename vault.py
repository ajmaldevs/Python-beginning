class Vault:
    def __init__(self,galleons=0,sickles=0,knuts=0):
        self.galleons=galleons
        self.knuts=knuts
        self.sickles=sickles
    def __str__(self):
        return f"Galleons = {self.galleons}\nSickles={self.sickles}\nknuckles={self.knuts}\n"
    def __add__(self,other):
        galleons=self.galleons+other.galleons
        knuts=self.knuts+other.knuts
        sickles=self.sickles+other.sickles
        return Vault(galleons,sickles,knuts)

potter=Vault(100,20,40)
print(potter)
weasly=Vault(10,40,40)
print(weasly)

total=weasly+potter
print(total)