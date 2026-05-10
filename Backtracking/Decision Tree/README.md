


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