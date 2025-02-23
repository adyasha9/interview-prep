# Problem Statement
# You are given a sorted unique integer array nums and two integers lower and upper representing the inclusive range [lower, upper].

# Your task is to return the smallest sorted list of ranges that cover all the missing numbers in the range [lower, upper] exactly. That is, each element of nums should be covered by one of the ranges, and there should be no overlaps.

# Each range [a, b] should be output as:

# "a" if a == b
# "a->b" if a < b
# Example 1:
# python
# Copy
# Edit
# Input: nums = [0, 1, 3, 50, 75], lower = 0, upper = 99
# Output: ["2", "4->49", "51->74", "76->99"]
# Example 2:
# python
# Copy
# Edit
# Input: nums = [], lower = 1, upper = 1
# Output: ["1"]
# Example 3:
# python
# Copy
# Edit
# Input: nums = [], lower = -3, upper = -1
# Output: ["-3->-1"]
# Constraints:
# 0 <= nums.length <= 100
# -2³¹ <= nums[i] <= 2³¹ - 1
# nums is sorted in ascending order and all elements are unique.
# -2³¹ <= lower <= upper <= 2³¹ - 1

# Input: nums = [0, 1, 3, 50, 75], lower = 0, upper = 99
# Output: ["2", "4->49", "51->74", "76->99"]

# Input: nums = [], lower = 1, upper = 1
# Output: ["1"]

# Input: nums = [], lower = -3, upper = -1
# Output: ["-3->-1"]

from typing import List

def missingRanges(nums:List[int],lower:int,upper:int)->List[str]:
    output = []
    prev = lower - 1
    for i in range(len(nums)+1):
        curr = nums[i] if i<len(nums) else upper + 1
        if curr - prev >= 2:
            if curr - prev == 2:
                output.append(f"{prev+1}")
            else:
                output.append(f"{prev+1}->{curr-1}")
        prev = curr
    return output

# Test cases
test_cases = [
    # Basic test cases
    ([0, 1, 3, 50, 75], 0, 99, ["2", "4->49", "51->74", "76->99"]),
    ([1], 0, 2, ["0", "2"]),
    
    # Edge cases with empty nums
    ([], 1, 1, ["1"]),
    ([], -3, -1, ["-3->-1"]),
    ([], 0, 0, ["0"]),
    
    # Ranges with single element gaps
    ([0, 2, 4, 6], 0, 6, ["1", "3", "5"]),
    ([1, 2, 3], 0, 4, ["0", "4"]),
    
    # Lower and upper bounds included
    ([1, 3, 50, 75], 0, 99, ["0", "2", "4->49", "51->74", "76->99"]),
    
    # nums containing all elements in range
    ([0, 1, 2, 3, 4], 0, 4, []),
    
    # Single missing element at the start and end
    ([1, 2, 3], 0, 4, ["0", "4"]),
    ([2, 3, 4], 0, 5, ["0->1", "5"]),
    
    # Negative ranges
    ([-10, -5, 0, 5, 10], -10, 10, ["-9->-6", "-4->-1", "1->4", "6->9"]),
    
    # Lower and upper both missing
    ([1, 2, 3, 7, 8], 0, 9, ["0", "4->6", "9"]),
    
    # Full range without any missing elements
    ([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], -5, 5, []),
]

# Run all test cases
for nums, lower, upper, expected in test_cases:
    result = missingRanges(nums, lower, upper)
    print(f"nums={nums}, lower={lower}, upper={upper} => {result} (Expected: {expected})")
    assert result == expected, f"Failed test case: nums={nums}, lower={lower}, upper={upper}"

print("All test cases passed! ✅")

    