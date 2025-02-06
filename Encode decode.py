# Encode and Decode Strings
# Solved 
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode
# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s 
        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1
            length = int(s[i:j])
            i = j+1
            j = i + length
            res.append(s[i:j])
            i=j
        return res