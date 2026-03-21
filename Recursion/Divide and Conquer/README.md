# 🔀 Divide and Conquer Approach

Divide and Conquer is a powerful problem-solving technique where a problem is broken down into smaller subproblems, each solved independently, and then combined to form the final result. In this solution, the exponentiation problem is divided by repeatedly halving the power (`n // 2`), solving the smaller subproblem recursively, and combining the results through multiplication. This approach significantly improves efficiency by reducing redundant computations, achieving a time complexity of **O(log n)** instead of **O(n)**.


---

## 1️⃣ Recursive Binary Search

### 📌 Problem Statement

Given a **sorted array** `nums` and a target value `target`, return the **index** of the target if it exists. Otherwise, return `-1`.

---

### 🚀 Approach: Divide and Conquer (Recursion)

This solution uses the **Divide and Conquer** strategy with recursion:

* Divide the array into two halves
* Compare the middle element with the target
* Recursively search in the relevant half

This reduces the search space exponentially, making it highly efficient.

---

### 🧠 Algorithm

1. Define a recursive function `binary_search(low, high)`
2. Base case:

   * If `low > high` → return `-1`
3. Find middle index:

   * `mid = (low + high) // 2`
4. Compare:

   * If `nums[mid] == target` → return `mid`
   * If `nums[mid] < target` → search right half
   * Else → search left half
5. Initial call:

   * `binary_search(0, len(nums) - 1)`

---

### 📊 Complexity Analysis

| Type             | Complexity                   |
| ---------------- | ---------------------------- |
| Time Complexity  | O(log n)                     |
| Space Complexity | O(log n) *(recursion stack)* |

---

### 📎 Examples

```text id="example1"
Input: nums = [-1,0,3,5,9,12], target = 9  
Output: 4
```

```text id="example2"
Input: nums = [-1,0,3,5,9,12], target = 2  
Output: -1
```

---

### 🔁 Iterative vs Recursive

| Approach  | Space    | Style              |
| --------- | -------- | ------------------ |
| Iterative | O(1)     | Loop-based         |
| Recursive | O(log n) | Cleaner, intuitive |

---

### ✅ Key Points

* Works only on **sorted arrays**
* Uses **divide and conquer**
* Recursive approach is more intuitive but uses stack space
* Efficient for large datasets

---

### 🏁 Conclusion

Recursive Binary Search is a clean and elegant way to implement searching in sorted arrays, leveraging recursion to reduce the problem size at every step and achieving **logarithmic time complexity**.


---


## 2️⃣ Maximum Subarray Sum (Divide & Conquer)

### 📌 Problem Statement

Given an integer array `nums`, find the **contiguous subarray** (containing at least one number) which has the **largest sum**, and return that sum.

---

### 🚀 Approach: Divide and Conquer

This solution uses the **Divide and Conquer** technique:

* Divide the array into two halves
* Recursively find the maximum subarray sum in:

  * Left half
  * Right half
* Find the maximum subarray sum that **crosses the midpoint**
* Return the maximum of all three

---

### 🧠 Key Insight

For any subarray, the maximum sum lies in one of three cases:

1. Entirely in the **left half**
2. Entirely in the **right half**
3. **Crossing the midpoint**

---

### 🧩 Algorithm

1. Base case:

   * If `left == right`, return `nums[left]`

2. Divide:

   * Find `mid = (left + right) // 2`

3. Conquer:

   * Recursively compute:

     * `left_sum`
     * `right_sum`

4. Combine:

   * Compute `cross_sum`:

     * Max sum from mid → left
     * Max sum from mid+1 → right

5. Return:

   * `max(left_sum, right_sum, cross_sum)`

---

### 📊 Complexity Analysis

| Type             | Complexity                   |
| ---------------- | ---------------------------- |
| Time Complexity  | O(n log n)                   |
| Space Complexity | O(log n) *(recursion stack)* |

---

### 📎 Examples

```text id="example1"
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]  
Output: 6  
Explanation: Subarray [4,-1,2,1] has the largest sum = 6
```

```text id="example2"
Input: nums = [1]  
Output: 1
```

---

### 🔁 Comparison with Kadane’s Algorithm

| Approach           | Time Complexity | Space    |
| ------------------ | --------------- | -------- |
| Divide & Conquer   | O(n log n)      | O(log n) |
| Kadane’s Algorithm | O(n)            | O(1)     |

👉 Kadane’s is more optimal, but Divide & Conquer is great for understanding recursion and problem structure.

---

### ✅ Key Points

* Uses **divide and conquer**
* Considers all possible subarray cases
* Helps build intuition for recursive problem solving
* Not the most optimal, but very important conceptually

---

### 🏁 Conclusion

The Divide and Conquer approach systematically breaks down the problem and combines results to find the maximum subarray sum. While not as fast as Kadane’s Algorithm, it provides deep insight into recursive problem-solving techniques.


---


Here’s a clean and professional **README.md** for your **Merge Sort (Divide & Conquer)** implementation 👇

