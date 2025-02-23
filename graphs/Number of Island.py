# Number of Islands
# Solved 
# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

# Example 1:

# Input: grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
# Output: 1

from collections import deque
from typing import List

class Solution:
        def numIslands(self, grid: List[List[str]]) -> int:
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                rowLen = len(grid)
                colLen = len(grid[0])
                island = 0
                def bfs(r,c):
                       q = deque()
                       q.append((r,c))
                       grid[r][c] = "0"
                       while q:
                             row,col = q.popleft()
                             for dr, dc in directions:
                                nr, nc = row + dr , col + dc
                                if (nr<0 or nr>= rowLen or nc<0 or nc>= colLen or grid[nr][nc] =="0"):
                                    continue
                                q.append((nr,nc))
                                grid[nr,nc] = "0"
                                

                for r in range(rowLen):
                    for c in range(colLen):
                           if grid[r][c] == '1':
                                  bfs(r,c)
                                  island +=1 
                return island
                           

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        numIsland = 0
        def dfs(r,c):
            if r>=row or c>=col or r<0 or c<0 or grid[r][c] == "0":
                return 
            grid[r][c] = "0"
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    dfs(r,c)
                    numIsland += 1
        return numIsland
