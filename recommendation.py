def main():
    difficulty = input("Diffult or Casual : ")
    players = input("Single player or Multiplayer : ")
    difficulty = difficulty.lower()
    players = players.lower().strip()
    if difficulty == "difficult":
        if players == "multiplayer":
            recommend("Valorant")
        else:
            recommend("Hogwards Legacy")
    else:
        if players == "multiplayer":
            recommend("Battle ground mobile india")
        else:
            recommend("Clash of clans")


def recommend(game):
    print("You might like", game)
    print("Have fun 😁")


main()
