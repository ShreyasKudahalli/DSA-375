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