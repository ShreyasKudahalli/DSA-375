# Prefix Sum & Array-Based Problems – DSA Notes

This document contains detailed explanations of **6 important array problems** that heavily rely on **Prefix Sum**, **Hash Maps**, and **Optimized Traversals**.  
These problems are frequently asked in coding interviews.

---

## 1️⃣ Subarray Sum Equals K


### 🧩 Problem Statement
Given an integer array `nums` and an integer `k`, return the **total number of continuous subarrays** whose sum equals `k`.


### 💡 Approach: Prefix Sum + Hash Map
Instead of checking all subarrays (O(n²)), we use a prefix sum and a hashmap to store how many times a prefix sum has appeared.


**Key Insight:**  
If  
`prefix_sum[j] - prefix_sum[i] = k`  
then the subarray `(i+1 → j)` sums to `k`.


### 🧠 Algorithm
1. Initialize a hashmap `count` with `{0: 1}`
2. Maintain a running sum `total`
3. For each element:
   - Add current number to `total`
   - Check if `total - k` exists in hashmap
   - Add its frequency to result
   - Update hashmap with current `total`


### 🔑 Key Concepts
- Prefix Sum
- Hash Map Frequency Counting
- Subarray Sum Optimization


### ⏱ Complexity
- **Time:** `O(n)`
- **Space:** `O(n)`


---


## 2️⃣ Matrix Block Sum


### 🧩 Problem Statement
Given a matrix mat and an integer k, return a matrix where each element is the sum of all elements within distance k from that cell.


### 💡 Approach: 2D Prefix Sum
We preprocess the matrix using a 2D prefix sum, allowing constant-time submatrix sum queries.


### 🧠 Algorithm
1. Build row-wise prefix sums
2. Convert to full 2D prefix sum
3. For each cell:
   - Compute valid boundary indices
   - Use prefix sum inclusion–exclusion to calculate area sum


### 🔑 Key Concepts
- 2D Prefix Sum
- Inclusion–Exclusion Principle
- Matrix Preprocessing


### ⏱ Complexity
- **Time:** `O(n*m)`
- **Space:** `O(n*m)`


---


## 3️⃣ Product of Array Except Self


### 🧩 Problem Statement
Given an array nums, return an array such that each element is the product of all elements except itself.


### 💡 Approach: Prefix & Suffix Products

Avoid division by computing:
- Prefix product from the left
- Suffix product from the right


### 🧠 Algorithm

1. Initialize result array with 1
2. Traverse left → right to build prefix product
3. Traverse right → left to multiply suffix product


### 🔑 Key Concepts

- Prefix Product
- Suffix Product
- Space Optimization


### ⏱ Complexity
- **Time:** `O(n)`
- **Space:** `O(1)`


---


## 4️⃣ Continuous Subarray Sum


### 🧩 Problem Statement

Return True if there exists a subarray of length at least 2 whose sum is a multiple of k.


### 💡 Approach: Prefix Sum Modulo

If two prefix sums have the same remainder modulo k, their difference is divisible by k.


### 🧠 Algorithm

1. Store remainder → index in hashmap
2. Track cumulative sum
3. If same remainder appears again with distance ≥ 2 → return True


### 🔑 Key Concepts
- Modulo Arithmetic
- Prefix Sum
- Hash Map Index Tracking


### ⏱ Complexity
- **Time:** `O(n)`
- **Space:** `O(k)`


---


## 5️⃣ Subarrays Divisible by K

### 🧩 Problem Statement
Return the number of subarrays whose sum is divisible by k.


### 💡 Approach: Prefix Sum + Mod Frequency

Same modulo ⇒ valid subarray.


### 🧠 Algorithm
1. Initialize {0:1} in hashmap
2. Maintain prefix sum modulo k
3. Count occurrences of same remainder


### 🔑 Key Concepts
- Modulo Prefix Sum
- Frequency Hash Map


### ⏱ Complexity
- **Time:** `O(n)`
- **Space:** `O(k)`


---


## 6️⃣ Find Pivot Index

### 🧩 Problem Statement
Return the index where the sum of elements to the left equals the sum to the right.
---

### 💡 Approach: Running Left Sum

Total sum is known; right sum can be derived


### 🧠 Algorithm
1. Compute total sum
2. Traverse array:
   - Check if left == total - left - nums[i]
3. Return index if found


### 🔑 Key Concepts
- Prefix Sum
- Array Traversal

---

### ⏱ Complexity
- **Time:** `O(n)`
- **Space:** `O(1)`