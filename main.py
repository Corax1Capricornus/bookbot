from stats import num_words
from stats import num_letters
from stats import report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    result = num_words(text)
    num_letters_result = num_letters(text)
    Dict = report(num_letters_result)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {result} total words.")
    print("--------- Character Count -------")
    for char_dict in Dict:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
