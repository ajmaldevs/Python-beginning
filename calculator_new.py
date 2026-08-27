import time
import sys
from datetime import date

try:
    def takeinput():
        num_1 = int(input("Enter a number: "))
        num_2 = int(input("Enter another number: "))
        print("Operators : + , - , * , / , ** , //")
        operator = input("Enter the operator: ")
        return num_1,num_2,operator
    
    def main():
        num_1,num_2,operator=takeinput()
        option=input("Do you Wanna Change Numbers ? Y/N").lower()
        if option=="y":
                takeinput()
        else:
                pass
        print("Calculating.......")
        time.sleep(2)
        print("Result: ")
        match operator:
            case "+":
                print(f"Addition = {num_1+num_2}")
            case "-":
                print(f"Substration = {num_1-num_2}")
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

        today = date.today()

        with open("History.txt", "a") as file:
            file.write(f"\n{today} : {num_1} {operator} {num_2}")

        options = input("Do you wanna see history Y/N: ").lower()
        with open("History.txt","r") as file:
            if options == "y":
                print("------HISTORY------")
                print(file.read().strip())
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
