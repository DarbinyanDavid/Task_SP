def coincidence(lst=[], rng=range(0)):
    if not lst or not rng:
        return []

    result = []

    for item in lst:
        if item is None:
            continue

        if isinstance(item, (int, float)):
            if rng.start <= item < rng.stop:
                result.append(item)
        else:
            try:
                float_item = float(item)
            except ValueError:
                continue

            if rng.start <= float_item < rng.stop:
                result.append(float_item)

    return sorted(result)


# Тесты
print(coincidence([1, 2, 3, 4, 5], range(3, 6)))  # => [3, 4, 5]
print(coincidence())  # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))  # => [1, 2, 2.5]

