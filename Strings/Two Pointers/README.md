# Two Pointers Technique

Two Pointer Technique is an efficient algorithmic approach where two pointers are used to traverse a data structure (such as an array or string) from different positions—usually from the start and end—to reduce time complexity and avoid extra space. It is commonly used to solve problems involving searching, comparison, reversal, and optimization in linear time.


## 1️⃣ Valid Palindrome

### 🧩 Problem Statement

Given a string `s`, determine if it is a palindrome, considering **only alphanumeric characters** and **ignoring cases**.

#### ✔️ Conditions
- Ignore spaces and special characters  
- Treat uppercase and lowercase letters as equal  
- Return `True` if the string is a palindrome, otherwise `False`

---

### 💡 Approach: Two Pointer Technique

We use **two pointers**:
- `l` → starts from the beginning of the string  
- `r` → starts from the end of the string  

#### Algorithm Steps:
1. Initialize `l = 0` and `r = len(s) - 1`
2. Move `l` forward until it points to an alphanumeric character
3. Move `r` backward until it points to an alphanumeric character
4. Compare characters at `l` and `r` (case-insensitive)
5. If they don’t match → return `False`
6. Move both pointers inward
7. If all characters match → return `True`

---
### 🧪 Example

#### Input
    "A man, a plan, a canal: Panama"

#### Output
    True
---
### Explanation
After removing non-alphanumeric characters and converting to lowercase:
`amanaplanacanalpanama`

Which is a palindrome.
---
### ⏱️ Complexity Analysis

| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(1)  |

---

### 📌 Key Takeaways
- `.isalnum()` filters valid characters
- `.lower()` ensures case-insensitive comparison
- Two pointers reduce extra space usage
- Clean and optimal solution for interviews


---


##  2️⃣ Reverse String 

### 🧩 Problem Statement

Given an array of characters `s`, reverse the array **in-place**.

#### ✔️ Constraints
- Do **not** return a new array
- Modify the input list directly
- Use constant extra space

---

### 💡 Approach: Two Pointer Technique

We use **two pointers**:
- `l` → starts from the beginning of the list
- `r` → starts from the end of the list

#### Algorithm Steps:
1. Initialize `l = 0` and `r = len(s) - 1`
2. Swap the elements at positions `l` and `r`
3. Move `l` one step forward
4. Move `r` one step backward
5. Repeat until `l >= r`

---

### 🧪 Example

#### Input
    ["h", "e", "l", "l", "o"]


#### Output
    ["o", "l", "l", "e", "h"]

---

### ⏱️ Complexity Analysis

| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(1)  |

---

### 📌 Key Takeaways
- In-place reversal avoids extra memory usage
- Two pointers ensure a single pass
- Simple and interview-friendly approach
- Commonly asked problem in coding interviews


---


## 3️⃣ Valid Palindrome II

### 🧩 Problem Statement

Given a string `s`, return `True` if the string can be a palindrome after deleting **at most one character**.  
Otherwise, return `False`.

---

### 💡 Approach: Two Pointers with Helper Palindrome Check

We use a **two pointer technique** combined with a **greedy check**.

#### Key Idea
- Compare characters from both ends
- On the **first mismatch**, try:
  - skipping the left character **or**
  - skipping the right character
- If either case forms a palindrome, return `True`

---

### 🧠 Algorithm Steps

1. Initialize two pointers:
   - `l = 0` (start)
   - `r = len(s) - 1` (end)
2. While `l < r`:
   - If `s[l] == s[r]`, move both pointers inward
   - If mismatch occurs:
     - Check if substring `s[l+1 : r]` is a palindrome
     - OR if substring `s[l : r-1]` is a palindrome
3. If one of the checks returns `True`, the string is valid
4. If no mismatches occur, the string is already a palindrome

---

### 🧪 Example

#### Input
    "abca"

#### Output
    True


#### Explanation
Removing `'b'` or `'c'` makes the string `"aca"` or `"aba"`, both palindromes.

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(1)  |

The helper palindrome check runs at most once.

### 📌 Key Takeaways
- Two pointers reduce unnecessary comparisons
- Greedy decision on first mismatch
- No extra space required
- Frequently asked interview problem