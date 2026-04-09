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


## 3️⃣ Clone Graph – Deep Copy of an Undirected Graph

### 📌 Problem Statement

Given a reference node of a **connected undirected graph**, return a **deep copy (clone)** of the graph.

👉 Each node contains:

* `val` → node value
* `neighbors` → list of adjacent nodes

---

### 🚀 Approach: BFS + HashMap

#### 🔹 Key Idea

* Use **Breadth-First Search (BFS)** to traverse the graph
* Maintain a **mapping** from original nodes → cloned nodes

👉 This ensures:

* Each node is cloned exactly once
* Graph structure is preserved

---

### 🧠 Algorithm

1. Handle edge case:

   * If input node is `None` → return `None`

2. Initialize:

   * Queue for BFS
   * Dictionary `old_to_new` to store mappings

3. Start BFS:

   * Clone the starting node
   * Push it into queue

4. For each node:

   * Traverse neighbors
   * If neighbor not cloned:

     * Clone it
     * Add to queue
   * Link cloned neighbors

5. Return cloned starting node

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(V + E)   |
| Space Complexity | O(V)       |

👉 `V` = number of nodes
👉 `E` = number of edges

---

### 📎 Example

```text id="example"
Input Graph:
1 -- 2
|    |
4 -- 3

Output:
Cloned graph with same structure
```

---

### 🔍 Dry Run

```text id="dryrun"
Start at node 1

Clone 1 → push to queue  
Visit neighbors 2, 4 → clone & store  

Continue BFS:
2 → clone 3  
4 → connect nodes  

Final:
All nodes cloned and properly linked ✔️
```

---

### ✅ Key Points

* Uses **BFS traversal**
* Maintains **mapping to avoid duplicates**
* Ensures **deep copy (no shared references)**
* Works for cyclic graphs

---

### ⚠️ Edge Cases

* Empty graph (`node = None`)
* Single node graph
* Graph with cycles
* Fully connected graph

---

### 🏁 Conclusion

This BFS-based approach efficiently clones a graph by traversing level-by-level and maintaining a mapping between original and cloned nodes, ensuring correctness and optimal performance.


---


## 4️⃣ Rotting Oranges – Minimum Time to Rot All

### 📌 Problem Statement

You are given an `n x m` grid where:

* `0` → Empty cell
* `1` → Fresh orange 🍊
* `2` → Rotten orange 🦠

👉 Every minute, any fresh orange adjacent (up, down, left, right) to a rotten orange becomes rotten.

### 🎯 Goal:

Return the **minimum time required** to rot all oranges.
If impossible → return `-1`

---

### 🚀 Approach: Multi-Source BFS

#### 🔹 Key Idea

* All rotten oranges act as **sources of infection**
* Spread happens **level by level (minute by minute)**

👉 Use **BFS** starting from all rotten oranges simultaneously

---

### 🧠 Algorithm

1. Initialize:

   * Queue → store `(row, col, time)`
   * Count fresh oranges

2. Traverse grid:

   * Add all rotten oranges to queue
   * Count fresh oranges

3. Perform BFS:

   * For each rotten orange:

     * Infect adjacent fresh oranges
     * Reduce fresh count
     * Add to queue with `time + 1`

4. After BFS:

   * If fresh oranges remain → return `-1`
   * Else → return total time

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n × m)   |
| Space Complexity | O(n × m)   |

👉 Each cell is processed at most once

---

### 📎 Example

```text id="example"
Input:
grid = [
  [2,1,1],
  [1,1,0],
  [0,1,1]
]

Output: 4
```

---

### 🔍 Dry Run

```text id="dryrun"
Minute 0 → Initial rotten oranges  
Minute 1 → Adjacent fresh become rotten  
Minute 2 → Spread continues  
Minute 3 → More infections  
Minute 4 → All oranges rotten ✔️

Final Answer = 4
```

---

### ✅ Key Points

* Uses **Multi-source BFS**
* Processes grid **level by level (time-based)**
* Efficiently simulates spread
* Avoids repeated traversal

---

### ⚠️ Edge Cases

* No fresh oranges → return `0`
* No rotten oranges but fresh exist → return `-1`
* All cells empty
* Single cell grid

---

### 🏁 Conclusion

This problem is a classic example of **BFS on grids**, where multiple sources propagate simultaneously. The approach ensures the minimum time is calculated efficiently in **O(n × m)**.


