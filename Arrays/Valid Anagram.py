# Valid Anagram
# Solved 
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_s = {}
        hashmap_t = {}
        for i in range(len(s)):
            if s[i] not in hashmap_s:
                hashmap_s[s[i]] = 1
            else:
                hashmap_s[s[i]] += 1
            if t[i] not in hashmap_t:
                hashmap_t[t[i]] = 1
            else:
                hashmap_t[t[i]] +=1
        return hashmap_t == hashmap_s