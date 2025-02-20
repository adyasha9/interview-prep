# Q. Given two strings of equal length made up of 'x', 'y', and 'z', with no consecutive characters 
# the same, determine the minimum number of operations needed to transform the first string into the
#  second. In one operation, you can change any character in the first string, ensuring no consecutive
#  characters become identical.


# for ex:
# str1: zxyz
# str2: zyxz

# zxyz → yxyz → yzyz → yzxz → zxzx → zxyz → zyxz

# result: 6

# ex #2:
# str1: xyzyzyxyzx
# str2: xzyzyzyxzy

# result: 15
# ex #3:
# str1: xyxyxyxyxy
# str2: xzyxyxzyxz

# result: 13
# ex #4:
# str1: xyxyzyzyxy
# str2: zyzyxzyzyz

# result: 9
# ex #5
# str1: xzxyxyzyzyxyzx
# str2: zyzyxzyzyzyxzy

# res: 20

from collections import deque

def min_operations(str1, str2):
    """
    Calculate minimum operations to transform str1 to str2 while ensuring no consecutive characters are same.
    
    Args:
        str1 (str): Source string
        str2 (str): Target string
        
    Returns:
        int: Minimum number of operations needed
    """
    if len(str1) != len(str2):
        return -1
        
    # Possible characters
    chars = ['x', 'y', 'z']
    n = len(str1)
    
    # Create state class to track string and operations
    class State:
        def __init__(self, string, ops):
            self.string = string
            self.ops = ops
            
    # Initialize queue and visited set
    queue = deque([State(str1, 0)])
    visited = {str1}
    
    while queue:
        current = queue.popleft()
        
        # If we've reached the target string, return operations
        if current.string == str2:
            return current.ops
            
        # Try changing each position
        for i in range(n):
            # Get valid characters for this position
            valid_chars = chars.copy()
            
            # Remove characters that would create consecutive duplicates
            if i > 0:
                if i < n-1:  # Middle position
                    valid_chars = [c for c in valid_chars if c != current.string[i-1] and c != current.string[i+1]]
                else:  # Last position
                    valid_chars = [c for c in valid_chars if c != current.string[i-1]]
            elif i < n-1:  # First position
                valid_chars = [c for c in valid_chars if c != current.string[i+1]]
                
            # Try each valid character
            for c in valid_chars:
                new_string = current.string[:i] + c + current.string[i+1:]
                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(State(new_string, current.ops + 1))
                    
    return -1  # If no solution is found

# Test cases
test_cases = [
    ("zxyz", "zyxz"),
    ("xyzyzyxyzx", "xzyzyzyxzy"),
    ("xyxyxyxyxy", "xzyxyxzyxz"),
    ("xyxyzyzyxy", "zyzyxzyzyz"),
    ("xzxyxyzyzyxyzx", "zyzyxzyzyzyxzy")
]

for str1, str2 in test_cases:
    result = min_operations(str1, str2)
    print(f"String 1: {str1}")
    print(f"String 2: {str2}")
    print(f"Minimum operations: {result}")
    print("-" * 40)