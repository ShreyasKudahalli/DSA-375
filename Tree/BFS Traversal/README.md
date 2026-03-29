# Breadth-First Search (BFS)

Breadth-First Search (BFS) traversal is a fundamental tree and graph traversal technique that explores nodes level by level, starting from the root or source node and moving outward. It uses a queue (FIFO structure) to ensure that nodes are processed in the order they are discovered, making it ideal for problems involving shortest paths, level-wise processing, or nearest neighbor exploration. In trees, BFS is commonly used for level order traversal, where all nodes at a given depth are visited before moving to the next level, providing a clear and structured way to analyze hierarchical data.



## 1️⃣ Binary Tree Level Order Traversal 

### 📌 Problem Statement

Given the root of a binary tree, return its **level order traversal**.

👉 Level order traversal means visiting nodes **level by level from left to right**.

---

### 🚀 Approach: Breadth-First Search (BFS)

We use a **queue (FIFO)** to perform **BFS traversal**:

* Start from the root node
* Process nodes level by level
* For each level:

  * Traverse all nodes currently in the queue
  * Add their children to the queue

---

### 🧠 Algorithm

1. Initialize:

   * Result list `res = []`
   * Queue with root node

2. While queue is not empty:

   * Get current level size `n = len(queue)`
   * Create empty list `level`

3. Process all nodes in current level:

   * Pop node from queue
   * Add its value to `level`
   * Push left and right children (if exist)

4. Append `level` to result

5. Return `res`

---

### 📊 Complexity Analysis

| Type             | Complexity                      |
| ---------------- | ------------------------------- |
| Time Complexity  | O(n)                            |
| Space Complexity | O(n) *(queue + result storage)* |

---

### 📎 Examples

```text id="ex1"
Input: root = [3,9,20,null,null,15,7]  
Output: [[3],[9,20],[15,7]]
```

```text id="ex2"
Input: root = [1]  
Output: [[1]]
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Queue: [3]

Level 1:
Process → [3]
Queue → [9,20]

Level 2:
Process → [9,20]
Queue → [15,7]

Level 3:
Process → [15,7]

Result → [[3],[9,20],[15,7]]
```

---

### ✅ Key Points

* Uses **BFS traversal (queue)**
* Processes nodes **level by level**
* Maintains clear separation of each level
* Widely used pattern in tree problems

---

### ⚠️ Edge Cases

* Empty tree → return `[]`
* Single node → `[[node]]`
* Skewed tree → each level has one node

---

### 🏁 Conclusion

This BFS-based approach efficiently traverses the tree level by level using a queue, ensuring all nodes are processed in the correct order with optimal **O(n)** time complexity.

---


## 2️⃣ Binary Tree Right Side View 

### 📌 Problem Statement

Given the root of a binary tree, return the values of the nodes that are **visible from the right side**.

👉 From each level of the tree, only the **rightmost node** is visible.

---

### 🚀 Approach: Breadth-First Search (BFS)

We use **level order traversal (BFS)** to process the tree level by level.

#### 💡 Key Idea:

* For each level, capture the **last node**
* That node represents the **rightmost view** of that level

---

### 🧠 Algorithm

1. If `root` is `None` → return empty list

2. Initialize:

   * Queue with root node
   * Result list `res = []`

3. While queue is not empty:

   * For each level:

     * Traverse all nodes in the current level
     * Store their values in a list `level`

4. Append:

   * The last element of `level` → `level[-1]` to result

5. Return `res`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(n)       |

---

### 📎 Examples

```text id="ex1"
Input: root = [1,2,3,null,5,null,4]  
Output: [1,3,4]
```

```text id="ex2"
Input: root = [1,null,3]  
Output: [1,3]
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Tree:
    1
   / \
  2   3
   \   \
    5   4

Levels:
[1] → take 1  
[2,3] → take 3  
[5,4] → take 4  

Result → [1,3,4]
```

---

### ✅ Key Points

* Uses **BFS (level order traversal)**
* Extracts **last node of each level**
* Simple and intuitive solution
* Works for all tree structures

---

### ⚠️ Edge Cases

* Empty tree → return `[]`
* Single node → `[node]`
* Skewed tree → all nodes visible

---

### 🏁 Conclusion

This BFS-based approach efficiently captures the right side view of a binary tree by processing each level and selecting the last node, achieving optimal **O(n)** time complexity.


---