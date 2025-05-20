def get_num_words(text: str):
    num_words = len(text.split())
    return f"{num_words} words found in the document"


def get_char_count(text: str):
    text_to_lowercase = text.lower()
    chars = {}

    for char in text_to_lowercase:
        if char not in chars:
            chars[char] = 0

        chars[char] = chars[char] + 1

    return chars


def get_sorted_char_count(char_count_dict: dict):
    sorted_list = []

    for ch in char_count_dict:
        sorted_list.append({"char": ch, "num": char_count_dict[ch]})

    sorted_list.sort(reverse=True, key=lambda d: d["num"])

    return sorted_list
