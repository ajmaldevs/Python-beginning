#Word game
from tabulate import tabulate
print("Enter a word...")
q1:str=input("Player 1? ")
q2:str=input("Player 2? ")

data = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10
}
print("Score Card..")
print(tabulate(data,tablefmt="grid"))
t1=0
t2=0
for letter in q1:
    if letter in data:
        t1+=data[letter]

for letter in q2:
    if letter in data:
        t2+=data[letter]

if t1==t2:
    print(f"tie !")
elif t1>t2:
    print(f"Player 1 wins 🥇")
else:
    print(f"Player 2 wins 🥇")