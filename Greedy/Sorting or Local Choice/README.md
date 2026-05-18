# Sorting and local choice 
 
Sorting and local choice greedy algorithms solve optimization problems by first arranging data in a meaningful order and then making the best immediate decision at each step without reconsidering previous choices. The core idea is that a locally optimal decision, such as selecting the earliest ending interval, highest value item, or farthest reachable position, gradually leads to a globally optimal solution. These techniques are widely used in interval scheduling, resource allocation, coverage problems, custom sorting, and reachability optimization due to their efficiency and simplicity.


## 1️⃣ Maximum Units on a Truck

### 📌 Problem Statement

You are given:

* `boxTypes[i] = [numberOfBoxes, unitsPerBox]`
* `truckSize` → maximum number of boxes the truck can carry

👉 Return the **maximum total units** that can be loaded onto the truck.

---

### 🚀 Approach: Greedy by Units per Box

#### 🔹 Key Idea

To maximize total units:

* Always pick boxes with the **highest units per box first**

👉 This is a classic greedy optimization strategy.

---

### 🧠 Algorithm

1. Sort `boxTypes` in descending order of:

   * `unitsPerBox`

2. Traverse sorted box types:

   * Take as many boxes as possible
   * Update total units
   * Reduce remaining truck capacity

3. Stop when truck becomes full

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n log n) |
| Space Complexity | O(1)       |

> Sorting dominates the runtime.

---

### 📎 Example

```text id="example"
Input:
boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4

Output:
8
```

---

### 🔍 Dry Run

```text id="dryrun"
Sorted by units:
[[1,3],[2,2],[3,1]]

Take 1 box → 3 units
Total = 3

Take 2 boxes → 4 units
Total = 7

Take 1 box → 1 unit
Total = 8
```

---

### 🌳 Visualization

```text id="visual"
Truck Capacity = 4

[1 box × 3 units]
[2 boxes × 2 units]
[1 box × 1 unit]

Total = 8
```

---

### ✅ Key Points

* Classic **greedy optimization problem**
* Prioritize highest value contribution first
* Similar to fractional knapsack strategy
* Efficient and simple implementation

---

### ⚠️ Edge Cases

* Truck size larger than total boxes
* Single box type
* Equal units per box
* Empty input list

---

### 🏁 Conclusion

This problem demonstrates how greedy sorting can maximize resource utilization by always selecting the highest-value option available at each step.


---


## 2️⃣ Largest Number

### 📌 Problem Statement

You are given:

* `nums` → a list of non-negative integers

👉 Arrange the numbers such that they form the **largest possible number**.

👉 Return the result as a string.

---

### 🚀 Approach: Custom Comparator Sorting

#### 🔹 Key Idea

Normal numeric sorting does not work here.

Instead, compare two numbers `a` and `b` by checking:

```text id="compare"
a + b  vs  b + a
```

👉 If:

* `a+b > b+a`

  * place `a` before `b`

This ensures the final concatenated number is maximized.

---

### 🧠 Algorithm

1. Convert all integers to strings

2. Define custom comparator:

   * Compare concatenated orders:

     * `a+b`
     * `b+a`

3. Sort numbers using custom comparison

4. Join all strings together

5. Handle edge case:

   * If result starts with `'0'`
   * Return `"0"`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n log n) |
| Space Complexity | O(n)       |

---

### 📎 Example

```text id="example"
Input:
nums = [3,30,34,5,9]

Output:
"9534330"
```

---

### 🔍 Dry Run

```text id="dryrun"
Compare:
"9"+"5" = "95"
"5"+"9" = "59"

→ 9 comes before 5

Sorted order:
["9","5","34","3","30"]

Result:
"9534330"
```

---

### 🌳 Visualization

```text id="visual"
3   30

"330" vs "303"

330 > 303
→ place 3 before 30
```

---

### ✅ Key Points

* Uses **custom greedy sorting**
* Concatenation order determines optimality
* Comparator is the core insight
* Important edge case for all zeros

---

