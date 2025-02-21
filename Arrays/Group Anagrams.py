# Group Anagrams
# Solved 
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap  = {}
        result = []
        for s in strs:
            temp = ''.join(sorted(s))
            if temp in hashmap:
                hashmap[temp].append(s)
            else:
                hashmap[temp] = [s]
        return hashmap.values()