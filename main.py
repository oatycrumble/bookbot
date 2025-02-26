from stats import (
    get_num_words,
    get_chars_dict,
    get_sorted_list,
)

from sys import argv, exit

def main():

    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    book_path = argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    sorted_dict = get_sorted_list(get_chars_dict(text))
    print_report(book_path, num_words, sorted_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        char = item["char"]
        count = item["count"]
        print(f"{char}: {count}")
    print("============= END ===============")

main()
