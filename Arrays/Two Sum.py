# Two Sum
# Solved 
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:
# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        result = []
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in hashmap:
                result.append(hashmap[temp])
                result.append(i)
            else:
                hashmap[nums[i]] = i
        return result