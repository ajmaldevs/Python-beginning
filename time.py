import time
welcome="Welcome to Typing Speed Tester.........."
for char in welcome:
    print(char,end="",flush=True)
    time.sleep(0.5)
time.sleep(1)
print("beginning.....")
time.sleep(2)
start_time=time.time()
variable=input("Enter the Sentence: ")
end_time=time.time()
time_taken=(end_time-start_time)
count=0
for i in variable:
    count=count+1

wc=1
for j in variable:
    if " " in j:
        wc=wc+1

print(f"✨ Number of Characters: {count}")
time.sleep(0.5)
print(f"🌐 Word Count: {wc}")
time.sleep(0.5)
print(f"⏱️ Time Taken :{time_taken:.2f} Seconds")
