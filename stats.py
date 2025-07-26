from config import path_to_file


# Take in book, open it, and read it. Then return the text
def get_book_text(path):
    with open(path) as f:
        return f.read()


# Split text into words and return number of words
def get_num_words(path):
    text = get_book_text(path).split()
    num_words = 0
    for words in text:
        num_words += 1
    message = f"{num_words} words found in the document"
    return message

num_words = get_num_words(path_to_file)


# Get the number of characters within the text
def get_num_chars(path):
    chars = {}
    text = get_book_text(path).lower().split()
    for words in text:
        for letters in words:
            if letters in chars:
                chars[letters] += 1
            else:
                chars[letters] = 1
    return chars

counts_dict = get_num_chars(path_to_file)

def create_report(path, num_words, counts_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_dict = sorted(counts_dict)
    for letter in sorted_dict:
        print(f"{letter} = {counts_dict[letter]}")


print(create_report(path_to_file, num_words, counts_dict))