# Subset Generation using Bitmasking

Subset Generation using **Bitmasking** is a powerful technique that leverages the binary representation of numbers to systematically enumerate all possible combinations of elements. For an array of size `n`, each bit in a number from `0` to `2ⁿ - 1` represents whether a particular element is included or excluded from a subset. This creates a direct one-to-one mapping between bit patterns and subsets, enabling elegant iterative solutions for problems involving power sets, combinations, subset sums, state compression, and exhaustive search. Bitmasking is widely used in competitive programming because it provides a simple and efficient way to represent and generate subsets while naturally supporting advanced optimization techniques such as dynamic programming on subsets.


## 1️⃣ Subsets

### 📌 Problem Statement

You are given:

* `nums[]` → an array of distinct integers

👉 Return all possible subsets (the power set).

👉 The solution set must not contain duplicate subsets.

👉 The order of subsets does not matter.

---

### 🚀 Approach: Bit Manipulation

#### 🔹 Key Idea

For an array of size `n`:

Each element has two choices:

* Include it in the subset
* Exclude it from the subset

Therefore, the total number of subsets is:

```text id="formula"
2^n
```

A binary number from:

```text id="range"
0 to (2^n - 1)
```

can represent one subset:

* Bit `1` → include the element
* Bit `0` → exclude the element

---

### 🧠 Algorithm

1. Let `n` be the size of the array.

2. Compute total subsets:

   ```text
   2^n
   ```

3. For every number from `0` to `(2^n - 1)`:

   * Check each bit position.
   * If bit `i` is set:

     * Include `nums[i]` in the current subset.

4. Store the subset.

5. Return all generated subsets.

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n × 2ⁿ)  |
| Space Complexity | O(n × 2ⁿ)  |

There are `2ⁿ` subsets and each subset may contain up to `n` elements.

---

### 📎 Example

```text id="example"
Input:

nums = [1,2,3]
```

Output:

```text id="output"
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
nums = [1,2,3]

n = 3

Total subsets = 2^3 = 8
```

Binary representation:

```text id="binary"
000 → []
001 → [1]
010 → [2]
011 → [1,2]
100 → [3]
101 → [1,3]
110 → [2,3]
111 → [1,2,3]
```

---

### 🌳 Visualization

```text id="visual"
Index:

0   1   2
1   2   3
```

Bitmask:

```text id="mask"
101
│ │ │
│ │ └── Include 1
│ └──── Exclude 2
└────── Include 3
```

Subset:

```text id="subset"
[1,3]
```

---

### ✅ Key Points

* Every bitmask uniquely represents a subset.
* Bit `i` determines whether `nums[i]` is included.
* Generates all subsets iteratively.
* Simple and elegant bit manipulation solution.

---

### ⚠️ Edge Cases

* Empty array
* Single element array
* Negative numbers
* Large values in the array
* Maximum allowed array size

---

### 🏁 Conclusion

The bit manipulation approach generates the power set by treating each number from `0` to `2ⁿ−1` as a binary mask. Each bit decides whether an element is included in the current subset, allowing all possible subsets to be generated efficiently in O(n × 2ⁿ) time.


---


## 2️⃣ Subsets II

### 📌 Problem Statement

You are given:

* `nums[]` → an integer array that may contain duplicates

👉 Return all possible subsets (the power set).

👉 The solution set must not contain duplicate subsets.

👉 Return the subsets in any order.

---

### 🚀 Approach: Bitmasking + Set

#### 🔹 Key Idea

For an array of size `n`, there are:

```text id="formula"
2^n
```

possible bitmasks.

Each bitmask represents one subset:

* Bit `1` → include element
* Bit `0` → exclude element

Since the array may contain duplicate values:

* Different bitmasks can generate identical subsets.
* Store subsets in a set as tuples to automatically remove duplicates.

Before generating subsets:

* Sort the array so duplicate subsets have the same ordering.

---

### 🧠 Algorithm

1. Sort the array.
2. Generate all bitmasks from `0` to `2ⁿ - 1`.
3. For each bitmask:

   * Build the corresponding subset.
4. Store the subset as a tuple inside a set.
5. Convert all tuples back to lists.
6. Return the resulting subsets.

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n × 2ⁿ)  |
| Space Complexity | O(n × 2ⁿ)  |

There are `2ⁿ` possible subsets and each subset may contain up to `n` elements.

---

### 📎 Example

```text id="example"
Input:

nums = [1,2,2]
```

Output:

```text id="output"
[
 [],
 [1],
 [2],
 [1,2],
 [2,2],
 [1,2,2]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
nums = [1,2,2]

Sorted:

[1,2,2]

Bitmasks:

000 → []
001 → [1]
010 → [2]
011 → [1,2]
100 → [2]
101 → [1,2]
110 → [2,2]
111 → [1,2,2]
```

Store in set:

```text id="set"
{
(),
(1),
(2),
(1,2),
(2,2),
(1,2,2)
}
```

Duplicates are removed automatically.

---

### 🌳 Visualization

```text id="visual"
nums = [1,2,2]

Mask = 110

Bits:

1 1 0

Include:

2, 2

Subset:

[2,2]
```

Duplicate generation:

```text id="duplicate"
010 → [2]
100 → [2]

Set keeps only one copy.
```

---

### ✅ Key Points

* Bitmasking generates every possible subset.
* Sorting ensures consistent ordering.
* Set removes duplicate subsets automatically.
* Simple alternative to backtracking.

---

### ⚠️ Edge Cases

* Empty array
* All elements identical
* Single element array
* Negative numbers
* Large input sizes

---

### 🏁 Conclusion

The Bitmasking approach generates all possible subsets by interpreting each number from `0` to `2ⁿ−1` as a selection mask. Since duplicate elements can produce identical subsets, sorting the array and storing subsets in a set ensures uniqueness, resulting in a clean and straightforward solution for generating all distinct subsets.
