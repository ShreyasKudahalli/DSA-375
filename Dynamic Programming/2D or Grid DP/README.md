# 2D or Grid Dynamic Programming
2D or Grid Dynamic Programming focuses on solving problems where states are represented using rows and columns, and each cell’s solution depends on previously computed neighboring cells. These problems commonly involve path counting, minimum or maximum cost traversal, obstacle handling, and movement constraints within a matrix. By storing intermediate results in a two-dimensional DP table, grid DP efficiently avoids repeated calculations and builds solutions incrementally using transitions from directions such as top, left, right, or diagonal cells, making it a fundamental technique for matrix-based optimization and traversal problems.


## 1️⃣ Unique Paths

### 📌 Problem Statement

You are given:

* `m` → number of rows
* `n` → number of columns

A robot starts at the top-left corner of an `m x n` grid.

👉 The robot can only move:

1. Right
2. Down

👉 Return the total number of unique paths to reach the bottom-right corner.

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

To reach any cell `(i, j)`:

The robot can come from:

1. Top cell `(i-1, j)`
2. Left cell `(i, j-1)`

So:

```text id="relation"
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

---

### 🧠 Algorithm

1. Create a 2D DP table:

   * `dp[i][j]` → number of paths to reach cell `(i,j)`

2. Initialize first row and first column:

   * Only one way to move straight right or straight down

3. Traverse remaining cells:

   * Add paths from top and left

4. Return `dp[m-1][n-1]`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(m × n)   |
| Space Complexity | O(m × n)   |

---

### 📎 Example

```text id="example"
Input:
m = 3
n = 7

Output:
28
```

---

### 🔍 Dry Run

```text id="dryrun"
m = 3, n = 3

Initial DP:
1 1 1
1 0 0
1 0 0

Fill remaining cells:

1 1 1
1 2 3
1 3 6

Answer = 6
```

---

### 🌳 Visualization

```text id="visual"
Grid:

S → → 
↓   ↓
↓ → E

S = Start
E = End
```

---

### ✅ Key Points

* Classic grid-based DP problem
* Each state depends on top and left cells
* First row and column always have one path
* Builds solution bottom-up efficiently

---

### ⚠️ Edge Cases

* Single row
* Single column
* Small grids like `1 x 1`
* Large grid dimensions

---

### 🏁 Conclusion

This problem demonstrates how dynamic programming efficiently counts paths in a grid by reusing previously computed subproblem results from neighboring cells.


---


## 2️⃣ Unique Paths II

### 📌 Problem Statement

You are given:

* `obstacleGrid` → an `m x n` grid where:

  * `0` → empty cell
  * `1` → obstacle

A robot starts at the top-left corner and wants to reach the bottom-right corner.

👉 The robot can only move:

1. Right
2. Down

👉 Return the number of unique paths while avoiding obstacles.

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

For each cell:

* If it contains an obstacle:

  * No path can pass through it
* Otherwise:

  * Paths come from:

    * top cell
    * left cell

So:

```text id="relation"
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

Only if the current cell is not blocked.

---

### 🧠 Algorithm

1. Traverse the grid

2. If current cell is an obstacle:

   * Set value to `0`

3. Handle starting cell:

   * Set `grid[0][0] = 1`

4. Fill first row and column:

   * Path depends on previous cell

5. For remaining cells:

   * Add paths from top and left

6. Return bottom-right cell value

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(m × n)   |
| Space Complexity | O(1)       |

> Uses input grid itself as DP storage.

---

### 📎 Example

```text id="example"
Input:
obstacleGrid =
[
 [0,0,0],
 [0,1,0],
 [0,0,0]
]

Output:
2
```

---

### 🔍 Dry Run

```text id="dryrun"
Initial Grid:
0 0 0
0 1 0
0 0 0

DP Build:

1 1 1
1 0 1
1 1 2

Answer = 2
```

---

### 🌳 Visualization

```text id="visual"
S → → 
↓ X ↓
↓ → E

S = Start
E = End
X = Obstacle
```

---

### ✅ Key Points

* Extension of Unique Paths problem
* Obstacles block path propagation
* Uses in-place dynamic programming
* Each cell depends on top and left paths

---

### ⚠️ Edge Cases

* Start cell blocked
* End cell blocked
* Entire row/column blocked
* Single cell grid

---

### 🏁 Conclusion

This problem demonstrates how dynamic programming can efficiently count valid paths in a grid while handling blocked cells and movement constraints using state transitions from neighboring cells.


---


## 3️⃣ Minimum Path Sum

### 📌 Problem Statement

You are given:

* `grid` → an `m x n` matrix containing non-negative integers

A robot starts at the top-left corner and wants to reach the bottom-right corner.

👉 The robot can only move:

1. Right
2. Down

👉 Return the minimum possible sum of values along the path.

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

To reach any cell `(i, j)` with minimum cost:

The robot can come from:

1. Top cell `(i-1, j)`
2. Left cell `(i, j-1)`

So:

```text id="relation"
grid[i][j] += min(
    grid[i-1][j],
    grid[i][j-1]
)
```

👉 Store the minimum path sum directly inside the grid.

---

### 🧠 Algorithm

1. Traverse the grid

2. Handle starting cell:

   * Keep original value

3. Fill first row:

   * Can only come from left

4. Fill first column:

   * Can only come from top

5. For remaining cells:

   * Add minimum of top or left path

6. Return bottom-right value

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(m × n)   |
| Space Complexity | O(1)       |

