# Heap for Top K Elements

The **Heap (Priority Queue) technique for Top K Elements** is a powerful approach used to efficiently retrieve the most frequent, largest, or smallest `k` elements from a dataset. Instead of sorting the entire data (which takes **O(n log n)** time), a heap allows us to maintain priority order and extract the required elements in **O(n log k)** or **O(n log n)** depending on implementation. By combining a **frequency map** with a **heap**, we can solve problems like Top K Frequent Elements, Top K Frequent Words, and K Closest Points efficiently, making this pattern a common and important technique in coding interviews and large-scale data processing.


## 1️⃣ Sort Characters by Frequency

### 📌 Problem Statement

Given a string `s`, sort it in **decreasing order based on the frequency of characters**.

The **frequency of a character** is the number of times it appears in the string.

Return the sorted string. If multiple valid answers exist, return **any of them**.

---

### 🧠 Approach — Frequency Map + Max Heap

To efficiently sort characters by their frequency, we use:

* **Frequency Map (`Counter`)** to count occurrences of each character.
* **Max Heap (Priority Queue)** to always extract the character with the highest frequency.

#### 🔹 Key Idea

1. Count how many times each character appears.
2. Push characters into a **max heap** based on frequency.
3. Continuously pop the character with the highest frequency and append it to the result.

Since Python’s `heapq` implements a **min heap**, we store frequencies as **negative values** to simulate a **max heap**.

---

### 🚀 Algorithm Steps

1️⃣ Count character frequencies using `Counter`.

2️⃣ Push `(−frequency, character)` into a heap.

3️⃣ Pop elements from the heap:

* The character with the highest frequency comes first.

4️⃣ Append the character `frequency` number of times to the result.

5️⃣ Join all parts into the final string.

---

### 🔍 Example

#### Input

```
s = "tree"
```

#### Frequency Count

| Character | Frequency |
| --------- | --------- |
| t         | 1         |
| r         | 1         |
| e         | 2         |

#### Output

```
"eert"
```

Another valid output:

```
"eetr"
```

Both are correct since `'e'` appears most frequently.

---

### ⏱ Time & Space Complexity

| Complexity | Value      |
| ---------- | ---------- |
| Time       | O(n log k) |
| Space      | O(n)       |

Where:

* `n` = length of string
* `k` = number of unique characters

Building the heap takes **O(k)** and each heap operation takes **O(log k)**.

---

### 🎯 Key Concepts Used

* Hash Map / Frequency Counting
* Heap (Priority Queue)
* Greedy Selection
* String Construction

---

### 🔥 Why Use a Heap?

A heap allows us to **efficiently retrieve the character with the highest frequency** each time, making the algorithm scalable for large inputs.


---


## 2️⃣ Top K Frequent Words

### 📌 Problem Statement

Given a list of strings `words` and an integer `k`, return the **k most frequent words**.

The result should be sorted according to:

1. **Frequency (highest first)**
2. **Lexicographical order (alphabetical order) if frequencies are equal**

---

### 🧠 Approach — Frequency Map + Max Heap

To efficiently determine the top `k` frequent words, we use:

* **Frequency Map (`Counter`)** to count how often each word appears.
* **Heap (Priority Queue)** to extract words with the highest frequency.

#### 🔹 Key Idea

1. Count frequency of each word.
2. Push elements into a heap using:

   ```
   (-frequency, word)
   ```
3. The negative frequency converts Python’s **min heap** into a **max heap**.
4. If two words have the same frequency, Python automatically sorts them **lexicographically**.

---

### 🚀 Algorithm Steps

1️⃣ Count word frequencies using `Counter`.

2️⃣ Push each `(−frequency, word)` into the heap.

3️⃣ Extract the top `k` elements from the heap.

4️⃣ Return the words in order.

---

### 🔍 Example

#### Input

```
words = ["i","love","leetcode","i","love","coding"]
k = 2
```

#### Frequency Count

| Word     | Frequency |
| -------- | --------- |
| i        | 2         |
| love     | 2         |
| leetcode | 1         |
| coding   | 1         |

#### Output

```
["i","love"]
```

Explanation:

* `"i"` and `"love"` have the highest frequency (2).
* Since frequencies are equal, they are sorted **alphabetically**.

---

### ⏱ Time & Space Complexity

| Complexity | Value      |
| ---------- | ---------- |
| Time       | O(n log n) |
| Space      | O(n)       |

Where:

* `n` = number of words in the input list.

Heap operations take **O(log n)** time.

---

### 🎯 Key Concepts Used

* Hash Map / Frequency Counting
* Heap (Priority Queue)
* Greedy Selection
* Lexicographical Sorting

---

### 🔥 Why Use a Heap?

A heap allows us to **efficiently retrieve the most frequent elements** without sorting the entire dataset.

This makes the solution scalable for large inputs.


---
