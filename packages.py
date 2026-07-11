class Package:
    def __init__(self,number,sender,recpient,weight):
        self.number=number
        self.sender=sender
        self.recpient=recpient
        self.weight=weight

    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recpient},{self.weight}Kg"
    def calculate_cost(self,cost_kg):
        return f"{self.weight*cost_kg}$"


    
    
    


def main():
    packages=[Package(number=1,sender="Luffy",recpient="Zoro",weight=10),
              Package(number=2,sender="Sanji",recpient="Brook",weight=5)]
    
    for thing in packages:
        print(f"{thing} and it costs {thing.calculate_cost(2)}")

    


if __name__=="__main__":
    main()