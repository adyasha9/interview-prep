# Pacific Atlantic Water Flow
# You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
# The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.
# Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.
# Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.

# Example 1:



# Input: heights = [
#   [4,2,7,3,4],
#   [7,4,6,4,7],
#   [6,3,5,3,6]
# ]

# Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowLen = len(heights)  # calculate length of row
        colLen = len(heights[0]) # calculate length of col
        directions = [[1,0],[-1,0],[0,1],[0,-1]]  # use directions array for graph traversal
        pacificVisit = [[False]*colLen for _ in range(rowLen)] # create a matrix to track which blocks and flow into pacific
        atlanticVisit = [[False]*colLen for _ in range(rowLen)] # create a matric to track which blocks flow into atlantic
        pacNodes = []                                           # starting pacific nodes for traversal 
        altNodes = []                                           # starting atlantic nodes for traversal
        for r in range(rowLen):
            pacNodes.append((r,0))                              #add first column to pacNodes
            altNodes.append((r,colLen-1))                       # add last column to atlNodes
        for c in range(colLen):
            pacNodes.append((0,c))                              # add first row to pacNodes
            altNodes.append((rowLen-1,c))                       # add last row to pacNodes
            # implementing breadth first traversal
        def bfs(sourceNodes,oceanVisit):   
            q = deque(sourceNodes)                      # make queue out of all Nodes in respective ocena array
            while q:
                r,c = q.popleft()                       # compute the first node
                oceanVisit[r][c] = True
                for dr,dc in directions:                # find neighboring nodes
                    nr,nc = r+dr,c+dc
                    if(0<=nr<rowLen and 0<=nc<colLen and not oceanVisit[nr][nc] and heights[nr][nc]>=heights[r][c]): # check if new node is in bound and not have been visited before and has height greater than or equal to the starting
                        q.append((nr,nc))  # add if all conditions are met to compute this node
        bfs(pacNodes,pacificVisit)
        bfs(altNodes,atlanticVisit)   # perform bfs on both oceans to find r,c where both have True
        res = []
        for r in range(rowLen):
            for c in range(colLen):
                if pacificVisit[r][c] and atlanticVisit[r][c]:
                    res.append((r,c))
        return res


        