# Decision tree
Decision tree backtracking is a recursive problem-solving approach where each recursive call represents a branching decision, forming a tree-like structure of choices and outcomes. At every level, the algorithm explores one possible decision, proceeds deeper if the choice is valid, and backtracks to try alternative paths when necessary. This method is widely used in combinatorial problems such as permutations, combinations, subset generation, maze traversal, and constraint satisfaction, where the complete solution space can be visualized as a decision tree.



## 1️⃣ Letter Combinations of a Phone Number – Backtracking

### 📌 Problem Statement

You are given:

* `digits` → a string containing digits from `2-9`

👉 Return all possible letter combinations that the number could represent using a phone keypad mapping.

---

### ☎️ Phone Keypad Mapping

```text id="mapping"
2 → abc
3 → def
4 → ghi
5 → jkl
6 → mno
7 → pqrs
8 → tuv
9 → wxyz
```

---

### 🚀 Approach: Backtracking

#### 🔹 Key Idea

* Each digit can map to multiple characters
* Build combinations one character at a time

👉 For every digit:

* Try all possible letters
* Recursively generate remaining combinations

---

### 🧠 Algorithm

1. Create digit-to-letter mapping

2. Start recursion from index `0`

3. For each digit:

   * Iterate through mapped characters
   * Add character to current combination
   * Recurse for next digit

4. Base case:

   * If all digits processed → store combination

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(4ⁿ × n)  |
| Space Complexity | O(n)       |

> Each digit can produce up to 4 letters

---

### 📎 Example

```text id="example"
Input:
digits = "23"

Output:
[
 "ad","ae","af",
 "bd","be","bf",
 "cd","ce","cf"
]
```

---

### 🔍 Dry Run

```text id="dryrun"
digits = "23"

2 → abc
3 → def

Start:
""

Pick 'a'
 → "ad"
 → "ae"
 → "af"

Pick 'b'
 → "bd"
 ...
```

---

### 🌳 Recursion Tree (Simplified)

```text id="tree"
              ""
         /     |     \
       "a"    "b"    "c"
      / | \   ...
   "ad""ae""af"
```

---

### ✅ Key Points

* Classic **cartesian product/backtracking problem**
* Builds combinations incrementally
* Efficient recursive generation
* Similar to permutation-style exploration

---

### ⚠️ Edge Cases

* Empty input → `[]`
* Single digit
* Digits with 4 letters (`7` and `9`)

---

### 🏁 Conclusion

This problem demonstrates how backtracking can generate all possible combinations by recursively exploring every character choice for each digit.


---


## 2️⃣ All Possible Full Binary Trees – Recursion + Memoization

### 📌 Problem Statement

You are given:

* `n` → number of nodes in a binary tree

👉 Return all possible **full binary trees** with exactly `n` nodes.

---

### 🌲 What is a Full Binary Tree?

A **Full Binary Tree (FBT)** is a binary tree where:

* Every node has either:

  * `0` children, or
  * `2` children

👉 No node can have only one child.

---

### 🚀 Approach: Recursive Tree Construction + Memoization

#### 🔹 Key Idea

For a full binary tree:

* Root uses `1` node
* Remaining nodes are divided into:

  * left subtree
  * right subtree

👉 Both subtree sizes must be **odd**
because full binary trees always contain an odd number of nodes.

---

### 🧠 Algorithm

1. If `n` is even:

   * Return empty list

2. Base case:

   * `n == 1`
   * Return single node tree

3. Recursively split:

   * Choose odd number of nodes for left subtree
   * Remaining nodes go to right subtree

4. Generate:

   * All left subtree combinations
   * All right subtree combinations

5. Combine:

   * Attach every left tree with every right tree

6. Use memoization:

   * Store results for repeated subtree sizes

---

### 📊 Complexity Analysis

| Type             | Complexity                        |
| ---------------- | --------------------------------- |
| Time Complexity  | Exponential (Catalan-like growth) |
| Space Complexity | O(number of generated trees)      |

---

### 📎 Example

```text id="example"
Input:
n = 7

Output:
All possible full binary trees with 7 nodes
```

---

### 🔍 Dry Run

```text id="dryrun"
n = 7

Root = 1 node

Possible splits:
Left = 1, Right = 5
Left = 3, Right = 3
Left = 5, Right = 1

Generate recursively ✔️
```

---

### 🌳 Recursive Construction

```text id="tree"
        Root
       /    \
   Left     Right

Recursively build all combinations
```

---

### ✅ Key Points

* Full binary trees require **odd node counts**
* Uses **divide-and-combine recursion**
* Memoization avoids repeated subtree generation
* Similar to Catalan-number tree problems

---

### ⚠️ Edge Cases

* Even `n` → no valid full binary tree
* `n = 1` → single node tree
* Large `n` → exponential number of trees

---

### 🏁 Conclusion

This problem demonstrates recursive tree generation with memoization, where all structurally unique full binary trees are constructed efficiently by reusing previously computed subtree results.

---