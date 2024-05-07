def count_words(string: str) -> dict:
    words = string.lower().split()

    word_counts = {}

    for word in words:
        if word == '--':
            continue
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

    return word_counts


def print_dict_in_expected_format(dictionary: dict):
    print("{", end="")
    for key, value in dictionary.items():
        print(f"'{key}': {value}, ", end="")
    print("}")


# Примеры тестов
print_dict_in_expected_format(count_words("A man, a plan, a canal -- Panama"))
print_dict_in_expected_format(count_words("Doo bee doo bee doo"))
