# Rotting Fruit
# Solved 
# You are given a 2-D matrix grid. Each cell can have one of three possible values:

# 0 representing an empty cell
# 1 representing a fresh fruit
# 2 representing a rotten fruit
# Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

# Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

# Example 1:



# Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

# Output: 4

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        time = 0 
        fresh = 0
        q = deque()
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        while fresh > 0 and q:
            length = len(q)
            for _ in range(length):
                row,col = q.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr, col+dc
                    if (nr in range(rowLen) and nc in range(colLen) and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1 
        