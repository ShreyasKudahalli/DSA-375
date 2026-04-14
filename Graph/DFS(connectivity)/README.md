# Depth-First Search (DFS) connectivity
Depth-First Search (DFS) for connectivity is a fundamental technique used to explore and identify connected components in graphs and grids by traversing as deep as possible along each branch before backtracking. Starting from a node or cell, DFS recursively visits all reachable neighbors, effectively marking an entire connected region. This approach is widely used in problems like island counting, flood fill, and graph connectivity checks, where the goal is to determine whether elements belong to the same group. Its simplicity and effectiveness make it a core method for solving connectivity-related problems in both graphs and matrices.


## 1️⃣ Number of Islands – Count Connected Components

### 📌 Problem Statement

Given a 2D grid of size `m x n`:

* `"1"` → Land 🌍
* `"0"` → Water 🌊

👉 Count the number of **islands**.

#### ✅ Definition:

An island is formed by connecting adjacent lands **horizontally or vertically** (not diagonally).

---

### 🚀 Approach: DFS (Flood Fill)

#### 🔹 Key Idea

* Treat the grid as a graph
* Each `"1"` is part of an island
* Use **DFS** to mark all connected land as visited

👉 Every time we find a new `"1"`, it represents a **new island**

---

### 🧠 Algorithm

1. Initialize `count = 0`

2. Traverse each cell in the grid:

   * If cell is `"1"`:

     * Increment island count
     * Run DFS to mark entire island as `"0"`

3. DFS (mark function):

   * If current cell is valid and `"1"`:

     * Mark it as `"0"` (visited)
     * Recursively visit all 4 directions

4. Return total island count

---

### 📊 Complexity Analysis

| Type             | Complexity                   |
| ---------------- | ---------------------------- |
| Time Complexity  | O(m × n)                     |
| Space Complexity | O(m × n) *(recursion stack)* |

👉 Each cell is visited at most once

---

### 📎 Example

```text id="example"
Input:
grid = [
  ["1","1","0","0"],
  ["1","1","0","0"],
  ["0","0","1","0"],
  ["0","0","0","1"]
]

Output: 3
```

---

### 🔍 Dry Run

```text id="dryrun"
Step 1:
Find first "1" → DFS marks entire island

Step 2:
Find next unvisited "1" → new island

Step 3:
Repeat until grid fully traversed

Total islands = 3 ✔️
```

---

### ✅ Key Points

* Uses **DFS (Flood Fill technique)**
* Marks visited land to avoid revisiting
* Counts connected components
* Works efficiently for grid traversal

---

### ⚠️ Edge Cases

* Empty grid
* All water (`0`) → result = 0
* All land (`1`) → result = 1
* Single cell grid

---

### 🏁 Conclusion

This problem is a classic example of **connected component detection** in a grid using DFS. By marking visited land, we efficiently count islands in **O(m × n)** time.


---


## 2️⃣ Flood Fill – Change Connected Region Color

### 📌 Problem Statement

Given a 2D grid `image` representing pixel values:

* Each cell contains a **color value**
* Starting from a pixel `(sr, sc)`, change its color and all **connected pixels (4-directionally)** with the same original color to a new `color`

👉 Return the modified image

---

### 🚀 Approach: DFS (Flood Fill Algorithm)

#### 🔹 Key Idea

* Treat the grid as a graph
* Start from `(sr, sc)`
* Use **DFS** to traverse all connected pixels with the same color

👉 Replace them with the new color

---

### 🧠 Algorithm

1. Store the **initial color** (`start = image[sr][sc]`)

2. If `start == color` → return image (no change needed)

3. Perform DFS:

   * If current cell is valid and matches `start`:

     * Change its color
     * Recurse in 4 directions

4. Return updated image

---

### 📊 Complexity Analysis

| Type             | Complexity                   |
| ---------------- | ---------------------------- |
| Time Complexity  | O(m × n)                     |
| Space Complexity | O(m × n) *(recursion stack)* |

