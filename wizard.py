class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError
        self.name=name


class Student(Wizard):
    def __init__(self,name,house):
        self.house=house
        super().__init__(name)

class Professor(Wizard):
    def __init__(self,name,subject):
        self.subject=subject
        super().__init__(name)
        

wizard=Wizard("Albus Dumbldore")
student=Student("Harry","gryffindor")
professor=Professor("Severus","Defense against the Dark Arts")
