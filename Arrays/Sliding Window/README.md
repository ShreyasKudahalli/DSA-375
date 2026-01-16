# Sliding Window & Two Pointer Problems – DSA Practice

This repository contains solutions and detailed explanations for classic **Sliding Window and Two Pointer problems** commonly asked in coding interviews and competitive programming.

Each problem focuses on optimizing brute-force approaches using efficient window-based techniques.

---

## 📌 Problems Covered

### 1️⃣ Maximum Average Subarray I

**Problem Statement**  
Given an integer array `nums` and an integer `k`, find the maximum average value of any contiguous subarray of length `k`.

**Approach: Fixed-Size Sliding Window**
- Compute the sum of the first `k` elements
- Slide the window by:
  - Subtracting the outgoing element
  - Adding the incoming element
- Track the maximum sum
- Return `max_sum / k`

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

---

### 2️⃣ Max Consecutive Ones

**Problem Statement**  
Given a binary array `nums`, return the maximum number of consecutive `1`s.

**Approach: Two Pointers**
- Use two pointers to track continuous segments of `1`s
- Reset the window whenever `0` is encountered
- Keep updating the maximum length

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

---

### 3️⃣ Max Consecutive Ones III

**Problem Statement**  
Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`s if you can flip at most `k` zeros.

**Approach: Variable Sliding Window**
- Expand the window using the right pointer
- Decrease `k` when encountering `0`
- If `k < 0`, shrink the window from the left
- Track the maximum window size

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

---

### 4️⃣ Subarray Product Less Than K

**Problem Statement**  
Given an array of positive integers `nums` and an integer `k`, return the number of contiguous subarrays where the product is strictly less than `k`.

**Approach: Sliding Window**
- Maintain a running product
- Shrink the window when product ≥ `k`
- Count valid subarrays ending at each index

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

---

### 5️⃣ Subarrays with K Distinct Integers

**Problem Statement**  
Return the number of contiguous subarrays that contain exactly `k` distinct integers.

**Approach: Sliding Window with Two Left Pointers**
- Use a frequency map to track elements
- `l2` maintains at most `k` distinct elements
- `l1` tracks valid starting points
- Count valid subarrays efficiently

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(k)`

---

### 6️⃣ Fruit Into Baskets

**Problem Statement**  
You are given an array `fruits` where `fruits[i]` represents the type of fruit on the `iᵗʰ` tree.  
You have two baskets and each basket can carry only one type of fruit.

Return the maximum number of fruits you can collect in a contiguous segment.

**Approach: Sliding Window**
- Window contains at most 2 distinct fruit types
- Expand window until invalid
- Shrink from the left when more than 2 types exist

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

---

### 7️⃣ Minimum Size Subarray Sum

**Problem Statement**  
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray whose sum is greater than or equal to `target`.

If no such subarray exists, return `0`.

**Approach: Variable Sliding Window**
- Expand the window until sum ≥ target
- Shrink window to minimize length
- Track the smallest valid window

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

---

### 8️⃣ Sliding Window Maximum

**Problem Statement**  
Given an integer array `nums` and an integer `k`, return the maximum value in every sliding window of size `k`.

**Approach: Heap (Priority Queue)**

We use a **max heap** to efficiently track the maximum element in the current window.

**Algorithm**
1. Initialize an empty heap and result array
2. Iterate through the array:
   - Push `(-nums[i], i)` into the heap
   - Remove heap elements whose index ≤ `i - k`
3. Once the window size reaches `k`, append the current maximum to the result
4. Continue until the end of the array

**Time Complexity:** `O(nlogn)`  
**Space Complexity:** `O(n)`

---

## 🚀 Key Concepts Used
- Sliding Window (Fixed & Variable Size)
- Two Pointer Technique
- Hash Maps for Frequency Counting
- Optimal Window Expansion & Shrinking
- Heaps (Priority Queue)

---

## 🧠 Why Sliding Window?
- Reduces time complexity from `O(n²)` to `O(n)`
- Ideal for contiguous subarray problems
- Frequently asked in FAANG and product-based company interviews

---

## 📂 Repository Goal
This repository is part of my DSA journey where I am solving **375 curated problems** concept-wise to build strong interview fundamentals.

---

⭐ If you find this repository helpful, don’t forget to star it!  
Happy Coding 🚀
