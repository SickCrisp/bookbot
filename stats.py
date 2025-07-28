# Take in book, open it, and read it. Then return the text
def get_book_text(path):
    with open(path) as f:
        return f.read()


# Split text into words and return number of words, no message
def get_num_words(path):
    text = get_book_text(path).split()
    num_words = 0
    for words in text:
        num_words += 1
    return num_words


# Get the number of characters within the text
def get_num_chars(path):
    chars = {}
    text = get_book_text(path).lower().split()
    for word in text:
        for letter in word:
            if letter.isalpha():
                if letter in chars:
                    chars[letter] += 1
                else:
                    chars[letter] = 1
    return chars


def create_report(path):
    num_words = get_num_words(path)
    counts_dict = get_num_chars(path)
    counts_dict_desc = sorted(counts_dict.items(), key=lambda item: item[1], reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter, count in counts_dict_desc:
        print(f"{letter}: {count}")
    print("============= END ===============")