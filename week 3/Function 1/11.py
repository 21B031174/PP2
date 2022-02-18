
def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string



s=input()
print(is_palindrome(s))