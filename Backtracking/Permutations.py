# Permutations
# Solved 
# Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]

# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [7]

# Output: [[7]]
# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
from typing import List
def permutations(nums:List)->int:
    n = len(nums)
    res = []
    def backtrack(i,curr):
        if i == n:
            res.append(curr[:])
            return
        for j in range(i,n):
            curr[i],curr[j] = curr[j],curr[i]
            backtrack(i+1,curr)
            curr[i],curr[j] = curr[j],curr[i]
    backtrack(0,nums)
    return res
nums = [1,2,3]
print(permutations(nums))
