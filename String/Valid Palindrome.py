# Valid Palindrome
# Solved 
# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for i in range(len(s)):
            if s[i].isalnum():
                s_new += s[i].lower()
        return s_new == s_new[::-1]