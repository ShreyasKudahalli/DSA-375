# Classis Binary Search

Classic Binary Search is an efficient divide-and-conquer algorithm used to locate a target element in a sorted array by repeatedly halving the search space, comparing the middle element with the target, and narrowing the range until the element is found or the search space is exhausted, achieving a time complexity of **O(log n)** with constant space usage.

## 1️⃣ Binary Search in Python

### 📌 Problem Statement

Given a **sorted integer array** `nums` and an integer `target`, return the **index of `target`** if it exists in the array.  
If the target is not present, return **`-1`**.

The solution must run in **O(log n)** time complexity.

---

### 💡 Approach: Binary Search

Binary Search works by repeatedly dividing the search space into two halves.

#### Steps:
1. Initialize two pointers:
    - `low` → start of the array
    - `high` → end of the array
2. Find the middle index:
    - mid = (low + high) // 2
3. Compare `nums[mid]` with `target`:
    - If equal → return `mid`
    - If smaller → move to the right half
    - If larger → move to the left half
4. Repeat until `low > high`
5. If the target is not found, return `-1`

---

### 🧠 Algorithm

1. Set `low = 0` and `high = len(nums) - 1`
2. While `low <= high`:
    - Calculate `mid`
    - If `nums[mid] == target`, return `mid`
    - If `nums[mid] < target`, update `low`
    - Else update `high`
3. Return `-1` if the element is not found

---

### 🧪 Example

#### Input
    nums = [1, 3, 5, 7, 9]  target = 7


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
- Uses constant extra space
- Widely used in technical interviews


---


## 2️⃣ Integer Square Root using Binary Search

### 📌 Problem Statement

Given a **non-negative integer** `x`, compute and return the **square root of `x`**.

Since the return type is an integer, the result should be **rounded down** to the nearest integer (i.e., return the floor value of √x).

---

### 💡 Approach: Binary Search

We use **Binary Search** to efficiently find the integer square root.

#### Key Idea:
- The square root of `x` lies between `0` and `x`
- Instead of checking every number, we narrow down the search space using binary search
- We keep track of the **largest integer whose square is ≤ x**

---

### 🧠 Algorithm

1. Initialize:
   - `low = 0`
   - `high = x`
2. While `low <= high`:
   - Compute `mid = (low + high) // 2`
   - If `mid * mid <= x`:
     - Move right (`low = mid + 1`)
   - Else:
     - Move left (`high = mid - 1`)
3. Return `high` as the integer square root

---

### 🧪 Example

#### Input
    x = 8

#### Output
    2

#### Explanation
    √8 ≈ 2.82 → floor value is 2

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(log x)  |
| Space Complexity | O(1)  |

---

### ✅ Key Notes

- No built-in square root functions used
- Works efficiently even for large values of x
- Classic Binary Search application
- Frequently asked in coding interviews


---


## 3️⃣ Search Insert Position

## 📌 Problem Statement

Given a **sorted array of distinct integers** `nums` and an integer `target`, return the **index** if the `target` is found.  
If not, return the **index where it would be inserted** in order.

The solution must run in **O(log n)** time.

---

### 💡 Approach: Binary Search

Since the array is **sorted**, Binary Search is the most efficient approach.

#### Key Idea:
- If `target` exists, return its index
- If not, find the **first index where an element is greater than or equal to `target`**
- That index is the correct insertion position

---

### 🧠 Algorithm

1. Initialize:
   - `low = 0`
   - `high = len(nums) - 1`
2. While `low <= high`:
   - Compute `mid = (low + high) // 2`
   - If `nums[mid] < target`:
     - Move right (`low = mid + 1`)
   - Else:
     - Move left (`high = mid - 1`)
3. Return `low` as the insert position

---

### 🧪 Example

#### Input
    nums = [1, 3, 5, 6]
    target = 5

#### Output
    2

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(log n)  |
| Space Complexity | O(1)  |

### ✅ Key Notes

- Array must be sorted
- No extra space used
- Handles both found and not found cases
- Frequently asked Binary Search interview question
