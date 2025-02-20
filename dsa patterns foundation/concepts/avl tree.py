# ### **AVL Tree - Self-Balancing Binary Search Tree**
# An **AVL Tree** is a **self-balancing Binary Search Tree (BST)** where the difference between the heights of left and right subtrees (**balance factor**) is at most **1** for every node.

# 💡 **Key Property:**  
# For every node in an AVL tree:  
# \[
# \{Balance Factor} = {Height of Left Subtree} - {Height of Right Subtree} in {-1, 0, 1}
# \]

# If the balance factor goes out of this range after an operation (insert or delete), **rotations** are performed to restore balance.

# ---

# ## **Time and Space Complexity**
# | Operation  | Average Case | Worst Case | Space Complexity |
# |------------|-------------|------------|------------------|
# | Search     | **O(log n)** | **O(log n)** | **O(n)** |
# | Insert     | **O(log n)** | **O(log n)** | - |
# | Delete     | **O(log n)** | **O(log n)** | - |

# 🔹 **Why?**  
# - Since AVL trees are **balanced**, height remains **O(log n)**, ensuring **logarithmic time** for search, insertion, and deletion.  
# - Rotations take **O(1)** to **O(log n)** time (in the worst case), but do not change overall complexity.  

# ---

# ## **Rotations in AVL Tree**
# When the balance factor is violated after insertion or deletion, **rotations** are used to restore balance. There are **four types of rotations**:

# ### 🔹 **1. Right Rotation (LL Rotation)**
# **Occurs when:**  
# A node is inserted into the left subtree of the left child, causing imbalance.

# **Fix:**  
# Perform a **right rotation** on the unbalanced node.

# ```
#        y
#       /
#      x
#     /
#    z
# ```
# After **Right Rotation**:
# ```
#      x
#     / \
#    z   y
# ```

# ---

# ### 🔹 **2. Left Rotation (RR Rotation)**
# **Occurs when:**  
# A node is inserted into the right subtree of the right child, causing imbalance.

# **Fix:**  
# Perform a **left rotation** on the unbalanced node.

# ```
#     x
#      \
#       y
#        \
#         z
# ```
# After **Left Rotation**:
# ```
#       y
#      / \
#     x   z
# ```

# ---

# ### 🔹 **3. Left-Right Rotation (LR Rotation)**
# **Occurs when:**  
# A node is inserted into the right subtree of the left child, causing imbalance.

# **Fix:**  
# First, perform a **left rotation** on the left child, then a **right rotation** on the unbalanced node.

# ```
#       z
#      /
#     x
#      \
#       y
# ```
# After **Left Rotation on x**:
# ```
#       z
#      /
#     y
#    /
#   x
# ```
# After **Right Rotation on z**:
# ```
#       y
#      / \
#     x   z
# ```

# ---

# ### 🔹 **4. Right-Left Rotation (RL Rotation)**
# **Occurs when:**  
# A node is inserted into the left subtree of the right child, causing imbalance.

# **Fix:**  
# First, perform a **right rotation** on the right child, then a **left rotation** on the unbalanced node.

# ```
#       x
#        \
#         z
#        /
#       y
# ```
# After **Right Rotation on z**:
# ```
#       x
#        \
#         y
#          \
#           z
# ```
# After **Left Rotation on x**:
# ```
#       y
#      / \
#     x   z
# ```

# ---

# ### **Advantages of AVL Trees**
# ✅ **Guaranteed O(log n) operations** due to balancing.  
# ✅ **Good for applications requiring frequent lookups (e.g., database indexing, interval trees).**  

# ### **Disadvantages**
# ❌ **More rotations → Higher insertion and deletion overhead** compared to unbalanced BSTs.  
# ❌ **Not always necessary** if insertions are random (e.g., Red-Black Trees have better worst-case insertion performance).  

# ---

### **How to Decide Which Rotation is Required in an AVL Tree?**  

# Whenever we **insert** a new node into an **AVL Tree**, we must check if the tree remains **balanced**. The AVL tree maintains its balance by ensuring that the **balance factor** (height difference between left and right subtrees) is always **-1, 0, or 1**.

# ---

# ## **Step 1: Calculate the Balance Factor**
# For a given node **N**, the **balance factor** is calculated as:

# \[
# \{Balance Factor} = {Height of Left Subtree} - {Height of Right Subtree}
# \]

# - **Balance Factor > 1** → Left-heavy (potential LL or LR rotation)
# - **Balance Factor < -1** → Right-heavy (potential RR or RL rotation)
# - **Balance Factor in [-1, 0, 1]** → Balanced, no rotation needed.

# ---

# ## **Step 2: Identify Rotation Type**
# Once we detect an imbalance, we determine **which rotation is required** based on the position of the newly inserted node.

# ### **Case 1: Left-Left (LL) → Right Rotation**
# 📌 **Condition:** Imbalance occurs in the **left subtree of the left child**  
# 📌 **Balance Factor > 1** and **key < root.left.key**  

# ✅ **Solution:** **Right Rotate (RR)**  

# #### **Example**
# **Before Inserting 10:**
# ```
#        30
#       /
#      20
#     /
#    10
# ```
# 🔺 **Imbalance detected at 30 (Balance Factor = 2) → LL Case**  

# ✅ **After Right Rotation at 30:**
# ```
#        20
#       /  \
#      10   30
# ```

# ---

