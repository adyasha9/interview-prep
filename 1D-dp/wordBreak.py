# Word Break
# Solved 
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into
# a space-separated sequence of dictionary words.

# You are allowed to reuse words in the dictionary an unlimited number of times. 
# You may assume all dictionary words are unique.

# Example 1:

# Input: s = "neetcode", wordDict = ["neet","code"]

# Output: true
# Explanation: Return true because "neetcode" can be split into "neet" and "code".

# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen","ape"]

# Output: true
# Explanation: Return true because "applepenapple" can be split into "apple", "pen" and
# "apple". Notice that we can reuse words and also not use all the words.

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s):True}
        def dfs(i):
            if i in memo:
                return memo[i]
            for w in wordDict:
                if ((len(w)<=len(s)) and s[i:i+len(w)] == w):
                    if dfs(i+len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)
