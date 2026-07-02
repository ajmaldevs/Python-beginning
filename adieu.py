import inflect
import sys
p=inflect.engine()
name=[]
try:
    while True:
        a=input("Name: ")
        name.append(a)
except EOFError:
    print()
    print("Adieu, adieu, to ",end="")
    print(p.join(name))
    sys.exit()




