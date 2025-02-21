# Min Cost to Connect Points
# Solved 
# You are given a 2-D integer array points, where points[i] = [xi, yi]. 
# Each points[i] represents a distinct point on a 2-D plane.

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan 
# distance between the two points, i.e. |xi - xj| + |yi - yj|.

# Return the minimum cost to connect all points together, such that there 
# exists exactly one path between each pair of points.

# Example 1:



# Input: points = [[0,0],[2,2],[3,3],[2,4],[4,2]]

# Output: 10

import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i,n):
                x2,y2 = points[j]
                d = abs(x1-x2) + abs(y1-y2)
                adj[i].append([d,j])
                adj[j].append([d,i])
        minHeap = [[0,0]]
        visit = set()
        res = 0
        while minHeap:
            cost,node = heapq.heappop(minHeap)
            if node in visit:
                continue
            res += cost
            visit.add(node)
            for neiCost,nei in adj[node]:
                if nei in visit:
                    continue
                heapq.heappush(minHeap,[neiCost,nei])
        return res
            


# Prim’s Algorithm - Overview
# Purpose: Finds the MST, ensuring the minimum total edge weight while connecting all vertices.
# Approach: Greedy algorithm that grows the MST by picking the smallest available edge.
# Steps of Prim’s Algorithm
# Choose an arbitrary starting vertex.
# Add the smallest edge that connects a new vertex to the MST.
# Repeat step 2 until all vertices are included in the MST.