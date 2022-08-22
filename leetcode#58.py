'''58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
#  Example 1:
Input: s = "Hello World"
Output: 5
#  Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
#  Example 3:
Input: s = "luffy is still joyboy"
Output: 6
'''


def lengthOfLastWord(s):
    s = s.split()
    return len(s[-1])

print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("luffy is still joyboy"))