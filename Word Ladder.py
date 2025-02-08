# Word Ladder
# You are given two words, beginWord and endWord, and also a list of words wordList. All of the given words are of the same length, consisting of lowercase English letters, and are all distinct.

# Your goal is to transform beginWord into endWord by following the rules:

# You may transform beginWord to any word within wordList, provided that at exactly one position the words have a different character, and the rest of the positions have the same characters.
# You may repeat the previous step with the new word that you obtain,
#  and you may do this as many times as needed.
# Return the minimum number of words within the transformation sequence needed to
#  obtain the endWord, or 0 if no such sequence exists.

# Example 1:

# Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]

# Output: 4
# Explanation: The transformation sequence is "cat" -> "bat" -> "bag" -> "sag".

# Example 2:

# Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sat","dag","dot"]

# Output: 0
# Explanation: There is no possible transformation sequence from "cat" to "sag"
#  since the word "sag" is not in the wordList.

from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
       if endWord == beginWord or endWord not in wordList:
           return 0
       m = len(wordList[0])
       steps = 0
       wordSet = set(wordList)
       fromBegin = {beginWord:1}
       fromEnd = {endWord:1}
       qb = deque([beginWord])
       qe = deque([endWord])
       while qb and qe:
           if len(qb)>len(qe):
               qb,qe = qe,qb
               fromBegin,fromEnd = fromEnd,fromBegin
           for _ in range(len(qb)):
                word = qb.popleft()
                steps = fromBegin[word]
                for i in range(m):
                    for k in range(97,123):
                        if word[i] == chr(k):
                            continue
                        nei = word[:i] + chr(k) + word[i+1:]
                        if nei not in wordSet:
                            continue
                        if nei in fromEnd:
                            return steps + fromEnd[nei]
                        if nei not in fromBegin:
                            fromBegin[nei] = 1 +steps
                            qb.append(nei)
       return 0
                                                      
