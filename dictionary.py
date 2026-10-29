#Dictrionary in Python
data={}
while True:
    name:str=input("Enter your name: ").title()
    place:str=input("Enter Your place: ").title()
    std:int=int(input("Enter Your phone number: "))
    if not name or not place or not std:
        break 
    data={
        "name":name,
        "place":place,
        "phno":std
    }

if data:
    print(f"""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ~~~~~~~~~~~~~~~~~~~~~~~~ STUDENT DETAILS ~~~~~~~~~~~~~~~~~~~~~~~~~~
            Name: {data['name']}
            Place: {data['place']}
            Phone number : {data['phno']}

            ####################################################################
            ####################################################################""")
