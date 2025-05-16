import sys
from stats import get_num_words, get_num_characters, sort_character_counts

def get_book_text(filePath):
    with open(filePath) as f:
        fileContents = f.read()
    return fileContents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_characters = get_num_characters(book_text)
    sorted_count = sort_character_counts(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_count:
        print(f"{c['char']}: {c['num']}")
    print("============= END ===============")


main()
