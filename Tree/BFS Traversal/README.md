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


## 3️⃣ Binary Tree Zigzag Level Order Traversal (BFS)

### 📌 Problem Statement

Given the root of a binary tree, return its **zigzag level order traversal**.

👉 Zigzag traversal means:

* Level 1 → Left to Right
* Level 2 → Right to Left
* Level 3 → Left to Right
* … and so on

---

### 🚀 Approach: Breadth-First Search (BFS)

We use **level order traversal (BFS)** with a twist:

* Traverse the tree level by level using a queue
* Reverse the order of nodes for every alternate level

---

### 🧠 Algorithm

1. If `root` is `None` → return empty list

2. Initialize:

   * Queue `q` with root
   * Result list `res = []`
   * Level counter `count = 1`

3. While queue is not empty:

   * Create empty list `level`

4. Process current level:

   * Pop all nodes in queue
   * Append their values to `level`
   * Push their children into queue

5. If level is even (`count % 2 == 0`):

   * Reverse the level list

6. Increment level counter and append to result

7. Return `res`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(n)       |

---

### 📎 Examples

```text id="ex1"
Input: root = [3,9,20,null,null,15,7]  
Output: [[3],[20,9],[15,7]]
```

```text id="ex2"
Input: root = [1]  
Output: [[1]]
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Tree:
    3
   / \
  9   20
     /  \
    15   7

Level 1 → [3]        (L → R)
Level 2 → [9,20] → [20,9] (R → L)
Level 3 → [15,7]     (L → R)

Result → [[3],[20,9],[15,7]]
```

---

### ✅ Key Points

* Uses **BFS traversal**
* Alternates direction at each level
* Custom reverse function used for in-place reversal
* Clean level-by-level processing

---

### ⚠️ Edge Cases

* Empty tree → return `[]`
* Single node → `[[node]]`
* Skewed tree → behaves like normal level order

---

### 🏁 Conclusion

This BFS-based approach efficiently performs zigzag traversal by reversing alternate levels, maintaining optimal **O(n)** time complexity while keeping the implementation simple and intuitive.


---


## 4️⃣ Average of Levels in Binary Tree (BFS / Level Order Traversal)


### 📌 Problem Statement

Given the root of a binary tree, return the **average value of the nodes on each level** in the form of an array.

👉 Each level’s average should be calculated independently.

---

### 🚀 Approach: Breadth-First Search (BFS)

We use **level order traversal (BFS)** to process the tree level by level:

* Traverse each level using a queue
* Collect node values for that level
* Compute the average and store it

---

### 🧠 Algorithm

1. If `root` is `None` → return empty list

2. Initialize:

   * Queue with root node
   * Result list `res = []`

3. While queue is not empty:

   * Get number of nodes in current level `n`
   * Initialize empty list `level`

4. Process current level:

   * Pop nodes from queue
   * Add their values to `level`
   * Push their children into queue

5. Compute average:

   * `average = sum(level) / n`

6. Append average to result

7. Return `res`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(n)       |

---

### 📎 Examples

```text id="ex1"
Input: root = [3,9,20,null,null,15,7]  
Output: [3.0, 14.5, 11.0]
```

```text id="ex2"
Input: root = [1,2,3,4,5]  
Output: [1.0, 2.5, 4.5]
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Tree:
    3
   / \
  9   20
     /  \
    15   7

Level 1 → [3] → avg = 3.0  
Level 2 → [9,20] → avg = 14.5  
Level 3 → [15,7] → avg = 11.0  

Result → [3.0, 14.5, 11.0]
```

---

### ✅ Key Points

* Uses **BFS traversal**
* Processes nodes **level by level**
* Computes average using `sum / count`
* Straightforward and efficient

---

### ⚠️ Edge Cases

* Empty tree → return `[]`
* Single node → `[node.val]`
* Skewed tree → one node per level

---

### 🏁 Conclusion

This BFS-based approach efficiently computes the average of each level in a binary tree by processing nodes level-wise and calculating their mean, achieving optimal **O(n)** time complexity.


---


## 5️⃣ Minimum Depth of Binary Tree (BFS / Level Order Traversal)


### 📌 Problem Statement

Given the root of a binary tree, return its **minimum depth**.

👉 The **minimum depth** is the number of nodes along the shortest path from the root node down to the nearest **leaf node**.

> ⚠️ A leaf node is a node with **no left and no right children**.

---

### 🚀 Approach: Breadth-First Search (BFS)

We use **BFS (level order traversal)** because it naturally explores the tree level by level.

#### 💡 Key Idea:

* The **first leaf node** encountered during BFS gives the **minimum depth**
* No need to traverse the entire tree → early stopping

---

### 🧠 Algorithm

1. If `root` is `None` → return `0`

2. Initialize queue:

   * Store `(node, depth)` → starting with `(root, 1)`

3. While queue is not empty:

   * Pop `(node, depth)`

4. Check if it is a leaf node:

   * If yes → return `depth`

5. Otherwise:

   * Add left child with `depth + 1`
   * Add right child with `depth + 1`

---

### 📊 Complexity Analysis

| Type             | Complexity          |
| ---------------- | ------------------- |
| Time Complexity  | O(n) *(worst case)* |
| Space Complexity | O(n)                |

---

### 📎 Examples

```text id="ex1"
Input: root = [3,9,20,null,null,15,7]  
Output: 2  
Explanation: Shortest path is 3 → 9
```

```text id="ex2"
Input: root = [2,null,3,null,4,null,5,null,6]  
Output: 5
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Queue: [(1,1)]

Level 1:
(1,1) → not leaf → add children

Level 2:
(2,2) → leaf ✔️ → return 2
```

---

### ✅ Key Points

* Uses **BFS traversal**
* Stops at **first leaf node**
* More efficient than DFS for this problem
* No unnecessary traversal

---

### ⚠️ Edge Cases

* Empty tree → depth = 0
* Single node → depth = 1
* Skewed tree → depth = n

---

## 🏁 Conclusion

This BFS-based approach efficiently finds the minimum depth by exploring the tree level by level and stopping at the first leaf node, ensuring optimal performance with early termination.


---
