name=[]
with open("names.txt") as file:
    for line in file:
        name.append(line.rstrip())

for names in sorted(name):
    print(f"Hello, {names}")
    