# Concept:

# Stores words efficiently for prefix-based lookups.
# Used in Autocomplete, Spell Checking, Dictionary Matching.


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word:str)->None:
        d = self.trie
        for char in word:
            if char not in d:
                d[char] = {}
            d = d[char]
        d['.'] = '.'

    def search(self, word:str)->bool:
        d = self.trie
        for char in word:
            if char not in d:
                return False
            d = d[char]
        return '.' in d

    def starts_with(self, prefix:str)->bool:
        d = self.trie
        for char in prefix:
            if char not in d:
                return False
            d = d[char]
        return True

# Test
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # Output: True
print(trie.starts_with("app"))  # Output: True
print(trie.search("ape"))  # Output: False


#          (root)
#         /     \
#        a       d
#       / \       \
#      p   p       o
#     /     \       \
#    p       p       g  ← "dog"
#     \       \
#      .       l
#               \
#                l
#                 \
#                   e
#                    \
#                     .