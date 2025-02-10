def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        count = len(words)
        print(count)


if __name__ == "__main__":
    main()
    count_words()