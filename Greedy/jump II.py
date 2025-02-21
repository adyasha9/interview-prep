# Jump Game II
# You are given an array of integers nums, where nums[i] represents the maximum
#  length of a jump towards the right from index i. For example, if you are at nums[i],
#  you can jump to any index i + j where:

# j <= nums[i]
# i + j < nums.length
# You are initially positioned at nums[0].

# Return the minimum number of jumps to reach the last position in the array
#  (index nums.length - 1). You may assume there is always a valid answer.

# Example 1:

# Input: nums = [2,4,1,1,1,1]

# Output: 2
# Explanation: Jump from index 0 to index 1, then jump from index 1 to the last index.

# Example 2:

# Input: nums = [2,1,2,1,0]

# Output: 2

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0  # This tracks the number of jumps needed
        l = r = 0  # 'l' and 'r' define the range of indices we can reach with the current jump
        
        while r < len(nums) - 1:  # Continue until we reach the last index
            farthest = 0  # Track the farthest index we can reach in the next step
            
            # Explore the current jump range to find the farthest reach
            for i in range(l, r + 1):  
                farthest = max(farthest, i + nums[i])  # Choose the index that maximizes reach
            
            # Move the jump window forward
            l = r + 1  # Shift 'l' to the next segment
            r = farthest  # Expand 'r' to the farthest reachable index
            res += 1  # Increment jump count
        
        return res