👉 Each cell is visited at most once

---

### 📎 Example

```text id="example"
Input:
image = [
  [1,1,1],
  [1,1,0],
  [1,0,1]
]
sr = 1, sc = 1, color = 2

Output:
[
  [2,2,2],
  [2,2,0],
  [2,0,1]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Start at (1,1) → color = 1

Step 1:
Change (1,1) → 2

Step 2:
Expand to neighbors with same color

Step 3:
Repeat until region is filled

Final:
All connected 1s → 2 ✔️
```

---

### ✅ Key Points

* Uses **DFS (Flood Fill technique)**
* Avoids unnecessary work if color is same
* Traverses only connected region
* Efficient and simple approach

---

### ⚠️ Edge Cases

* Starting pixel already has target color
* Single cell image
* No connected neighbors
* Entire image same color

---

### 🏁 Conclusion

Flood Fill is a classic DFS problem used in image processing and region-based traversal. This approach efficiently updates all connected pixels in **O(m × n)** time.


---


## 3️⃣ All Paths from Source to Target (DFS + Backtracking)

### 📌 Problem Statement

Given a **Directed Acyclic Graph (DAG)** represented as an adjacency list `graph`, where:

* `graph[i]` contains all nodes you can visit from node `i`

👉 Find **all possible paths** from **node `0` (source)** to **node `n-1` (target)**.

---

### 🚀 Approach: DFS + Backtracking

#### 🔹 Key Idea

* Use **Depth-First Search (DFS)** to explore all possible paths
* Use **backtracking** to build paths step by step

👉 Since the graph is a DAG, no cycles → safe traversal

---

### 🧠 Algorithm

1. Initialize:

   * `result` → stores all valid paths

2. Start DFS from node `0`:

   * Maintain current path

3. At each node:

   * If node == target (`n-1`):

     * Add path to result
     * Return

4. For each neighbor:

   * Add neighbor to path
   * Recurse
   * Backtrack (remove last node)

5. Return all collected paths

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(2^n × n) |
| Space Complexity | O(n)       |

👉 Worst case: exponential number of paths
👉 Path copying takes `O(n)`

---

### 📎 Example

```text id="example"
Input:
graph = [[1,2], [3], [3], []]

Output:
[
  [0,1,3],
  [0,2,3]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Start: [0]

Path → 0 → 1 → 3 ✔️  
Path → 0 → 2 → 3 ✔️  

All paths collected
```

---

### ✅ Key Points

* Uses **DFS for path exploration**
* Backtracking ensures correct path formation
* Works efficiently for DAGs (no cycles)
* Collects **all possible valid paths**

---

### ⚠️ Edge Cases

* Single node graph
* No path to target
* Large DAG (many paths)
* Linear graph

---

### 🏁 Conclusion

This DFS + backtracking approach systematically explores all possible paths from source to target, ensuring correctness while handling exponential path combinations efficiently.


---


## 4️⃣ Surrounded Regions – Capture Regions in Board

### 📌 Problem Statement

You are given an `m x n` board containing:

* `'X'` → Blocked cell
* `'O'` → Open cell

👉 Capture all regions surrounded by `'X'` by flipping `'O'` → `'X'`.

#### ✅ Rule:

* An `'O'` is **NOT captured** if it is:

  * On the boundary, OR
  * Connected to a boundary `'O'`

---

### 🚀 Approach: DFS (Boundary Traversal)

#### 🔹 Key Idea

* Instead of finding surrounded regions directly:
  👉 Find **safe regions** (connected to boundary)

* Mark boundary-connected `'O'` as temporary `'T'`

* Convert:

  * Remaining `'O'` → `'X'` (captured)
  * `'T'` → `'O'` (restore safe cells)

---

### 🧠 Algorithm

1. Traverse boundary cells:

   * If cell is `'O'` → run DFS and mark as `'T'`

