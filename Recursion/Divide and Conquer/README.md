# 🔀 Divide and Conquer Approach

Divide and Conquer is a powerful problem-solving technique where a problem is broken down into smaller subproblems, each solved independently, and then combined to form the final result. In this solution, the exponentiation problem is divided by repeatedly halving the power (`n // 2`), solving the smaller subproblem recursively, and combining the results through multiplication. This approach significantly improves efficiency by reducing redundant computations, achieving a time complexity of **O(log n)** instead of **O(n)**.


Here’s a clean and professional **README.md** for your **Recursive Binary Search** implementation 👇

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
