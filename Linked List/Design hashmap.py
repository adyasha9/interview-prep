# 706. Design HashMap
# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. 
# If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 
# if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the 
# mapping for the key.
 

# Example 1:

# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

class ListNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None 
class MyHashMap:

    def __init__(self):
        self.size = 100
        self.buckets = [None] * self.size

    def hash(self,key):
        return key%self.size 

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = ListNode(key,value)
        else: 
            cur = self.buckets[index]
            while True:
                if cur.key == key:
                    cur.value = value
                    return
                if cur.next is None:
                    break
                cur = cur.next
            cur.next = ListNode(key,value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1
    
    def remove(self, key: int) -> None:
        index = self.hash(key)
        curr = self.buckets[index]
        prev = None
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next  # Remove node from linked list
                else:
                    self.buckets[index] = curr.next  # Update head
                return
            prev, curr = curr, curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)