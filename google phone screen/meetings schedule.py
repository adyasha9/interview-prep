# You have a list of meetings in your calendar with a start and end time.
# You are very busy, so meetings can overlap.
# You also have one "Do Not Schedule" interval during which you don't attend any meeting.
# Any meeting schedule that overlaps with a DNS slot is automatically cut such that it does 
# not overlap with the DNS slot anymore.


# Return a list of non-overlapping time intervals when you are in a meeting.


# Meeting  | ____    _______________    ___
#          |  _____         ________          __
# DNS      |             xxxx
# -------------------------------------------------> t
# RES.     | ______  ____xxxx_______    ___   __
# Sample input (for simplicity, all intervals include the left point and exclude the right point):


# Meetings: [(1, 7), (5, 10), (12, 30), (22, 30), (40, 50), (60, 70)]
# DNS: (18, 25)
# Sample output: [(1, 10), (12, 18), (25, 30), (40, 50), (60, 70)]

meeting = [(1, 7), (5, 10), (12, 30), (22, 30), (40, 50), (60, 70)]
dns = (18, 25)

def scheduleMeetings(meetings, dns):
    # Sort the meetings by their start time
    meetings.sort()
    output = []
    
    for start, end in meetings:
        # Case 1: The meeting doesn't overlap with the DNS interval
        if end <= dns[0] or start >= dns[1]:
            # If the meeting overlaps with the previous one, merge them
            if output and output[-1][1] >= start:
                output[-1] = (output[-1][0], max(output[-1][1], end))
            else:
                output.append((start, end))
        else:
            # Case 2: The meeting overlaps with the DNS interval
            # If part of the meeting is before DNS, add it
            if start < dns[0]:
                output.append((start, dns[0]))
            # If part of the meeting is after DNS, add it
            if end > dns[1]:
                output.append((dns[1], end))
    
    return output

# Test with your sample input
meetings = [(1, 7), (5, 10), (12, 30), (22, 30), (40, 50), (60, 70)]
dns = (18, 25)
print(scheduleMeetings(meetings, dns))