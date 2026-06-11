# DP on Trees
Dynamic Programming on Trees extends the DP paradigm to hierarchical structures where each node represents a subproblem and decisions depend on information from its children. Unlike linear or grid DP, tree DP typically uses postorder traversal to compute and propagate results from leaf nodes toward the root. Common patterns include calculating heights, diameters, maximum path sums, subtree properties, and optimization problems involving choosing or excluding nodes. By storing and combining results for each subtree, tree DP efficiently solves complex problems on recursive tree structures while avoiding redundant computations.


## 1️⃣ Diameter of Binary Tree

### 📌 Problem Statement

You are given:

* `root` → the root of a binary tree

👉 The **diameter** of a binary tree is the length of the longest path between any two nodes in the tree.

👉 The path may or may not pass through the root.

👉 Return the diameter of the tree.

---

### 🚀 Approach: DFS + Height Calculation

#### 🔹 Key Idea

For every node:

* Compute the height of its left subtree.
* Compute the height of its right subtree.

The longest path passing through that node is:

```text id="relation"
leftHeight + rightHeight
```

We maintain a global diameter and update it at every node.

Meanwhile, the recursive function returns the height of the current subtree:

```text id="height"
height(node)
=
1 + max(
    leftHeight,
    rightHeight
)
```

---

### 🧠 Algorithm

1. Initialize:

   * `diameter = 0`

2. Perform DFS traversal.

3. For each node:

   * Compute left subtree height.
   * Compute right subtree height.
   * Update diameter using:

     * `left + right`

4. Return:

   * `1 + max(left, right)` as the node's height.

5. After traversal completes:

   * Return the maximum diameter found.

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(h)       |

Where:

* `n` = number of nodes
* `h` = height of the tree

---

### 📎 Example

```text id="example"
Input:

        1
       / \
      2   3
     / \
    4   5

Output:
3
```

---

### 🔍 Dry Run

```text id="dryrun"
Node 4:

left = 0
right = 0

diameter = 0

Node 5:

left = 0
right = 0

diameter = 0

Node 2:

left = 1
right = 1

diameter = 2

Node 1:

left = 2
right = 1

diameter = 3

Answer = 3
```

---

### 🌳 Visualization

```text id="visual"
        1
       / \
      2   3
     / \
    4   5

Longest Path:

4 → 2 → 1 → 3

Edges = 3
```

---

### ✅ Key Points

* Diameter may or may not pass through the root.
* Height calculation naturally helps compute diameter.
* Every node is processed exactly once.
* DFS simultaneously computes height and updates diameter.

---

### ⚠️ Edge Cases

* Empty tree
* Single node tree
* Completely skewed tree
* Perfect binary tree

---

### 🏁 Conclusion

The Diameter of Binary Tree problem can be solved efficiently using a single DFS traversal. By computing the height of each subtree and updating the longest path through every node, we can determine the tree's diameter in linear time while only using recursion stack space proportional to the tree height.
