# Generate Parentheses
# Category	Difficulty	Likes	Dislikes
# algorithms	Medium (76.02%)	21789	1009
# Tags
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8


# generrate the parantheses using stack and backtracking
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(openN,closedN):
            if openN == closedN == n:     # append to result when open parantheses == closed == n given
                res.append("".join(stack))
                return 
            if openN < n:                  # start by appending open brack
                stack.append("(")
                backtrack(openN+1,closedN)   # increase open count
                stack.pop()                   # backtrack
            if closedN < openN:
                stack.append(")")           # if closed parantheses are less than open then add one
                backtrack(openN,closedN+1)  # increase close count
                stack.pop()                 # backtrack
        backtrack(0,0)                      # start with 0,0 
        return res                          # return result