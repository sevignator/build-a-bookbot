def main():
    book_path = "books/frankeinstein.txt"
    text = get_file_text(book_path)
    word_count = get_word_count(text)
    print(f"This document contains {word_count} words.")


def get_word_count(text):
    words = text.split()
    return len(words)


def get_file_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


main()
