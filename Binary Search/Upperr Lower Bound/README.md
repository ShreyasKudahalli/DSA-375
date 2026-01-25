# Upper and Lower Bound

Upper and Lower Bound in Binary Search refers to two fundamental techniques used to identify boundary positions in a sorted array, where the lower bound finds the first index at which a target value can be inserted without violating order (first element ≥ target), and the upper bound locates the first index where elements become strictly greater than the target, both enabling efficient range queries, frequency counting, and insertion point determination in O(log n) time.


## 1️⃣ Find First and Last Position of Element in Sorted Array

### 📌 Problem Statement

Given a **sorted integer array** `nums` and an integer `target`, find the **starting and ending position** of `target` in the array.

If the target is not found, return **`[-1, -1]`**.

The algorithm must run in **O(log n)** time.

---

### 💡 Approach: Binary Search (Two Passes)

To achieve logarithmic time complexity, we use **Binary Search twice**:
- First to find the **leftmost (first) occurrence**
- Second to find the **rightmost (last) occurrence**

---

### 🧠 Algorithm

#### Step 1: Find First Occurrence
1. Initialize `low = 0`, `high = len(nums) - 1`
2. Perform binary search:
   - If `nums[mid] == target`, store `mid` and continue searching left
   - If `nums[mid] < target`, move right
   - Else, move left

#### Step 2: Find Last Occurrence
1. Reset `low = 0`, `high = len(nums) - 1`
2. Perform binary search:
   - If `nums[mid] == target`, store `mid` and continue searching right
   - If `nums[mid] < target`, move right
   - Else, move left

#### Step 3: Return the result
- Return `[first, last]`

---

### 🧪 Example

#### Input
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

#### Output
    [3, 4]

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(log n)  |
| Space Complexity | O(1)  |

---

### ✅ Key Notes

- Array must be sorted
- Works efficiently with duplicate elements
- Uses binary search boundaries
- Popular LeetCode medium-level problem


---


## 2️⃣ Find Number of Rotations in a Rotated Sorted Array

### 📌 Problem Statement

Given a **rotated sorted array** `arr` with **distinct elements**, determine the **number of times the array has been rotated**.

The number of rotations is equal to the **index of the minimum element** in the array.

---

### 💡 Approach: Modified Binary Search

A rotated sorted array always contains one **sorted half**.  
By identifying the sorted half at each step, we can efficiently locate the **minimum element** and its index.

#### Key Idea:
- If the left half is sorted, the minimum could be at `arr[low]`
- If the left half is not sorted, the minimum lies in the left half
- Track the smallest element and its index during the search

---

### 🧠 Algorithm

1. Initialize:
   - `low = 0`
   - `high = len(arr) - 1`
   - `ans = +∞`
   - `index = -1`
2. While `low <= high`:
   - Compute `mid`
   - If `arr[low] <= arr[mid]`:
     - Left half is sorted
     - Update minimum using `arr[low]`
     - Move right
   - Else:
     - Rotation point lies in left half
     - Update minimum using `arr[mid]`
     - Move left
3. Return `index` of the minimum element

---

### 🧪 Example

#### Input
    arr = [15, 18, 2, 3, 6, 12]

#### Output
    2

#### Explanation
Minimum element is 2 at index 2
Array is rotated 2 times

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(log n)  |
| Space Complexity | O(1)  |

---

### ✅ Key Notes

-  Array is rotated but originally sorted
- All elements are distinct
- Number of rotations = index of minimum element
- Classic binary search on rotated arrays


---


## 3️⃣ Count Frequency of an Element in a Sorted Array

### 📌 Problem Statement

Given a **sorted array** `arr` and a value `target`, determine the **number of times `target` appears** in the array.

If the target is not present, return **`0`**.

The solution must run in **O(log n)** time.

---

### 💡 Approach: Binary Search (First & Last Occurrence)

To count the frequency efficiently, we locate:
1. The **first occurrence** of `target`
2. The **last occurrence** of `target`

