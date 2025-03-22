import sys
from stats import get_word_count, get_letter_counts, sort_letter_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    frankenstein_text = get_book_text(book_path)

    print("----------- Word Count ----------")
    num_words = get_word_count(frankenstein_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    num_letters = get_letter_counts(frankenstein_text)
    sorted_counts = sort_letter_counts(num_letters)
    for count in sorted_counts:
        if count["letter"].isalpha():
            print(f"{count['letter']}: {count['count']}")
    
    print("============= END ===============")

main()