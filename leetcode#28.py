'''28. Implement strStr()
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
Clarification:What should we return when needle is an empty string?
For the purpose of this problem, we will return 0 when needle is an empty string.
#  Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2
#  Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''


def strStr(haystack,needle):
    if needle == "":
        return 0
    for i in range(len(haystack) + 1 + len(needle)):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1

print(strStr('hello','ll'))
print(strStr('implementation','tation'))
print(strStr('aaaaa', 'bba'))