# Two Integer Sum II
# Solved 
# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use 
# O
# (
# 1
# )
# O(1) additional space.

# Example 1:

# Input: numbers = [1,2,3,4], target = 3

# Output: [1,2]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        result = []
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if temp not in hashmap:
                hashmap[numbers[i]] = i
            else:
                result = [i+1,hashmap[temp]+1]
        return sorted(result)       