> Uses input grid as DP table.

---

### 📎 Example

```text id="example"
Input:
grid =
[
 [1,3,1],
 [1,5,1],
 [4,2,1]
]

Output:
7
```

---

### 🔍 Dry Run

```text id="dryrun"
Initial Grid:
1 3 1
1 5 1
4 2 1

DP Build:

1 4 5
2 7 6
6 8 7

Answer = 7
```

---

### 🌳 Visualization

```text id="visual"
Optimal Path:

1 → 3 → 1
        ↓
1    5 → 1
        ↓
4 → 2 → 1

Minimum Sum = 7
```

---

### ✅ Key Points

* Classic grid DP optimization problem
* Each state depends on top and left cells
* In-place DP reduces extra space usage
* Greedily choosing local minimum alone does not work

---

### ⚠️ Edge Cases

* Single row
* Single column
* Grid with all zeros
* Large grid values

---

### 🏁 Conclusion

This problem demonstrates how dynamic programming efficiently computes minimum-cost paths in a grid by building solutions incrementally from previously optimized neighboring states.


---


## 4️⃣ Maximum Path Sum in Matrix

### 📌 Problem Statement

You are given:

* `mat` → an `n x n` matrix of integers

You can start from any cell in the first row.

👉 From cell `(i, j)`, you can move to:

1. Down `(i+1, j)`
2. Down-left `(i+1, j-1)`
3. Down-right `(i+1, j+1)`

👉 Return the maximum possible path sum from the first row to the last row.

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

For each cell `(i, j)`:

The maximum path reaching it can come from:

1. Top `(i-1, j)`
2. Top-left `(i-1, j-1)`
3. Top-right `(i-1, j+1)`

So:

```text id="relation"
mat[i][j] += max(
    top,
    top-left,
    top-right
)
```

👉 Store DP values directly inside the matrix.

---

### 🧠 Algorithm

1. Traverse matrix row by row starting from row `1`

2. For each cell:

   * Add maximum value from valid upper neighbors

3. Continue updating matrix in-place

4. Final answer:

   * Maximum value in last row

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n²)      |
| Space Complexity | O(1)       |

> Uses input matrix itself as DP storage.

---

### 📎 Example

```text id="example"
Input:
mat =
[
 [10,10,2,0,20,4],
 [1,0,0,30,2,5],
 [0,10,4,0,2,0],
 [1,0,2,20,0,4]
]

Output:
74
```

---

### 🔍 Dry Run

```text id="dryrun"
Possible Maximum Path:

20 → 30 → 10 → 20

Total = 80
```

---

### 🌳 Visualization

```text id="visual"
10  10   2   0  20   4
                ↓
 1   0   0  30   2   5
             ↓
 0  10   4   0   2   0
          ↓
 1   0   2  20   0   4
```

---

### ✅ Key Points

* Grid-based optimization DP problem
* Each state depends on three upper cells
* In-place matrix updates reduce extra memory
* Similar to Minimum Falling Path Sum with maximization

---

### ⚠️ Edge Cases

* Single row matrix
* Negative values
* Multiple optimal paths
* Large matrix dimensions

---

### 🏁 Conclusion

This problem demonstrates how dynamic programming efficiently computes optimal path sums in a matrix by propagating the best achievable values from previous rows using valid directional transitions.



---


## 5️⃣ Minimum Falling Path Sum

### 📌 Problem Statement

You are given:

* `matrix` → an `n x n` integer matrix

A falling path starts at any element in the first row and chooses one element from each row.

👉 From cell `(i, j)`, you can move to:

1. Down `(i+1, j)`
2. Down-left `(i+1, j-1)`
3. Down-right `(i+1, j+1)`

👉 Return the minimum sum of any falling path through the matrix.

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

For each cell `(i, j)`:

The minimum falling path reaching it can come from:

1. Top cell `(i-1, j)`
2. Top-left `(i-1, j-1)`
3. Top-right `(i-1, j+1)`

So:

```text id="relation"
matrix[i][j] += min(
    top,
    top-left,
    top-right
)
```

👉 Store DP values directly inside the matrix.

---

### 🧠 Algorithm

1. Traverse rows starting from row `1`

2. For each cell:

   * Add minimum value from valid upper neighbors

3. Continue updating matrix in-place

4. Final answer:

   * Minimum value in last row

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n²)      |
| Space Complexity | O(1)       |

> Uses input matrix itself as DP storage.

---

### 📎 Example

```text id="example"
Input:
matrix =
[
 [2,1,3],
 [6,5,4],
 [7,8,9]
]

Output:
13
```

---

### 🔍 Dry Run

```text id="dryrun"
Initial Matrix:
2 1 3
6 5 4
7 8 9

After Row 1:
7 6 5

After Row 2:
13 13 14

Answer = 13
```

---

### 🌳 Visualization

```text id="visual"
2   1   3
 \ / \ /
 6   5   4
  \ / \ /
   7   8   9

Minimum Falling Path = 1 → 5 → 7
Total = 13
```

---

### ✅ Key Points

* Classic grid-based DP problem
* Each cell depends on three upper neighbors
* In-place DP optimization
* Computes minimum path efficiently row by row

---

### ⚠️ Edge Cases

* Single row matrix
* Negative values
* Large matrix sizes
* Equal path sums

---

### 🏁 Conclusion

This problem demonstrates how dynamic programming efficiently computes optimal path costs in a matrix by combining results from multiple valid previous states while traversing row by row.
