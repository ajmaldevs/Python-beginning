class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    #getter
    @property
    def house(self):
        return self._house
    
    #setter
    @house.setter
    def house(self,house):
        if not house.lower() in ["gryffindor","hufflepuff","slytherin","ravenclaw"]:
            raise ValueError("invalid house")
        self._house=house

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    def __str__(self):
        return f"{self.name} is from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()