### ⚠️ Edge Cases

* All zeros → `"0"`
* Single number
* Numbers with same prefixes
* Very large input sizes

---

### 🏁 Conclusion

This problem demonstrates how custom comparator-based greedy sorting can optimize concatenation order to construct the largest possible number.


---


## 3️⃣ Partition Labels

### 📌 Problem Statement

You are given:

* `s` → a string of lowercase English letters

👉 Partition the string into as many parts as possible such that:

* Each letter appears in **at most one partition**

👉 Return a list containing the size of each partition.

---

### 🚀 Approach: Greedy Character Range Tracking

#### 🔹 Key Idea

Each character has a:

* first occurrence
* last occurrence

👉 A partition must extend until the **last occurrence** of every character included in it.

---

### 🧠 Algorithm

1. Store the last occurrence of every character

2. Traverse the string:

   * Continuously update current partition end

3. If current index reaches partition end:

   * Partition complete
   * Store partition length
   * Start new partition

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(1)       |

> Only 26 lowercase characters are stored.

---

### 📎 Example

```text id="example"
Input:
s = "ababcbacadefegdehijhklij"

Output:
[9,7,8]
```

---

### 🔍 Dry Run

```text id="dryrun"
String:
"ababcbacadefegdehijhklij"

Track last occurrences.

Partition 1:
"ababcbaca"
Ends at index 8
Length = 9

Partition 2:
"defegde"
Length = 7

Partition 3:
"hijhklij"
Length = 8
```

---

### 🌳 Visualization

```text id="visual"
ababcbaca | defegde | hijhklij
---------   -------   --------
    9          7          8
```

---

### ✅ Key Points

* Greedy interval expansion problem
* Partition extends to include all occurrences of characters
* Single-pass efficient solution
* Similar to interval merging concepts

---

### ⚠️ Edge Cases

* Single character string
* All same characters
* All unique characters
* Entire string forms one partition

---

### 🏁 Conclusion

This problem demonstrates how greedy range tracking can partition a sequence optimally by expanding intervals until all dependent characters are fully contained within a segment.

---


## 4️⃣ Minimum Cost of Ropes – Greedy Heap Approach

### 📌 Problem Statement

You are given:

* `arr` → lengths of ropes

👉 Connect all ropes into one rope.

#### Cost Rule:

* Connecting two ropes of lengths `a` and `b` costs:

```text id="cost"
a + b
```

👉 Return the **minimum total cost** required.

---

### 🚀 Approach: Min Heap Greedy Strategy

#### 🔹 Key Idea

To minimize total cost:

* Always connect the **two smallest ropes first**

👉 This prevents large costs from accumulating repeatedly.

---

### 🧠 Algorithm

1. Insert all rope lengths into a min heap

2. While more than one rope exists:

   * Remove two smallest ropes
   * Compute connection cost
   * Add cost to total
   * Push merged rope back into heap

3. Return total cost

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n log n) |
| Space Complexity | O(n)       |

---

### 📎 Example

```text id="example"
Input:
arr = [4,3,2,6]

Output:
29
```

---

### 🔍 Dry Run

```text id="dryrun"
Heap:
[2,3,4,6]

Take 2 + 3 = 5
Total = 5
Heap → [4,5,6]

Take 4 + 5 = 9
Total = 14
Heap → [6,9]

Take 6 + 9 = 15
Total = 29
```

---

### 🌳 Visualization

```text id="visual"
2 + 3 = 5
4 + 5 = 9
6 + 9 = 15

Total:
5 + 9 + 15 = 29
```

---

### ✅ Key Points

* Classic **greedy + min heap problem**
* Similar to Huffman Coding strategy
* Always combine smallest elements first
* Heap guarantees efficient minimum extraction

---

### ⚠️ Edge Cases

* Single rope → cost = 0
* Two ropes only
* Large rope values
* Duplicate lengths

---

### 🏁 Conclusion

This problem demonstrates how greedy selection with a min heap minimizes cumulative merge costs by always combining the smallest available elements first.

---
