# Max Area of Island
# Solved 
# You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

# An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

# The area of an island is defined as the number of cells within the island.

# Return the maximum area of an island in grid. If no island exists, return 0.

# Example 1:



# Input: grid = [
#   [0,1,1,0,1],
#   [1,0,1,0,1],
#   [0,1,1,0,1],
#   [0,1,0,0,1]
# ]

# Output: 6

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]] # use directions to traverse the neighbouring land
        rowLen = len(grid) 
        colLen = len(grid[0])
        islandArea = 0 
        def bfs(r,c):
            q = deque() # add land to queue to compute it's neighbour
            q.append((r,c))  #append the current row and col to queue for computinh
            grid[r][c] = 0   #mark as visited
            tempArea = 1     # temp Area is set to 1
            while q:
                row,col = q.popleft() # compute the first inputted row and col
                for dr,dc in directions: # compute neighbouring nodes
                    nr, nc = row + dr , col + dc # update the row and col for neighbouring nodes
                    if(nr<0 or nc<0 or nr>=rowLen or nc>= colLen or grid[nr][nc]==0):  # check if index out of bounds or visited
                        continue
                    q.append((nr,nc))    #add the new node for further computatiom
                    grid[nr][nc] = 0      # mark as visited
                    tempArea += 1         # increment the area
            return tempArea
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 1:
                    islandArea = max(islandArea,bfs(r,c))  # compare temp Area or global area
        return islandArea