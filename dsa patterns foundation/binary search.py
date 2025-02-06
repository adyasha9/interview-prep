#💡 Tip: Used in rotated sorted arrays, closest elements, finding bounds.
def binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid integer overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search in right half
        else:
            right = mid - 1  # Search in left half

    return -1

# Test
print(binary_search([1, 3, 5, 7, 9], 7))  # Output: 3
