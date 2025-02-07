# Word Search II
# Solved 
# Given a 2-D grid of characters board and a list of strings words,
#  return all words that are present in the grid.

# For a word to be present it must be possible to form the word with
# a path in the board with horizontally or vertically neighboring cells. 
# The same cell may not be used more than once in a word.

# Example 1:



# Input:
# board = [
#   ["a","b","c","d"],
#   ["s","a","a","t"],
#   ["a","c","k","e"],
#   ["a","c","d","n"]
# ],
# words = ["bat","cat","back","backend","stack"]

# Output: ["cat","back","backend"]



from typing import List


class TrieNode: 
    def __init__(self):
        self.trie = {}
    def addWord(self,word):
        d = self.trie
        for w in word:
            if w not in d:
                d[w] = {}
            d = d[w]
        d["."] = "."

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        rowLen = len(board)
        colLen = len(board[0])
        res, visit = set(),set()
        def dfs(r,c,node,word):
            if (r<0 or c<0 or r>=rowLen or c>= colLen or (r,c) in visit or board[r][c] not in node):
                return 
            visit.add((r,c))
            word += board[r][c]
            node = node[board[r][c]]
            if '.' in node:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        for r in range(rowLen):
            for c in range(colLen):
                dfs(r,c,root.trie,"")
        return list(res)