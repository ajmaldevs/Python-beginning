name =input("Whats your name:")

name= name.strip()
#strip here does that it removes unnesary spaces given in the input
name= name.capitalize()
#This function capitalizes the first letter of the variable inputed
name= name.title()
#this function capitalizes the first world of every word in the variable input
name= name.strip().title()
#this combines both functions reduces lines of code and makes it more easy to use
first,last =name.split(" ")
#this is used to split the input to two and save one on first variable and another on swecond variable


print("your first name is ",first)


print(f"your last name is {last}")


book =input("Whats your favourite book:").strip().title()
#this is more efficient way of combing the functions in one line of code


print(f"hello,{name}")

print(f"Your favourite book is {book}")   
