def sort_list(lst: list) -> list:
    if not lst:
        return []

    min_value = min(lst)
    max_value = max(lst)

    for i, value in enumerate(lst):
        if value == min_value:
            lst[i] = max_value
        elif value == max_value:
            lst[i] = min_value

    lst.append(min_value)

    return lst


# Тесты
print(sort_list([]))  # => []
print(sort_list([2, 4, 6, 8]))  # => [8, 4, 6, 2, 2]
print(sort_list([1]))  # => [1, 1]
print(sort_list([1, 2, 1, 3]))  # => [3, 2, 3, 1, 1]
