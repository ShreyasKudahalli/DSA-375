# Binary Search in 2D Matrix

Binary Search on a 2D Matrix is an efficient technique used to solve matrix problems where rows and/or columns are sorted, by applying binary search either on indices or on the value range. By smartly mapping a 2D matrix to a virtual 1D structure or by searching within the possible answer space, this approach reduces time complexity from linear or quadratic to logarithmic, making it ideal for large matrices and commonly used in competitive programming and interview problems.

## 1️⃣ Search a 2D Matrix

### 📌 Problem Statement

You are given a 2D matrix with the following properties:

- Each row is sorted in **ascending order**
- The **first integer of each row is greater than the last integer of the previous row**

Given an integer `target`, return `true` if the target exists in the matrix, otherwise return `false`.

---

### 💡 Approach

Instead of performing binary search row by row, we can treat the **entire 2D matrix as a single sorted 1D array**.

#### Why this works?
Because the matrix is globally sorted due to the given constraints.

---

### 🔁 Index Mapping Trick

If the matrix has:
- `m` rows
- `n` columns

We can map a 1D index `mid` to 2D indices as:

```text
row = mid // n
col = mid % n
```

---

###  🧠 Algorithm

1. Calculate total elements = m * n
2. Apply binary search on index range [0, (m*n)-1]
3. Convert mid index to (row, col)
4. Compare matrix[row][col] with target
5. Adjust search space accordingly

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O( log(m * n) )  |
| Space Complexity | O(1)  |

### 🧪 Example

#### Input
        matrix = [[1, 3, 5, 7],          target = 3
                [10, 11, 16, 20],
                [23, 30, 34, 60]]
        

#### Output
        true

---

### ✅ Key Takeaways

- Treating a 2D matrix as a 1D sorted array simplifies the problem
- Binary search on answers/index space is extremely powerful
- Always verify row/column mapping carefully


---


## 2️⃣ Search a 2D Matrix II

### 📌 Problem Statement

You are given a 2D matrix where:

- Each row is sorted in **ascending order**
- Each column is sorted in **ascending order**

Given an integer `target`, return `true` if the target exists in the matrix, otherwise return `false`.

---

### 💡 Approach: Staircase Search

This approach starts from the **top-right corner** of the matrix and eliminates one row or one column at each step.

#### Why top-right?
- Moving **left** decreases values
- Moving **down** increases values

This allows us to efficiently narrow the search space.

---

### 🧠 Algorithm

1. Start at position `(0, n-1)` (top-right corner)
2. While row index is within bounds and column index is valid:
   - If current value equals target → return `true`
   - If current value is **less than** target → move **down**
   - If current value is **greater than** target → move **left**
3. If search ends, return `false`

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(m + n)  |
| Space Complexity | O(1)  |

---

### 🧪 Example

#### Input:
        matrix = [                     target = 5
        [1, 4, 7, 11],
        [2, 5, 8, 12],
        [3, 6, 9, 16],
        [10, 13, 14, 17]
        ]

#### Output:
        true

---

### ✅ Key Takeaways

- No binary search required
- Eliminates one row or column in each step
- Very intuitive and optimal for row + column sorted matrices


---


## 3️⃣ Kth Smallest Element in a Sorted Matrix

### 📌 Problem Statement

You are given an `m x n` matrix where:

- Each row is sorted in **ascending order**
- Each column is sorted in **ascending order**

Given an integer `k`, return the **kᵗʰ smallest element** in the matrix.

---

### 💡 Approach: Binary Search on Answer

Instead of flattening or using a heap, we apply **binary search on the value range**.

#### Key Observation
- The smallest possible answer is `matrix[0][0]`
- The largest possible answer is `matrix[m-1][n-1]`
- For any value `mid`, we can count how many elements in the matrix are `≤ mid`

If the count is **at least `k`**, then `mid` could be the answer.

---

### 🧠 Algorithm

1. Set `low` to the smallest element in the matrix
2. Set `high` to the largest element in the matrix
3. While `low <= high`:
   - Compute `mid`
   - Count how many elements are `≤ mid`
   - If count ≥ `k`, shrink the right boundary
   - Else, move the left boundary
4. Return `low` as the kᵗʰ smallest element

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(m × n × log(max - min))  |
| Space Complexity | O(1)  |

---

### 🧪 Example

#### Input:
        matrix = [              k = 8
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
        ]

#### Output:
        13

---

### ✅ Key Takeaways

- This is a classic Binary Search on Answer problem
- No extra space required
- Works well when value range is manageable


---


## 4️⃣ Median of a Row-Wise Sorted Matrix

### 📌 Problem Statement

You are given a matrix where **each row is sorted in ascending order**.  
The task is to find the **median** of the matrix.

> The total number of elements is always odd, so the median is the middle element when all elements are sorted.

---

### 💡 Approach: Binary Search on Answer

Instead of flattening the matrix and sorting it, we apply **binary search on the value range**.

#### Key Observations

- Minimum possible value = smallest element in the matrix
- Maximum possible value = largest element in the matrix
- The median is the element for which **at least half of the elements are smaller or equal**

---

### 🧠 Algorithm

1. Compute the required position of the median  
- required = (n × m) // 2 + 1
2. Set `low` to the minimum element and `high` to the maximum element
3. For a given value `mid`, count how many elements are `≤ mid`
- Use `bisect_right` since rows are already sorted
4. If count ≥ required, move left to find a smaller candidate
5. Otherwise, move right
6. Return `low` as the median

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n × log m × log(max - min))  |
| Space Complexity | O(1)  |

---

### 🧪 Example

#### Input:
        mat = [
        [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]
        ]

#### Output:
        5

---

### ✅ Key Takeaways

- This is a classic Binary Search on Answer problem
- Uses the sorted property of rows effectively
- Avoids extra space and full sorting
- Frequently asked in interviews and coding contests


---


## 5️⃣ Count Elements Less Than or Equal to K in a Sorted Matrix

### 📌 Problem Statement

You are given a 2D matrix where:

- Each row is sorted in **ascending order**
- Each column is sorted in **ascending order**

Given an integer `k`, return the **count of elements less than or equal to `k`** in the matrix.

---

### 💡 Approach: Staircase Traversal

This method starts from the **top-right corner** of the matrix and eliminates a row or a column at each step.

#### Why Top-Right?
- Moving **left** → smaller values
- Moving **down** → larger values

This allows counting in linear time.

---

### 🧠 Algorithm

1. Initialize:
   - `row = 0`
   - `col = n - 1`
   - `count = 0`
2. While within matrix bounds:
   - If `matrix[row][col] ≤ k`  
     → All elements to the left of `col` in this row are also ≤ `k`  
     → Add `(col + 1)` to count and move **down**
   - Else  
     → Move **left**
3. Return `count`

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(m + n)  |
| Space Complexity | O(1)  |

---

### 🧪 Example

#### Input:
        matrix = [      k = 5
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
        ]

#### Output:
        5

---

### ✅ Key Takeaways

- Extremely efficient for row + column sorted matrices0
- No extra space required
- Common helper function in:

        Kth smallest element problems

        Median in matrix problems
- Frequently used in Binary Search on Answer