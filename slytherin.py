students=[
    {"name":"Harry", "house":"Gryffindor"},
   { "name":"Hermoine", "house":"Gryffindor"},
    {"name":"Ron", "house":"Gryffindor"},
    {"name":"Draco", "house":"Slytherin"
}]

def is_slytherin(s):
    if s["house"]=='Slytherin':
        return True
    else:
        return False
    
slytherin=filter(is_slytherin,students)
print(*slytherin)