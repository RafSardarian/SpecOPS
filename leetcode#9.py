'''Palindrome number'''


def isPalindrome(x):
    if x < 0:
        return None
    x = list(str(x))
    if x[0:] == x[::-1]:
        return True
    return False


print(isPalindrome(1001))
print(isPalindrome(1222332221))
print(isPalindrome(8557))
print(isPalindrome((-121)))