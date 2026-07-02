name=input("Students Name: ")
with open("students.csv","a") as file:
    file.write(name)

with open("students.csv") as file:
    a=file.readlines()

for line in a:
    print(line)