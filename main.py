import sys
from stats import get_num_words
from stats import get_count_characters
from stats import sort_on
from stats import get_sorted_char_counts_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    raw_counts = get_count_characters(text)
    char_counts = get_sorted_char_counts_list(raw_counts)
      
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in char_counts:
        character = char["char"]
        count = char["num"]
        print(f"{character}: {count}")  
    print("============= END ===============")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
main(book_path)