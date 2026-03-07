# 🪟 Sliding Window + Hash Map Technique

The **Sliding Window + Hash Map** technique is a powerful pattern used to efficiently solve substring and subarray problems involving constraints like uniqueness, frequency limits, or target sums. By maintaining a dynamic window using two pointers and leveraging a hash map to track counts or last-seen positions, we can expand and shrink the window intelligently without reprocessing elements. This approach reduces brute-force solutions from O(n²) to O(n) time, making it essential for solving problems like longest substring without repeating characters, minimum window substring, and anagram detection in coding interviews and competitive programming.


## 1️⃣ Longest Substring Without Repeating Characters

### 📌 Problem Statement

Given a string `s`, return the **length of the longest substring** without repeating characters.

A substring must be:

* Continuous
* Contain **unique characters only**

---

### 🧠 Approach — Sliding Window + Hash Map

We use the **Sliding Window technique** combined with a **Hash Map** to efficiently track character positions.

#### 🔹 Key Idea

* Maintain a window defined by two pointers:

  * `left` → Start of window
  * `right` → End of window
* Use a dictionary (`last_seen`) to store the last index where each character appeared.
* If a duplicate character appears inside the current window:

  * Move `left` pointer just after the previous occurrence.

This ensures:

* No repeated characters inside the window.
* Each character is processed once → O(n) time.

---

### 🚀 Algorithm Steps

1️⃣ Initialize:

* `left = 0`
* `max_length = 0`
* `last_seen = {}`

2️⃣ Iterate with `right` pointer:

* If character already seen **inside current window**, update `left`.
* Update character’s last seen index.
* Update maximum length.

---

### 🔍 Example

#### Input

```
s = "abcabcbb"
```

#### Window Movement

| Step       | Window    | Length |
| ---------- | --------- | ------ |
| a          | "a"       | 1      |
| b          | "ab"      | 2      |
| c          | "abc"     | 3 ✅    |
| a (repeat) | move left |        |
| b (repeat) | move left |        |
| c (repeat) | move left |        |

#### Output

```
3
```

Longest substring = `"abc"`

---

### ⏱ Time & Space Complexity

| Complexity | Value        |
| ---------- | ------------ |
| Time       | O(n)         |
| Space      | O(min(n, m)) |

Where:

* `n` = length of string
* `m` = size of character set

Each character is visited at most twice.

---

### 🎯 Key Concepts Used

* Sliding Window
* Two Pointers
* Hash Map (Last Seen Index)
* Dynamic Window Adjustment

---

### 🔥 Why This Approach is Optimal

* Avoids brute force O(n²)
* Processes string in one pass
* Efficient and interview-friendly
* Works for all ASCII/Unicode characters


---


## 2️⃣ Fruits Into Baskets

### 📌 Problem Statement

You are given an integer array `fruits` where `fruits[i]` represents the type of fruit on the `iᵗʰ` tree.

You have **two baskets**, and each basket can hold **only one type of fruit**, but **unlimited quantity** of that type.

Starting from any tree, you must pick exactly **one fruit from each tree moving to the right**, and you must stop when you encounter a fruit that cannot fit into your baskets.

Return the **maximum number of fruits you can collect**.

---

### 🧠 Approach — Sliding Window + Hash Map

This problem is equivalent to finding the **longest subarray containing at most 2 distinct numbers**.

We use a **sliding window technique** with a **hash map** to keep track of fruit counts inside the current window.

#### 🔹 Key Idea

* Use two pointers:

  * `l` → left boundary of window
  * `r` → right boundary of window
* Maintain a dictionary `basket` to track how many fruits of each type exist in the window.
* If the number of fruit types exceeds **2**, shrink the window from the left.

---

### 🚀 Algorithm Steps

1️⃣ Initialize:

* `l = 0`
* `res = 0`
* `basket = {}`

2️⃣ Expand the window using `r`.

3️⃣ Add fruit to the basket (increase count).

4️⃣ If basket contains **more than 2 fruit types**:

* Shrink window from the left
* Reduce count
* Remove fruit type when count becomes `0`.

5️⃣ Update maximum window size.

---

### 🔍 Example

#### Input

```
fruits = [1,2,1]
```

#### Output

```
3
```

Explanation:

You can pick fruits `[1,2,1]` using two baskets.

---

#### Another Example

Input

```
fruits = [1,2,3,2,2]
```

Output

```
4
```

Subarray:

```
[2,3,2,2]
```

---

### ⏱ Time & Space Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(1)  |

* Each element is processed at most **twice**.
* Basket holds at most **2 fruit types**.

---

### 🎯 Key Concepts Used

* Sliding Window
* Two Pointer Technique
* Hash Map (Frequency Counting)
* Longest Subarray with K Distinct Elements

---

### 🔥 Pattern Recognition

This problem is a classic example of:

**Longest Subarray with At Most K Distinct Elements**

Where:

```
K = 2
```

---


## 3️⃣ Find All Anagrams in a String

### 📌 Problem Statement

Given two strings `s` and `p`, return a list of **all starting indices of `p`'s anagrams in `s`**.

An **anagram** is a word or phrase formed by rearranging the letters of another word using **all the original letters exactly once**.

---

### 🧠 Approach — Sliding Window + Frequency Map

To efficiently find all anagrams of `p` in `s`, we use:

* **Sliding Window Technique**
* **Hash Map (Frequency Counting)**

#### 🔹 Key Idea

* Maintain a window of size equal to `len(p)`.
* Track character frequencies in:

  * `p_count` → frequency of characters in `p`
  * `window_count` → frequency of characters in the current window of `s`
* If the two frequency maps match, the current window forms an **anagram**.

---

### 🚀 Algorithm Steps

1️⃣ If `p` is longer than `s`, return an empty list.

2️⃣ Build a frequency map for string `p`.

3️⃣ Use a sliding window over `s`:

* Expand the window by moving `right`.
* Update frequency of the current character.

4️⃣ If window size exceeds `len(p)`:

* Remove the leftmost character from the window.

5️⃣ Compare frequency maps:

* If equal → record the starting index.

---

### 🔍 Example

#### Input

```
s = "cbaebabacd"
p = "abc"
```

#### Output

```
[0, 6]
```

#### Explanation

Substrings of `s` that are anagrams of `"abc"`:

| Index | Substring | Reason                   |
| ----- | --------- | ------------------------ |
| 0     | `"cba"`   | Rearrangement of `"abc"` |
| 6     | `"bac"`   | Rearrangement of `"abc"` |

---

### ⏱ Time & Space Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(1)  |

Where:

* `n` = length of string `s`

Space is **O(1)** because the frequency map stores characters from a fixed alphabet (at most 26 lowercase letters).

---

### 🎯 Key Concepts Used

* Sliding Window
* Two Pointer Technique
* Hash Map / Frequency Counting
* String Anagram Detection

---

### 🔥 Why Sliding Window Works Here

Instead of checking every substring (which would take **O(n × m)** time), we maintain a **moving window** of size `len(p)` and update counts dynamically.

This reduces the time complexity to **linear time**.


---
