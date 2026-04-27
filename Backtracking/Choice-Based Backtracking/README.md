# Choice-based backtracking

Choice-based backtracking is a recursive problem-solving technique where, at each step, you make a decision among multiple possible choices (such as include/exclude, pick/skip, or try all options) and explore all resulting paths systematically. By building solutions incrementally and backtracking (undoing choices) when needed, it efficiently traverses the decision space to generate all valid combinations, permutations, or configurations, making it a powerful approach for combinatorial problems.


## 1️⃣ Subsets (Power Set) – Backtracking Approach

### 📌 Problem Statement

You are given:

* `nums` → a list of **distinct integers**

👉 Return **all possible subsets** (the power set)

#### 🎯 Constraints:

* Each element can either be **included or excluded**
* No duplicate subsets allowed

---

### 🚀 Approach: Backtracking

#### 🔹 Key Idea

* At each index, you have **two choices**:

  1. Include the element
  2. Exclude the element

👉 This creates a decision tree of size `2^n`

---

### 🧠 Algorithm

1. Start from index `0` with an empty subset

2. For each element:

   * Include it → move to next index
   * Exclude it → move to next index

3. When you reach the end:

   * Add the current subset to result

---

### 📊 Complexity Analysis

| Type             | Complexity             |
| ---------------- | ---------------------- |
| Time Complexity  | O(2ⁿ × n)              |
| Space Complexity | O(n) (recursion stack) |

---

### 📎 Example

```text id="example"
Input:
nums = [1,2,3]

Output:
[
 [],
 [1],
 [2],
 [1,2],
 [3],
 [1,3],
 [2,3],
 [1,2,3]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Start:
[]

Include 1 → [1]
Include 2 → [1,2]
Include 3 → [1,2,3]

Backtrack and explore all combinations ✔️
```

---

### 🌳 Recursion Tree

```text id="tree"
                []
           /           \
        [1]             []
      /     \        /     \
  [1,2]    [1]    [2]      []
   ...      ...    ...      ...
```

---

### ✅ Key Points

* Classic **Backtracking problem**
* Generates **power set (2ⁿ subsets)**
* Uses **include/exclude pattern**
* Ensures no duplicates (since input is distinct)

---

### ⚠️ Edge Cases

* Empty input → `[[]]`
* Single element
* Large input (exponential growth)

---

### 🏁 Conclusion

Backtracking provides a clean and intuitive way to generate all subsets by exploring every possible combination, making it a foundational pattern for many combinatorial problems.


---


## 2️⃣ Subsets II – Handling Duplicates (Backtracking)

### 📌 Problem Statement

You are given:

* `nums` → a list of integers (may contain duplicates)

👉 Return **all possible unique subsets** (the power set)

#### 🎯 Constraints:

* Subsets must be **unique**
* Order of subsets does not matter

---

### 🚀 Approach: Backtracking + Sorting

#### 🔹 Key Idea

* Sort the array to bring duplicates together
* Skip duplicate elements during recursion

👉 Avoid generating duplicate subsets by checking:

```
if i > start and nums[i] == nums[i-1]:
    continue
```

---

### 🧠 Algorithm

1. Sort the input array

2. Start backtracking from index `0`

3. At each step:

   * Add current combination to result
   * Iterate through remaining elements

4. Skip duplicates:

   * If current element is same as previous and not the first in loop → skip

5. Continue recursion

---

### 📊 Complexity Analysis

| Type             | Complexity             |
| ---------------- | ---------------------- |
| Time Complexity  | O(2ⁿ) (worst case)     |
| Space Complexity | O(n) (recursion stack) |

---

### 📎 Example

```text id="example"
Input:
nums = [1,2,2]

Output:
[
 [],
 [1],
 [1,2],
 [1,2,2],
 [2],
 [2,2]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Sorted nums = [1,2,2]

Start:
[]

Include 1 → [1]
Include 2 → [1,2]
Include 2 → [1,2,2]

Backtrack:
Skip duplicate 2 at same level ✔️
```

---

### 🌳 Recursion Tree (Simplified)

```text id="tree"
        []
     /   |   \
   [1]  [2]  (skip duplicate)
   / \    \
[1,2] [1]  [2,2]
```

---

### ✅ Key Points

* Sorting helps **group duplicates**
* Skip duplicates using **index check**
* Generates **unique subsets only**
* Efficient pruning avoids redundant work

---

### ⚠️ Edge Cases

* Empty input → `[[]]`
* All elements same → limited subsets
* Large input → exponential growth

---

### 🏁 Conclusion

This approach efficiently generates all unique subsets by combining backtracking with smart duplicate handling, making it a common pattern for problems involving combinations with repeated elements.


---