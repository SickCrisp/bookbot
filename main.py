def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # num_words = get_num_words(text)
    # char_count = get_num_chars(text)

    create_report(text)


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


# This function is good. Boots verified
def get_letter_count(text):
    lower_text = text.lower()
    char_dict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
                }

    for letter in lower_text:
        if letter.isalpha():
            char_dict[letter] += 1

    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=sorting)
    return char_list


# Sorting is good
def sorting(dict):
    return dict["num"]
        

# TODO Finish this
def create_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print()
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print()
    reported_chars = get_letter_count(text)

    for letter in reported_chars:
        char = letter["char"]
        value = letter["num"]
        print(f"The '{char}' character was found {value} times")

    print("--- End report ---")


main()