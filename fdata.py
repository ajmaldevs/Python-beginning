from faker import Faker
n:int=int(input("Enter the number of data: "))
fake=Faker()
for i in range(n):
    print(f"{fake.name()} {fake.address()} {fake.email()}")
    