# ### **Case 2: Right-Right (RR) → Left Rotation**
# 📌 **Condition:** Imbalance occurs in the **right subtree of the right child**  
# 📌 **Balance Factor < -1** and **key > root.right.key**  

# ✅ **Solution:** **Left Rotate (LL)**  

# #### **Example**
# **Before Inserting 50:**
# ```
#      10
#        \
#         20
#           \
#            50
# ```
# 🔺 **Imbalance detected at 10 (Balance Factor = -2) → RR Case**  

# ✅ **After Left Rotation at 10:**
# ```
#        20
#       /  \
#      10   50
# ```

# ---

# ### **Case 3: Left-Right (LR) → Left Rotate + Right Rotate**
# 📌 **Condition:** Imbalance occurs in the **right subtree of the left child**  
# 📌 **Balance Factor > 1** and **key > root.left.key**  

# ✅ **Solution:** **First Left Rotate (LL) on Left Child, then Right Rotate (RR) on Root**  

# #### **Example**
# **Before Inserting 15:**
# ```
#        30
#       /
#      10
#        \
#         15
# ```
# 🔺 **Imbalance detected at 30 (Balance Factor = 2) → LR Case**  

# ✅ **Step 1: Left Rotate on 10**
# ```
#        30
#       /
#      15
#     /
#    10
# ```
# ✅ **Step 2: Right Rotate on 30**
# ```
#       15
#      /  \
#     10   30
# ```

# ---

# ### **Case 4: Right-Left (RL) → Right Rotate + Left Rotate**
# 📌 **Condition:** Imbalance occurs in the **left subtree of the right child**  
# 📌 **Balance Factor < -1** and **key < root.right.key**  

# ✅ **Solution:** **First Right Rotate (RR) on Right Child, then Left Rotate (LL) on Root**  

# #### **Example**
# **Before Inserting 25:**
# ```
#       10
#         \
#          30
#         /
#        25
# ```
# 🔺 **Imbalance detected at 10 (Balance Factor = -2) → RL Case**  

# ✅ **Step 1: Right Rotate on 30**
# ```
#       10
#         \
#          25
#            \
#             30
# ```
# ✅ **Step 2: Left Rotate on 10**
# ```
#       25
#      /  \
#     10   30
# ```

# ---

# ## **Final Decision Table**
# | Case | Condition | Rotation Needed |
# |------|-----------|----------------|
# | **LL** | **Balance Factor > 1** and **key < root.left.key** | **Right Rotate (RR)** |
# | **RR** | **Balance Factor < -1** and **key > root.right.key** | **Left Rotate (LL)** |
# | **LR** | **Balance Factor > 1** and **key > root.left.key** | **Left Rotate on left child, then Right Rotate on root (LR)** |
# | **RL** | **Balance Factor < -1** and **key < root.right.key** | **Right Rotate on right child, then Left Rotate on root (RL)** |

# ---


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Initial height of node is 1

class AVLTree:
    # Get height of a node
    def get_height(self, node):
        return node.height if node else 0

    # Get balance factor of a node
    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    # Right Rotation (LL Rotation)  
    # Imbalance occurs in the LEFT subtree of the LEFT child
    # Before Rotation:
    #         y
    #        /
    #       x
    #      /
    #     z
    #
    # After Right Rotate:
    #       x
    #      / \
    #     z   y
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x  # New root

    # Left Rotation (RR Rotation)  
    # Imbalance occurs in the RIGHT subtree of the RIGHT child
    # Before Rotation:
    #     x
    #      \
    #       y
    #        \
    #         z
    #
    # After Left Rotate:
    #       y
    #      / \
    #     x   z
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # New root

    # Insert a node into AVL tree
    def insert(self, root, key):
        # Standard BST insert
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update height of ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get balance factor
        balance = self.get_balance(root)

        # Case 1: Left-Left (LL) Imbalance -> Right Rotate
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Case 2: Right-Right (RR) Imbalance -> Left Rotate
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Case 3: Left-Right (LR) Imbalance -> Left Rotate, then Right Rotate
        # Before:
        #         y
        #        /
        #       x
        #        \
        #         z
        #
        # Step 1: Left Rotation on x
        #         y
        #        /
        #       z
        #      /
        #     x
        #
        # Step 2: Right Rotation on y
        #       z
        #      / \
        #     x   y
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4: Right-Left (RL) Imbalance -> Right Rotate, then Left Rotate
        # Before:
        #     x
        #      \
        #       y
        #      /
        #     z
        #
        # Step 1: Right Rotation on y
        #     x
        #      \
        #       z
        #        \
        #         y
        #
        # Step 2: Left Rotation on x
        #       z
        #      / \
        #     x   y
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root  # Return unchanged root

    # Preorder traversal (Root -> Left -> Right)
    def preorder_traversal(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

# Example usage
avl_tree = AVLTree()
root = None
values = [10, 20, 30, 40, 50, 25]  # Unbalanced sequence
for val in values:
    root = avl_tree.insert(root, val)

print("Preorder traversal of AVL tree:")
avl_tree.preorder_traversal(root)

# ### **Summary of Rotations**
# | Case | Imbalance Type | Rotation Required |
# |------|---------------|-------------------|
# | **LL** | Left-Left (Deep left) | Right Rotate (RR) |
# | **RR** | Right-Right (Deep right) | Left Rotate (LL) |
# | **LR** | Left-Right | Left Rotate, then Right Rotate (LR) |
# | **RL** | Right-Left | Right Rotate, then Left Rotate (RL) |
