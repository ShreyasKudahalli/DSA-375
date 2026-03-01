# 🔢 Frequency Map / Counting Technique

The **Frequency Map (Counting) technique** is a fundamental approach in data structures and algorithms used to track how many times elements appear in a dataset. By leveraging a hash map (dictionary), we can efficiently count occurrences of characters, numbers, or objects in linear time, enabling optimized solutions for problems involving duplicates, majority elements, anagrams, sorting by frequency, and pattern matching. This technique is widely used in competitive programming and coding interviews because it simplifies complex counting logic into a clean, scalable, and high-performance solution.


## 1️⃣ Majority Element (Hash Map Approach)

### 📌 Problem Statement

Given an integer array `nums` of size `n`, return the **majority element**.

The majority element is the element that appears **more than ⌊n / 2⌋ times** in the array.

> ✅ It is guaranteed that the majority element always exists.

---

### 🧠 Approach — Hash Map (Frequency Counting)

We use a **dictionary (hash map)** to count the frequency of each element while iterating through the array.

#### 🔹 Key Idea

* Traverse the array once.
* Store frequency of each element in a dictionary.
* The moment any element's frequency becomes greater than `n // 2`, return it immediately.

This avoids unnecessary full traversal after counting.

---

### 🔍 Example

#### Input

```
nums = [2, 2, 1, 1, 1, 2, 2]
```

#### Frequency Progression

| Element | Count |
| ------- | ----- |
| 2       | 1     |
| 2       | 2     |
| 1       | 1     |
| 1       | 2     |
| 1       | 3     |
| 2       | 3     |
| 2       | 4 ✅   |

Since `n = 7`,
`n // 2 = 3`

Element `2` appears `4` times → Majority Element = **2**

---

### ⏱ Time & Space Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(n)  |

* We traverse the array once.
* In worst case, store all elements in dictionary.

---

### 🎯 Why This Works

* Majority element appears more than half the time.
* As soon as its count crosses `n // 2`, it must be the answer.
* No need to sort the array.

---

### 🧩 Alternative Approaches (For Interviews)

* 🔹 Sorting (O(n log n))
* 🔹 Boyer-Moore Voting Algorithm (O(n) time, O(1) space ⭐ optimal)
* 🔹 Brute Force (O(n²))

---

### 🚀 Interview Insight

This solution is:

* Easy to implement
* Good starting approach
* Clear demonstration of hash map usage

However, for optimized space complexity, interviewers may expect **Boyer-Moore Voting Algorithm**.


---


## 2️⃣ Sort Characters by Frequency

### 📌 Problem Statement

Given a string `s`, sort it in **decreasing order based on the frequency of characters**.

The frequency of a character is the number of times it appears in the string.

> If multiple answers exist, return any valid result.

---

### 🧠 Approach — Hash Map + Sorting

We solve this problem in **three main steps**:

#### 1️⃣ Count Frequency

Use a dictionary to store how many times each character appears.

#### 2️⃣ Sort by Frequency

Sort the dictionary items in **descending order** based on frequency.

#### 3️⃣ Build Result String

Repeat each character according to its frequency and concatenate them.

---

### 🔍 Example

#### Input

```
s = "tree"
```

#### Frequency Count

| Character | Count |
| --------- | ----- |
| t         | 1     |
| r         | 1     |
| e         | 2     |

#### Sorted by Frequency (Descending)

```
e → 2  
t → 1  
r → 1
```

#### Output

```
"eetr"
```

(or `"eert"` — both are valid)

---

### ⏱ Time & Space Complexity

| Complexity | Value      |
| ---------- | ---------- |
| Time       | O(n log k) |
| Space      | O(k)       |

Where:

* `n` = length of string
* `k` = number of unique characters

Sorting takes `O(k log k)` time.

---

### 🎯 Key Concepts Used

* Hash Map (Dictionary)
* Sorting with Custom Key
* String Manipulation
* Frequency Counting


---