2. DFS (mark function):

   * Mark current `'O'` → `'T'`
   * Visit all 4 directions

3. Traverse entire board:

   * `'O'` → `'X'` (captured)
   * `'T'` → `'O'` (restore safe region)

---

### 📊 Complexity Analysis

| Type             | Complexity                   |
| ---------------- | ---------------------------- |
| Time Complexity  | O(m × n)                     |
| Space Complexity | O(m × n) *(recursion stack)* |

👉 Each cell is visited at most once

---

### 📎 Example

```text id="example"
Input:
[
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]

Output:
[
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Step 1:
Mark boundary-connected 'O' → 'T'

Step 2:
Convert inner 'O' → 'X'

Step 3:
Restore 'T' → 'O'

Final board ready ✔️
```

---

### ✅ Key Points

* Uses **DFS to mark safe regions**
* Boundary traversal is crucial
* Avoids unnecessary checks
* Efficient and optimal solution

---

### ⚠️ Edge Cases

* All cells are `'O'`
* No `'O'` present
* Single row or column
* Large grid

---

### 🏁 Conclusion

This problem demonstrates a clever use of DFS by focusing on **boundary-connected regions**, allowing us to efficiently identify and capture only truly surrounded areas in **O(m × n)** time.


---


## 5️⃣ Eventual Safe Nodes – Detect Safe States in Graph

### 📌 Problem Statement

You are given a **directed graph** where:

* `graph[i]` contains all nodes reachable from node `i`

👉 A node is called **safe** if **all possible paths starting from it eventually lead to a terminal node** (a node with no outgoing edges).

#### 🎯 Goal:

Return all **eventual safe nodes** in **sorted order**

---

### 🚀 Approach: DFS + Cycle Detection

#### 🔹 Key Idea

* Unsafe nodes are part of **cycles** or lead to cycles
* Safe nodes eventually reach a **terminal node**

👉 Use DFS to detect cycles and classify nodes

---

### 🧠 State Definition

We maintain a `state` array:

* `0` → Unvisited
* `1` → Visiting (currently in recursion → cycle detection)
* `2` → Safe (processed, no cycle found)

---

### 🧠 Algorithm

1. For each node:

   * Run DFS

2. In DFS:

   * If node is `1` → cycle detected → return False
   * If node is `2` → already safe → return True

3. Mark node as `1` (visiting)

4. Visit all neighbors:

   * If any neighbor is unsafe → current node is unsafe

5. If all neighbors are safe:

   * Mark node as `2` (safe)

6. Collect all safe nodes

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(V + E)   |
| Space Complexity | O(V)       |

👉 `V` = nodes, `E` = edges

---

### 📎 Example

```text id="example"
Input:
graph = [[1,2],[2,3],[5],[0],[5],[],[]]

Output:
[2,4,5,6]
```

---

### 🔍 Dry Run

```text id="dryrun"
Node 0 → leads to cycle → unsafe  
Node 1 → leads to cycle → unsafe  
Node 2 → leads to terminal → safe  
Node 5 → terminal → safe  

Final safe nodes = [2,4,5,6] ✔️
```

---

### ✅ Key Points

* Uses **DFS with cycle detection**
* Efficiently avoids recomputation using states
* Identifies nodes that do not lead to cycles
* Works well for directed graphs

---

### ⚠️ Edge Cases

* Graph with no edges
* All nodes part of cycle
* Single node graph
* Fully disconnected graph

---

### 🏁 Conclusion

This problem is a classic application of **DFS with cycle detection**, where identifying cycles helps determine unsafe nodes. By marking safe nodes, we efficiently compute all eventual safe states in linear time.

---


## 6️⃣ Count Complete Components in an Undirected Graph

### 📌 Problem Statement

You are given:

* An integer `n` → number of nodes (0 to n-1)
* A list of edges representing an **undirected graph**

👉 A **connected component** is called **complete** if:

* Every pair of distinct nodes in the component is connected by an edge

