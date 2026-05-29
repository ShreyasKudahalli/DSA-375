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


---


## 3️⃣ Edit Distance

### 📌 Problem Statement

You are given:

* `word1`
* `word2`

👉 Return the minimum number of operations required to convert `word1` into `word2`.

Allowed operations:

1. Insert a character
2. Delete a character
3. Replace a character

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

For every pair of indices `(i, j)`:

* If characters match:

  * No operation needed

* Otherwise:

  * Perform one of:

    * Insert
    * Delete
    * Replace

So:

```text id="relation"
If word1[i-1] == word2[j-1]:

dp[i][j] = dp[i-1][j-1]

Else:

dp[i][j] = 1 + min(
    dp[i-1][j-1],   # Replace
    dp[i-1][j],     # Delete
    dp[i][j-1]      # Insert
)
```

---

### 🧠 Algorithm

1. Create DP table:

   * `dp[i][j]` → minimum operations to convert:

     * first `i` characters of `word1`
     * into first `j` characters of `word2`

2. Initialize base cases:

   * Empty string conversions

3. Traverse both strings

4. If characters match:

   * Copy diagonal value

5. Otherwise:

   * Take minimum among insert, delete, replace

6. Return `dp[n][m]`

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
word1 = "horse"
word2 = "ros"

Output:
3
```

---

### 🔍 Dry Run

```text id="dryrun"
horse → rorse   (replace h → r)
rorse → rose    (remove r)
rose  → ros     (remove e)

Total Operations = 3
```

---

### 🌳 Visualization

```text id="visual"
word1 = horse
word2 = ros

Operations:
h → r
remove r
remove e
```

---

### ✅ Key Points

* Classic string DP problem
* Uses insert/delete/replace transitions
* DP table stores minimum edit operations
* Foundation for spell check and text correction systems

---

### ⚠️ Edge Cases

* Empty strings
* Identical strings
* Completely different strings
* Large input lengths

---

### 🏁 Conclusion

This problem demonstrates how dynamic programming efficiently computes minimum transformation operations between strings by exploring all possible edit choices and reusing optimal subproblem solutions.


---


## 4️⃣ Delete Operation for Two Strings

### 📌 Problem Statement

You are given:

* `word1`
* `word2`

👉 Return the minimum number of deletions required to make both strings equal.

Allowed operation:

1. Delete a character from either string

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

For every pair of indices `(i, j)`:

* If characters match:

  * No deletion needed

* Otherwise:

  * Delete one character from either string

So:

```text id="relation"
If word1[i-1] == word2[j-1]:

dp[i][j] = dp[i-1][j-1]

Else:

dp[i][j] = 1 + min(
    dp[i-1][j],   # Delete from word1
    dp[i][j-1]    # Delete from word2
)
```

---

### 🧠 Algorithm

1. Create DP table:

   * `dp[i][j]` → minimum deletions needed for:

     * first `i` characters of `word1`
     * first `j` characters of `word2`

2. Initialize base cases:

   * Empty string conversions

3. Traverse both strings

4. If characters match:

   * Carry forward diagonal value

5. Otherwise:

   * Delete from one of the strings

6. Return `dp[n][m]`

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
word1 = "sea"
word2 = "eat"

Output:
2
```

---

### 🔍 Dry Run

```text id="dryrun"
sea → ea    (delete 's')
eat → ea    (delete 't')

Total deletions = 2
```

---

### 🌳 Visualization

```text id="visual"
word1 = s e a
word2 = e a t

Common Remaining String:
e a
```

---

### ✅ Key Points

* String DP based on deletions only
* Similar to Edit Distance problem
* Matching characters require no operation
* DP explores optimal deletion choices

---

### ⚠️ Edge Cases

* Empty strings
* Identical strings
* No common characters
* Large strings

---

### 🏁 Conclusion

This problem demonstrates how dynamic programming efficiently minimizes deletion operations between two strings by building optimal solutions for smaller string prefixes and reusing computed results.


---


## 5️⃣ Minimum Insertions to Make a String Palindrome

### 📌 Problem Statement

You are given:

* `s` → a string

👉 Return the minimum number of insertions required to make the string a palindrome.

You may insert characters at any position.

---

### 🚀 Approach: Longest Palindromic Subsequence + Dynamic Programming

#### 🔹 Key Idea

If we know the:

```text id="idea"
Longest Palindromic Subsequence (LPS)
```

then the remaining characters must be inserted to form a palindrome.

So:

```text id="relation"
Minimum Insertions =
Length of String - Length of LPS
```

The LPS is computed using:

```text id="lcs"
LCS(s, reverse(s))
```

---

### 🧠 Algorithm

1. Reverse the string:

   * `rev = s[::-1]`

2. Compute Longest Common Subsequence:

   * Between `s` and `rev`

3. The resulting LCS length equals:

   * Longest Palindromic Subsequence

4. Compute answer:

   * `len(s) - LPS`

5. Return result

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
s = "mbadm"

Output:
2
```

---

### 🔍 Dry Run

```text id="dryrun"
s = "mbadm"

reverse = "mdabm"

LPS = "mam"
Length = 3

Minimum Insertions =
5 - 3 = 2
```

---

### 🌳 Visualization

```text id="visual"
Original:
m b a d m

Palindrome After Insertions:
m d a b a d m

Insertions Needed = 2
```

---

### ✅ Key Points

* Converts palindrome problem into LCS problem
* Uses Longest Palindromic Subsequence
* Remaining characters require insertion
* Efficient DP-based string optimization

---

### ⚠️ Edge Cases

* Empty string
* Single character
* Already palindrome
* Strings with all distinct characters

---

### 🏁 Conclusion

This problem demonstrates how dynamic programming and sequence transformation techniques can efficiently solve palindrome construction problems by leveraging the Longest Common Subsequence between a string and its reverse.
