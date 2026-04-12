import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--number", type=int, default=0, help="Enter a number")

args = parser.parse_args()

print(args.number)