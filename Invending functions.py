def hello():
    print("Hello,",end='')




name=input("Enter your name:").strip().title()
hello()
print(name)
#the function used here is hello() which is defined at the top and i can use the function as many as i want 
#the function hello prints hello and end with " " so that the next print statement doesnt skip lines
