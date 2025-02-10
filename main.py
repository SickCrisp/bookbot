def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_num_chars(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    print(char_count)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_num_chars(text):
    lower_text = text.lower()
    char_count = {}
    for letter in lower_text:
        if letter not in char_count:
            char_count[letter] = 1
        else:
            char_count[letter] += 1
    return char_count


main()