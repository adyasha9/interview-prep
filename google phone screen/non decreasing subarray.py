# Screening Round :

# Given an array of size N, find the maximum length of non-decreasing subarray:
# [0 7 3 10 2 4 6 8 0 9 -20 4]
# ans = 4, [2 4 6 8]


# Follow up:
# You can choose any one index and change its value to any number that you like. 
# What will be the longest non decreasing subarray now:


# In the same example as before, the answer would now be :
# ans = 6, [2 4 6 8 0 9], by changing 0 -> 8 so the subarray becomes non-decreasing.

from typing import List

def maxLength(arr: List[int]) -> int:
    n = len(arr)
    maxLen = 1
    currLen = 1
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            currLen += 1
        else:
            maxLen = max(maxLen,currLen)
            currLen = 1
    return max(currLen,maxLen)
arr = [0, 7, 3, 10, 2, 4, 6, 8, 0, 9, -20, 4]
print(maxLength(arr))


def maxLengthWithOneChange(arr: List[int]) -> int:
    n = len(arr)
    max_len = 1
    l = 0
    changed = False  # Flag to indicate whether we have made a change

    for r in range(1, n):
        if arr[r] < arr[r - 1]:  # Found a decrease
            if changed:  # We have already made one change
                max_len = max(max_len, r - l)  # Update max length
                while l < r and arr[l] <= arr[l + 1]:  # Move left pointer
                    l += 1
                l += 1  # Skip the element that caused the decrease
            changed = True  # Mark that we've made our one allowed change

        max_len = max(max_len, r - l + 1)  # Update max length

    return max_len

# Test
arr = [0, 7, 3, 10, 2, 4, 6, 8, 0, 9, -20, 4]
print(maxLengthWithOneChange(arr))  # Output: 6 ([2, 4, 6, 8, 0, 9])

