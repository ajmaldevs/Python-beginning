import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
available_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    choice = True
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        choice = False
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

if choice == True:
    selected_font = random.choice(available_fonts)
else:
    if sys.argv[2] not in available_fonts:
        sys.exit("Invalid usage")
    else:
        selected_font = sys.argv[2]

text = input("Input: ")
font = Figlet(font=selected_font)
print(font.renderText(text))
