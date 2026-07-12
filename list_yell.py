def main():
    yell("Hi! this is me ")

def yell(*words):
    uppercased=[word.upper() for word in words]
    print(*uppercased)

if __name__=="__main__":
    main()