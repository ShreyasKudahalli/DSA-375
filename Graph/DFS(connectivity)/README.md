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