---


## 5️⃣ Shortest Path in Binary Matrix (8-Directional BFS)

### 📌 Problem Statement

Given an `n x n` binary matrix `grid`:

* `0` → Open cell (can move)
* `1` → Blocked cell (cannot move)

👉 Find the **shortest path** from the **top-left (0,0)** to the **bottom-right (n-1,n-1)**.

#### ✅ Rules:

* You can move in **8 directions**:

  * Up, Down, Left, Right
  * Diagonals (↖ ↗ ↘ ↙)
* Return the **length of the shortest path**
* If no path exists → return `-1`

---

### 🚀 Approach: BFS (Shortest Path in Grid)

#### 🔹 Key Idea

* Treat each cell as a **node**
* Use **Breadth-First Search (BFS)** to explore shortest paths
* BFS guarantees the **minimum distance** in unweighted grids

---

### 🧠 Algorithm

1. Check edge cases:

   * If start or end is blocked → return `-1`

2. Initialize:

   * Queue → `(row, col, path_length)`
   * Visited set → to avoid revisiting

3. Perform BFS:

   * Pop current cell
   * If destination reached → return length
   * Explore all 8 directions
   * Add valid, unvisited cells to queue

4. If BFS समाप्त without reaching target → return `-1`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n²)      |
| Space Complexity | O(n²)      |

👉 Each cell is visited at most once

---

### 📎 Example

```text id="example"
Input:
grid = [
  [0,1],
  [1,0]
]

Output: 2

Explanation:
(0,0) → (1,1) via diagonal ✔️
```

---

### 🔍 Dry Run

```text id="dryrun"
Start at (0,0)

Step 1:
Explore all 8 directions

Step 2:
Reach (1,1)

Path length = 2 ✔️
```

---

### ✅ Key Points

* Uses **BFS for shortest path**
* Supports **8-directional movement**
* Maintains **visited set to prevent cycles**
* Efficient for grid-based problems

---

### ⚠️ Edge Cases

* Start or end blocked → return `-1`
* Single cell grid
* No valid path
* Fully blocked grid

---

### 🏁 Conclusion

This problem is a classic BFS application where exploring all possible directions ensures finding the shortest path in an unweighted grid. The approach guarantees optimal results with **O(n²)** complexity.


---


## 6️⃣ Walls and Gates – Distance to Nearest Gate

### 📌 Problem Statement

You are given a 2D grid `a` of size `n x m` representing:

* `0` → Gate 🚪
* `-1` → Wall 🧱
* `INF` (large value) → Empty room

👉 Fill each empty room with the **distance to its nearest gate**.
If it is impossible to reach a gate, keep it as `INF`.

---

### 🚀 Approach: Multi-Source BFS

#### 🔹 Key Idea

* All gates (`0`) act as **starting points**
* Spread distance **simultaneously** from all gates

👉 This guarantees the **shortest distance** for each room

---

### 🧠 Algorithm

1. Initialize queue:

   * Add all gate positions `(i, j, 0)`

2. Perform BFS:

   * For each cell:

     * Explore 4 directions (up, down, left, right)
     * If neighbor is a valid empty room:

       * Update distance if smaller
       * Push into queue with `length + 1`

3. Continue until queue is empty

4. Return updated grid

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n × m)   |
| Space Complexity | O(n × m)   |

👉 Each cell is processed at most once

---

### 📎 Example

```text id="example"
Input:
[
  [INF, -1,  0, INF],
  [INF, INF, INF, -1],
  [INF, -1, INF, -1],
  [0,   -1, INF, INF]
]

Output:
[
  [3, -1, 0, 1],
  [2,  2, 1, -1],
  [1, -1, 2, -1],
  [0, -1, 3, 4]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Step 1:
Push all gates into queue

Step 2:
Expand outward level by level

Step 3:
Update nearest distances

Final:
Each room gets shortest distance to gate ✔️
```

---

### ✅ Key Points

* Uses **Multi-source BFS**
* Computes shortest distance efficiently
* Avoids redundant traversal
* Works perfectly for grid-based shortest path problems

---

### ⚠️ Edge Cases

* No gates present → all remain INF
* All walls
* Single cell grid
* Large grid sizes

---

### 🏁 Conclusion

This problem is a classic **multi-source BFS** application where starting from all gates ensures optimal distance computation for all rooms in a single traversal with **O(n × m)** complexity.


---