#### 🎯 Goal:

Return the **number of complete connected components**

---

### 🚀 Approach: DFS + Graph Properties

#### 🔹 Key Idea

* Traverse each connected component using **DFS**
* Count:

  * Number of **nodes** in the component
  * Number of **edges** in the component

👉 A component is **complete** if:

[
\text{edges} = \frac{n \times (n - 1)}{2}
]

---

### 🧠 Algorithm

1. Build adjacency list from edges

2. Maintain a `visited` array

3. For each unvisited node:

   * Run DFS to explore component
   * Count:

     * `nodes`
     * `edges` (sum of degrees ÷ 2)

4. Check:

   * If `edges == nodes * (nodes - 1) // 2`
     → it's a complete component

5. Count such components

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(V + E)   |
| Space Complexity | O(V + E)   |

👉 `V` = nodes, `E` = edges

---

### 📎 Example

```text id="example"
Input:
n = 6
edges = [[0,1],[0,2],[1,2],[3,4]]

Output: 3

Explanation:
Component 1: {0,1,2} → complete ✔️  
Component 2: {3,4} → complete ✔️  
Component 3: {5} → complete ✔️  
```

---

### 🔍 Dry Run

```text id="dryrun"
Component 1:
Nodes = 3, Edges = 3 → complete

Component 2:
Nodes = 2, Edges = 1 → complete

Component 3:
Nodes = 1, Edges = 0 → complete

Total = 3 ✔️
```

---

### ✅ Key Points

* Uses **DFS for connected components**
* Leverages **complete graph formula**
* Counts edges carefully (divide by 2)
* Works efficiently for large graphs

---

### ⚠️ Edge Cases

* No edges → all nodes are individual components
* Fully connected graph
* Disconnected graph
* Single node

---

### 🏁 Conclusion

This problem combines **graph traversal (DFS)** with a mathematical property of **complete graphs** to efficiently count valid components in **O(V + E)** time.

---


## 7️⃣ Is Graph Bipartite

### 📌 Problem Statement

You are given an undirected graph `graph`, where:

* `graph[i]` contains all nodes connected to node `i`

👉 Determine whether the graph is **bipartite**.

#### ✅ Definition:

A graph is **bipartite** if its nodes can be divided into **two groups** such that:

* No two adjacent nodes are in the same group

---

### 🚀 Approach: DFS + Graph Coloring

#### 🔹 Key Idea

* Try to color the graph using **2 colors (0 and 1)**
* Adjacent nodes must have **different colors**
* If a conflict occurs → graph is not bipartite

---

### 🧠 Algorithm

1. Initialize:

   * `group[] = -1` → uncolored nodes

2. For each unvisited node:

   * Start DFS with color `0`

3. In DFS:

   * Assign current node a color
   * Visit all neighbors:

     * If uncolored → assign opposite color
     * If same color → return `False`

4. If all components are valid → return `True`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(V + E)   |
| Space Complexity | O(V)       |

👉 `V` = nodes, `E` = edges

---

### 📎 Example

```text id="example"
Input:
graph = [[1,3],[0,2],[1,3],[0,2]]

Output: true

Explanation:
Group 0: {0,2}
Group 1: {1,3} ✔️
```

---

### 🔍 Dry Run

```text id="dryrun"
Start node 0 → color 0  
→ neighbors get color 1  
→ propagate coloring  

No conflicts found → bipartite ✔️
```

---

### ✅ Key Points

* Uses **DFS graph coloring**
* Ensures adjacent nodes have opposite colors
* Handles disconnected graphs
* Detects odd-length cycles

---

### ⚠️ Edge Cases

* Empty graph
* Single node graph
* Graph with self-loop → not bipartite
* Disconnected components

---

### 🏁 Conclusion

This problem uses **DFS-based 2-coloring** to determine whether a graph can be split into two independent sets, efficiently detecting conflicts in **O(V + E)** time.

---