import time
import sys
from datetime import date

try:
    #Function to take inputs
    def takeinput():
        num_1 = int(input("Enter a number: "))
        num_2 = int(input("Enter another number: "))
        operators=["+","-","*","/","**","//"]
        print(operators)
        operator = input("Enter the operator: ")
        return num_1,num_2,operator

    #Main Function
    def main():
        num_1,num_2,operator=takeinput()
        option=input("Do you Wanna Change Numbers ? Y/N : ").lower()
        if option=="y":
                print("Loading....")
                time.sleep(1)
                num_1,num_2,operator=takeinput()
        else:
                pass
        print("Calculating.......")
        time.sleep(2)
        print("Result: ")
        calculate(num_1,num_2,operator)
        history(num_1,num_2,operator)

    #Function to calculate
    def calculate(num_1,num_2,operator):
        match operator:
            case "+":
                print(f"Addition = {num_1+num_2}")
            case "-":
                print(f"Subtration = {num_1-num_2}")
            case "*":
                print(f"Multiplication = {num_1*num_2}")
            case "/":
                print(f"Division = {num_1/num_2}")
            case "**":
                print(f"Power = {num_1**num_2}")
            case "//":
                print(f"Floor Division = {num_1//num_2}")
            case _:
                print(f"No Operator Entered....")
                sys.exit()

    #Fuction used to Access and Write History
    def history(num_1,num_2,operator):

        today = date.today()

        with open("History.txt", "a") as file:
            file.write(f"\n{today} : {num_1} {operator} {num_2}")

        options = input("Do you wanna see or clear history Y/N/C: ").lower()
        with open("History.txt","r") as file:
            if options == "y":
                print("------HISTORY------")
                print(file.read().strip())
                print("------END----------")
                
            elif options == "C":
                with open("History.txt","w") as file:
                    pass

            else:
                sys.exit()
        

except ValueError:
    print("Value Error")
    sys.exit()
except ZeroDivisionError:
    print("Zero Division Error")
    sys.exit()
except FileNotFoundError:
    sys.exit("File Not Found")



if __name__=="__main__":
    main()


