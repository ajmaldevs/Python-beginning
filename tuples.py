#tuples are a data that we cant change or add once entered 
#tuples and lists are mostly same but what differs them is the fact tuple takes less memory and 
#list takes more memory
def main():
    coordinates=(42.376,-71.156)
    latitude,longitude=coordinates
    #what this statement does is that it stores the tuples value in two variables respectively
    print(f"{latitude}:Latitude")
    print(f"{longitude}:Longitude")

main()