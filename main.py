
from config import path_to_file
from stats import get_num_words, get_num_chars

def main():
    print(get_num_words(path_to_file))
    print(get_num_chars(path_to_file))


main()