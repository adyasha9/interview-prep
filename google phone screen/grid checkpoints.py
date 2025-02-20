# LeetCode-Style Problem Statement
# Unique Paths with Constraints
# You are given an n × m grid where you start at the bottom-left corner (n-1, 0), 
# and your goal is to reach the bottom-right corner (n-1, m-1). You are only allowed to move:

# Right (i, j) → (i, j+1)
# Diagonally Up-Right (i, j) → (i-1, j+1) if i > 0
# Diagonally Down-Right (i, j) → (i+1, j+1) if i < n-1
# Return the number of unique paths that satisfy the movement constraints.

# Follow-Up 1: Paths Passing Through Specific Checkpoints
# You are given a list of checkpoints checkpoints = [(x1, y1), (x2, y2), ..., (xk, yk)]. 
# A valid path must pass through all given checkpoints at least once before reaching (n-1, m-1). 
# Return the number of such unique paths.

# Follow-Up 2: Ordered Checkpoints
# You are given an ordered list of checkpoints. A valid path must pass through them 
# in the given order before reaching (n-1, m-1). Return the number of such unique paths.

# Function Signature
# python
# def uniquePaths(n: int, m: int) -> int:
#     pass

# def uniquePathsWithCheckpoints(n: int, m: int, checkpoints: List[Tuple[int, int]]) -> int:
#     pass

# def uniquePathsOrderedCheckpoints(n: int, m: int, checkpoints: List[Tuple[int, int]]) -> int:
#     pass
# Example 1: Base Case
# Input
# python
# Copy
# Edit
# n = 3
# m = 4
# Output
# python
# Copy
# Edit
# 6
# Explanation
# Valid paths from (2,0) to (2,3) are:

# Copy
# Edit
# → → → 
# ↗ → → 
# → ↗ → 
# ↓ → → 
# → ↓ →
# ↓ ↗ →
# Example 2: Paths with Checkpoints
# Input
# python
# Copy
# Edit
# n = 3
# m = 4
# checkpoints = [(1,2)]
# Output
# python
# Copy
# Edit
# 3
# Explanation
# Only paths passing through (1,2) are counted.

# Example 3: Ordered Checkpoints
# Input
# n = 3
# m = 4
# checkpoints = [(1,1), (1,2)]
# Output
# python
# Copy
# Edit
# 2
# Explanation
# Only paths visiting (1,1) before (1,2) count.

# Constraints
# 1 ≤ n, m ≤ 100
# 0 ≤ len(checkpoints) ≤ min(n, m)
# (xi, yi) are valid grid positions with 0 ≤ xi < n, 0 ≤ yi < m
# No duplicate checkpoints


# Example 1: Base Case
# Input
# python

def count_paths_base(n, m):
    """
    Counts paths from bottom-left to bottom-right corner.
    n: number of rows
    m: number of columns
    """
    # Initialize dp array
    dp = [[0] * m for _ in range(n)]
    
    # Set starting position
    dp[n-1][0] = 1
    
    # Fill dp array
    for j in range(1, m):
        for i in range(n):
            # Right move
            dp[i][j] += dp[i][j-1]
            
            # Up-right diagonal
            if i < n-1:
                dp[i][j] += dp[i+1][j-1]
                
            # Down-right diagonal
            if i > 0:
                dp[i][j] += dp[i-1][j-1]
    
    return dp[n-1][m-1]

def count_paths_checkpoints(n, m, checkpoints):
    """
    Counts paths passing through all checkpoints in any order.
    checkpoints: list of (row, col) coordinates
    """
    def count_between_points(start, end):
        # Count paths between two points
        start_row, start_col = start
        end_row, end_col = end
        
        if start_col >= end_col:
            return 0
            
        sub_n = abs(end_row - start_row) + 1
        sub_m = end_col - start_col + 1
        
        # Similar to base case but with adjusted boundaries
        dp = [[0] * sub_m for _ in range(sub_n)]
        dp[start_row - (min(start_row, end_row))][0] = 1
        
        for j in range(1, sub_m):
            for i in range(sub_n):
                if i > 0:
                    dp[i][j] += dp[i-1][j-1]  # Down-right
                dp[i][j] += dp[i][j-1]      # Right
                if i < sub_n-1:
                    dp[i][j] += dp[i+1][j-1]  # Up-right
                    
        return dp[end_row - (min(start_row, end_row))][sub_m-1]
    
    def solve_with_permutations(curr_point, remaining_points, memo):
        if not remaining_points:
            # Count paths from last checkpoint to destination
            return count_between_points(curr_point, (n-1, m-1))
            
        key = (curr_point, tuple(sorted(remaining_points)))
        if key in memo:
            return memo[key]
            
        total = 0
        for i, next_point in enumerate(remaining_points):
            paths = count_between_points(curr_point, next_point)
            if paths > 0:
                new_remaining = remaining_points[:i] + remaining_points[i+1:]
                total += paths * solve_with_permutations(next_point, new_remaining, memo)
                
        memo[key] = total
        return total
    
    # Start from bottom-left corner
    start_point = (n-1, 0)
    memo = {}
    return solve_with_permutations(start_point, checkpoints, memo)

def count_paths_ordered_checkpoints(n, m, checkpoints):
    """
    Counts paths passing through checkpoints in specified order.
    checkpoints: ordered list of (row, col) coordinates
    """
    def count_between_points(start, end):
        # Same as in previous function
        start_row, start_col = start
        end_row, end_col = end
        
        if start_col >= end_col:
            return 0
            
        sub_n = abs(end_row - start_row) + 1
        sub_m = end_col - start_col + 1
        
        dp = [[0] * sub_m for _ in range(sub_n)]
        dp[start_row - (min(start_row, end_row))][0] = 1
        
        for j in range(1, sub_m):
            for i in range(sub_n):
                if i > 0:
                    dp[i][j] += dp[i-1][j-1]
                dp[i][j] += dp[i][j-1]
                if i < sub_n-1:
                    dp[i][j] += dp[i+1][j-1]
                    
        return dp[end_row - (min(start_row, end_row))][sub_m-1]
    
    # Start from bottom-left corner
    points = [(n-1, 0)] + checkpoints + [(n-1, m-1)]
    total_paths = 1
    
    # Multiply paths between consecutive points
    for i in range(len(points)-1):
        paths = count_between_points(points[i], points[i+1])
        total_paths *= paths
        if paths == 0:
            return 0
            
    return total_paths