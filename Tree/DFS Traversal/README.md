# 🌳 Depth-First Search (DFS) Traversal

Depth-First Search (DFS) is a fundamental tree and graph traversal technique that explores as far as possible along each branch before backtracking. In structures like trees, DFS is commonly implemented using recursion, naturally following patterns such as **preorder, inorder, and postorder traversals**. It works by visiting a node, then recursively exploring its children, making it ideal for problems involving hierarchical data, path exploration, and backtracking. DFS is efficient, with a time complexity of **O(n)**, and leverages the call stack (or an explicit stack) to manage traversal state.


## 1️⃣ Binary Tree Inorder Traversal (Recursion)

### 📌 Problem Statement

Given the root of a binary tree, return the **inorder traversal** of its nodes' values.

👉 Inorder traversal follows the order:

[
\text{Left} \rightarrow \text{Root} \rightarrow \text{Right}
]

```text id="tree-example"
Input Tree:
        1
         \
          2
         /
        3

Output: [1, 3, 2]
```

---

### 🚀 Approach: Recursion

We use recursion to traverse the tree:

1. Traverse the **left subtree**
2. Visit the **current node**
3. Traverse the **right subtree**

---

### 🧠 Key Idea

* Recursively visit nodes in **Left → Root → Right** order
* Use a list to store the traversal result
* The recursion stack naturally handles tree depth

---

### 🧩 Algorithm

1. Initialize an empty list `res`
2. Define recursive function `inorder(root)`
3. If node exists:

   * Call `inorder(root.left)`
   * Append `root.val` to `res`
   * Call `inorder(root.right)`
4. Call function with root
5. Return result list

---

### 📊 Complexity Analysis

| Type             | Complexity                                   |
| ---------------- | -------------------------------------------- |
| Time Complexity  | O(n)                                         |
| Space Complexity | O(h) *(recursion stack, h = height of tree)* |

---

### 📎 Examples

```text id="ex1"
Input: root = [1,null,2,3]  
Output: [1,3,2]
```

```text id="ex2"
Input: root = []  
Output: []
```

```text id="ex3"
Input: root = [1]  
Output: [1]
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Traverse Left → Visit Node → Traverse Right

For tree:
    1
     \
      2
     /
    3

Steps:
→ Visit 1
→ Go right → 2
→ Go left → 3
→ Output: [1,3,2]
```

---

### 🔁 Iterative vs Recursive

| Approach  | Space | Style              |
| --------- | ----- | ------------------ |
| Iterative | O(n)  | Uses stack         |
| Recursive | O(h)  | Cleaner, intuitive |

---

### ✅ Key Points

* Fundamental tree traversal technique
* Used in many tree-based problems
* Recursive approach is simple and readable
* Forms basis for BST operations (gives sorted order)

---

### ⚠️ Edge Cases

* Empty tree (`root = None`)
* Single node tree
* Skewed tree (height = n)

---

### 🏁 Conclusion

Inorder traversal is a fundamental binary tree technique that processes nodes in a structured left-root-right order. The recursive approach is intuitive and leverages the call stack to efficiently traverse the tree.


---


## 2️⃣ Binary Tree Preorder Traversal (Recursion)

### 📌 Problem Statement

Given the root of a binary tree, return the **preorder traversal** of its nodes' values.

👉 Preorder traversal follows the order:

[
\text{Root} \rightarrow \text{Left} \rightarrow \text{Right}
]

```text id="tree-example"
Input Tree:
        1
         \
          2
         /
        3

Output: [1, 2, 3]
```

---

### 🚀 Approach: Recursion

We use recursion to traverse the tree in **Root → Left → Right** order:

1. Visit the current node
2. Traverse the left subtree
3. Traverse the right subtree

---

### 🧠 Key Idea

* Process the node **before** its children
* Recursion naturally handles traversal order
* Store results in a list

---

### 🧩 Algorithm

1. Initialize an empty list `res`
2. Define recursive function `preorder(root)`
3. If node exists:

   * Append `root.val` to `res`
   * Call `preorder(root.left)`
   * Call `preorder(root.right)`
4. Call function with root
5. Return result list

---

### 📊 Complexity Analysis

| Type             | Complexity                                   |
| ---------------- | -------------------------------------------- |
| Time Complexity  | O(n)                                         |
| Space Complexity | O(h) *(recursion stack, h = height of tree)* |

---

### 📎 Examples

```text id="ex1"
Input: root = [1,null,2,3]  
Output: [1,2,3]
```

```text id="ex2"
Input: root = []  
Output: []
```

```text id="ex3"
Input: root = [1]  
Output: [1]
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Traverse Root → Left → Right

For tree:
    1
     \
      2
     /
    3

Steps:
→ Visit 1
→ Go left (None)
→ Go right → 2
→ Visit 2
→ Go left → 3
→ Visit 3

Output: [1,2,3]
```

