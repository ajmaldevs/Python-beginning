score =int(input("whats the score? "))

if score>=90 and score<=100:
    print('Grade A')

elif score>=80 and score<=90:
    print('grade B')

elif score>=70 and score<=80:
    print("Grade C")

elif score>=60 and score<=70:
    print("Grade D")

else:
    print("Grade F")

# Here we use a new keyword "AND" which check if both the conditions are true/false then execute according to that
# on python we use indentaton instead of {} curly braces