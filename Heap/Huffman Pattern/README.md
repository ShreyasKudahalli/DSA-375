# Huffman Pattern

The **Huffman Pattern** is a greedy algorithmic technique used in problems where we repeatedly **combine the two smallest elements to achieve an optimal overall cost or structure**. It is inspired by **Huffman Coding**, a compression algorithm that builds an optimal binary tree by merging the least frequent characters first. In many algorithm problems, this pattern is implemented using a **Min Heap (Priority Queue)** to efficiently extract the two smallest values, combine them, and insert the result back into the heap until only one element remains. This approach ensures minimal total cost or optimal arrangement and is commonly used in problems like **connecting ropes with minimum cost, file merging, optimal merge patterns, and Huffman encoding**.


## 1️⃣ Minimum Cost to Connect Ropes

### 📌 Problem Statement

You are given an array `arr` representing the **lengths of ropes**.
The task is to **connect all the ropes into one rope** with the **minimum possible cost**.

#### Cost Rule

When two ropes are connected:

```
cost = length1 + length2
```

The resulting rope with length `(length1 + length2)` is then added back to the ropes list and can be used for further connections.

The goal is to **minimize the total cost of connecting all ropes**.

---

### 🧠 Approach — Greedy + Min Heap

To minimize the total cost, we should **always connect the two smallest ropes first**.

Why?

Connecting larger ropes earlier would increase the total cost significantly because their combined length will be used again in future connections.

A **Min Heap (Priority Queue)** helps efficiently retrieve the **two smallest ropes** every time.

#### Strategy

1. Convert the array into a **Min Heap**.
2. Repeatedly:

   * Extract the **two smallest ropes**.
   * Calculate their connection cost.
   * Add the cost to the total cost.
   * Insert the combined rope back into the heap.
3. Continue until only **one rope remains**.

This greedy strategy guarantees the **minimum total cost**.

---

### 🚀 Algorithm Steps

1️⃣ Convert the array into a **min heap**

```python
heapq.heapify(arr)
```

2️⃣ Initialize `total_cost = 0`

3️⃣ While more than one rope exists:

* Pop the two smallest ropes
* Compute their connection cost
* Add the cost to `total_cost`
* Push the combined rope back into the heap

4️⃣ Return `total_cost`

---

### 🔍 Example

#### Input

```
arr = [4, 3, 2, 6]
```

#### Steps

| Rope1 | Rope2 | Cost | New Heap |
| ----- | ----- | ---- | -------- |
| 2     | 3     | 5    | [4,5,6]  |
| 4     | 5     | 9    | [6,9]    |
| 6     | 9     | 15   | [15]     |

#### Total Cost

```
5 + 9 + 15 = 29
```

#### Output

```
29
```

---

### ⏱ Time & Space Complexity

| Complexity | Value          |
| ---------- | -------------- |
| Time       | **O(n log n)** |
| Space      | **O(n)**       |

Explanation:

* Building the heap takes **O(n)**.
* Each pop/push operation takes **O(log n)**.
* We perform about **n operations**.

---

### 🔑 Key Concepts Used

* Min Heap (Priority Queue)
* Greedy Algorithm
* Heapify Operation
* Optimal Merge Pattern

---

### ⚠️ Important Insight

This problem is a classic example of the **Optimal Merge Pattern**, where merging smaller elements first results in the **lowest overall cost**.

This same principle is used in:

* **Huffman Coding**
* **File merging algorithms**
* **Optimal merge patterns in external sorting**


---


## 2️⃣ Reorganize String

### 📌 Problem Statement

Given a string `s`, rearrange its characters so that **no two adjacent characters are the same**.

If such a rearrangement is possible, return the **reorganized string**. Otherwise, return an **empty string**.

Example:

```text
Input:  s = "aab"
Output: "aba"
```

```text
Input:  s = "aaab"
Output: ""
```

In the second example, it's impossible to rearrange the characters without placing two `a` characters next to each other.

---

### 🧠 Approach — Greedy + Max Heap

To avoid placing the same character next to itself, we always choose the **character with the highest remaining frequency** that is **different from the previously placed character**.

To efficiently get the most frequent character each time, we use a **Max Heap**.

Since Python provides only a **Min Heap**, we store frequencies as **negative values**.

#### Key Idea

1. Count the frequency of each character.
2. Push `(−frequency, character)` into a heap.
3. Always pick the character with the **highest frequency**.
4. Temporarily hold the **previous character** so it isn’t reused immediately.
5. Push the previous character back into the heap once it becomes safe to use again.

This ensures **no two adjacent characters are the same**.

---

### 🚀 Algorithm Steps

1️⃣ Count the frequency of each character using `Counter`.

2️⃣ Create a **max heap** using negative frequencies.

3️⃣ Maintain:

* `prev` → the previously used character
* `result` → the final string being built

4️⃣ While the heap is not empty:

* Pop the character with the highest frequency.
* Add it to the result.
* If the previous character still has remaining frequency, push it back into the heap.
* Update the current character's frequency.
* Store it as `prev`.

5️⃣ After the loop, check:

```python
if len(result) != len(s)
```

If true → return `""` because a valid reorganization isn't possible.

---

### 🔍 Example

#### Input

```text
s = "aab"
```

#### Frequency Map

```text
a → 2
b → 1
```

#### Heap

```text
[(-2, 'a'), (-1, 'b')]
```

#### Steps

| Step | Heap Pop | Result | Prev    |
| ---- | -------- | ------ | ------- |
| 1    | a        | a      | (-1, a) |
| 2    | b        | ab     | (0, b)  |
| 3    | a        | aba    | (0, a)  |

#### Output

```text
"aba"
```

---

### ⏱ Time & Space Complexity

| Complexity | Value          |
| ---------- | -------------- |
| Time       | **O(n log k)** |
| Space      | **O(k)**       |

Where:

* `n` = length of string
* `k` = number of unique characters

Heap operations take **log k** time.

---

### 🔑 Key Concepts Used

* Max Heap (Priority Queue)
* Greedy Algorithm
* Frequency Counting
* String Construction
* Heap Rebalancing

---

### ⚠️ Important Insight

If the **maximum frequency of any character exceeds `(n + 1) / 2`**, then it is **impossible** to reorganize the string without adjacent duplicates.

Example:

```text
s = "aaab"
```

Here:

```
max frequency = 3
n = 4
(4 + 1) / 2 = 2.5
```

Since `3 > 2.5`, a valid arrangement **does not exist**.

---