import re
def is_palindrome(string):
    clean = re.sub(r'[^a-zA-Z0-9]', '', string).lower()
    return clean == clean[::-1]


print(is_palindrome("momomm"))  # Expected output: True
print(is_palindrome("A man, a plan, a canal: Panama"))  # Expected output: True
print(is_palindrome("hello"))  # Expected output: False

