import random


def main():
    score = 0
    level = get_level()
    for i in range(10):
        num1 =generate_integer(level)
        num2 =generate_integer(level)

        res = num1 + num2
        n = 1
        while n <= 3:
            try:
                inp = int(input(f"{num1} + {num2} = "))
                if inp == res:
                    score += 1
                    break
                elif inp != res:
                    print("EEE")
                    n += 1
            except ValueError:
                print("EEE")
                n += 1

        if n == 4:
            print(f"{num1} + {num2} = {res}")

    print(f"{score}")


def get_level():
    while True:
        level = input("Level: ")
        if level.isdigit():
            level = int(level)
            if level > 0 and level <= 3:
                return level


def generate_integer(level):
    try:
        if level == 1:
            return random.randint(0,9)
        elif level == 2:
            return random.randint(10,99)
        elif level == 3:
            return random.randint(100,999)
    except ValueError:
        pass


if __name__ == "__main__":
    main()
