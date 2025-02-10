# Given an integer array arr[]. You need to find the maximum sum of a subarray.

# Examples:

# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 11
# Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.
# Input: arr[] = [-2, -4]
# Output: -2
# Explanation: The subarray {-2} has the largest sum -2.

class Solution:
    def maxSubArraySum(self, arr):
        res = arr[0]
        currMax = 0
        currMin= 0
        for num in arr:
            temp = currMax + num
            currMax = max(temp,currMin+num,num)
            currMin = min(temp,currMin+num,num)
            res = max(currMax,res)
        return res