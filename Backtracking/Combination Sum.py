# Combination Sum
# Solved 
# You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

# The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

# Example 1:

# Input: 
# nums = [2,5,6,9] 
# target = 9

# Output: [[2,2,5],[9]]
# Explanation:
# 2 + 2 + 5 = 9. We use 2 twice, and 5 once.
# 9 = 9. We use 9 once.

# Example 2:

# Input: 
# nums = [3,4,5]
# target = 16

# Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]
# Example 3:

# Input: 
# nums = [3]
# target = 5

# Output: []
# Constraints:

# All elements of nums are distinct.
# 1 <= nums.length <= 20
# 2 <= nums[i] <= 30
# 2 <= target <= 30

from typing import List

def combinationSum(nums: List[int], target: int) -> List[List[int]]:
    res = []
    n = len(nums)
    nums.sort()
    def backtrack(i,total,curr):
        if total == target:
            res.append(curr[:])
            return
        for j in range(i,n):
            if total + nums[j] > target:
                return
            curr.append(nums[j])
            backtrack(i+1,total+nums[j],curr)
            curr.pop()
    backtrack(0,0,[])
    return res
nums = [3,4,5]
target = 16
print(combinationSum(nums,target))