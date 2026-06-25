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

This problem is a classic subset-generation task where each element can either be included or excluded. Using backtracking, we explore all `2ⁿ`
subsets while maintaining the current XOR value, allowing us to efficiently compute the sum of XOR totals without storing every subset 
explicitly.


---


## 2️⃣ Maximum XOR of Two Numbers in an Array

### 📌 Problem Statement

You are given:

* `nums[]` → an array of integers

👉 Find the maximum value of:

```text id="formula"
nums[i] XOR nums[j]
```

where:

```text
0 ≤ i < j < n
```

👉 Return the maximum possible XOR value.

---

### 🚀 Approach: Bitwise Trie (Binary Trie)

#### 🔹 Key Idea

To maximize XOR:

```text id="xoridea"
0 XOR 1 = 1
1 XOR 0 = 1
```

A bit contributes most to the answer when it differs from the corresponding bit of the other number.

Therefore, for each bit position:

* If current bit is `0`, we prefer `1`.
* If current bit is `1`, we prefer `0`.

A Binary Trie stores every number bit-by-bit, allowing us to efficiently search for the number that produces the maximum XOR.

---

### 🧠 Algorithm

1. Create a Binary Trie.
2. Insert the first number into the Trie.
3. For every remaining number:

   * Query the Trie for the best XOR partner.
   * Update the maximum XOR.
   * Insert the current number into the Trie.
4. Return the maximum XOR found.

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(32 × n)  |
| Space Complexity | O(32 × n)  |

Since every integer contains at most 32 bits.

---

### 📎 Example

```text id="example"
Input:

nums = [3,10,5,25,2,8]
```

Output:

```text id="output"
28
```

---

### 🔍 Dry Run

```text id="dryrun"
nums = [3,10,5,25,2,8]

Binary:

3  = 00011
10 = 01010
5  = 00101
25 = 11001
2  = 00010
8  = 01000
```

For:

```text
5 XOR 25
```

```text
00101
11001
-----
11100
```

Result:

```text
28
```

Maximum XOR = 28

---

### 🌳 Visualization

```text id="visual"
Binary Trie

          Root
         /    \
        0      1
       /        \
      ...       ...
```

Querying number:

```text
5 = 00101
```

For each bit:

```text
Current Bit = 0
Prefer = 1

Current Bit = 1
Prefer = 0
```

Choose opposite bits whenever available to maximize XOR.

---

### ✅ Key Points

* Binary Trie stores numbers bit-by-bit.
* Opposite bits maximize XOR contribution.
* Query and insertion both take O(32).
* Much faster than brute force O(n²).

---

### ⚠️ Edge Cases

* Single element array
* All numbers identical
* Presence of zero
* Large integers
* Maximum array size

---

### 🏁 Conclusion

The Binary Trie approach efficiently computes the maximum XOR pair by greedily selecting opposite bits at every position. By storing previously 
seen numbers in a bitwise Trie and querying for the best possible complement, we reduce the problem from O(n²) brute force to O(32 × n), making 
it optimal for large inputs.

