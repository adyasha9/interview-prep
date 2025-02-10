# Partition Equal Subset Sum
# Solved 
# You are given an array of positive integers nums.

# Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

# Example 1:

# Input: nums = [1,2,3,4]

# Output: true
# Explanation: The array can be partitioned as [1, 4] and [2, 3].

# Example 2:

# Input: nums = [1,2,3,4,5]

# Output: false

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target = sum(nums)//2
        dp = set()
        for i in range(len(nums)-1,-1,-1):  # iterating from the back to make sure data is used only once and hence avoiding duplicates
            nextDp =set()                   # new set created to keep track of sum of subsets in this iteration
            for t in dp:           
                nextDp.add(nums[i]+t)       # add new subset sum
                nextDp.add(t)               # add the previous element too
            dp = nextDp                     # reassign nextdp to dp to iterate through new sums
        return True if target in dp else False        # if target was found then true or false
