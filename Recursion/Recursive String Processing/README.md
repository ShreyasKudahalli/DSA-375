


## 1️⃣ Decode String (Recursion / DFS)

### 📌 Problem Statement

Given an encoded string `s`, return its **decoded string**.

#### 🔐 Encoding Rule:

* `k[encoded_string]` → the `encoded_string` inside brackets is repeated exactly `k` times
* `k` is a positive integer
* The input string is always valid (well-formed brackets, no extra spaces)

---

### 🧾 Examples

```text id="ex1"
Input:  s = "3[a]2[bc]"  
Output: "aaabcbc"
```

```text id="ex2"
Input:  s = "3[a2[c]]"  
Output: "accaccacc"
```

```text id="ex3"
Input:  s = "2[abc]3[cd]ef"  
Output: "abcabccdcdcdef"
```

---

### 🚀 Approach: Recursion (DFS)

We use **Depth-First Search (DFS)** to process nested patterns:

* Traverse the string character by character
* Build numbers (`k`) for repetition
* When encountering `[`, recursively decode the substring
* When encountering `]`, return the decoded result to the previous call

---

### 🧠 Key Idea

* Use recursion to handle **nested brackets**
* Maintain:

  * `num` → repetition count
  * `res` → current decoded string
* Multiply decoded substring with `num` and append

---

### 🧩 Algorithm

1. Initialize:

   * `res = ""`, `num = 0`

2. Traverse string:

   * If digit → build `num`
   * If `'['` → recursively decode substring
   * If `']'` → return current result
   * Else → append character to `res`

3. Combine:

   * `res += decoded_substring * num`

4. Return final decoded string

---

### 📊 Complexity Analysis

| Type             | Complexity               |
| ---------------- | ------------------------ |
| Time Complexity  | O(n)                     |
| Space Complexity | O(n) *(recursion stack)* |

---

### 🔍 Dry Run (Brief)

```text id="dryrun"
Input: "3[a2[c]]"

→ dfs:
   num = 3
   enter [ → dfs:
       res = "a"
       num = 2
       enter [ → dfs:
           res = "c"
       → return "c"
       res = "acc"
   → return "acc"

Final = "acc" * 3 = "accaccacc"
```

---

### ✅ Key Points

* Handles **nested encoding** efficiently
* Uses recursion for clean structure
* Avoids explicit stack implementation
* Common interview problem (LeetCode Medium)

---

### ⚠️ Edge Cases

* Multiple nested brackets
* Multi-digit numbers (e.g., `"12[a]"`)
* No brackets (plain string)
* Deep recursion (large nesting)

---

### 🏁 Conclusion

This recursive DFS approach provides a clean and efficient way to decode encoded strings, especially when dealing with nested patterns. It leverages the call stack to naturally handle bracket matching and string expansion.


---