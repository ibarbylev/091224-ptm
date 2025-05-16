import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Path to input file')
parser.add_argument('--output', help='Path to output file')
args = parser.parse_args()

print(args.input)
print(args.output)


# python theory_06_argparse_practice.py --output 10 --input 5

