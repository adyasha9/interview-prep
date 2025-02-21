# Non-overlapping Intervals
# Given an array of intervals intervals where intervals[i] = [start_i, end_i], 
# return the minimum number of intervals you need to remove to make the rest of 
# the intervals non-overlapping.

# Note: Intervals are non-overlapping even if they have a common point. 
# For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.

# Example 1:

# Input: intervals = [[1,2],[2,4],[1,4]]

# Output: 1
# Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.

# Example 2:

# Input: intervals = [[1,2],[2,4]]
# Output: 0

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        # Sort intervals based on their end times
        intervals.sort(key=lambda x: x[1])
        # Initialize the end time of the last non-overlapping interval
        end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                # Overlapping interval, increment count
                count += 1
            else:
                # Non-overlapping interval, update the end time
                end = intervals[i][1]
                
        return count