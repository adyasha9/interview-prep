# Word Search
# Solved 
# Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

# For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

# Example 1:



# Input: 
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "CAT"

# Output: true
# Example 2:



# Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"

# Output: false
# Constraints:

# 1 <= board.length, board[i].length <= 5
# 1 <= word.length <= 10
# board and word consists of only lowercase and uppercase English letters.

from typing import List
from xmlrpc.client import boolean

def exist(board:List[List[str]],word:str) -> boolean:
    row = len(board)
    col = len(board[0])
    n = len(word)
    def backtrack(r,c,i):
        if i == n:
            return True
        if r>=row or c>= col or i>n:
            return False
        board[r][c] = '#'
        res = (backtrack(r+1,c,i+1) or backtrack(r-1,c,i+1) or backtrack(r,c+1,i+1) or backtrack(r,c-1,i+1))
        board[r][c] = word[i]
        return res
    for r in range(row):
        for c in range(col):
            if backtrack(r,c,0):
                return True
    return False
