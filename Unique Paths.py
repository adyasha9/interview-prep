# Unique Paths
# Solved 
# There is an m x n grid where you are allowed to move either down or to 
# the right at any point in time.

# Given the two integers m and n, return the number of possible unique paths 
# that can be taken from the top-left corner of the grid (grid[0][0]) to the 
# bottom-right corner (grid[m - 1][n - 1]).

# You may assume the output will fit in a 32-bit integer.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]  # create a dp array of r,c to keep track of no of steps to reach that position
        for i in range(m):
            dp[i][0] = 1                # assign first column steps as 1
        for i in range(n):
            dp[0][i] = 1                #assign first row steps as 1
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]     #as we can move only right or down to get to r,c we calculate from position above it and right to it
        return dp[m-1][n-1]             # return value for last position.
 
