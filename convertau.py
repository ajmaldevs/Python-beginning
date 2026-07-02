def main():
    while True:
        try:

            user=input("How many AU: ")
            au=float(user)
            break
        except:
            continue

    
    print(f"{user}AU is {convert(au)}m")

def convert(au):
    if not isinstance(au,(int,float)):
        print("Enter AU in int or float")

    return au*149597870700


if __name__=="__main__":
    main()

