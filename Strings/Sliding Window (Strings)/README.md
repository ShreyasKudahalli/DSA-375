# Sliding Window Technique

The Sliding Window Technique is an efficient approach used to solve problems involving subarrays or substrings by maintaining a window of elements that expands and contracts dynamically. Instead of recalculating results for every possible window, it reuses previous computations, reducing the time complexity from quadratic to linear in many cases. This technique is especially useful for problems related to strings, arrays, frequency counting, and constraints-based windows, making it a common and important pattern in coding interviews and competitive programming.


## 1️⃣ Find All Anagrams in a String

### 🧩 Problem Statement

Given two strings `s` and `p`, return a list of all **start indices** of `p`’s anagrams in `s`.

#### ✔️ Notes
- Strings consist of lowercase English letters
- The order of output indices does not matter
- An anagram is formed by rearranging characters

---

### 💡 Approach: Sliding Window + Frequency Count

We maintain a **fixed-size sliding window** of length `len(p)` over string `s`.

#### Key Idea
- Use two frequency arrays of size 26:
  - `pCount` → frequency of characters in `p`
  - `sCount` → frequency of characters in the current window of `s`
- Slide the window one character at a time and compare frequencies

---

### 🧠 Algorithm Steps

1. Initialize two arrays `sCount` and `pCount` of size 26 with zeros
2. Fill `pCount` with character frequencies from string `p`
3. Use two pointers:
   - `l` → left boundary of the window
   - `r` → right boundary of the window
4. For each character at index `r` in `s`:
   - Add `s[r]` to the window frequency
   - If window size exceeds `len(p)`, remove `s[l]` and move `l`
5. If `sCount` matches `pCount`, record index `l`
6. Return the result list

---

### 🧪 Example

#### Input
    s = "cbaebabacd"
    p = "abc"

#### Output
    [0, 6]

#### Explanation
Anagrams of `"abc"` start at indices:
- `"cba"` → index 0
- `"bac"` → index 6

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(1)  |
 Frequency array size is constant (26 letters).

### 📌 Key Takeaways
- Sliding window avoids re-counting
- Fixed window size simplifies logic
- Frequency arrays are faster than maps
- Common pattern in string problems


---


## 2️⃣ Longest Substring Without Repeating Characters — Sliding Window

### 🧩 Problem Statement

Given a string `s`, find the **length of the longest substring** without repeating characters.

---

### 💡 Approach: Sliding Window + Set

We maintain a dynamic window that always contains **unique characters**.

#### Key Idea
- Use a **set** to track characters inside the current window
- Expand the window by moving the right pointer
- If a duplicate is found, shrink the window from the left until it becomes valid again

---

### 🧠 Algorithm Steps

1. Initialize:
   - `word` → empty set to store characters
   - `l = 0` → left pointer
   - `res = 0` → result (maximum length)
2. Move the right pointer `r` through the string:
   - While `s[r]` is already in the set:
     - Remove `s[l]` from the set
     - Move `l` forward
   - Add `s[r]` to the set
   - Update the result with current window size
3. Return the maximum length found

---

### 🧪 Example

#### Input
    "abcabcbb"

#### Output
    3

#### Explanation
The answer is `"abc"`, which has a length of 3.

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(min(n, charset))  |

---

### 📌 Key Takeaways

- Sliding window ensures linear time complexity
- Set provides O(1) lookup and removal
- Classic interview and LeetCode problem
- Foundation for many string window problems


---


## 3️⃣ Minimum Window Substring 

### 🧩 Problem Statement

Given two strings `s` and `t`, return the **minimum window substring** of `s` such that **every character in `t` (including duplicates)** is included in the window.

If no such substring exists, return an empty string.

---

### 💡 Approach: Sliding Window with Frequency Maps

We maintain a **dynamic sliding window** that expands and contracts to find the smallest valid substring.

#### Key Idea
- Track required character frequencies using `tCount`
- Track current window frequencies using `windowCount`
- Use a counter (`have`) to know when the window satisfies all characters of `t`

---

### 🧠 Algorithm Steps

1. Handle edge cases:
   - If `t` is empty or `s` is shorter than `t`, return `""`
2. Build frequency map `tCount` for string `t`
3. Initialize:
   - Two pointers `l` and `r`
   - `have` → number of matched characters
   - `start` and `minlen` to track the best window
4. Expand the window by moving `r`:
   - Add `s[r]` to `windowCount`
   - If the character is needed and within required count, increment `have`
5. When all characters are matched (`have == len(t)`):
   - Try shrinking the window from the left
   - Update the minimum window if smaller
   - Remove characters and update `have` if window becomes invalid
6. Return the smallest valid substring found

---

### 🧪 Example

#### Input
    s = "ADOBECODEBANC"
    t = "ABC"

#### Output
    "BANC"

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(k)  |

Where:
- n = length of string s
- k = number of unique characters in t

### 📌 Key Takeaways

- Sliding window allows linear-time solution
- Hash maps efficiently track character frequencies
- Window expansion + contraction finds optimal solution
- One of the most important interview problems


