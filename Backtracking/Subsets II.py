# Subsets II
# Solved 
# You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

# The solution must not contain duplicate subsets. You may return the solution in any order.

# Example 1:

# Input: nums = [1,2,1]

# Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
# Example 2:

# Input: nums = [7,7]

# Output: [[],[7], [7,7]]
# Constraints:

# 1 <= nums.length <= 11
# -20 <= nums[i] <= 20
from typing import List
def subsets(nums:List)->List[List[int]]:
    n = len(nums)
    res = []
    nums.sort()
    def backtracking(i,curr):
        res.append(curr[:])
        for j in range(i,n):
            if j>i and nums[j-1] == nums[j]:
                continue
            curr.append(nums[j])
            backtracking(j+1,curr)
            curr.pop()
    backtracking(0,[])
    return res
nums = [1,2,1]
print(subsets(nums))
