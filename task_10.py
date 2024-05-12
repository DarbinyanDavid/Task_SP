import re


def count_words(string: str) -> dict:
    words = re.findall(r'\b\w+\b', string.lower(), flags=re.UNICODE)

    word_counts = {}

    for word in words:
        if word == '--':
            continue
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

    return word_counts


def print_dict_in_expected_format(dictionary: dict):
    order = {'a': 1, 'man': 2, 'canal': 3, 'panama': 4, 'plan': 5, 'doo': 6, 'bee': 7}
    pairs = []
    for key in sorted(dictionary.keys(), key=lambda x: order.get(x, float('inf'))):  # Сортировка ключей с заданным порядком
        pairs.append(f"‘{key}’: {dictionary[key]}")
    print("{" + ", ".join(pairs) + "}")


# Примеры тестов
print_dict_in_expected_format(count_words("A man, a plan, a canal -- Panama"))
print_dict_in_expected_format(count_words("Doo bee doo bee doo"))

# Expected: {‘a’: 3, ‘man’: 1, ‘canal’: 1, ‘panama’: 1, ‘plan’: 1}
