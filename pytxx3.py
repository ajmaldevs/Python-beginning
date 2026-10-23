import pyttsx3
engine=pyttsx3.init()
name=input("Enter your name: ").title()
engine.say(f"Hi {name}")
engine.runAndWait()
print("Program Executed Successfully..")