---

### 🔁 Iterative vs Recursive

| Approach  | Space | Style              |
| --------- | ----- | ------------------ |
| Iterative | O(n)  | Uses stack         |
| Recursive | O(h)  | Cleaner, intuitive |

---

### ✅ Key Points

* Visits node **before** its children
* Useful for copying trees or prefix expressions
* Simple and intuitive using recursion
* Foundation for many tree problems

---

### ⚠️ Edge Cases

* Empty tree (`root = None`)
* Single node tree
* Skewed tree (height = n)

---

### 🏁 Conclusion

Preorder traversal is a fundamental tree traversal technique where nodes are processed before their subtrees. The recursive approach makes it simple and aligns naturally with the structure of binary trees.


---

## 3️⃣ Binary Tree Postorder Traversal (Recursion)

### 📌 Problem Statement

Given the root of a binary tree, return the **postorder traversal** of its nodes' values.

👉 Postorder traversal follows the order:

[
\text{Left} \rightarrow \text{Right} \rightarrow \text{Root}
]


```text id="tree-example"
Input Tree:
        1
         \
          2
         /
        3

Output: [3, 2, 1]
```

---

### 🚀 Approach: Recursion

We use recursion to traverse the tree in **Left → Right → Root** order:

1. Traverse the left subtree
2. Traverse the right subtree
3. Visit the current node

---

### 🧠 Key Idea

* Process the node **after** its children
* Useful when child nodes must be handled before the parent
* Recursion naturally follows tree structure

---

### 🧩 Algorithm

1. Initialize an empty list `res`
2. Define recursive function `postorder(root)`
3. If node exists:

   * Call `postorder(root.left)`
   * Call `postorder(root.right)`
   * Append `root.val` to `res`
4. Call function with root
5. Return result list

---

### 📊 Complexity Analysis

| Type             | Complexity                                   |
| ---------------- | -------------------------------------------- |
| Time Complexity  | O(n)                                         |
| Space Complexity | O(h) *(recursion stack, h = height of tree)* |

---

### 📎 Examples

```text id="ex1"
Input: root = [1,null,2,3]  
Output: [3,2,1]
```

```text id="ex2"
Input: root = []  
Output: []
```

```text id="ex3"
Input: root = [1]  
Output: [1]
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Traverse Left → Right → Root

For tree:
    1
     \
      2
     /
    3

Steps:
→ Go left (None)
→ Go right → 2
→ Go left → 3 → visit 3
→ Visit 2
→ Visit 1

Output: [3,2,1]
```

---

### 🔁 Iterative vs Recursive

| Approach  | Space | Style              |
| --------- | ----- | ------------------ |
| Iterative | O(n)  | Uses stack         |
| Recursive | O(h)  | Cleaner, intuitive |

---

### ✅ Key Points

* Visits node **after** its children
* Useful for deletion of trees, evaluation problems
* Clean recursive structure
* Fundamental tree traversal technique

---

### ⚠️ Edge Cases

* Empty tree (`root = None`)
* Single node tree
* Skewed tree (height = n)

---

### 🏁 Conclusion

Postorder traversal is essential when operations must be performed on child nodes before the parent. The recursive approach provides a simple and intuitive way to traverse the tree in **Left → Right → Root** order.


---


## 4️⃣ Same Tree (DFS / Recursion)

### 📌 Problem Statement

Given the roots of two binary trees `p` and `q`, determine if they are **identical**.

👉 Two binary trees are considered the same if:

* They have the **same structure**
* Their corresponding nodes have the **same values**

```text id="example-vis"
Tree 1:        Tree 2:
   1              1
  / \            / \
 2   3          2   3

Output: True
```

---

### 🚀 Approach: Depth-First Search (DFS)

We use **DFS (recursion)** to compare both trees node by node:

* Traverse both trees simultaneously
* Compare values at each node
* Recursively check left and right subtrees

---

### 🧠 Key Idea

At each step:

* If both nodes are `None` → they match
* If one is `None` → not identical
* If values differ → not identical
* Otherwise → check left and right subtrees

---

### 🧩 Algorithm

1. If both nodes are `None` → return `True`
2. If one is `None` → return `False`
3. If values differ → return `False`
4. Recursively check:

   * Left subtree → `p.left` vs `q.left`
   * Right subtree → `p.right` vs `q.right`
5. Return logical AND of both results

---

### 📊 Complexity Analysis

| Type             | Complexity                                   |
| ---------------- | -------------------------------------------- |
| Time Complexity  | O(n)                                         |
| Space Complexity | O(h) *(recursion stack, h = height of tree)* |

---

### 📎 Examples

