#Hogwards house determining program
# Using "MATCH" keyword 
name=input("Whats your name: ")

match name:
    case "Harry"|"Hermoine"|"Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who? ")    