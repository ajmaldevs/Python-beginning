import sys
if len(sys.argv)<2:
    sys.exit("Too few arguments")

for name in sys.argv[1:]:
    print("Hey, Its me ",name)

# here what the list inside the for loop does is that it starts the list from 1 instead of zero
# this is called slice
# by using slice we can add the starting point and ending point in a program
     