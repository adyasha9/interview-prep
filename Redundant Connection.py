# Redundant Connection
# You are given a connected undirected graph with n nodes 
#     labeled from 1 to n. Initially, it contained no cycles and consisted of n-1 edges.

# We have now added one additional edge to the graph. 
# The edge has two different vertices chosen from 1 to n, 
# and was not an edge that previously existed in the graph.

# The graph is represented as an array edges of length n 
# where edges[i] = [ai, bi] represents an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the graph is 
# still a connected non-cyclical graph. If there are multiple answers, 
# return the edge that appears last in the input edges.

# Example 1:



# Input: edges = [[1,2],[1,3],[3,4],[2,4]]

# Output: [2,4]


from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [[] for _ in range(n+1)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        cycle = set()
        cycleStart = -1
        def dfs(node,par):
            nonlocal cycleStart
            if node in visited:
                cycleStart = node
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei == par:
                    continue
                if dfs(nei,node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if cycleStart == node:
                        cycleStart = -1
                    return True
            return False
        dfs(1,-1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        return []