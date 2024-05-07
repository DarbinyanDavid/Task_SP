from typing import Dict


def count_words(string: str) -> Dict[str, int]:
    words = string.lower().split()

    word_counts = {}

    for word in words:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

    return word_counts


# Тесты
print(count_words("A man, a plan, a canal -- Panama"))  # => {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}
print(count_words("Doo bee doo bee doo"))  # => {"doo": 3, "bee": 2}
