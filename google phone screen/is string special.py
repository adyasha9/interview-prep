# given a string s and a list of strings st.
# A string is special if its length >= 3 
# and it is a subsequence of the string s,
# and the string should be present in st.
# given a string s and st, return true if all 
# the subsequences(length >= 3) are special words. else return false.
# s = "abcd"
# st = ["abc", "bcd", "acd"]

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.is_end = True
    def search(self,word):
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.is_end
       # Step 2: Use DFS with memoization to check subsequences
memo = {}

def dfs(idx, subseq):
    if len(subseq) >= 3:
        if subseq in memo:
            return memo[subseq]
        if not trie.search(subseq):  # If any subsequence is invalid, return False
            memo[subseq] = False
            return False
        memo[subseq] = True

        for i in range(idx, len(s)):
            if not dfs(i + 1, subseq + s[i]):  
                return False  # Early termination if found an invalid subsequence
        return True

    return dfs(0, "")

def is_special(s, st):
    trie = Trie()
    for word in st:
        if len(word) >= 3:
            trie.insert(word)

