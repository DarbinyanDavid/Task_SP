def is_palindrome(input):
    if isinstance(input, str):
        cleaned_string = input.lower().replace(" ", "").replace(",", "").replace(".", "").replace("-", "").replace("!",
                                                                                                                   "").replace(
            "'", "")

        return cleaned_string == cleaned_string[::-1]

    elif isinstance(input, int):
        string = str(input)

        return string == string[::-1]

    #
    else:
        return False


print(is_palindrome("A man, a plan, a canal -- Panama"))  # True
print(is_palindrome("Madam, I'm Adam!"))  # True
print(is_palindrome(333))  # True
print(is_palindrome(None))  # False
print(is_palindrome("Abracadabra"))  # False
print(is_palindrome(12321))  # True
print(is_palindrome(12345))  # False
print(is_palindrome(100001))  # True
