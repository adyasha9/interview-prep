# ### **Red-Black Tree (RBT) - Self-Balancing Binary Search Tree**  
# A **Red-Black Tree** is a **self-balancing Binary Search Tree (BST)** that ensures logarithmic time complexity for search, insertion, and deletion by maintaining balance using color properties and rotations.

# ---

# ## **Properties of a Red-Black Tree**
# 1. **Every node is either red or black.**  
# 2. **The root is always black.**  
# 3. **Every leaf (NIL/NULL node) is black.**  
# 4. **If a node is red, both its children must be black (No two consecutive red nodes).**  
# 5. **Every path from a given node to its descendant leaves contains the same number of black nodes.**

# These properties ensure that the tree remains balanced, making all operations **O(log n).**

# ---

# ## **Time and Space Complexity**
# | Operation  | Average Case | Worst Case | Space Complexity |
# |------------|-------------|------------|------------------|
# | Search     | **O(log n)** | **O(log n)** | **O(n)** |
# | Insert     | **O(log n)** | **O(log n)** | - |
# | Delete     | **O(log n)** | **O(log n)** | - |

# ---

## **Python Implementation of a Red-Black Tree**

class Node:
    def __init__(self, key, color="R"):
        self.key = key
        self.color = color  # Red by default
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0, "B")  # Sentinel NIL node (black)
        self.root = self.NIL

    # Left Rotation
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Right Rotation
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Fix insert violations
    def insert_fixup(self, z):
        while z.parent and z.parent.color == "R":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right  # Uncle node
                if y.color == "R":  # Case 1: Uncle is red
                    z.parent.color = "B"
                    y.color = "B"
                    z.parent.parent.color = "R"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:  # Case 2: z is right child
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "B"  # Case 3: z is left child
                    z.parent.parent.color = "R"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left  # Uncle node
                if y.color == "R":
                    z.parent.color = "B"
                    y.color = "B"
                    z.parent.parent.color = "R"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "B"
                    z.parent.parent.color = "R"
                    self.left_rotate(z.parent.parent)
        self.root.color = "B"

    # Insert a node
    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.NIL
        new_node.right = self.NIL

        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y is None:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        new_node.color = "R"
        self.insert_fixup(new_node)

    # Fix delete violations
    def delete_fixup(self, x):
        while x != self.root and x.color == "B":
            if x == x.parent.left:
                s = x.parent.right
                if s.color == "R":  # Case 1: Sibling is red
                    s.color = "B"
                    x.parent.color = "R"
                    self.left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == "B" and s.right.color == "B":  # Case 2: Both children of sibling are black
                    s.color = "R"
                    x = x.parent
                else:
                    if s.right.color == "B":  # Case 3: Sibling's right child is black
                        s.left.color = "B"
                        s.color = "R"
                        self.right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color  # Case 4: Sibling's right child is red
                    x.parent.color = "B"
                    s.right.color = "B"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == "R":
                    s.color = "B"
                    x.parent.color = "R"
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.right.color == "B" and s.left.color == "B":
                    s.color = "R"
                    x = x.parent
                else:
                    if s.left.color == "B":
                        s.right.color = "B"
                        s.color = "R"
                        self.left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = "B"
                    s.left.color = "B"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "B"

    # Delete a node
    def delete(self, key):
        z = self.root
        while z != self.NIL:
            if z.key == key:
                break
            elif key < z.key:
                z = z.left
            else:
                z = z.right

        if z == self.NIL:
            return

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "B":
            self.delete_fixup(x)

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def inorder(self, node):
        if node != self.NIL:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

# Example Usage
if __name__ == "__main__":
    rbt = RedBlackTree()
    for key in [10, 20, 30, 40, 50, 25]:
        rbt.insert(key)

    print("Inorder traversal of Red-Black tree:")
    rbt.inorder(rbt.root)  # Should print sorted order
# ```

# 🚀 This Red-Black Tree maintains balance using rotations and color changes! Let me know if you need explanations!




## **How to Decide Which Rotation is Required in a Red-Black Tree?**  

# A **Red-Black Tree** is a **self-balancing binary search tree** that maintains balance using a set of properties and **coloring (Red or Black) rules**.  
# Unlike AVL trees, Red-Black Trees allow some imbalance but use **recoloring and rotations** to restore balance.

# ---

# ## **Step 1: Understand the Red-Black Tree Properties**
# A Red-Black Tree must satisfy the following **5 properties**:

# 1. **Every node is either Red or Black.**
# 2. **The root node is always Black.**
# 3. **Red nodes cannot have Red children (No two consecutive Reds - "Red-Red Violation").**
# 4. **Every path from a node to its descendant NULL nodes must have the same number of Black nodes.**
# 5. **A new node is always inserted as Red.**

# ---

# ## **Step 2: Identify Violation & Rotation Type**
# Since insertion always results in a **Red node**, violations occur when:
# - **A Red node has a Red parent** (**Red-Red Violation**).
# - The **Black height rule** is violated.

# We fix these violations using:
# 1. **Recoloring** (if the parent’s sibling is Red).
# 2. **Rotations** (if the parent’s sibling is Black or NULL).

# ### **Case 1: No Violation (Black Parent) → No Action Needed**
# - If the newly inserted node’s **parent is Black**, the tree remains valid.
# - No rotations or recoloring are required.

# ---

# ### **Case 2: Red-Red Violation → Recoloring (Parent’s Sibling is Red)**
# 📌 **Condition:** **Parent is Red** AND **Uncle (parent’s sibling) is also Red**  
# 📌 **Action:** **Recoloring**
# ✅ **Solution:** 
# - **Change the parent and uncle to Black.**
# - **Grandparent becomes Red.**
# - **Repeat process on grandparent (may cause further violations).**

