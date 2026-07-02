distance = {
    "Voyager 1" : 163 ,
    "Voyager 2" : 361 ,
    "Pioneer 10" : 80 ,
    "New horizon" : 58,
    "Pioneer 14" : 44
}

def main():
    for dis in distance.values():
        print(f"{dis} in AU is {convert(dis)} in meters")

def convert(a):
    return a*14957870700

main()