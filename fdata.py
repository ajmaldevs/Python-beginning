from faker import Faker
from tabulate import tabulate
n:int=int(input("Enter the number of data: "))
fake=Faker()
l= []
for i in range(n):
    l.append([fake.name(),
   fake.email(),
    fake.phone_number(),])

head=["Name","Email","Phone number"]

print(tabulate(l,headers=head,tablefmt="grid"))
    


    
