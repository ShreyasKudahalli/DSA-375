# Advanced XOR

Advanced XOR techniques leverage the unique properties of the XOR operator—such as **self-cancellation (`a ^ a = 0`)**, **identity (`a ^ 0 = a`)**, and **associativity/commutativity**—to solve complex problems involving subsets, missing numbers, unique elements, bit transformations, and recursive binary structures. These problems often require recognizing hidden XOR patterns, exploiting symmetry, using bitmasking, or combining XOR with recursion and dynamic programming. Mastering advanced XOR concepts enables elegant solutions with minimal space usage and often reduces seemingly difficult combinatorial problems to efficient bit-level operations.


## 1️⃣ Sum of All Subset XOR Totals

### 📌 Problem Statement

You are given:

* `nums[]` → an array of integers

👉 For every possible subset, compute its XOR total.

👉 Return the sum of XOR totals of all subsets.

The XOR total of an empty subset is:

```text id="empty"
0
```

---

### 🚀 Approach: Backtracking

#### 🔹 Key Idea

For every element, there are two choices:

* Exclude it from the current subset
* Include it in the current subset

This naturally forms a recursion tree containing all possible subsets.

At each recursive call:

* Maintain the XOR of the current subset.
* When all elements have been processed:

  * Add the subset XOR value to the final answer.

Since every subset is explored exactly once, the sum of all subset XOR totals can be computed directly.

---

### 🧠 Algorithm

1. Initialize `res = 0`.
2. Define a recursive function:

   * Parameters:

     * Current XOR value
     * Current index
3. Base Case:

   * If all elements are processed:

     * Add current XOR to `res`.
4. Recursive Choices:

   * Skip current element.
   * Include current element and update XOR.
5. Return the accumulated result.

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(2ⁿ)      |
| Space Complexity | O(n)       |

Where:

* `n` = number of elements
* Total subsets = `2ⁿ`

---

### 📎 Example

```text id="example"
Input:

nums = [1,3]
```

Output:

```text id="output"
6
```

---

### 🔍 Dry Run

```text id="dryrun"
nums = [1,3]

Subsets:

[]      XOR = 0
[1]     XOR = 1
[3]     XOR = 3
[1,3]   XOR = 2

Sum:

0 + 1 + 3 + 2 = 6
```

---

### 🌳 Visualization

```text id="visual"
                 XOR=0
                /     \
           Skip 3     Take 3
            /            \
        XOR=0          XOR=3
        /   \          /   \
    Skip1 Take1    Skip1 Take1
      |      |       |      |
     0      1       3      2
```

Subset XOR totals:

```text id="totals"
[]
[1]
[3]
[1,3]

0 + 1 + 3 + 2 = 6
```

---

### ✅ Key Points

* Every subset contributes its XOR value exactly once.
* Backtracking naturally generates all subsets.
* Current XOR is updated incrementally.
* No need to explicitly store all subsets.

---

### ⚠️ Edge Cases

* Empty array
* Single element
* All elements equal
* Elements containing zero
* Larger input sizes

---

### 🏁 Conclusion

This problem is a classic subset-generation task where each element can either be included or excluded. Using backtracking, we explore all `2ⁿ` subsets while maintaining the current XOR value, allowing us to efficiently compute the sum of XOR totals without storing every subset explicitly.
