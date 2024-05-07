def is_palindrome(data):
    data = data.replace(' ', '').lower()
    data = ''.join(filter(lambda c: c.isalpha(), data))
    return True if data == data[::-1] else False


print(is_palindrome("A man, a plan, a canal -- Panama"))  # => True

