# Valid Parenthesis String
# Solved 
# You are given a string s which contains only three types of characters: '(', ')' and '*'.

# Return true if s is valid, otherwise return false.

# A string is valid if it follows all of the following rules:

# Every left parenthesis '(' must have a corresponding right parenthesis ')'.
# Every right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# A '*' could be treated as a right parenthesis ')' character or a left parenthesis 
# '(' character, or as an empty string "".
# Example 1:

# Input: s = "((**)"

# Output: true
# Explanation: One of the '*' could be a ')' and the other could be an empty string.

# Example 2:

# Input: s = "(((*)"

# Output: false

class Solution:
    def checkValidString(self, s: str) -> bool:
        openBrack = 0
        closeBrack = 0
        for c in s:
            if c =="(":
                openBrack,closeBrack = openBrack+1,closeBrack+1
            elif c == ")":
                openBrack,closeBrack = openBrack -1, closeBrack -1
            else:
                openBrack,closeBrack = openBrack -1, closeBrack +1
            if closeBrack<0:
                return False
            if openBrack<0:
                openBrack = 0
        return openBrack == 0