# Find maximum length of a substring of a string with first charachter lexicographically smaller than its last charachter.
# assume string length 10^5 char long, assume 26 small case english letters in string
# solve it in linear time.
# input : "dbabcb"
# output : 4

"""
Using two pointer approach
TC = O(n)
SC = O(n)
"""
def max_valid_substring_length(s):
    n = len(s)
    first_pos = [-1]*26
    max_len = 0
    for i,c in enumerate(s):
        index = ord(c) - ord("a")
        if first_pos[index] == -1:
            first_pos[index] = i
    for j in range(n):
        lexIndex = ord(s[j]) - ord('a')
        for c in range(lexIndex):
            if first_pos[c] != -1:
                max_len = max(max_len,j-first_pos[c]+1)
    return max_len

        