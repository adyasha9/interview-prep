# Subsets
# Solved 
# Given an array nums of unique integers, return all possible subsets of nums.

# The solution set must not contain duplicate subsets. You may return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]

# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [7]

# Output: [[],[7]]

from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    sol = []
    def backtrack(i):
        if i==len(nums):
            res.append(sol[:])
            return
        backtrack(i+1)
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop()
    backtrack(0)
    return res
nums = [1,2,3]
print(subsets(nums))