The frequency is calculated as:

frequency = last_index - first_index + 1

---

### 🧠 Algorithm

#### Step 1: Find First Occurrence
1. Initialize `low = 0`, `high = len(arr) - 1`
2. Perform binary search:
   - If `arr[mid] == target`, store `mid` and move left
   - If `arr[mid] < target`, move right
   - Else, move left
3. If first occurrence is not found, return `0`

#### Step 2: Find Last Occurrence
1. Reset `low = 0`, `high = len(arr) - 1`
2. Perform binary search:
   - If `arr[mid] == target`, store `mid` and move right
   - If `arr[mid] < target`, move right
   - Else, move left

#### Step 3: Compute Frequency
frequency = last - first + 1

---

### 🧪 Example

#### Input
    arr = [1, 2, 2, 2, 3, 4]
    target = 2

#### Output
    3

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(log n)  |
| Space Complexity | O(1)  |

---

### ✅ Key Notes

- Array must be sorted
- Handles duplicate values efficiently
- Uses two binary searches
- Common interview problem


---


## 4️⃣ Floor of an Element in a Sorted Array

### 📌 Problem Statement

Given a **sorted array** `arr` and a value `x`, find the **floor** of `x`.

The **floor of `x`** is defined as the **greatest element in the array that is less than or equal to `x`**.  
If no such element exists, return **`-1`**.

---

### 💡 Approach: Binary Search

Since the array is **sorted**, we can efficiently find the floor using **Binary Search**.

#### Key Idea:
- If `arr[mid] <= x`, it is a valid candidate for floor → move right to find a larger value
- If `arr[mid] > x`, move left
- At the end of the search, `high` will point to the floor index

---

### 🧠 Algorithm

1. Initialize:
   - `low = 0`
   - `high = len(arr) - 1`
2. While `low <= high`:
   - Compute `mid`
   - If `arr[mid] <= x`, move right (`low = mid + 1`)
   - Else, move left (`high = mid - 1`)
3. Return `high` (index of floor element)

---

### 🧪 Example

#### Input
    arr = [1, 2, 4, 6, 10]
    x = 5

#### Output
    2

#### Explanation
arr[2] = 4 is the greatest element ≤ 5

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(log n)  |
| Space Complexity | O(1)  |

---

### ✅ Key Notes

- Array must be sorted
- Returns index of floor element
- If x is smaller than all elements, returns -1
- Efficient and interview-friendly solution


---


## 5️⃣ Ceil of an Element in a Sorted Array

### 📌 Problem Statement

Given a **sorted array** `arr` and a value `x`, find the **ceil** of `x`.

The **ceil of `x`** is defined as the **smallest element in the array that is greater than or equal to `x`**.  
If no such element exists, return **`-1`**.

---

### 💡 Approach: Binary Search

Since the array is **sorted**, Binary Search allows us to efficiently locate the ceil.

#### Key Idea:
- If `arr[mid] < x`, the ceil must be on the right side
- If `arr[mid] >= x`, it is a valid candidate → continue searching left for a smaller value
- After the search, `low` will point to the ceil index

---

### 🧠 Algorithm

1. Initialize:
   - `low = 0`
   - `high = len(arr) - 1`
2. While `low <= high`:
   - Compute `mid`
   - If `arr[mid] < x`, move right (`low = mid + 1`)
   - Else, move left (`high = mid - 1`)
3. If `low` is within bounds, return `low`
4. Otherwise, return `-1`

---

### 🧪 Example

#### Input
    arr = [1, 2, 4, 6, 10]
    x = 5

#### Output
    3

#### Explanation
arr[3] = 6 is the smallest element ≥ 5

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(log n)  |
| Space Complexity | O(1)  |

---

### ✅ Key Notes

- Array must be sorted
- Returns index of the ceil element
- If x is greater than all elements, returns -1
- Efficient and commonly asked binary search problem

