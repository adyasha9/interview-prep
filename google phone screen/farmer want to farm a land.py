# A farmer wants to farm their land with the maximum area where good land is present.
# The land is represented as a matrix with ones and zeros,
# where ones mean good land and zeros mean bad land.
# The farmer only wants to farm in a square of good land with the maximum area.
# Please help the farmer to find a maximum area of the land
# they can farm in good land.

def max_square_farmland(land):
    """
    Find the maximum square area of good farmland (1s) in the given matrix.
    
    Args:
        land (List[List[int]]): Matrix representing the land where 1 is good land and 0 is bad
    
    Returns:
        int: Side length of the maximum square area of good land
    """
    # Base case: if land is empty or has no columns
    if not land or not land[0]:
        return 0
    
    rowLen = len(land)
    colLen = len(land[0])
    dp = [[0]*colLen for _ in range(rowLen)]
    max_side = 0
    
    # Initialize first row and column
    for i in range(rowLen):
        dp[i][0] = land[i][0]
        if dp[i][0] == 1:
            max_side = 1
            
    for j in range(colLen):  # Changed from rowLen to colLen
        dp[0][j] = land[0][j]
        if dp[0][j] == 1:
            max_side = 1
    
    # Fill the dp table
    for i in range(1, rowLen):  # Start from 1 since we use i-1
        for j in range(1, colLen):  # Start from 1 since we use j-1
            if land[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    
    return max_side

# Test the function
land = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0]
]
print(max_square_farmland(land))  