# 💡 Tip: Works well for sorted arrays.


def two_sum_sorted(arr, target):
    """
    Given a sorted array, find two numbers that add up to the target.
    """
    left, right = 0, len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]

        if curr_sum == target:
            return [left, right]  # Found target sum
        elif curr_sum < target:
            left += 1  # Increase sum by moving left
        else:
            right -= 1  # Decrease sum by moving right

    return []

# Test
print(two_sum_sorted([1, 2, 3, 4, 6], 6))  # Output: [1, 3]
