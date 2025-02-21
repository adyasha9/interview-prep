# Number of Connected Components in an Undirected Graph
# Solved 
# There is an undirected graph with n nodes. 
# There is also an edges array, where edges[i] = [a, b]
# means that there is an edge between node a and node b in the graph.

# The nodes are numbered from 0 to n - 1.

# Return the total number of connected components in that graph.

# Example 1:

# Input:
# n=3
# edges=[[0,1], [0,2]]

# Output:
# 1
# Example 2:

# Input:
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]

# Output:
# 2

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visit = [False] * n
        res = 0
        def dfs(node):
            for nei in graph[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res