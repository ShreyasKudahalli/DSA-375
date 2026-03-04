# 🔁 Prefix Sum with Hash Map Technique

The **Prefix Sum with Hash Map** technique is a powerful pattern used to efficiently solve subarray problems involving sums, divisibility, or frequency conditions in linear time. By maintaining a running cumulative sum and storing previously seen prefix sums (or their remainders) in a dictionary, we can quickly determine whether a valid subarray exists without recomputing sums repeatedly. This approach is widely used for problems like subarray sum equals `k`, subarray sums divisible by `k`, and longest or count-based subarray variations, making it a must-know concept for coding interviews and competitive programming.



## 1️⃣ Subarray Sum Equals K

### 📌 Problem Statement

Given an integer array `nums` and an integer `k`, return the **total number of continuous subarrays** whose sum equals `k`.

A **subarray** is a contiguous part of an array.

---

### 🧠 Approach — Prefix Sum + Hash Map

To solve this efficiently, we use:

* **Prefix Sum** to keep track of cumulative sums.
* **Hash Map (Dictionary)** to store the frequency of prefix sums encountered so far.

#### 🔹 Key Insight

If:

```
current_prefix_sum = total
```

And we want:

```
subarray_sum = k
```

Then:

```
previous_prefix_sum = total - k
```

If we have seen `total - k` before, it means there exists a subarray ending at the current index whose sum equals `k`.

---

### 🚀 Why Initialize `{0: 1}`?

We initialize:

```python
count = {0: 1}
```

This handles cases where a subarray starting from index `0` itself sums to `k`.

---

### 🔍 Example

#### Input

```
nums = [1, 1, 1]
k = 2
```

#### Step-by-Step

| Index | Number | Prefix Sum | total - k | Found? | Result |
| ----- | ------ | ---------- | --------- | ------ | ------ |
| 0     | 1      | 1          | -1        | ❌      | 0      |
| 1     | 1      | 2          | 0         | ✅      | 1      |
| 2     | 1      | 3          | 1         | ✅      | 2      |

#### Output

```
2
```

There are 2 subarrays with sum = 2:

* `[1,1]` (index 0–1)
* `[1,1]` (index 1–2)

---

### ⏱ Time & Space Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(n)  |

* Each element is processed once.
* Hash map stores prefix sums.

---

### 🎯 Key Concepts Used

* Prefix Sum
* Hash Map / Frequency Counting
* Subarray Properties
* Cumulative Sum Optimization

---

### 🔥 Why This Approach is Powerful

* Works with **negative numbers** (unlike sliding window).
* Avoids brute force O(n²).
* Very common interview pattern.
* Used in many advanced variations.


---


## 2️⃣ Continuous Subarray Sum (Multiple of K)

### 📌 Problem Statement

Given an integer array `nums` and an integer `k`, return **True** if the array contains a continuous subarray of size **at least 2** whose sum is a multiple of `k`. Otherwise, return **False**.

A subarray must:

* Be **continuous**
* Have **length ≥ 2**
* Satisfy:

  ```
  sum % k == 0
  ```

---

### 🧠 Approach — Prefix Sum + Remainder Hashing

#### 🔹 Key Idea

If two prefix sums have the **same remainder when divided by `k`**, then the subarray between them has a sum divisible by `k`.

Why?

If:

```
prefix_sum[i] % k == prefix_sum[j] % k
```

Then:

```
(prefix_sum[i] - prefix_sum[j]) % k == 0
```

Which means the subarray between `j+1` and `i` is divisible by `k`.

---

### 🚀 Strategy

- 1️⃣ Maintain a running prefix sum (`total`).
- 2️⃣ Compute remainder `rem = total % k`.
- 3️⃣ Store first occurrence of each remainder in a dictionary.
- 4️⃣ If the same remainder appears again:

* Check if the subarray length is ≥ 2
* If yes → return `True`

---

### 🔹 Why Initialize `{0: -1}`?

```python
rem_index = {0 : -1}
```

This handles cases where:

* A subarray starting from index `0` itself forms a valid answer.

