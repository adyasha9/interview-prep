# Maximum Subarray
# Given an array of integers nums, find the subarray with the largest sum and return the sum.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [2,-3,4,-2,2,1,-1,4]

# Output: 8
# Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

# Example 2:

# Input: nums = [-1]

# Output: -1

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMin = 0
        currMax = nums[0]
        res = nums[0]
        for num in nums[1:]:
            temp = currMax + num
            currMax = max(temp,currMin+num,num)
            currMin = min(temp,currMin+num,num)
            res = max(res,currMax)
        return res