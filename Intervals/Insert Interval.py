# Insert Interval
# Solved 
# You are given an array of non-overlapping intervals intervals where 
# intervals[i] = [start_i, end_i] represents the start and the end time 
# of the ith interval. intervals is initially sorted in ascending order by start_i.

# You are given another interval newInterval = [start, end].

# Insert newInterval into intervals such that intervals is still 
# sorted in ascending order by start_i and also intervals still does 
# not have any overlapping intervals. You may merge the overlapping intervals if needed.

# Return intervals after adding newInterval.

# Note: Intervals are non-overlapping if they have no common point. 
# For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

# Example 1:

# Input: intervals = [[1,3],[4,6]], newInterval = [2,5]

# Output: [[1,6]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]

# Output: [[1,2],[3,5],[6,7],[9,10]]

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:   # if the end of newInterval is less than the start of the current interval (newInterval[1] < intervals[i][0]), it means newInterval should be placed before the current interval without any overlap
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0]>intervals[i][1]:   # if the start of newInterval is greater than the end of the current interval (newInterval[0] > intervals[i][1]), it means newInterval should be placed after the current interval without any overlap. 
                res.append(intervals[i])
            else:
                temp = [
                    min(newInterval[0],intervals[i][0]),  #Finally, if neither of the above conditions is met, it means there is an overlap between newInterval and the current interval. The method then creates a new interval temp by taking the minimum start value and the maximum end value of the overlapping intervals. This merged interval is appended to res.
                    max(newInterval[1],intervals[i][1])]
                res.append(temp)
        return res