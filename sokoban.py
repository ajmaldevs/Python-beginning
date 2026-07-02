def main():
    history=[]

    while True:
        act=input("Enter Action: ")
        action=act.lower()
        if action=="undo":
            red=history.pop()
            print(f"Undone:{red}")
        elif action=="restart":
            history.clear()
            print("History Cleared")
        elif action=="stop":
            break
        else:
            history.append(action)
        print(history)

main()
