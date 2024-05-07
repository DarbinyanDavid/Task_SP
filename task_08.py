def multiply_numbers(inputs=None):
    if inputs is None or not isinstance(inputs, (str, int, float, list)):
        return None

    digits = []
    if isinstance(inputs, str):
        digits = [int(char) for char in inputs if char.isdigit()]
    elif isinstance(inputs, (int, float)):
        digits = [int(char) for char in str(inputs) if char.isdigit()]
    elif isinstance(inputs, list):
        digits = [int(num) for num in inputs if isinstance(num, int)]

    if digits:
        product = 1
        for digit in digits:
            product *= digit
        return product
    else:
        return None


# Тесты
print(multiply_numbers())  # => None
print(multiply_numbers('ss'))  # => None
print(multiply_numbers('1234'))  # => 24
print(multiply_numbers('sssdd34'))  # => 12
print(multiply_numbers(2.3))  # => 6
print(multiply_numbers([5, 6, 4]))  # => 120
