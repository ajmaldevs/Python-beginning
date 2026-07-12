import cowsay
import pyttsx3
engine=pyttsx3.init()


say=input("Whats the text: ")
cowsay.dragon(say)
engine.say(say)
engine.runAndWait()

