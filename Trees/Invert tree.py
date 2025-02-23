# Invert Binary Tree
# Solved 
# You are given the root of a binary tree root. Invert the binary tree and return its root.

# Example 1:



# Input: root = [1,2,3,4,5,6,7]

# Output: [1,3,2,7,6,5,4]
# Example 2:



# Input: root = [3,2,1]

# Output: [3,1,2]
# Example 3:

# Input: root = []

# Output: []
# Constraints:

# 0 <= The number of nodes in the tree <= 100.
# -100 <= Node.val <= 100

from typing import Optional


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def invertBinaryTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)
    return root

def printTree(root: Optional[TreeNode]):
    if not root:
        return "[]"
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(printTree(invertBinaryTree(root)))