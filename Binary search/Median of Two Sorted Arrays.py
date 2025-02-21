# # binary search
# Median of Two Sorted Arrays
# Solved 
# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

# Your solution must run in O(log(m+n)) time.

# Example 1:

# Input: nums1 = [1,2], nums2 = [3]

# Output: 2.0
# Explanation: Among [1, 2, 3] the median is 2.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # A = [1,3] B = [2,4]
        # A = [1,3] B = [2]
        total = len(nums1) + len(nums2)
        half = total//2
        A , B = nums1, nums2
        if len(A)>len(B):
            A,B = B,A
        l , r = 0, len(A) -1 
        while True:
            midA = (l+r)//2
            midB = half - midA - 2
            leftA = A[midA] if midA>=0 else float("-inf")
            rightA = A[midA+1] if midA + 1 < len(A) else float("inf")
            leftB = B[midB] if midB>=0 else float("-inf")
            rightB = B[midB+1] if midB+1 < len(B) else float("inf")

            if leftA<=rightB and rightA>=leftB:
                if total%2:
                    return min(rightA,rightB)
                else:
                    return (min(rightA,rightB) + max(leftA,leftB))/2
            elif leftA>rightB:
                r = midA - 1
            else:
                l = midA + 1