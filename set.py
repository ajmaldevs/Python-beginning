students=[
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Hermoine","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"Draco","house":"Slytherin"},
    {"name":"Padma","house":"Ravenclaw"}
]

house=set()
for student in students:
    house.add(student["house"])

for houses in house:
    print(houses)