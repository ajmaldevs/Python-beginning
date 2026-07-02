def main():
    a=use_int()
    print(f"X is {a}")

def use_int():
    while True:
        try:
            x=int(input("Whats x? "))
            return x
        except ValueError:
            pass

main()
# here the pass keyword is used what it does is
# nothing pass keyword is used when you literally wanna do nothing just ignore if something happens
# this makes the program repeat whats x? 