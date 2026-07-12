def main():
    yell("Hi! this is me ")
    yell(["I","am","Beautiful"])

def yell(*words):
    uppercased=[word.upper() for word in words]
    print(*uppercased)

if __name__=="__main__":
    main()