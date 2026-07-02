students = [
    {"name": "harry", "house": "Gryffindor", "pattronus": "stag"},
    {"name": "hermoine", "house": "Gryffindor", "pattronus": "otter"},
    {"name": "Draco", "house": "Slytherin", "pattronus": None},
]

for s in students:
    print(s["name"], s["house"], s["pattronus"], sep=", ")
