def main():
    """Main function for this program."""

    book_path = "books/frankenstein.txt"
    text = get_file_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    print(f"This document contains {word_count} words.")
    print(char_count)


def get_word_count(text: str):
    """Read a string and return a number indicating how many words it contains."""

    words = text.split()
    return len(words)

def get_char_count(text: str):
    """Read a string and return a dictionary indicating the count of each character."""

    chars = {}

    for char in text:
        converted_char = char.lower()

        if converted_char not in chars:
            chars[converted_char] = 0

        chars[converted_char] += 1

    return chars


def get_file_text(path_to_file: str):
    """Open a text file from a given path and return its contents as a string."""

    with open(path_to_file, encoding="utf-8") as f:
        return f.read()


main()
