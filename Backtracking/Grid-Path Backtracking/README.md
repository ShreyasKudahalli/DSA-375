# Grid-path backtracking

Grid-path backtracking is a recursive exploration technique used to find valid paths in matrix or grid-based problems by moving step by step through allowed directions while respecting constraints such as boundaries, obstacles, or visited cells. At each position, the algorithm explores all possible moves, marks the current path, and backtracks when a path becomes invalid or fully explored. This approach is widely used in maze solving, path generation, word search, and traversal problems where multiple routes must be explored systematically.



## 1️⃣ Rat in a Maze – Backtracking Approach

### 📌 Problem Statement

You are given:

* `maze` → an `N × N` binary matrix

Where:

* `1` → open path
* `0` → blocked cell

👉 A rat starts from the **top-left cell `(0,0)`** and must reach the **bottom-right cell `(N-1,N-1)`**

---

### 🎯 Goal

Return **all possible paths** the rat can take.

#### Allowed Moves:

* `D` → Down
* `L` → Left
* `R` → Right
* `U` → Up

#### Constraints:

* Rat can only move through cells with value `1`
* Cannot revisit the same cell in a single path

---

### 🚀 Approach: Backtracking + DFS

#### 🔹 Key Idea

* Explore all possible directions recursively
* Mark visited cells to avoid cycles
* Backtrack after exploring each path

👉 If destination is reached:

* Store the generated path string

---

### 🧠 Algorithm

1. Check if starting cell is blocked:

   * If `maze[0][0] == 0` → return empty result

2. Use DFS/Backtracking:

   * Try all 4 directions:

     * Down
     * Left
     * Right
     * Up

3. Conditions for valid move:

   * Inside grid bounds
   * Cell value is `1`
   * Not visited

4. Mark current cell visited before recursion

5. Backtrack:

   * Unmark visited cell after recursion

6. If destination reached:

   * Add current path to result

---

### 📊 Complexity Analysis

| Type             | Complexity             |
| ---------------- | ---------------------- |
| Time Complexity  | O(4^(N²)) (worst case) |
| Space Complexity | O(N²)                  |

---

### 📎 Example

```text id="example"
Input:
maze =
[
 [1,0,0,0],
 [1,1,0,1],
 [1,1,0,0],
 [0,1,1,1]
]

Output:
["DDRDRR", "DRDDRR"]
```

---

### 🔍 Dry Run

```text id="dryrun"
Start at (0,0)

Move Down → (1,0)
Move Down → (2,0)
Move Right → (2,1)
Move Down → (3,1)
Move Right → (3,2)
Move Right → (3,3) ✔️

Path = "DDRDRR"
```

---

### 🌳 Recursion Tree (Simplified)

```text id="tree"
(0,0)
  |
  D
(1,0)
 /   \
D     R
...   ...
```

---

### ✅ Key Points

* Classic **DFS + Backtracking problem**
* Uses **visited matrix** to avoid cycles
* Explores all valid paths
* Backtracking restores state after recursion

---

### ⚠️ Edge Cases

* Starting cell blocked
* No valid path exists
* Single cell maze
* Multiple valid paths

---

### 🏁 Conclusion

Rat in a Maze is a classic pathfinding problem that demonstrates how backtracking can systematically explore all possible routes while avoiding revisiting cells and invalid paths.

---