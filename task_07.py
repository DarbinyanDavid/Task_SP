from typing import List, Dict


def combine_anagrams(words_array: List[str]) -> List[List[str]]:
    anagram_groups: Dict[str, List[str]] = {}

    for word in words_array:

        sorted_word = ''.join(sorted(word.lower()))

        if sorted_word in anagram_groups:

            anagram_groups[sorted_word].append(word)

        else:

            anagram_groups[sorted_word] = [word]

    return list(anagram_groups.values())


# Тест
words = ["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]
print(combine_anagrams(words))  # => [["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"], ["creams", "scream"]]