---


## 4️⃣ Longest Substring with At Most K Distinct Characters

### 🧩 Problem Statement

Given a string `s` and an integer `k`, find the **longest substring** that contains **at most `k` distinct characters**.

If `k = 0`, return an empty result.

---

### 💡 Approach: Sliding Window + Frequency Map

We maintain a **dynamic sliding window** that expands and shrinks based on the number of distinct characters in the current window.

### Key Idea
- Use a hash map (`freq`) to track character frequencies in the window
- Expand the window by moving the right pointer
- Shrink the window when the number of distinct characters exceeds `k`

---

### 🧠 Algorithm Steps

1. Handle edge case:
   - If `k == 0`, return an empty result
2. Initialize:
   - `l = 0` → left pointer
   - `freq` → frequency map of characters
   - `start` and `size` → track longest valid window
3. Move the right pointer `r` through the string:
   - Add `s[r]` to the frequency map
4. While the number of distinct characters exceeds `k`:
   - Remove characters from the left
   - Delete character from map if its count becomes zero
5. Update the longest substring whenever a larger valid window is found
6. Return the longest substring

---

### 🧪 Example

#### Input
      s = "eceba"
      k = 2

#### Output
      "ece"

#### Explanation
The substring `"ece"` contains at most 2 distinct characters (`e` and `c`) and has the maximum length.

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(k)  |


Where:
- n = length of the string
- k = maximum number of distinct characters allowed

### 📌 Key Takeaways

- Sliding window avoids recalculating substrings
- Frequency map tracks distinct characters efficiently
- Works well for constraint-based substring problems
- Classic interview question pattern


---


## 5️⃣ Permutation in String 

### 🧩 Problem Statement

Given two strings `s1` and `s2`, return `True` if **any permutation of `s1`** is a substring of `s2`.  
Otherwise, return `False`.

---

### 💡 Approach: Sliding Window with Fixed-Size Frequency Arrays

We maintain a **fixed-size sliding window** of length `len(s1)` over string `s2`.

#### Key Idea
- Use two arrays of size 26:
  - `s1Count` → frequency of characters in `s1`
  - `s2Count` → frequency of characters in the current window of `s2`
- Slide the window one character at a time and compare the frequency arrays

---

### 🧠 Algorithm Steps

1. Handle edge cases:
   - If `s1` is longer than `s2`, return `False`
2. Initialize two frequency arrays of size 26 with zeros
3. Populate `s1Count` with character frequencies from `s1`
4. Use two pointers `l` and `r` to represent the window in `s2`
5. For each character at index `r`:
   - Add it to `s2Count`
6. When the window size equals `len(s1)`:
   - Compare `s1Count` and `s2Count`
   - If equal, a permutation exists → return `True`
   - Otherwise, remove the left character and slide the window
7. If no permutation is found, return `False`

---

### 🧪 Example

#### Input
      s1 = "ab"
      s2 = "eidbaooo"

#### Output
      True

#### Explanation
The substring `"ba"` is a permutation of `"ab"`.

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(1)  |

Frequency arrays are fixed at size 26.

---

### 📌 Key Takeaways

- Fixed-size sliding window ensures linear time
- Frequency arrays are faster than hash maps
- Ideal for lowercase alphabet problems
- Common LeetCode sliding window pattern


---


## 6️⃣ Subarrays with K Distinct Integers

### 🧩 Problem Statement

Given an integer array `nums` and an integer `k`, return the number of **subarrays that contain exactly `k` distinct integers**.

---

### 💡 Approach: At Most K Distinct → Exactly K Distinct

Instead of directly counting subarrays with **exactly `k`** distinct elements, we use a key observation:

> **Exactly K = At Most K − At Most (K − 1)**

#### Why this works
- `atMost(K)` counts subarrays with **≤ K** distinct elements
- `atMost(K−1)` counts subarrays with **≤ K−1** distinct elements
- Their difference gives subarrays with **exactly K** distinct elements

---

### 🧠 Algorithm Steps

#### Helper Function: `atMost(k)`
1. Use a sliding window with two pointers `l` and `r`
2. Maintain a frequency map to track elements in the window
3. Expand the window by moving `r`
4. Shrink the window when distinct elements exceed `k`
5. At each step, add `r - l + 1` to the count (all subarrays ending at `r`)
6. Return the total count

#### Final Answer
atMost(k) - atMost(k - 1)

---

### 🧪 Example

#### Input
      nums = [1,2,1,2,3]
      k = 2

#### Output
      7

#### Explanation
Subarrays with exactly 2 distinct integers are:
[1,2], [2,1], [1,2], [2,3],
[1,2,1], [2,1,2], [1,2,1,2]


### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(k)  |

Where:
- n = length of the array
- k = number of distinct elements allowed in the window

---

### 📌 Key Takeaways

- Directly counting exactly K is hard
- AtMost(K) trick simplifies the problem
- Sliding window ensures linear performance
- Extremely important interview pattern


