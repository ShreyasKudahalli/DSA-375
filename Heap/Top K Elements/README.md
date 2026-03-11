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


## 3️⃣ Kth Largest Element in an Array

### 📌 Problem Statement

Given an integer array `nums` and an integer `k`, return the **kth largest element** in the array.

> Note: It is the **kth largest element in the sorted order**, not the kth distinct element.

---

### 🧠 Approach — Min Heap (Priority Queue)

To efficiently find the **kth largest element**, we use a **Min Heap** of size `k`.

#### 🔹 Key Idea

* Maintain a heap that stores **only the k largest elements seen so far**.
* The smallest element in this heap will represent the **kth largest element** in the array.

Steps:

1. Iterate through the array.
2. Push each element into the heap.
3. If heap size becomes greater than `k`, remove the smallest element.
4. After processing all elements, the root of the heap is the **kth largest element**.

---

### 🚀 Algorithm Steps

1️⃣ Initialize an empty heap.

2️⃣ Traverse each number in the array.

3️⃣ Insert the number into the heap.

4️⃣ If heap size exceeds `k`, remove the smallest element.

5️⃣ Return the root of the heap (`heap[0]`).

---

### 🔍 Example

#### Input

```
nums = [3,2,1,5,6,4]
k = 2
```

#### Heap Process

| Step   | Heap                  |
| ------ | --------------------- |
| Push 3 | [3]                   |
| Push 2 | [2,3]                 |
| Push 1 | [1,3,2] → pop → [2,3] |
| Push 5 | [2,3,5] → pop → [3,5] |
| Push 6 | [3,5,6] → pop → [5,6] |
| Push 4 | [4,6,5] → pop → [5,6] |

#### Output

```
5
```

The **2nd largest element** is `5`.

---

### ⏱ Time & Space Complexity

| Complexity | Value      |
| ---------- | ---------- |
| Time       | O(n log k) |
| Space      | O(k)       |

Where:

* `n` = number of elements in the array.

Heap size is always limited to `k`.

---

### 🎯 Key Concepts Used

* Heap (Priority Queue)
* Min Heap Optimization
* Top K Pattern
* Efficient Element Selection

---

### 🔥 Why This Approach Works

Instead of sorting the entire array (**O(n log n)**), we maintain a heap of size `k`.

This ensures:

* Faster performance
* Lower memory usage
* Efficient extraction of the kth largest element


---


## 4️⃣ Top K Frequent Elements

### 📌 Problem Statement

Given an integer array `nums` and an integer `k`, return the **k most frequent elements**.

You may return the answer in **any order**.

---

### 🧠 Approach — Frequency Map + Min Heap

To efficiently find the **k most frequent elements**, we use:

* **Frequency Map (`Counter`)** to count occurrences of each number.
* **Min Heap (Priority Queue)** to maintain the top `k` frequent elements.

#### 🔹 Key Idea

Instead of storing all elements in a heap, we maintain a **min heap of size `k`**.

Steps:

1. Count the frequency of each number.
2. Push `(frequency, number)` into the heap.
3. If heap size exceeds `k`, remove the smallest frequency.
4. At the end, the heap contains the **k most frequent elements**.

This keeps the heap size limited and improves efficiency.

---

### 🚀 Algorithm Steps

1️⃣ Compute frequency using `Counter`.

2️⃣ Iterate through each `(number, frequency)` pair.

3️⃣ Push `(frequency, number)` into the heap.

4️⃣ If heap size becomes greater than `k`, remove the smallest element.

5️⃣ Extract numbers from the heap.

---
### 🔍 Example

#### Input

```
nums = [1,1,1,2,2,3]
k = 2
```

#### Frequency Count

| Number | Frequency |
| ------ | --------- |
| 1      | 3         |
| 2      | 2         |
| 3      | 1         |

#### Output

```
[1,2]
```

Explanation:

The two most frequent elements are **1** and **2**.

---

### ⏱ Time & Space Complexity

| Complexity | Value      |
| ---------- | ---------- |
| Time       | O(n log k) |
| Space      | O(n)       |

Where:

* `n` = number of elements in the array.

The heap size is maintained at **k**, making operations efficient.

---

### 🎯 Key Concepts Used

* Hash Map / Frequency Counting
* Heap (Priority Queue)
* Min Heap Optimization
* Top K Pattern

---

### 🔥 Why Use a Min Heap of Size K?

Instead of storing all elements in a heap:

* We maintain **only the top k elements**
* The smallest frequency stays at the root
* If a larger frequency appears, it replaces the smallest

This keeps the heap small and improves performance.


---


## 5️⃣ Find Median from Data Stream

### 📌 Problem Statement

Design a data structure that supports the following operations efficiently:

* **addNum(num)** → Add a number to the data stream.
* **findMedian()** → Return the median of all elements added so far.

The **median** is:

* The middle element in a sorted list if the number of elements is odd.
* The average of the two middle elements if the number of elements is even.

---

### 🧠 Approach — Two Heaps (Max Heap + Min Heap)

To efficiently maintain the median while numbers are continuously added, we use **two heaps**:

| Heap                   | Purpose                            |
| ---------------------- | ---------------------------------- |
| **Max Heap (`small`)** | Stores the smaller half of numbers |
| **Min Heap (`large`)** | Stores the larger half of numbers  |

Since Python only supports **min heap**, we simulate a **max heap** by pushing **negative values**.

---

### 🔹 Key Idea

We maintain two important properties:

1️⃣ **Order Property**

```
max(small) <= min(large)
```

All elements in `small` must be less than or equal to elements in `large`.

2️⃣ **Size Property**

The heaps should have sizes:

```
len(small) == len(large)
or
len(small) == len(large) + 1
```

This ensures the median can be calculated easily.

---

### 🚀 Algorithm

#### addNum(num)

1. Push the number into the **max heap (`small`)**.
2. If the largest value in `small` is greater than the smallest value in `large`, move it to `large`.
3. Balance the heap sizes:

   * If `small` has more than one extra element → move one to `large`.
   * If `large` has more elements → move one to `small`.

#### findMedian()

* If `small` has more elements → median is the top of `small`.
* If both heaps have equal size → median is the average of the two tops.

---

### 🔍 Example

#### Operations

```
addNum(1)
addNum(2)
findMedian() → 1.5
addNum(3)
findMedian() → 2
```

#### Heap State

| Step  | small (max heap) | large (min heap) | Median |
| ----- | ---------------- | ---------------- | ------ |
| add 1 | [1]              | []               | 1      |
| add 2 | [1]              | [2]              | 1.5    |
| add 3 | [2,1]            | [3]              | 2      |

---

### ⏱ Time & Space Complexity

| Operation  | Complexity |
| ---------- | ---------- |
| addNum     | O(log n)   |
| findMedian | O(1)       |
| Space      | O(n)       |

Where `n` is the number of elements added.

---

### 🎯 Key Concepts Used

* Heap (Priority Queue)
* Max Heap Simulation using Negative Values
* Min Heap
* Balanced Data Structures
* Streaming Data Processing

---

### 🔥 Why Two Heaps Work

Using two heaps allows us to:

* Maintain sorted order **implicitly**
* Access middle values **in constant time**
* Insert numbers efficiently

This makes the solution ideal for **real-time streaming data**.


---