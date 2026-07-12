students=[
    {"name":"Harry", "house":"Gryffindor"},
   { "name":"Hermoine", "house":"Gryffindor"},
    {"name":"Ron", "house":"Gryffindor"},
    {"name":"Draco", "house":"Slytherin"
}]

griffindor=[student["name"] for student in students if student["house"]=="Gryffindor"]

print(*griffindor)