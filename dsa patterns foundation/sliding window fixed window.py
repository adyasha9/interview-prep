
# 💡 Tip: Use Fixed Sliding Window when the subarray size is known.

def max_sum_subarray(arr, k):
    """
    Given an array and an integer k, find the maximum sum of any contiguous subarray of size k.
    """
    max_sum, window_sum = 0, 0
    left = 0

    for right in range(len(arr)):
        window_sum += arr[right]  # Expand window by adding new element
        
        # If window size reaches 'k'
        if right - left + 1 == k:
            max_sum = max(max_sum, window_sum)  # Update max sum
            window_sum -= arr[left]  # Shrink window from left
            left += 1  # Move left pointer

    return max_sum

# Test
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # Output: 9