---

## 3️⃣ Merge Sort Algorithm

### 📌 Problem Statement

Given an array `arr`, sort the array in **ascending order** using the **Merge Sort** algorithm.

---

### 🚀 Approach: Divide and Conquer

Merge Sort follows the **Divide and Conquer** paradigm:

1. **Divide** the array into two halves
2. **Recursively sort** each half
3. **Merge** the two sorted halves into a single sorted array

---

### 🧠 Key Idea

* Keep dividing the array until each subarray contains a single element
* Merge subarrays in a sorted manner
* Build the final sorted array step by step

---

### 🧩 Algorithm

#### 🔹 Merge Sort Function

1. If `l >= r`, return (base case)
2. Find middle index:

   * `mid = (l + r) // 2`
3. Recursively sort:

   * Left half → `mergeSort(arr, l, mid)`
   * Right half → `mergeSort(arr, mid + 1, r)`
4. Merge both halves using `merge()`

---

#### 🔹 Merge Function

1. Use two pointers:

   * Left subarray → `l to mid`
   * Right subarray → `mid+1 to r`
2. Compare elements and store in a temporary list
3. Copy remaining elements (if any)
4. Write back sorted elements into original array

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n log n) |
| Space Complexity | O(n)       |

---

### 📎 Example

```text id="example1"
Input:  arr = [5, 2, 4, 6, 1, 3]  
Output: [1, 2, 3, 4, 5, 6]
```

```text id="example2"
Input:  arr = [3, 1]  
Output: [1, 3]
```

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
[5,2,4,6,1,3]
→ Split → [5,2,4] [6,1,3]
→ Split → [5] [2,4] ...
→ Merge → [2,4] → [2,4,5]
→ Final Merge → [1,2,3,4,5,6]
```

---

### ✅ Key Points

* Stable sorting algorithm ✅
* Guarantees **O(n log n)** in all cases
* Uses extra space for merging
* Ideal for large datasets and linked lists

---

### ⚖️ Advantages & Disadvantages

#### ✔️ Advantages

* Consistent performance
* Easy to implement using recursion
* Works well for large data

#### ❌ Disadvantages

* Requires extra space (not in-place)
* Slightly slower than quicksort in practice

---

### 🏁 Conclusion

Merge Sort is a reliable and efficient sorting algorithm based on **divide and conquer**, ensuring predictable performance across all cases. It is especially useful when stability and guaranteed time complexity are required.


---


## 4️⃣ Search in Rotated Sorted Array

### 📌 Problem Statement

Given a **rotated sorted array** `nums` and a target value `target`, return the **index** of the target if it exists. Otherwise, return `-1`.

👉 The array was originally sorted in ascending order but then **rotated at some pivot**.

---

### 🧾 Example of Rotation

```text
Original: [0,1,2,4,5,6,7]
Rotated:  [4,5,6,7,0,1,2]
```

---

### 🚀 Approach: Modified Binary Search (Divide & Conquer)

We use **binary search**, but with a twist:

* At every step, **one half of the array is always sorted**
* We determine which half is sorted and decide where to search next

---

### 🧠 Key Insight

For any `mid`:

* If `nums[left] <= nums[mid]` → Left half is sorted
* Else → Right half is sorted

Then check if the target lies in the sorted half:

* If yes → search that half
* Else → search the other half

---

### 🧩 Algorithm

1. Base case:

   * If `left > right` → return `-1`

2. Find middle:

   * `mid = (left + right) // 2`

3. If `nums[mid] == target` → return `mid`

4. Check sorted half:

   * **Left sorted**:

     * If `nums[left] <= target < nums[mid]` → search left
     * Else → search right
   * **Right sorted**:

     * If `nums[mid] < target <= nums[right]` → search right
     * Else → search left

---

### 📊 Complexity Analysis

| Type             | Complexity                   |
| ---------------- | ---------------------------- |
| Time Complexity  | O(log n)                     |
| Space Complexity | O(log n) *(recursion stack)* |

---

### 📎 Examples

```text
Input: nums = [4,5,6,7,0,1,2], target = 0  
Output: 4
```

```text
Input: nums = [4,5,6,7,0,1,2], target = 3  
Output: -1
```

---

### 🔁 Iterative vs Recursive

| Approach  | Space    | Style              |
| --------- | -------- | ------------------ |
| Iterative | O(1)     | More optimal       |
| Recursive | O(log n) | Cleaner, intuitive |

---

### ✅ Key Points

* Modified version of **binary search**
* Works in **logarithmic time**
* At least one half is always sorted
* Efficient for rotated arrays

---

### ⚠️ Edge Cases

* Single element array
* Target not present
* No rotation (fully sorted array)
* Rotation at index `0` (same as sorted)

---

### 🏁 Conclusion

This approach efficiently searches in a rotated sorted array by leveraging the sorted nature of one half at each step. It maintains **O(log n)** performance while handling the complexity introduced by rotation.


---