# Longest Substring with At Most Two Distinct Characters
# Given a string s, return the length of the longest substring that contains at most two distinct characters.

# Example 1:
# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which contains 2 distinct characters.
# Example 2:
# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which contains 2 distinct characters.
# Constraints:
# 1 <= s.length <= 10^5
# s consists of English letters.



def longestSubstring(s:str) -> int:
    n = len(s)
    max_length = 0
    hashmap = {}
    l = 0 
    for r in range(n):
        hashmap[s[r]] = 1 + hashmap.get(s[r],0)
        while len(hashmap) > 2:
            hashmap[s[l]] -= 1
            if hashmap[s[l]] == 0:
                del hashmap[s[l]]
            l += 1
        max_length = max(max_length, r - l + 1)
    return max_length
s = "eceba"
print(longestSubstring(s))

