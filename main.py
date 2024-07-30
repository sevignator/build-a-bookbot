def main():
    """Main function for this program."""

    book_path = "books/frankenstein.txt"
    print_report(book_path)


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


def print_report(path_to_file: str):
    """Print a human-readable report to the console."""

    text = get_file_text(path_to_file)
    word_count = get_word_count(text)
    char_count_dict = get_char_count(text)
    char_count_list = list(
        map(
            lambda char: {"char": char, "count": char_count_dict[char]},
            filter(lambda char: char.isalpha(), list(char_count_dict)),
        )
    )
    char_count_list.sort(reverse=True, key=lambda item: item["count"])

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")

    for item in char_count_list:
        print(f"The \'{item['char']}\' character was found {item['count']} times")

    print("--- End report ---")


main()
