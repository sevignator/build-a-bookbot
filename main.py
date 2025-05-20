import sys
from stats import get_num_words, get_char_count, get_sorted_char_count


def get_book_text(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def print_report(file_path: str, text: str, num_words: int, chars_list: list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in chars_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    chars_list = get_sorted_char_count(char_count)

    print_report(file_path, text, num_words, chars_list)


main()
