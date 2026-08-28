import time
import sys

def welcome():
    welcome="Welcome to ⌨️  Typing Speed Tester..........\nBeginning......   3️⃣  2️⃣  1️⃣  \n"
    for char in welcome:
        print(char,end="",flush=True)
        time.sleep(0.125)
    time.sleep(0.5)

def times():
    start_time=time.time()
    variable=input("Enter the Sentence: ")
    end_time=time.time()
    time_taken=(end_time-start_time)
    return variable,time_taken

def words(variable):
    count=0
    for i in variable:
        count=count+1

    wc=1
    for j in variable:
        if " " in j:
            wc=wc+1

    return count,wc

def quality(wc,character,time_taken):
    typing_score=(wc*60+character)/time_taken
    return typing_score

def main():
    welcome()
    variable,time_taken=times()
    count,wc=words(variable)
    score=quality(wc,count,time_taken)

    print(f"✨ Number of Characters: {count}")
    time.sleep(0.5)
    print(f"🌐 Word Count: {wc}")
    time.sleep(0.5)
    print(f"⏱️ Time Taken :{time_taken:.2f} Seconds")
    time.sleep(0.5)
    print(f"🔖 Typing Score :{score:.2f}")

if __name__=="__main__":
    try:
        main()
    except ValueError:
        print("Value Error..")
        sys.exit()
