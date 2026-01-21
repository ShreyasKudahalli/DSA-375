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

### Explanation
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

n = length of string s

k = number of unique characters in t

### 📌 Key Takeaways

- Sliding window allows linear-time solution
- Hash maps efficiently track character frequencies
- Window expansion + contraction finds optimal solution
- One of the most important interview problems


