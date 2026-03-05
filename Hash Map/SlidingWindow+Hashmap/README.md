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

