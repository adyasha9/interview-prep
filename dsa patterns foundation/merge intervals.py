# 💡 Tip: Sorting ensures merging is efficient.
def merge_intervals(intervals):
    """
    Given a list of intervals, merge all overlapping ones.
    """
    intervals.sort()  # Sort by start time
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:  # Overlapping case
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged

# Test
print(merge_intervals([[1,3], [2,6], [8,10], [15,18]]))  # Output: [[1,6], [8,10], [15,18]]