```text id="ex1"
Input: p = [1,2,3], q = [1,2,3]  
Output: True
```

```text id="ex2"
Input: p = [1,2], q = [1,null,2]  
Output: False
```

```text id="ex3"
Input: p = [1,2,1], q = [1,1,2]  
Output: False
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Compare root nodes → 1 == 1 ✔️
Compare left → 2 == 2 ✔️
Compare right → 3 == 3 ✔️

All nodes match → return True
```

---

### 🔁 Alternative Approach

* Use **BFS (level-order traversal)** with a queue
* Compare nodes level by level

---

### ✅ Key Points

* Uses **DFS recursion**
* Compares both **structure and values**
* Stops early if mismatch found
* Simple and efficient approach

---

### ⚠️ Edge Cases

* Both trees empty → `True`
* One tree empty → `False`
* Different structure
* Same structure but different values

---

### 🏁 Conclusion

This DFS-based recursive solution efficiently checks whether two binary trees are identical by comparing nodes and their subtrees simultaneously, ensuring both structure and values match perfectly.


---


## 5️⃣ Diameter of Binary Tree (DFS / Recursion)

### 📌 Problem Statement

Given the root of a binary tree, return the **diameter** of the tree.

👉 The **diameter** is defined as the **length of the longest path between any two nodes** in the tree.
This path may or may not pass through the root.

---

### 🚀 Approach: Depth-First Search (DFS)

We use **DFS (recursion)** to compute the height of each node while simultaneously updating the diameter.

#### 💡 Key Idea:

* At every node, the longest path passing through it is:

  [
  \text{left height} + \text{right height}
  ]

* Keep track of the maximum such value during traversal.

---

### 🧠 Algorithm

1. Initialize a variable `diameter = 0`

2. Define a helper function `height(node)`:

   * If node is `None` → return `0`
   * Recursively compute:

     * `left = height(node.left)`
     * `right = height(node.right)`
   * Update diameter:

     * `diameter = max(diameter, left + right)`
   * Return height:

     * `1 + max(left, right)`

3. Call `height(root)`

4. Return `diameter`

---

### 📊 Complexity Analysis

| Type             | Complexity                                   |
| ---------------- | -------------------------------------------- |
| Time Complexity  | O(n)                                         |
| Space Complexity | O(h) *(recursion stack, h = height of tree)* |

---

### 📎 Examples

```text
Input: root = [1,2,3,4,5]  
Output: 3  
Explanation: Longest path is [4 → 2 → 1 → 3]
```

```text
Input: root = [1,2]  
Output: 1
```

---

### 🔍 Dry Run (Brief)

```text
For node 2:
left = 1 (node 4)
right = 1 (node 5)
diameter = 2

For root 1:
left = 2
right = 1
diameter = 3 (maximum)
```

---

### ✅ Key Points

* Uses **DFS with post-order traversal**
* Computes height while updating diameter
* Avoids recomputation → efficient
* Diameter is measured in **edges**, not nodes

---

### ⚠️ Edge Cases

* Empty tree → diameter = 0
* Single node → diameter = 0
* Skewed tree → diameter = n - 1

---

### 🏁 Conclusion

This approach efficiently computes the diameter of a binary tree in a single DFS traversal by combining height calculation with diameter updates, achieving optimal **O(n)** time complexity.


---


## 6️⃣ Maximum Depth of Binary Tree (DFS / Recursion)

### 📌 Problem Statement

Given the root of a binary tree, return its **maximum depth**.

👉 The **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

---

### 🚀 Approach: Depth-First Search (DFS)

We use **DFS (recursion)** to compute the depth of the tree:

* Recursively calculate the depth of left and right subtrees
* The depth of the current node is:

  [
  1 + \max(\text{left depth}, \text{right depth})
  ]

---

### 🧠 Algorithm

1. Base case:

   * If `root` is `None` → return `0`

2. Recursive step:

   * Compute:

     * `left = maxDepth(root.left)`
     * `right = maxDepth(root.right)`

3. Return:

   * `1 + max(left, right)`

---

### 📊 Complexity Analysis

| Type             | Complexity                                   |
| ---------------- | -------------------------------------------- |
| Time Complexity  | O(n)                                         |
| Space Complexity | O(h) *(recursion stack, h = height of tree)* |

---

### 📎 Examples

```text id="ex1"
Input: root = [3,9,20,null,null,15,7]  
Output: 3
```

```text id="ex2"
Input: root = [1,null,2]  
Output: 2
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Tree:
    1
   / \
  2   3

Depth calculation:
left = 1
right = 1

Depth = 1 + max(1,1) = 2
```

---

### ✅ Key Points

* Uses **DFS recursion**
* Computes depth bottom-up
* Simple and efficient solution
* Works for all tree shapes

---

