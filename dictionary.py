#Dictrionary in Python
data={}
while True:
    name:str=input("Enter your name: ").title()
    place:str=input("Enter Your place: ").title()
    std:int=int(input("Enter Your phone number: "))
    if not name or place or std:
        break 
    data={
        "name":name,
        "place":place,
        "phno":std
    }

for key,value in data.items():
    print(f"""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ~~~~~~~~~~~~~~~~~~~~~~~~ STUDENT DETAILS ~~~~~~~~~~~~~~~~~~~~~~~~~~
            Name: {data["name"]}
            Place: {data["place"]}
            Phone number : {data['phno']}

            ####################################################################
            ####################################################################""")