---

### 🔍 Example

#### Input

```
nums = [23, 2, 4, 6, 7]
k = 6
```

#### Prefix Sums & Remainders

| Index | Value | Prefix Sum | Remainder (mod 6) |
| ----- | ----- | ---------- | ----------------- |
| 0     | 23    | 23         | 5                 |
| 1     | 2     | 25         | 1                 |
| 2     | 4     | 29         | 5 ✅               |

Remainder `5` appears again.

Subarray from index `1` to `2`:

```
[2, 4] → sum = 6 → divisible by 6
```

✅ Output: `True`

---

### ⏱ Time & Space Complexity

| Complexity | Value        |
| ---------- | ------------ |
| Time       | O(n)         |
| Space      | O(min(n, k)) |

* We traverse array once.
* Dictionary stores at most `k` remainders.

---

### 🎯 Key Concepts Used

* Prefix Sum
* Modulo Arithmetic
* Hash Map (Remainder Tracking)
* Subarray Length Validation
* Mathematical Observation

---

### ⚠️ Important Edge Cases

* `k = 0` (needs special handling in some variations)
* Negative numbers in array
* Multiple same remainders
* Minimum subarray length constraint (≥ 2)

---

### 🔥 Why This Pattern is Important

This is a very common interview pattern combining:

* Prefix sums
* Modulo properties
* Hashing

It appears in many advanced variations like:

* Subarray Sum Divisible by K
* Count Subarrays with Sum Multiple of K
* Equal 0s and 1s
* Longest Subarray with Given Condition


---


## 3️⃣ Subarrays Divisible by K

### 📌 Problem Statement

Given an integer array `nums` and an integer `k`, return the **total number of continuous subarrays** whose sum is divisible by `k`.

A subarray must be:

* Continuous
* Have sum such that

  ```
  sum % k == 0
  ```

---

### 🧠 Approach — Prefix Sum + Remainder Frequency Map

#### 🔹 Key Insight

If two prefix sums have the **same remainder when divided by `k`**, then the subarray between them has a sum divisible by `k`.

Why?

If:

```
prefix_sum[i] % k == prefix_sum[j] % k
```

Then:

```
(prefix_sum[i] - prefix_sum[j]) % k == 0
```

So the subarray between `j+1` and `i` is divisible by `k`.

---

### 🚀 Strategy

- 1️⃣ Maintain a running sum (`total`).
- 2️⃣ Compute remainder:

```
remainder = total % k
```

- 3️⃣ Use a dictionary to count how many times each remainder appears.
- 4️⃣ If the same remainder appears again, it means we found new valid subarrays.

---

## 🔹 Why Initialize `{0: 1}`?

```python
count = {0: 1}
```

This handles cases where:

* A prefix sum itself is divisible by `k`.
* Subarray starting from index `0` is valid.

---

### 🔍 Example

#### Input

```
nums = [4, 5, 0, -2, -3, 1]
k = 5
```

#### Output

```
7
```

There are 7 subarrays whose sum is divisible by 5.

---

### 🧩 How Counting Works

If a remainder `r` appears `f` times, then it contributes:

```
fC2 = f * (f - 1) / 2
```

valid subarrays.

Our code dynamically counts these combinations while iterating.

---

### ⏱ Time & Space Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(k)  |

* Each element is processed once.
* Dictionary stores at most `k` different remainders.

---

### 🎯 Key Concepts Used

* Prefix Sum
* Modulo Arithmetic
* Hash Map (Frequency Counting)
* Subarray Properties
* Mathematical Observation

---

### ⚠️ Important Note (Negative Numbers)

In some languages, negative modulo may give negative remainder.
In Python, `%` already returns a non-negative remainder.

In other languages, you may need:

```python
remainder = (total % k + k) % k
```

---

### 🔥 Why This Pattern is Important

This is a very common and powerful interview pattern used in:

* Subarray Sum Equals K
* Continuous Subarray Sum
* Count Subarrays with Given Condition
* Equal 0s and 1s
* Longest Subarray with Constraint


---
