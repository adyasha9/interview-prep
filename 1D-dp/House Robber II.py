# House Robber II
# Solved 
# You are given an integer array nums where nums[i] represents the amount of money the ith house has.
# The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

# You are planning to rob money from the houses, but you cannot rob two adjacent houses because
# the security system will automatically alert the police if two adjacent houses were both broken into.

# Return the maximum amount of money you can rob without alerting the police.

# Example 1:

# Input: nums = [3,4,3]

# Output: 4
# Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses.
# The maximum you can rob is nums[1] = 4.

# Example 2:

# Input: nums = [2,9,8,3,6]

# Output: 15
# Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4]
# are adjacent houses. The maximum you can rob is nums[1] + nums[4] = 15.

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        arr1 = nums[1:]
        arr2 = nums[:-1]
        memo1 = [-1]*len(arr1)
        memo2 = [-1]*len(arr2)
        def dfs(i,arr,memo):
            if i>= len(arr):
                return 0
            if memo[i] == -1:
                memo[i] = max(dfs(i+1,arr,memo),arr[i]+ dfs(i+2,arr,memo))
            return memo[i]
        return max(dfs(0,arr1,memo1),dfs(0,arr2,memo2))
        