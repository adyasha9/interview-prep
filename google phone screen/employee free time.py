# Problem Statement:
# We are given a list schedule, where schedule[i] represents the working hours of the i-th employee.
#  Each employee has a list of non-overlapping intervals sorted in increasing order.

# Return a list of finite intervals representing common free time slots that are available for
#  all employees. These intervals should be sorted in increasing order and should not overlap.

# Example 1:
# Input:

# schedule = [
#     [[1,2], [5,6]],
#     [[1,3]],
#     [[4,10]]
# ]
# Output:
# [[3,4]]
# Explanation:

# Employee 1 works during [1,2] and [5,6]
# Employee 2 works during [1,3]
# Employee 3 works during [4,10]
# The only free time available for all employees is [3,4].
# Example 2:
# Input:
schedule = [
    [[1,3], [6,7]],
    [[2,4]],
    [[2,5], [9,12]]
]
# Output:
# [[5,6], [7,9]]
# Explanation:

# Employees have different working times.
# The common free slots available are [5,6] and [7,9].
# Constraints:
# 1 <= schedule.length, schedule[i].length <= 50
# 0 <= schedule[i].start < schedule[i].end <= 10^8
# The schedule is sorted within each employee’s list.

# schedule = [
#     [[1,2], [5,6]],
#     [[1,3]],
#     [[4,10]]
# ]
# [1,2],[1,3],[5,6],[4,10]

def employeeFreeTime(schedule):
    intervals = [interval for employee in schedule for interval in employee]
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    for i in range(1,len(intervals)):
        if res[-1][1] >= intervals[i][0]:
            res[-1][1] = max(res[-1][1],intervals[i][1])
        else:
            res.append(intervals[i])
    result = []
    i = 0
    while i < len(res)-1:
        interval1 , interval2 = res[i], res[i+1]
        freeTime = [interval1[1],interval2[0]]
        result.append(freeTime)
        i += 1
    return result

print(employeeFreeTime(schedule))

