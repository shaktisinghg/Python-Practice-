import argparse

parser = argparse.ArgumentParser(description="sumple line counter in file")

parser.add_argument('filename', help='file which line to count ')

args = parser.parse_args()
# print(args)

with open(args.filename, 'r') as f:
    lines = f.readlines()
    print(len(lines))

