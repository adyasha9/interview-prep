# LRU Cache
# Solved 
# Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the 
# following operations

# LRUCache(int capacity) Initialize the LRU cache of size capacity.
# int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, 
# add the key-value pair to the cache. If the introduction of the new pair causes the cache to 
# exceed its capacity, remove the least recently used key.
# A key is considered used if a get or a put operation is called on it.

# Ensure that get and put each run in 
# O
# (
# 1
# )
# O(1) average time complexity.

# Example 1:

# Input:
# ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], 
# "put", [3, 30], "get", [2], "get", [1]]

# Output:
# [null, null, 10, null, null, 20, -1]

# Explanation:
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 10);  // cache: {1=10}
# lRUCache.get(1);      // return 10
# lRUCache.put(2, 20);  // cache: {1=10, 2=20}
# lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
# lRUCache.get(2);      // returns 20 
# lRUCache.get(1);      // return -1 (not found)
# Constraints:

# 1 <= capacity <= 100
# 0 <= key <= 1000
# 0 <= value <= 1000


from typing import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last = False)
        
lru = LRUCache(2)
lru.put(1, 1)  # Cache = {1=1}
lru.put(2, 2)  # Cache = {1=1, 2=2}
print(lru.get(1))  # Returns 1, Cache = {2=2, 1=1}
lru.put(3, 3)  # LRU (2) is removed, Cache = {1=1, 3=3}
print(lru.get(2))  # Returns -1 (2 was evicted)
lru.put(4, 4)  # LRU (1) is removed, Cache = {3=3, 4=4}
print(lru.get(1))  # Returns -1
print(lru.get(3))  # Returns 3
print(lru.get(4))  # Returns 4

# Using Doubly Linked List & HashMap

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.cache = {}
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        newnode = Node(key,value)
        self._add_to_front(newnode)
        self.cache[key] = newnode
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


lru = LRUCache(2)
lru.put(1, 1)  # Cache = {1=1}
lru.put(2, 2)  # Cache = {1=1, 2=2}
print(lru.get(1))  # Returns 1, Cache = {2=2, 1=1}
lru.put(3, 3)  # LRU (2) is removed, Cache = {1=1, 3=3}
print(lru.get(2))  # Returns -1 (2 was evicted)
lru.put(4, 4)  # LRU (1) is removed, Cache = {3=3, 4=4}
print(lru.get(1))  # Returns -1
print(lru.get(3))  # Returns 3
print(lru.get(4))  # Returns 4