### ⚠️ Edge Cases

* Empty tree → depth = 0
* Single node → depth = 1
* Skewed tree → depth = n

---

### 🏁 Conclusion

This recursive DFS approach efficiently computes the maximum depth of a binary tree by exploring all paths and selecting the longest one, achieving optimal **O(n)** time complexity.


---


## 7️⃣ Path Sum (DFS / Recursion)

### 📌 Problem Statement

Given the root of a binary tree and an integer `targetSum`, determine if the tree has a **root-to-leaf path** such that adding up all the values along the path equals `targetSum`.

👉 A **root-to-leaf path** is a path starting from the root and ending at a leaf node (a node with no children).

---

### 🚀 Approach: Depth-First Search (DFS)

We use **DFS (recursion)** to explore all possible root-to-leaf paths:

* Traverse the tree while maintaining a running sum
* At each node, add its value to the current sum
* When a leaf node is reached, compare the sum with `targetSum`

---

### 🧠 Algorithm

1. Define a recursive function `dfs(node, curr_sum)`

2. Base case:

   * If `node` is `None` → return `False`

3. Update sum:

   * `curr_sum += node.val`

4. Check leaf node:

   * If `node.left` and `node.right` are `None`:

     * Return `curr_sum == targetSum`

5. Recursive calls:

   * Check left subtree OR right subtree

6. Initial call:

   * `dfs(root, 0)`

---

### 📊 Complexity Analysis

| Type             | Complexity                                   |
| ---------------- | -------------------------------------------- |
| Time Complexity  | O(n)                                         |
| Space Complexity | O(h) *(recursion stack, h = height of tree)* |

---

### 📎 Examples

```text id="ex1"
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22  
Output: True  
Explanation: Path 5 → 4 → 11 → 2 sums to 22
```

```text id="ex2"
Input: root = [1,2,3], targetSum = 5  
Output: False
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Path: 5 → 4 → 11 → 2  
Sum = 5 + 4 + 11 + 2 = 22 ✔️

Reached leaf → matches target → return True
```

---

### ✅ Key Points

* Uses **DFS traversal**
* Tracks **running sum** along the path
* Stops early when a valid path is found
* Only considers **root-to-leaf paths**

---

### ⚠️ Edge Cases

* Empty tree → return `False`
* Single node tree
* Negative values in tree
* Multiple valid paths

---

### 🏁 Conclusion

This DFS-based recursive approach efficiently checks whether a valid root-to-leaf path exists that matches the target sum. It explores all paths while maintaining optimal **O(n)** time complexity.


---


## 8️⃣ Minimum Depth of Binary Tree (DFS / Recursion)

### 📌 Problem Statement

Given the root of a binary tree, return its **minimum depth**.

👉 The **minimum depth** is the number of nodes along the shortest path from the root node down to the nearest **leaf node**.

> ⚠️ A leaf node is a node with **no left and no right child**.

---

### 🚀 Approach: Depth-First Search (DFS)

We use **DFS (recursion)** to compute the minimum depth:

* Traverse the tree recursively
* Carefully handle cases where one child is missing
* Only consider valid root-to-leaf paths

---

### 🧠 Algorithm

1. Define a recursive function `find(root)`

2. Base case:

   * If `root` is `None` → return `0`

3. If left child is missing:

   * Return `1 + find(root.right)`

4. If right child is missing:

   * Return `1 + find(root.left)`

5. If both children exist:

   * Return:

     ```
     1 + min(find(root.left), find(root.right))
     ```

---

### 📊 Complexity Analysis

| Type             | Complexity                                   |
| ---------------- | -------------------------------------------- |
| Time Complexity  | O(n)                                         |
| Space Complexity | O(h) *(recursion stack, h = height of tree)* |

---

### 📎 Examples

```text id="ex1"
Input: root = [3,9,20,null,null,15,7]  
Output: 2  
Explanation: The shortest path is 3 → 9
```

```text id="ex2"
Input: root = [2,null,3,null,4,null,5,null,6]  
Output: 5  
Explanation: Only one path exists
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Tree:
    1
   /
  2

Only left child exists:
minDepth = 1 + depth(left)
= 1 + 1 = 2
```

---

### ✅ Key Points

* Uses **DFS recursion**
* Handles **single-child nodes carefully**
* Avoids incorrect min calculation when one subtree is missing
* Ensures only **valid leaf paths** are considered

---

### ⚠️ Edge Cases

* Empty tree → depth = 0
* Single node → depth = 1
* Skewed tree → depth = n
* Nodes with only one child

---

### 🏁 Conclusion

This recursive DFS approach correctly computes the minimum depth by considering only valid root-to-leaf paths and carefully handling edge cases where nodes have a single child, achieving optimal **O(n)** time complexity.


---