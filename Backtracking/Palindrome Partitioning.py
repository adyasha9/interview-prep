# Palindrome Partitioning
# Solved 
# Given a string s, split s into substrings where every substring is a 
# palindrome. Return all possible lists of palindromic substrings.

# You may return the solution in any order.

# Example 1:

# Input: s = "aab"

# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"

# Output: [["a"]]
# Constraints:

# 1 <= s.length <= 20
# s contains only lowercase English letters.
from typing import List
def palindromePartition(s:str)->List[List[str]]:
    res = []
    sol = []
    n = len(s)
    def backtrack(i,j):
        if i ==n:
            res.append(sol[:])
            return
        if j>n:
            return
        temp = s[i:j+1]
        if temp == temp[::-1]:
            sol.append(temp)
            backtrack(j+1,j+1)
            sol.pop()
        backtrack(i,j+1)
    backtrack(0,0)
    return res
s = "aab"
print(palindromePartition(s))
