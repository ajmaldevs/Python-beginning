distance = {
    "Voyager 1" : 163 ,
    "Voyager 2" : 361 ,
    "Pioneer 10" : 80 ,
    "New horizon" : 58,
    "Pioneer 14" : 44
}

def main():
    for name in distance.keys():
        print(f"{name} is {distance.get(name)} AU from Earth".upper())

main()