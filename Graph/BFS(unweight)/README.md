# Breadth-First Search (BFS)

Breadth-First Search (BFS) in unweighted graphs is a fundamental traversal technique used to explore nodes level by level, ensuring the shortest path (in terms of number of edges) from a source node to all other reachable nodes. By using a queue, BFS systematically visits all neighbors before moving to the next level, making it ideal for problems like shortest path, connectivity, and minimum transformations where edge weights are uniform. Its ability to guarantee optimal solutions in unweighted scenarios makes it a powerful and widely used approach in graph and grid-based problems.


## 1️⃣ Matrix – Distance to Nearest Zero

### 📌 Problem Statement

Given a binary matrix `mat` consisting of `0s` and `1s`, return a matrix where each cell contains the **distance to the nearest 0**.

👉 The distance between two adjacent cells is **1** (up, down, left, right).

---

### 🚀 Approach: Multi-Source BFS

#### 🔹 Key Idea

* Instead of running BFS from every `1`, we:
  ✅ Start BFS from **all 0s simultaneously**
  ✅ Treat all `0s` as **sources**

👉 This ensures the shortest distance is computed efficiently.

---

### 🧠 Algorithm

1. Initialize a queue

2. Traverse the matrix:

   * If cell = `0` → push into queue
   * If cell = `1` → mark as `∞`

3. Perform **BFS traversal**:

   * For each cell, explore 4 directions
   * Update neighbor if a shorter distance is found

4. Continue until queue is empty

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(m × n)   |
| Space Complexity | O(m × n)   |

👉 Each cell is processed at most once in BFS

---

### 📎 Example

```text id="example"
Input:
mat = [
  [0,0,0],
  [0,1,0],
  [1,1,1]
]

Output:
[
  [0,0,0],
  [0,1,0],
  [1,2,1]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Initial queue = all 0s

Step 1:
Update neighbors of 0 → distance = 1

Step 2:
Expand further → distance = 2

Final matrix:
Each cell stores shortest distance to nearest 0 ✔️
```

---

### ✅ Key Points

* Uses **Multi-source BFS** for optimal performance
* Avoids redundant BFS from each `1`
* Guarantees **shortest distance**
* Works efficiently for large grids

---

### ⚠️ Edge Cases

* Matrix with all `0s`
* Matrix with all `1s` (remains ∞ unless handled)
* Single row or column
* Large grid sizes

---

### 🏁 Conclusion

This problem is a classic example of **multi-source BFS**, where starting from all zero cells ensures that distances are computed optimally in a single traversal, achieving **O(m × n)** time complexity.


---


## 2️⃣ Word Ladder – Shortest Transformation Sequence

### 📌 Problem Statement

Given two words `beginWord` and `endWord`, and a dictionary `wordList`, return the **length of the shortest transformation sequence** from `beginWord` to `endWord`.

#### ✅ Rules:

* Only **one letter can be changed at a time**
* Each transformed word must exist in the `wordList`
* Return `0` if no such transformation is possible

---

### 🚀 Approach: BFS (Shortest Path in Unweighted Graph)

#### 🔹 Key Idea

* Treat each word as a **node**
* An edge exists if two words differ by **one letter**
* Use **Breadth-First Search (BFS)** to find the shortest path

👉 BFS guarantees the shortest transformation sequence.

---

### 🧠 Algorithm

1. Convert `wordList` into a **set** for fast lookup

2. If `endWord` not in set → return `0`

3. Initialize queue with `(beginWord, 1)`

4. For each word:

   * Try changing each character (`a → z`)
   * Generate new words
   * If new word == `endWord` → return `level + 1`
   * If valid → add to queue & remove from set

5. If BFS ends → return `0`

---

### 📊 Complexity Analysis

| Type             | Complexity    |
| ---------------- | ------------- |
| Time Complexity  | O(N × L × 26) |
| Space Complexity | O(N)          |

👉 Where:

* `N` = number of words
* `L` = length of each word

---

### 📎 Example

```text id="example"
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation:
hit → hot → dot → dog → cog
```

---

### 🔍 Dry Run

```text id="dryrun"
Start: ("hit", 1)

Level 2 → hot  
Level 3 → dot, lot  
Level 4 → dog, log  
Level 5 → cog ✔️

Answer = 5
```

---

### ✅ Key Points

* Uses **BFS for shortest path**
* Converts list → **set for O(1) lookup**
* Removes visited words to avoid cycles
* Efficient for large dictionaries

---

### ⚠️ Edge Cases

* `endWord` not in wordList → return 0
* No valid transformation path
* beginWord == endWord
* Large wordList

---

### 🏁 Conclusion

This problem models a **graph traversal scenario**, where BFS efficiently finds the shortest transformation path by exploring all possible one-letter variations level by level.


---