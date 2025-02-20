# LeetCode-Style Question: Maximum Subsequence of Size K
# Problem Statement
# Given an integer array nums and an integer k, return the maximum subsequence of size k. The subsequence must maintain the relative order of the elements in nums.

# Example 1:
# Input:

# Output:
# [5, 6]
# Explanation:

# Possible subsequences of size 2: [3,5], [3,2], [3,6], [5,2], [5,6], [2,6]
# The maximum possible subsequence is [5, 6].
# Example 2:
# Input:
# nums = [4, 9, 0, 2]
# k = 2
# Output:
# [9, 2]
# Explanation:

# Possible subsequences of size 2: [4,9], [4,0], [4,2], [9,0], [9,2], [0,2]
# The maximum subsequence is [9, 2].
nums = [4, 9, 0, 2,9]
k = 3
from typing import List
def maxSubsequence(nums: List[int], k: int) -> List[int]:
    output = []
    n = len(nums)
    for i,num in enumerate(nums):
        while output and len(output) + (n - i) > k  and num> output[-1]:
            output.pop()
        if k > len(output):
            output.append(num)
    return int("".join(map(str, output)))

print(maxSubsequence(nums,3))


