import time
try:
    num_1=int(input("Enter a number: "))
    num_2=int(input("Enter another number: "))
    operator=input("Enter the operator: ")
except ValueError:
    raise ValueError("Not expected Character")
finally:
    print("Calculating.......")
    time.sleep(5)
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





