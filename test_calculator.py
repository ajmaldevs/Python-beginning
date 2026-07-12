from calcul import square


def main():
    test_cal()

def test_cal():
    if square(2)!=4:
        print("2 Square is not 4")
    if square(3)!=9:
        print("3 square is not 9")

main()