# Letter Combinations of a Phone Number
# Solved 
# You are given a string digits made up of digits from 2 through 9 inclusive.

# Each digit (not including 1) is mapped to a set of characters as shown below:

# A digit could represent any one of the characters it maps to.

# Return all possible letter combinations that digits could represent. You may return the answer in any order.



# Example 1:

# Input: digits = "34"

# Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
# Example 2:

# Input: digits = ""

# Output: []
from typing import List
def letterCombination(digits:str)-> List[str]:
    n = len(digits)
    numToChar = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    res = []
    def backtrack(i,curr):
        if i == n:
            res.append(curr)
            return
        for c in numToChar[digits[i]]:
            backtrack(i+1,curr+c)
    backtrack(0,"")
    return res
digits = "34"
print(letterCombination(digits))