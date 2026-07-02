import csv

name=input("Whats your name: ")
home= input("Where is your home: ")

with open("students.csv","a") as file:
    write=csv.writer(file)
    write.writerow([name,home])

#here instead of csv.writer i could use dict writer for a more advanced way in which it would take the file as a list and search accordingly or add
#accordingly with the keys 