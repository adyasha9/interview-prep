#💡 Tip: Used in maze solving, islands counting, topological sorting.
def dfs(graph, node, visited):
    """
    Perform DFS traversal on a graph.
    """
    if node in visited:
        return
    visited.add(node)
    print(node)  # Process node

    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)

# Example Graph
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

visited = set()
dfs(graph, 0, visited)
