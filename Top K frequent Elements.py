# Top K Frequent Elements
# Solved 
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]

import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num,0)
        minHeap = []
        for num in hashmap.keys():
            heapq.heappush(minHeap,(hashmap[num],num))
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res