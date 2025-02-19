# Given an sorted array, find the maximum frequency of a number.
# Eg: [1,2,2,3,3,3,3,4,4,5,6] : Answer: 4 (3 is repeated 4 times).


# O(N) is straight forward solution. Asked if the performance can be improved.

from bisect import bisect_left, bisect_right

def max_frequency(sorted_arr):
    max_freq = 0
    n = len(sorted_arr)
    i = 0

    while i < n:
        num = sorted_arr[i]
        left = bisect_left(sorted_arr, num)   # First occurrence of num
        right = bisect_right(sorted_arr, num) # Position after last occurrence

        freq = right - left
        max_freq = max(max_freq, freq)
        
        i = right  # Move to the next unique number
    
    return max_freq

# Example
sorted_arr = [1,2,2,3,3,3,3,3,4,4,4,5,6]
print(max_frequency(sorted_arr))  # Output: 4

# time complexity O(U log N).
