def main():
    yell("Hi! this is me ")
    yell(["I","am","Beautiful"])

def yell(*words):
    uppercased=map(str.upper,*words)
    print(*uppercased)

if __name__=="__main__":
    main()