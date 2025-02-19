# Given a binary tree with n nodes and an array edges where each element is of the form[from, to],
#  representing an edge from from to to.


# Remove all the edges in the edges array from the tree and return an array with the total node 
# count in each connected component formed after removing all the edges from the tree.


# Note: All the node values in the Binary Tree are unique.

# Example:

# Input:  Tree: [1, 2, 3, 4, 5, null, null] , Edges: [[1, 2], [2, 4]] 
# Output: [2,2,1]

from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(values):
    """ Builds a binary tree from a level-order list representation. """
    if not values or values[0] is None:
        return None

    nodes = {i + 1: TreeNode(val) if val is not None else None for i, val in enumerate(values)}
    root = nodes[1]

    for i in range(len(values)):
        if values[i] is not None:
            node = nodes[i + 1]
            left_idx, right_idx = 2 * (i + 1), 2 * (i + 1) + 1
            if left_idx <= len(values) and nodes.get(left_idx):
                node.left = nodes[left_idx]
            if right_idx <= len(values) and nodes.get(right_idx):
                node.right = nodes[right_idx]

    return root

def get_adjacency_list(root):
    """ Converts a binary tree to an adjacency list representation. """
    if not root:
        return {}

    adj_list = defaultdict(set)
    stack = [root]

    while stack:
        node = stack.pop()
        if node.left:
            adj_list[node.val].add(node.left.val)
            adj_list[node.left.val].add(node.val)
            stack.append(node.left)
        if node.right:
            adj_list[node.val].add(node.right.val)
            adj_list[node.right.val].add(node.val)
            stack.append(node.right)

    return adj_list

def remove_edges(adj_list, edges):
    """ Removes the given edges from the adjacency list. """
    for u, v in edges:
        if u in adj_list:
            adj_list[u].discard(v)
        if v in adj_list:
            adj_list[v].discard(u)

def find_connected_components(adj_list):
    """ Finds connected components in a graph using DFS. """
    visited = set()
    components = []

    def dfs(node):
        stack = [node]
        count = 0
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                count += 1
                stack.extend(adj_list[curr])
        return count

    for node in adj_list:
        if node not in visited:
            components.append(dfs(node))

    return components

def get_connected_components(values, edges):
    root = build_tree_from_list(values)
    adj_list = get_adjacency_list(root)
    remove_edges(adj_list, edges)
    return find_connected_components(adj_list)

# Example usage:
tree_values = [1, 2, 3, 4, 5, None, None]
edges_to_remove = [[1, 2], [2, 4]]

output = get_connected_components(tree_values, edges_to_remove)
print(output)  # Output: [2, 2, 1]
