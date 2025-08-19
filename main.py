import sys
from stats import get_char_frequency, get_word_count, sort_frequency

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_frequency = get_char_frequency(book_text)
    sorted_frequency = sort_frequency(char_frequency)
    print("--------- Character Count -------")
    for entry in sorted_frequency:
        print(f"{entry["char"]}: {entry["count"]}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
