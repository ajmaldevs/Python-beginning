try :
    n=int(input("Enter a number:"))
except ValueError:
    raise ValueError("Value is not an Integer")
dist=[]
for _ in range(n):
    name=input("Enter Your Name : ")
    dist.append(name)

dist=set(dist)
print(f"Names with no repetion :")
print()
for n in dist:
    print(n)
    with open('names.txt',"w") as file:
        file.write(n)

    