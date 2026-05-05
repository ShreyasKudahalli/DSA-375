# Constraint-based backtracking

Constraint-based backtracking is a refined form of recursion where solutions are built step by step while strictly enforcing given constraints at every stage. Instead of exploring all possibilities blindly, it prunes invalid paths early by checking conditions (such as validity, limits, or rules) before proceeding further. This approach significantly reduces the search space and is widely used in problems like generating valid parentheses, solving Sudoku, graph coloring, and combinatorial configurations where only feasible solutions are explored.



## 1️⃣ Graph Coloring (M-Coloring Problem) – Backtracking

### 📌 Problem Statement

You are given:

* `v` → number of vertices
* `edges` → list of undirected edges
* `m` → number of available colors

👉 Determine whether it is possible to **color the graph using at most `m` colors** such that:

#### 🎯 Constraint:

* No two **adjacent vertices** share the same color

---

### 🚀 Approach: Backtracking

#### 🔹 Key Idea

* Assign colors to vertices one by one
* Try all possible colors (1 to `m`)
* Check if the current color assignment is valid

👉 If invalid → backtrack

---

### 🧠 Algorithm

1. Build adjacency list from edges

2. Initialize:

   * `color[]` array to store assigned colors

3. For each node:

   * Try all colors from `1 → m`
   * Check if safe using `possible()`

4. If safe:

   * Assign color
   * Recurse for next node

5. If no color works:

   * Backtrack

6. If all nodes are colored:

   * Return `True`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(m^v)     |
| Space Complexity | O(v)       |

---

### 📎 Example

```text id="example"
Input:
v = 4
edges = [[0,1],[1,2],[2,3],[3,0]]
m = 3

Output:
True
```

---

### 🔍 Dry Run

```text id="dryrun"
Node 0 → Color 1 ✔️  
Node 1 → Color 2 ✔️  
Node 2 → Color 1 ✔️  
Node 3 → Color 2 ✔️  

All nodes colored successfully ✔️
```

---

### 🌳 Recursion Tree (Simplified)

```text id="tree"
        Node0
     /    |    \
   C1    C2    C3
   |
 Node1
   ...
```

---

### ✅ Key Points

* Classic **constraint satisfaction problem**
* Uses **backtracking + pruning**
* Checks adjacency before assignment
* Stops early if solution found

---

### ⚠️ Edge Cases

* `m = 1` → only works for no edges
* Fully connected graph → needs `v` colors
* Disconnected graph → handle separately
* No valid coloring → return `False`

---

### 🏁 Conclusion

The M-Coloring problem demonstrates how backtracking can be used to solve constraint-based graph problems by exploring all possibilities while pruning invalid color assignments.

---


## 2️⃣ Knight's Tour

### 📌 Problem Statement

You are given:

* `KnightPos` → starting position of the knight
* `TargetPos` → destination position
* `N` → size of the chessboard (N × N)

👉 Find the **minimum number of steps** required for a knight to reach the target

---

### ♟️ Knight Movement Rules

A knight moves in **L-shape**:

* 2 steps in one direction + 1 step perpendicular

#### 🔄 Possible Moves (8 directions):

```text
(-2, +1), (+2, -1), (-2, -1), (+2, +1)
(-1, +2), (+1, -2), (-1, -2), (+1, +2)
```

---

### 🚀 Approach: Breadth-First Search (BFS)

#### 🔹 Key Idea

* Treat the board as a **graph**
* Each cell is a node
* Each valid knight move is an edge

👉 Use BFS to find the **shortest path in an unweighted graph**

---

### 🧠 Algorithm

1. Convert positions to **0-based indexing**

2. Initialize:

   * `visited` matrix
   * queue storing `(x, y, steps)`

3. Push starting position into queue

4. While queue is not empty:

   * Pop current position
   * If target reached → return steps
   * Explore all 8 possible moves
   * If valid and unvisited → push to queue

5. If target not reachable → return `-1`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(N²)      |
| Space Complexity | O(N²)      |

---

### 📎 Example

```text id="example"
Input:
KnightPos = [4,5]
TargetPos = [1,1]
N = 6

Output:
3
```

---

### 🔍 Dry Run

```text id="dryrun"
Start: (4,5)

Level 1 → all possible moves  
Level 2 → expand further  
Level 3 → reach target ✔️  

Answer = 3
```

---

### 🌐 Visualization

```text id="grid"
Board (6x6):
K → Start
T → Target

Moves expand layer by layer (BFS)
```

---

### ✅ Key Points

* Classic **shortest path in unweighted graph**
* BFS guarantees **minimum steps**
* Uses **visited matrix to avoid cycles**
* Works for any board size

---

### ⚠️ Edge Cases

* Start = Target → 0 steps
* Small board (N = 1)
* Target unreachable (rare but handled)

---

### 🏁 Conclusion

This problem demonstrates how BFS can be effectively applied to grid-based movement problems to compute the shortest path with uniform edge weights.


---


## 3️⃣ N-Queens – Backtracking with Constraints

### 📌 Problem Statement

You are given:

* `n` → size of the chessboard (n × n)

👉 Place `n` queens on the board such that:

#### 🎯 Constraints:

* No two queens attack each other
* A queen can attack:

  * Same **row**
  * Same **column**
  * Same **diagonal**

👉 Return **all valid board configurations**

---

### 🚀 Approach: Constraint-Based Backtracking

#### 🔹 Key Idea

* Place one queen per row
* Try all columns in that row
* Ensure no conflicts using:

  * `cols` → occupied columns
  * `diag1 (r - c)` → main diagonal
  * `diag2 (r + c)` → anti-diagonal

👉 Skip invalid placements early (pruning)

---

### 🧠 Algorithm

1. Initialize:

   * Empty board filled with `'.'`
   * Sets for columns and diagonals

2. For each row:

   * Try placing queen in every column

3. Check:

   * Column not used
   * Diagonals not occupied

4. If valid:

   * Place queen
   * Mark sets
   * Recurse to next row

5. Backtrack:

   * Remove queen
   * Unmark sets

6. If all rows filled:

   * Store solution

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(N!)      |
| Space Complexity | O(N)       |

---

### 📎 Example

```text id="example"
Input:
n = 4

Output:
[
 [".Q..",
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",
  "Q...",
  "...Q",
  ".Q.."]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Row 0 → Place Q at column 1  
Row 1 → Place Q at column 3  
Row 2 → Place Q at column 0  
Row 3 → Place Q at column 2  

Valid configuration ✔️
```

---

### 🌳 Recursion Tree (Simplified)

```text id="tree"
Row0
 ├── Col0 ❌
 ├── Col1 ✔️
 │    ├── Row1 choices...
 │
 ├── Col2 ✔️
 └── Col3 ✔️
```

---

### ✅ Key Points

* Classic **constraint-based backtracking problem**
* Uses **sets for O(1) conflict checking**
* Efficient pruning reduces search space
* One queen per row strategy

---

### ⚠️ Edge Cases

* `n = 1` → `[["Q"]]`
* `n = 2 or 3` → no solution
* Larger `n` → exponential growth

---

### 🏁 Conclusion

The N-Queens problem is a classic example of constraint-based backtracking, where invalid configurations are pruned early, allowing efficient exploration of valid solutions.


---