
def main():
    student=get_student()
    print(f"{student[0]} is from {student[1]}")

def get_student():
    name= input("Enter your name: ")
    house= input("Enter your house: ")
    return (name,house)

if __name__=="__main__":
    main()
