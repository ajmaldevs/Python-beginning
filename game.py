import random


def level_check():
    while True:
        level = input("Level: ")
        if level.isdigit():
            level = int(level)
            if level > 0:
                return level
        else:
            continue


def guess_check():
    while True:
        guess = input("Guess: ")
        if guess.isdigit():
            guess = int(guess)
            if guess > 0:
                return guess
        else:
            continue


def main():
    n = level_check()
    num = random.randint(1, n)

    while True:
        guess = guess_check()
        if guess > num:
            print("Too large!")
        elif guess < num:
            print("Too small!")
        elif guess == num:
            print("Just right!")
            break
        else:
            break


main()
