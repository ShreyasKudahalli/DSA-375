# Lowest Common Ancestor (LCA) and range queries
Lowest Common Ancestor (LCA) and range queries are fundamental operations on trees—especially Binary Search Trees (BSTs)—that leverage the tree’s hierarchical and ordered structure for efficient computation. The LCA problem focuses on identifying the deepest node that serves as a common ancestor for two given nodes, which is crucial in applications like path queries and network routing. Range queries, on the other hand, involve retrieving or processing all node values that lie within a specified interval, often using the BST property to prune unnecessary branches and optimize traversal. Together, these operations highlight how tree structures enable fast querying and decision-making, typically achieving optimal time complexities by avoiding full traversal of the tree.



## 1️⃣ Lowest Common Ancestor (LCA) in Binary Search Tree

### 📌 Problem Statement

Given the root of a **Binary Search Tree (BST)** and two nodes `p` and `q`, return their **Lowest Common Ancestor (LCA)**.

👉 The LCA is the lowest node in the tree such that both `p` and `q` are descendants of it.

---

### 🚀 Approach: BST Property Optimization

#### 🔹 Key Idea

A **Binary Search Tree** follows:

* Left subtree → values **less than** root
* Right subtree → values **greater than** root

👉 Use this property to determine where `p` and `q` lie.

---

### 🧠 Algorithm

1. Start from the root

2. If both `p` and `q` are:

   * **Greater than root** → move to right subtree
   * **Less than root** → move to left subtree

3. Otherwise:

   * Current node is the **split point**
   * This is the **LCA**

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(h)       |
| Space Complexity | O(h)       |

👉 `h` = height of the tree

* Balanced BST → **O(log n)**
* Skewed BST → **O(n)**

---

### 📎 Example

```text id="example"
Input:
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5

p = 2, q = 8

Output: 6
```

---

### 🔍 Dry Run

```text id="dryrun"
Start at root = 6

p = 2 (left), q = 8 (right)

Split occurs here ✔️  
LCA = 6
```

---

### ✅ Key Points

* Uses **BST property for efficient traversal**
* Finds LCA without exploring entire tree
* Works in **O(h)** time
* Much faster than general binary tree approach

---

### ⚠️ Edge Cases

* `p` or `q` is the root
* One node is ancestor of another
* Skewed BST
* Tree with only one node

---

### 🏁 Conclusion

This optimized approach leverages the BST property to find the Lowest Common Ancestor efficiently by identifying the split point between two nodes, achieving optimal **O(h)** performance.


---


## 2️⃣ Minimum Absolute Difference in BST

### 📌 Problem Statement

Given a **Binary Search Tree (BST)** and an integer `K`, find the **minimum absolute difference** between `K` and any node value present in the BST.

👉 Return the smallest value of:
[
|node.val - K|
]

---

### 🚀 Approach: BST Traversal (Optimized Search)

#### 🔹 Key Idea

* A **BST** allows efficient searching using its ordered property:

  * Left subtree → smaller values
  * Right subtree → larger values

👉 Instead of traversing all nodes, we **move intelligently** toward the closest value.

---

### 🧠 Algorithm

1. Initialize:

   * `ans = ∞`
   * Start from `root`

2. Traverse the BST:

   * At each node:

     * Update `ans = min(ans, abs(node.data - K))`
   * If `K < node.data` → go **left**
   * Else → go **right**

3. Continue until reaching `None`

4. Return `ans`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(h)       |
| Space Complexity | O(1)       |

👉 `h` = height of BST

* Balanced BST → **O(log n)**
* Skewed BST → **O(n)**

---

### 📎 Example

```text id="example"
Input:
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13

K = 5

Output: 1
```

---

### 🔍 Dry Run

```text id="dryrun"
Start at root = 8
|8 - 5| = 3 → ans = 3 → go left

Node = 3
|3 - 5| = 2 → ans = 2 → go right

Node = 6
|6 - 5| = 1 → ans = 1 → go left

Node = 4
|4 - 5| = 1 → ans = 1 → go right (None)

Final Answer = 1 ✔️
```

---

### ✅ Key Points

* Uses **BST property for efficient traversal**
* Avoids full tree traversal
* Works in **O(h)** time
* Space optimized (no recursion)

---

### ⚠️ Edge Cases

* Empty tree
* Single node tree
* `K` smaller than all nodes
* `K` larger than all nodes
* Exact match (`ans = 0`)

---

### 🏁 Conclusion

This approach efficiently finds the closest value to `K` in a BST by leveraging its ordered structure, achieving optimal **O(h)** time complexity and constant space usage.


---