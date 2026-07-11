
import random
class Hat:
    houses=["gryffindor","Slytherin","Hufflepuff","Ravenclaw"]

    @classmethod
    def sort(cls,name):
        house=random.choice(cls.houses)
        print(f"{name} is in {house}")


name=input("Enter the name: ")
Hat.sort(name)