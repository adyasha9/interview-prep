# Graph Valid Tree
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
# (each edge is a pair of nodes), write a function to check whether these 
# edges make up a valid tree.

# Example 1:

# Input:
# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

# Output:
# true
# Example 2:

# Input:
# n = 5
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

# Output:
# false
# Note:

# You can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0, 1] is the same as [1, 0] 
# and thus will not appear together in edges.
# Constraints:

# 1 <= n <= 100
# 0 <= edges.length <= n * (n - 1) / 2



# A tree is a special type of graph that must satisfy the following conditions:

# No cycles – A tree cannot have any cycles.
# Connected – There must be a path between any two nodes.
# Exactly n-1 edges – A valid tree with n nodes must have exactly n-1 edges.



from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: # a tree must have n-1 edges
            return False
        # build adjacency list
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(node,parent):
            if node in visited:
                return False # cycle detceted
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor != parent: # ignore parent node
                    if not dfs(neighbor,node):
                        return False
            return True
        if not dfs(0,-1):
            return False
        return len(visited) == n

