
name=input("Whats Your name: ")
#I could add things to file in two or more ways one is that 
# file=open("Names.txt","a")
# file.write(name)
# file.close()
# closing a file like this can cause problems such as corruptions and errors
# so Another way to do this is 
# use of with variable
with open("names.txt","a") as file:
    file.write(f"{name}\n")

# what this does is it makes code more reliable 
# it opens and closes the code Automatically