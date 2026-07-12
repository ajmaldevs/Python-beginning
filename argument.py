import argparse

arg=argparse.ArgumentParser()
arg.add_argument("-n")
args=arg.parse_args()

for _ in range(int(args.n)):
    print("meow")