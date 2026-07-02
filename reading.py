with open("names.txt","r") as file:
    line = file.readlines()
#what the readline function here does is it returns the value as a list
for lines in line:
    print(f"Hello, {lines.rstrip()}")

    