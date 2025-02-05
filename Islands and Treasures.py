# Islands and Treasure
# Solved 
# You are given a 
# m
# ×
# n
# m×n 2D grid initialized with these three possible values:

# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

# Assume the grid can only be traversed up, down, left, or right.

# Modify the grid in-place.

# Example 1:

# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]

# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]



class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rowLen = len(grid)
        colLen = len(grid[0])
        INF = 2147483647  
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
            q = deque([(r,c)])  # add current position to queue
            visits = [[False]*colLen for _ in range(rowLen)] # create an adjacency matrix for visits
            visits[r][c] = True   # mark current as visited
            steps = 0  # steps should be 0 at first 
            while q:   
                for _ in range(len(q)):  # iterate the queue till we find treasure
                    row,col = q.popleft() # get the first queue element
                    if grid[row][col] == 0:  # at 0 we get treasure 
                        return steps         # return step value when we get the treasure
                    for dr,dc in directions:   # use this to add surrounding nodes in the queue to iterate
                        nr,nc = row+dr,col+dc   # update new nodes
                        if (0<=nr<rowLen and 0<=nc<colLen and not visits[nr][nc] and grid[nr][nc] != -1): # check if new nodes are within bounds, haven't been visited or is not -1 as -1 leads to halt
                            visits[nr][nc] = True # update visit
                            q.append((nr,nc))   # add to queue
                steps += 1                      # after a single row col update steps
            return INF                          # if nothing matches return INF

        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c) # get element 