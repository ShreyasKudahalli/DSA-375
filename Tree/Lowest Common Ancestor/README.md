# Lowest Common Ancestors
**Lowest Common Ancestor (LCA)** is a fundamental concept in tree data structures that identifies the deepest node in a binary tree that has two given nodes as descendants. It plays a crucial role in hierarchical queries, path-related problems, and tree-based optimizations. The LCA helps efficiently determine relationships between nodes by tracing their ancestry, and it can be solved using various approaches such as Depth-First Search (DFS), parent mapping with Breadth-First Search (BFS), or optimized methods in Binary Search Trees (BSTs), making it a key technique in both theoretical and practical applications of trees.


## 1️⃣ All Nodes Distance K in Binary Tree (DFS + BFS)

### 📌 Problem Statement

Given the root of a binary tree, a target node, and an integer `k`, return all the values of the nodes that are **exactly distance `k` away** from the target node.

👉 Distance between two nodes is defined as the number of edges in the shortest path connecting them.

---

### 🚀 Approach: DFS + BFS

This problem is solved in **two phases**:

#### 🔹 Phase 1: DFS (Build Parent Map)

* Traverse the tree and store each node’s **parent**
* This allows upward traversal (not normally possible in trees)

#### 🔹 Phase 2: BFS (Level-wise Traversal from Target)

* Start BFS from the **target node**
* Traverse in all directions:

  * Left child
  * Right child
  * Parent
* Stop when distance `k` is reached

---

### 🧠 Algorithm

#### Step 1: Build Parent Mapping

* Use DFS to store:

  ```
  parent[node] = parent_node
  ```

#### Step 2: BFS from Target

1. Initialize:

   * Queue with target node
   * Visited set to avoid cycles
   * Distance counter `dist = 0`

2. While queue is not empty:

   * If `dist == k`:

     * Return all node values in queue

3. For each node:

   * Explore neighbors:

     * `node.left`
     * `node.right`
     * `parent[node]`

4. Add unvisited nodes to queue

5. Increment distance

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(n)       |

---

### 📎 Examples

```text id="ex1"
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2  
Output: [7,4,1]
```

```text id="ex2"
Input: root = [1], target = 1, k = 0  
Output: [1]
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Target = 5, k = 2

Level 0 → [5]  
Level 1 → [6,2,3]  
Level 2 → [7,4,1] ✔️

Return → [7,4,1]
```

---

### ✅ Key Points

* Combines **DFS (for parent mapping)** and **BFS (for distance traversal)**
* Treats tree like an **undirected graph**
* Uses **visited set** to prevent cycles
* Efficient level-based traversal

---

### ⚠️ Edge Cases

* `k = 0` → return `[target.val]`
* Single node tree
* Target at leaf node
* Large tree with deep levels

---

### 🏁 Conclusion

This hybrid DFS + BFS approach efficiently finds all nodes at distance `k` by enabling upward traversal through parent mapping and then performing a level-order traversal from the target, achieving optimal **O(n)** time complexity.

---


## 2️⃣ Lowest Common Ancestor (LCA) in Binary Tree (BFS + Parent Mapping)

### 📌 Problem Statement

Given the root of a binary tree and two nodes `p` and `q`, return their **Lowest Common Ancestor (LCA)**.

👉 The **LCA** of two nodes is the **lowest node in the tree** that has both `p` and `q` as descendants (a node can be a descendant of itself).

---

### 🚀 Approach: BFS + Parent Mapping

This approach works in **two phases**:

#### 🔹 Phase 1: BFS to Build Parent Map

* Traverse the tree using BFS
* Store each node’s **parent reference**
* Continue until both `p` and `q` are found

#### 🔹 Phase 2: Find Common Ancestor

* Trace all ancestors of node `p` and store them in a set
* Traverse ancestors of node `q`
* The first common node is the **LCA**

---

### 🧠 Algorithm

#### Step 1: Build Parent Map

1. Initialize:

   * `parent[root] = None`
   * Queue with root node

2. Perform BFS:

   * For each node:

     * Store parent of left child
     * Store parent of right child
   * Stop when both `p` and `q` are found

---

#### Step 2: Track Ancestors of `p`

* Traverse from `p` to root using parent map
* Store all visited nodes in a set

---

#### Step 3: Find LCA using `q`

* Traverse from `q` upwards
* First node found in `p`'s ancestor set → LCA

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(n)       |

---

### 📎 Examples

```text id="ex1"
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1  
Output: 3
```

```text id="ex2"
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4  
Output: 5
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Ancestors of p = 5:
{5, 3}

Traverse q = 1:
1 → parent = 3 ✔️ (found in set)

LCA = 3
```

---

### ✅ Key Points

* Uses **BFS** to build parent relationships
* Converts tree into a structure with **bidirectional traversal**
* Uses **set for fast ancestor lookup**
* Efficient and intuitive approach

---

### ⚠️ Edge Cases

* `p == q` → return `p`
* One node is ancestor of another
* Tree with only one node
* Skewed tree

---

### 🏁 Conclusion

This BFS + parent mapping approach efficiently finds the Lowest Common Ancestor by enabling upward traversal and leveraging set-based lookup, achieving optimal **O(n)** time complexity.


---
