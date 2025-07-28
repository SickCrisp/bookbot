
import sys
from stats import create_report

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    program = sys.argv[0]
    path_to_file = sys.argv[1]


def main():
    create_report(path_to_file)


main()