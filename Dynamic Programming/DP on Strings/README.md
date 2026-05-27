# Dynamic Programming on strings

Dynamic Programming on strings focuses on solving problems involving character sequences by breaking them into smaller overlapping substring or subsequence problems. These techniques are commonly used for matching, transformation, comparison, partitioning, and optimization tasks such as longest common subsequence, edit distance, palindrome problems, and pattern matching. By storing intermediate results in DP tables based on string indices or prefixes, string DP efficiently avoids repeated computations and builds solutions incrementally through well-defined state transitions between characters or substrings.


## 1️⃣ Longest Common Subsequence

### 📌 Problem Statement

You are given:

* `text1`
* `text2`

👉 Return the length of the longest common subsequence between the two strings.

A subsequence is formed by deleting some characters without changing the relative order of the remaining characters.

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

For every pair of indices `(i, j)`:

* If characters match:

  * Include that character in LCS

* Otherwise:

  * Skip one character from either string

So:

```text id="relation"
If text1[i-1] == text2[j-1]:

dp[i][j] = 1 + dp[i-1][j-1]

Else:

dp[i][j] = max(
    dp[i-1][j],
    dp[i][j-1]
)
```

---

### 🧠 Algorithm

1. Create a DP table:

   * `dp[i][j]` stores LCS length for:

     * first `i` characters of `text1`
     * first `j` characters of `text2`

2. Traverse both strings

3. If characters match:

   * Extend subsequence length

4. Otherwise:

   * Take maximum by skipping one character

5. Return `dp[n][m]`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n × m)   |
| Space Complexity | O(n × m)   |

---

### 📎 Example

```text id="example"
Input:
text1 = "abcde"
text2 = "ace"

Output:
3
```

---

### 🔍 Dry Run

```text id="dryrun"
text1 = "abcde"
text2 = "ace"

DP Table:

    a c e
  0 0 0 0
a 0 1 1 1
b 0 1 1 1
c 0 1 2 2
d 0 1 2 2
e 0 1 2 3

Answer = 3
```

---

### 🌳 Visualization

```text id="visual"
text1 = a b c d e
text2 = a   c   e

LCS = "ace"
Length = 3
```

---

### ✅ Key Points

* Classic 2-string DP problem
* Uses prefix-based state transitions
* Matching characters extend subsequence
* Non-matching characters explore alternatives

---

### ⚠️ Edge Cases

* Empty strings
* No common characters
* Identical strings
* Large input lengths

---

### 🏁 Conclusion

This problem demonstrates how dynamic programming efficiently solves sequence matching problems by storing optimal subsequence lengths for smaller string prefixes and building the final solution incrementally.


---


## 2️⃣ Longest Palindromic Subsequence

### 📌 Problem Statement

You are given:

* `s` → a string

👉 Return the length of the longest subsequence of `s` that is also a palindrome.

A subsequence can be formed by deleting characters without changing the order of the remaining characters.

---

### 🚀 Approach: LCS with Reversed String

#### 🔹 Key Idea

A palindrome reads the same forward and backward.

👉 So, the problem can be transformed into:

```text id="idea"
Find the Longest Common Subsequence
between:

s
and
reverse(s)
```

The resulting LCS represents the longest palindromic subsequence.

---

### 🧠 Algorithm

1. Reverse the string:

   * `rev = s[::-1]`

2. Compute LCS between:

   * `s`
   * `rev`

3. Use Dynamic Programming:

   * If characters match:

     * extend subsequence
   * Otherwise:

     * take maximum from neighboring states

4. Return final LCS length

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n²)      |
| Space Complexity | O(n²)      |

---

### 📎 Example

```text id="example"
Input:
s = "bbbab"

Output:
4
```

---

### 🔍 Dry Run

```text id="dryrun"
s        = "bbbab"
reverse  = "babbb"

Longest Common Subsequence:
"bbbb"

Length = 4
```

---

### 🌳 Visualization

```text id="visual"
Original:
b b b a b

Reverse:
b a b b b

Common Palindromic Subsequence:
b b b b
```

---

### ✅ Key Points

* Converts palindrome problem into LCS problem
* Uses classic 2D dynamic programming
* Matching characters extend subsequence length
* Efficient alternative to direct palindrome DP

---

### ⚠️ Edge Cases

* Single character string
* Entire string already palindrome
* No repeated characters
* Large strings

---

### 🏁 Conclusion

This problem demonstrates how dynamic programming and sequence transformation can solve palindrome optimization problems efficiently by reducing them to the Longest Common Subsequence problem.
