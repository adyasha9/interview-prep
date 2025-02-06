#💡 Tip: Used in shortest paths, social networks, flood-fill.
from collections import deque

def bfs(graph, start):
    """
    Perform BFS traversal on a graph.
    """
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        print(node)  # Process node

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Test
bfs(graph, 0)
