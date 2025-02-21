# Merge Intervals
# Given an array of intervals where intervals[i] = [start_i, end_i],
# merge all overlapping intervals, and return an array of the non-overlapping 
# intervals that cover all the intervals in the input.

# You may return the answer in any order.

# Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

# Example 1:

# Input: intervals = [[1,3],[1,5],[6,7]]

# Output: [[1,5],[6,7]]
# Example 2:

# Input: intervals = [[1,2],[2,3]]

# Output: [[1,3]]

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] =  max(res[-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
        return res