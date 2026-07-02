def index():
    words_in_game= {
    "PAIR" : 4,
    "HAIR" : 4,
    "CHAIR" : 5,
    "GRAPHIC" : 7
}
    for word,points in words_in_game.items():
        print(f"You have {word} with {points} points")

def main():
    words= {
    "PAIR" : 4,
    "HAIR" : 4,
    "CHAIR" : 5,
    "GRAPHIC" : 7
}
    print("Welcome to BEE Spelling Game")
    print("Your Letters Are: A I P C R H G")
    total=0
    while len(words)>0:
        gues=input("Enter your guess : ")
        guess=gues.upper()
        if guess=="GRAPHIC":
            total=7
            print("YOU WON")
            words.clear()
        elif guess in words.keys():
            point=words.pop(guess)
            print(f"{len(words)} words left!")
            print(f"Congrats! You have scored {point} points")
            total+=point
#What .pop() does is removes the entered word from the dictionary 
    print("Thats the game THANK YOU for playing ")
    print(f"{total} is your total points")
    a=input("Do you wanna see all the words and points? (yes/no) ")
    b=a.lower()
    if b=="yes":
        index()
    else:
        print("OK")


main()
