# Serialization and Construction of Binary Trees
**Serialization and Construction of Binary Trees** are essential techniques used to convert a tree structure into a storable or transmittable format and then rebuild it back into its original form. Serialization encodes the tree into a sequence (such as a string or list) using traversal methods like preorder, level order, or DFS while preserving null relationships, ensuring the exact structure can be reconstructed. Construction (deserialization) is the reverse process, where the encoded data is used to rebuild the tree node by node. These concepts are widely used in data storage, network transmission, and system design problems, making them fundamental for handling tree-based data efficiently.



## 1️⃣ Invert Binary Tree (DFS - Recursion)

### 📌 Problem Statement

Given the root of a binary tree, invert the tree and return its root.

👉 Inverting a binary tree means swapping the left and right child of every node in the tree.

---

### 🚀 Approach: Depth-First Search (Recursion)

This problem is best solved using **DFS (recursive traversal)**.

#### 🔹 Idea

* For each node:

  * Recursively invert its left subtree
  * Recursively invert its right subtree
  * Swap the left and right children

---

### 🧠 Algorithm

1. **Base Case**:

   * If the node is `None`, return `None`

2. **Recursive Step**:

   * Recursively invert left subtree
   * Recursively invert right subtree

3. **Swap**:

   * Assign:

     ```
     root.left = right
     root.right = left
     ```

4. Return the root

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(h)       |

👉 `n` = number of nodes
👉 `h` = height of the tree (recursion stack)

---

### 📎 Example

```text id="example"
Input:
      4
     / \
    2   7
   / \ / \
  1  3 6  9

Output:
      4
     / \
    7   2
   / \ / \
  9  6 3  1
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Start at root (4)

Invert left subtree → (2 becomes subtree with 3,1)  
Invert right subtree → (7 becomes subtree with 9,6)  

Swap children of 4 → (7,2)
```

---

### ✅ Key Points

* Uses **DFS recursion**
* Works in **post-order traversal style**
* Swaps children at every node
* Simple and elegant solution

---

### ⚠️ Edge Cases

* Empty tree (`root = None`)
* Single node tree
* Skewed tree (left-heavy or right-heavy)

---

### 🏁 Conclusion

The recursive DFS approach efficiently inverts a binary tree by swapping children at every node, leveraging the natural tree structure. It achieves optimal **O(n)** time complexity with minimal extra space.


---


## 2️⃣ Flatten Binary Tree to Linked List (DFS - Reverse Preorder)

### 📌 Problem Statement

Given the root of a binary tree, flatten the tree into a "linked list" in-place.

👉 The linked list should:

* Use the same `TreeNode` structure
* Follow **preorder traversal (Root → Left → Right)**
* Use the **right pointer** as the next node
* Set all **left pointers to `None`**

---

### 🚀 Approach: DFS (Reverse Preorder Traversal)

#### 🔹 Key Idea

Instead of normal preorder, we traverse in **reverse preorder**:

```
Right → Left → Root
```

👉 Why?

* This allows us to **build the linked list from the end**
* We keep track of the **previous node (`self.prev`)**
* At each step:

  * Point current node’s right to `prev`
  * Set left to `None`

---

### 🧠 Algorithm

1. Initialize:

   * `self.prev = None`

2. Define DFS:

   * Traverse **right subtree first**
   * Then **left subtree**

3. Process current node:

   * `node.right = self.prev`
   * `node.left = None`
   * Update `self.prev = node`

4. Call DFS on root

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(h)       |

👉 `n` = number of nodes
👉 `h` = height of the tree (recursion stack)

---

### 📎 Example

```text id="example"
Input:
    1
   / \
  2   5
 / \   \
3   4   6

Output (Linked List):
1 → 2 → 3 → 4 → 5 → 6
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Traverse in reverse preorder:

Visit: 6 → 5 → 4 → 3 → 2 → 1

Rewiring:
6 → None  
5 → 6  
4 → 5  
3 → 4  
2 → 3  
1 → 2
```

---

### ✅ Key Points

* Uses **reverse preorder traversal**
* Maintains a **previous pointer**
* Modifies tree **in-place**
* Ensures correct preorder-linked structure

---

### ⚠️ Edge Cases

* Empty tree (`root = None`)
* Single node tree
* Left-skewed tree
* Right-skewed tree

---

### 🏁 Conclusion

This approach efficiently flattens a binary tree into a linked list by leveraging reverse preorder traversal and pointer manipulation. It avoids extra data structures and achieves optimal **O(n)** time complexity.


---


## Here’s a clean and professional **README.md** for your **Populating Next Right Pointers in Each Node (BFS)** solution 👇

---

## Populating Next Right Pointers in Each Node (BFS)

### 📌 Problem Statement

Given a binary tree, populate each node’s `next` pointer to point to its **next right node**. If there is no next right node, the `next` pointer should be set to `None`.

👉 The connection should be done **level by level**.

---

### 🚀 Approach: Breadth-First Search (Level Order Traversal)

This problem is efficiently solved using **BFS (queue-based level order traversal)**.

#### 🔹 Key Idea

* Traverse the tree **level by level**
* Maintain a pointer `prev` to track the previous node in the same level
* Connect:

  ```
  prev.next → current node
  ```

---

### 🧠 Algorithm

1. **Base Case**:

   * If `root` is `None`, return `None`

2. **Initialize**:

   * Queue with root node

3. **Level Order Traversal**:

   * For each level:

     * Initialize `prev = None`
     * Traverse all nodes in the level:

       * Pop node from queue
       * Add its children to queue
       * If `prev` exists:

         * Set `prev.next = node`
       * Update `prev = node`

4. Return root

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(n)       |

👉 `n` = number of nodes

---

### 📎 Example

```text id="example"
Input Tree:
        1
      /   \
     2     3
    / \     \
   4   5     7

Output (Next Pointers):
1 → None  
2 → 3 → None  
4 → 5 → 7 → None
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Level 1: 1 → None  
Level 2: 2 → 3 → None  
Level 3: 4 → 5 → 7 → None
```

---

### ✅ Key Points

* Uses **BFS (level order traversal)**
* Connects nodes **within the same level**
* Maintains a `prev` pointer for linking
* Works for **any binary tree (not just perfect trees)**

---

### ⚠️ Edge Cases

* Empty tree (`root = None`)
* Single node tree
* Skewed tree (left or right heavy)

---

### 🏁 Conclusion

This BFS-based approach efficiently connects nodes at the same level using a queue and a simple pointer mechanism, achieving optimal **O(n)** time complexity while maintaining clarity and simplicity.


---