# #### **Example**
# **Before Inserting 40 (Violation at 30 & 40)**
# ```
#         50 (B)
#        /
#      30 (R)
#     /   \
#   20 (B) 40 (R) <- Newly inserted
# ```
# 🔺 **Red-Red Violation at (30, 40), Uncle (20) is also Red.**  

# ✅ **After Recoloring:**
# ```
#         50 (R)
#        /
#      30 (B)
#     /   \
#   20 (B) 40 (B)
# ```
# 💡 **New violation might occur at 50 (R). Repeat process if needed.**

# ---

# ### **Case 3: Red-Red Violation → Rotation Needed (Uncle is Black or NULL)**
# 📌 **Condition:** **Parent is Red** AND **Uncle is Black or NULL**  
# 📌 **Action:** **Rotation + Recoloring**

# There are **4 Rotation Cases**:
# 1. **Left-Left (LL) → Right Rotation**
# 2. **Right-Right (RR) → Left Rotation**
# 3. **Left-Right (LR) → Left Rotate, then Right Rotate**
# 4. **Right-Left (RL) → Right Rotate, then Left Rotate**

# ---

# ### **Case 3.1: Left-Left (LL) → Right Rotation**
# 📌 **Condition:** **New node is inserted into the left subtree of the left child.**  
# 📌 **Solution:** **Right Rotate grandparent + Swap colors of parent & grandparent.**

# #### **Example**
# **Before Inserting 10:**
# ```
#        50 (B)
#       /
#     30 (R)
#    /
#   10 (R) <- Newly inserted
# ```
# 🔺 **Violation at (30, 10), Uncle (NULL) is Black.**  

# ✅ **After Right Rotation on 50:**
# ```
#        30 (B)
#       /   \
#     10 (R) 50 (R)
# ```
# ✅ **Color Swap (30 → Black, 50 → Red).**

# ---

# ### **Case 3.2: Right-Right (RR) → Left Rotation**
# 📌 **Condition:** **New node is inserted into the right subtree of the right child.**  
# 📌 **Solution:** **Left Rotate grandparent + Swap colors of parent & grandparent.**

# #### **Example**
# **Before Inserting 70:**
# ```
#        50 (B)
#           \
#           60 (R)
#              \
#              70 (R) <- Newly inserted
# ```
# 🔺 **Violation at (60, 70), Uncle (NULL) is Black.**  

# ✅ **After Left Rotation on 50:**
# ```
#        60 (B)
#       /   \
#     50 (R) 70 (R)
# ```
# ✅ **Color Swap (60 → Black, 50 → Red).**

# ---

# ### **Case 3.3: Left-Right (LR) → Left Rotate, then Right Rotate**
# 📌 **Condition:** **New node is inserted into the right subtree of the left child.**  
# 📌 **Solution:** **Left Rotate parent → Right Rotate grandparent → Swap colors.**

# #### **Example**
# **Before Inserting 25:**
# ```
#        50 (B)
#       /
#     30 (R)
#       \
#       25 (R) <- Newly inserted
# ```
# 🔺 **Violation at (30, 25), Uncle (NULL) is Black.**  

# ✅ **Step 1: Left Rotate on 30**
# ```
#        50 (B)
#       /
#     25 (R)
#    /
#   30 (R)
# ```
# ✅ **Step 2: Right Rotate on 50**
# ```
#        25 (B)
#       /   \
#     30 (R) 50 (R)
# ```

# ---

# ### **Case 3.4: Right-Left (RL) → Right Rotate, then Left Rotate**
# 📌 **Condition:** **New node is inserted into the left subtree of the right child.**  
# 📌 **Solution:** **Right Rotate parent → Left Rotate grandparent → Swap colors.**

# #### **Example**
# **Before Inserting 55:**
# ```
#        50 (B)
#           \
#           60 (R)
#          /
#        55 (R) <- Newly inserted
# ```
# 🔺 **Violation at (60, 55), Uncle (NULL) is Black.**  

# ✅ **Step 1: Right Rotate on 60**
# ```
#        50 (B)
#           \
#           55 (R)
#             \
#             60 (R)
# ```
# ✅ **Step 2: Left Rotate on 50**
# ```
#        55 (B)
#       /   \
#     50 (R) 60 (R)
# ```

# ---

# ## **Final Decision Table**
# | Case | Condition | Fix |
# |------|-----------|----------------------|
# | **Recoloring** | Parent is Red & Uncle is Red | Recolor Parent & Uncle to Black, Grandparent to Red |
# | **LL (Left-Left)** | Parent is Red & Uncle is Black, Node inserted in left-left | **Right Rotate** on Grandparent & Swap Colors |
# | **RR (Right-Right)** | Parent is Red & Uncle is Black, Node inserted in right-right | **Left Rotate** on Grandparent & Swap Colors |
# | **LR (Left-Right)** | Parent is Red & Uncle is Black, Node inserted in left-right | **Left Rotate on Parent, then Right Rotate on Grandparent** & Swap Colors |
# | **RL (Right-Left)** | Parent is Red & Uncle is Black, Node inserted in right-left | **Right Rotate on Parent, then Left Rotate on Grandparent** & Swap Colors |

# ---

# ### **Summary**
# 1. **Newly inserted node is always Red**.
# 2. **If parent is Black** → No change.
# 3. **If parent is Red**:
#    - **If uncle is Red** → **Recolor**.
#    - **If uncle is Black or NULL** → **Rotation (LL, RR, LR, RL)**.
# 4. **Always ensure the root remains Black.**

# Let me know if you need code with comments for visualization! 🚀