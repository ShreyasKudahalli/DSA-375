# Kadane’s Algorithm

🔹 Overview
Kadane’s Algorithm is an efficient **dynamic programming / greedy** technique used to find the **maximum sum of a contiguous subarray** within a one-dimensional array of numbers.
It solves the problem in **linear time** and **constant space**, making it one of the most important algorithms for coding interviews and competitive programming.

🔹 Why Kadane’s Algorithm?
- Handles negative numbers efficiently
- Avoids brute-force `O(n²)` solutions
- Works as a base for many advanced problems




## 1️⃣ Maximum Subarray Sum (Kadane’s Algorithm)

### 📌 Problem Statement
Given an integer array `nums`, find the **contiguous subarray** (containing at least one number) which has the **largest sum**, and return that sum.

### 🧠 Intuition
1. At every index, we decide:
  - **Extend** the previous subarray, or
  - **Start fresh** from the current element
2. If the previous sum becomes harmful (negative), we drop it.
3. This greedy decision leads to an optimal solution.

### 💡 Approach (Kadane’s Algorithm)
We maintain two variables:
- `cur` → Maximum subarray sum **ending at current index**
- `res` → Maximum subarray sum **found so far**

For each element:
1. Either add it to the previous subarray
2. Or start a new subarray from the current element

### 🧮 Algorithm Steps
1. Initialize `cur` and `res` to **negative infinity**
2. Traverse the array:
   - `cur = max(cur + nums[i], nums[i])`
   - `res = max(res, cur)`
3. Return `res`

### ⏱️Time & Space Complexity
Time Complexity: O(n)
Space Complexity: O(1)


---


## 2️⃣ Maximum Product Subarray

### 📌 Problem Statement
Given an integer array `nums`, find the **contiguous subarray** that has the **largest product**, and return that product.

### 🧠 Key Insight
Unlike maximum sum, **product behaves differently**:
- Negative numbers can turn small products into large ones
- Zero breaks subarrays
- The maximum product can come from **either direction**

👉 To handle this, we scan:
- From **left to right**
- From **right to left**

This ensures we don’t miss subarrays affected by odd/even negative numbers.

### 💡 Approach (Two Direction Product Scan)
We maintain:
- `l_prod` → Product while scanning from left
- `r_prod` → Product while scanning from right
- `res` → Maximum product found so far

#### Important Rules
- If product becomes `0`, reset it to `1`
- At every step, update the result with the max of left and right products

### 🧮 Algorithm Steps
1. Initialize:
   - `l_prod = 1`
   - `r_prod = 1`
   - `res = -∞`
2. Traverse array from `0 → n-1`:
   - Multiply current number from left and right
   - Reset product to `1` if it becomes `0`
   - Update result
3. Return `res`

### ⏱️ Time & Space Complexity
Time Complexity: O(n)
Space Complexity: O(1)


---


## 3️⃣ Maximum Sum Circular Subarray

### 📌 Problem Statement
Given a **circular integer array** `nums`, return the **maximum possible sum of a non-empty subarray**.

A circular array means:
- The element after the last element is the **first element**
- Subarrays may **wrap around** the end of the array

### 🧠 Key Idea
There are **two possible cases** for the maximum subarray:

#### Case 1: Subarray does **NOT wrap**
- This is the normal **Kadane’s Algorithm**
- Gives `max_sum`

#### Case 2️: Subarray **wraps around**
- Equivalent to:
  total_sum - minimum_subarray_sum
- So the final answer is:
  max(max_sum, total_sum - min_sum)

### ⚠️ Important Edge Case (All Negative Numbers)

If **all numbers are negative**:
- `total_sum - min_sum = 0` ❌ (invalid)
- The answer must be the **maximum element**

Hence:
if max_sum < 0:
    return max_sum

### 💡 Approach (Dual Kadane’s Algorithm)
We calculate simultaneously:
- Maximum subarray sum (max_sum)
- Minimum subarray sum (min_sum)
- Total array sum (total)

### 🧮 Algorithm Steps
1. Initialize:
    - cur_max_sum, max_sum for max subarray
    - cur_min_sum, min_sum for min subarray
    - total = 0
2. Traverse the array:
    - Apply Kadane for max & min
    - Accumulate total sum
3. Handle all-negative case
4. Return max of wrapped and non-wrapped sums

### ⏱️ Time & Space Complexity
Time Complexity: O(n)
Space Complexity: O(1)


---


## 4️⃣ Maximum Absolute Subarray Sum

### 📌 Problem Statement
Given an integer array `nums`, find the **maximum absolute value** of the sum of **any non-empty subarray**.

Formally, return:
 - max(|sum(subarray)|)

### 🧠 Key Insight
The absolute value can be maximized in **two ways**:
1. A subarray with the **largest positive sum**
2. A subarray with the **most negative (minimum) sum**

So we compute:
- Maximum subarray sum
- Minimum subarray sum

👉 The answer is:
max(abs(max_sum), abs(min_sum))

### 💡 Approach (Dual Kadane’s Algorithm)
We apply Kadane’s Algorithm **twice in one pass**:
- One to track **maximum subarray sum**
- One to track **minimum subarray sum**

This allows us to handle both positive and negative extremes efficiently.

### 🧮 Algorithm Steps
1. Initialize:
   - `cur_max_sum`, `max_sum`
   - `cur_min_sum`, `min_sum`
2. Traverse the array:
   - Update current max and min subarray sums
   - Update global max and min
3. Return the maximum absolute value

### ⏱️ Time & Space Complexity
Time Complexity: O(n)
Space Complexity: O(1)
