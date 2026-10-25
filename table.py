from tabulate import tabulate
name=[
    ["Ajmal","08","91234567890"],
    ["Amal","09","+911234567892"],
    ["Rohit","10","+91789456123"]
     ]
header=["Name","Rollno","Phone no"]

print(tabulate(name,headers=header,tablefmt="grid"))

with open("table.html","w") as file:
    file.write(tabulate(name,headers=header,tablefmt="html"))
    print("Program Saved to table.html")
    