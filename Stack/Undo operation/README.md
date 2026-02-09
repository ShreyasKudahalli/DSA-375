# Stack Simulation & Undo Operations

**Stack Simulation & Undo Operations** refer to a powerful problem-solving pattern where a stack is used to mimic step-by-step execution and reversal of actions, just like an undo feature in text editors or applications. By always keeping track of the most recent operation at the top, stacks allow efficient addition, removal, and rollback of states, making them ideal for problems involving backtracking, adjacent cancellations, expression evaluation, and string reductions. This pattern ensures clean, intuitive, and optimal solutions where each operation can be applied or undone in constant time.


## 1️⃣ Backspace String Compare (Using Stack)

### 📌 Problem Statement
You are given two strings `s` and `t` containing lowercase letters and the character `'#'`, where `'#'` represents a **backspace**.

Each `'#'` deletes the **previous character**, if any.

Return **true** if the two strings are equal after processing all backspaces; otherwise, return **false**.

---

### 🧠 Intuition

Backspace behavior mimics a **text editor**:
- Normal characters are typed
- `'#'` deletes the most recent character

A **stack** naturally models this behavior:
- Push characters as they appear
- Pop the last character when a backspace is encountered

After processing both strings, simply compare the final results.

---

### 🚀 Approach (Stack Simulation)

1. Create a helper function to process a string:
   - Initialize an empty stack
   - Traverse characters:
     - If character is not `'#'`, push to stack
     - If character is `'#'` and stack is not empty, pop
2. Convert the stack into a string
3. Compare the processed results of both strings

---

### Example

**Example 1**
#### Input
    s = "ab#c"
    t = "ad#c"
#### Output
    True
Explanation: Both strings become "ac"

**Example 2**
#### Input
    s = "a#c"
    t = "b"
#### Output
    False

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n + m)  |
| Space Complexity | O(n + m)  |

Where:
n = length of string s
m = length of string t

---

### ✅ Key Takeaways

- Stack perfectly simulates backspace behavior
- Clean and intuitive solution
- Avoids unnecessary string manipulations
- Great example of real-world stack usage


---


## 2️⃣ Remove All Adjacent Duplicates in String (Using Stack)

### 📌 Problem Statement
Given a string `s`, repeatedly remove **adjacent duplicate characters** until no such duplicates remain.

Return the final string after all possible removals.

---

### 🧠 Intuition

Whenever two **adjacent characters are the same**, they cancel each other out.  
This behavior is similar to **undoing actions**, which makes a **stack** the ideal data structure.

- Push characters onto the stack
- If the current character matches the stack’s top, remove the top
- Otherwise, add the character to the stack

The stack always represents the **current valid string**.

---

### 🚀 Approach (Stack-Based)

1. Initialize an empty stack
2. Traverse the string character by character
3. For each character:
   - If the stack is empty, push the character
   - If the top of the stack matches the character, pop it
   - Otherwise, push the character
4. Convert the stack to a string and return it

---

### Example

#### Input
    s = "abbaca"
#### Output
    "ca"
**Steps**
- a → push
- b → push
- b → pop
- a → pop
- c → push
- a → push

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the string.

---

### ✅ Key Takeaways

- Stack efficiently handles adjacent comparisons
- Each character is pushed and popped at most once
- Eliminates duplicates in a single pass
- Clean and intuitive solution


---


## 3️⃣ Make The String Great (Using Stack)

### 📌 Problem Statement
Given a string `s` consisting of lowercase and uppercase English letters, repeatedly remove **adjacent characters** if:
- They are the **same letter**
- They have **different cases** (one uppercase, one lowercase)

Return the final string after all such removals.

---

### 🧠 Intuition

In ASCII:
- The difference between a lowercase and uppercase version of the same letter is **32**
  - Example: `'a' (97)` and `'A' (65)`

So, if two adjacent characters differ by exactly **32 in ASCII value**, they form a **bad pair** and should be removed.

This removal may create new adjacent pairs, making a **stack** the perfect choice.

---

### 🚀 Approach (Stack-Based)

1. Initialize an empty stack
2. Traverse the string character by character
3. For each character:
   - If the stack is not empty **and**
     - `abs(ord(stack[-1]) - ord(current)) == 32`
     → pop the stack
   - Else, push the character onto the stack
4. Join the stack to form the final string

---
###  Example

#### Input
    s = "leEeetcode"

#### Output
    "leetcode"

**Process**
- e and E cancel out
- Remaining string is processed again

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the string.

---

### ✅ Key Takeaways

- ASCII value trick simplifies case comparison
- Stack handles cascading removals naturally
- Single-pass, clean solution
- Great example of string processing using stack


---


## 4️⃣ Minimum String Length After Removing Substrings (Using Stack)

### 📌 Problem Statement
You are given a string `s` consisting of uppercase English letters.

Repeatedly remove the substrings:
- `"AB"`
- `"CD"`

Return the **minimum possible length** of the string after performing all valid removals.

---

### 🧠 Intuition

Whenever the characters:
- `'A'` followed by `'B'`, or
- `'C'` followed by `'D'`

appear **adjacent**, they can be removed.

Removing one pair may create **new adjacent pairs**, so we need a way to:
- Track the most recent character
- Efficiently remove and re-check neighbors

A **stack** is ideal for this scenario.

---

### 🚀 Approach (Stack-Based)

1. Initialize an empty stack
2. Traverse the string character by character
3. For each character:
   - If the stack is empty, push the character
   - Otherwise, check the top of the stack:
     - If top + current forms `"AB"` or `"CD"`, pop the stack
     - Else, push the current character
4. After processing all characters, the stack size is the answer

---
### Example

#### Input
    s = "ABFCACDB"

#### Output
    2

#### Process
- Remove "AB" → "FCACDB"
- Remove "CD" → "FCAB"
- Remove "AB" → "FC"

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the string.

---

### ✅ Key Takeaways

- Stack efficiently handles adjacent substring removals
- Each character is pushed and popped at most once
- Handles cascading deletions naturally
- Clean and optimal solution

---
