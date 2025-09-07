import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", type=str, help="Input file")
parser.add_argument("--filter", type=str, help="keyword")

args = parser.parse_args()

input_file = args.input
keyword = args.filter


try:
    with open(input_file) as f:
        data = f.readlines()
        for line in data:
            line = line.strip("\n")
            if keyword in line:
                print(line)
except FileExistsError as e:
    print()