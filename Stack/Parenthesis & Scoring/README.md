# Parenthesis Handling & Scoring Using Stack

Parenthesis Handling & Scoring Using Stack is a fundamental pattern where stacks are used to validate, balance, and compute values from parenthesis-based expressions by tracking nesting depth and structural order. By leveraging the LIFO nature of stacks, we can efficiently match opening and closing brackets, calculate scores based on hierarchy, and resolve nested structures in a single pass, making this approach both intuitive and optimal for problems involving balanced expressions and scoring rules.

## 1️⃣ Valid Parentheses (Using Stack)

## 📌 Problem Statement
Given a string `s` containing only the characters:
- `'(' , ')'`
- `'{' , '}'`
- `'[' , ']'`

Determine if the input string is **valid**.

A string is valid if:
- Open brackets are closed by the **same type** of brackets
- Open brackets are closed in the **correct order**
- Every closing bracket has a corresponding opening bracket

---

### 🧠 Intuition

Parentheses validation is a classic **stack simulation** problem:
- Opening brackets should be matched with the **most recent unmatched opening**
- This **Last In, First Out (LIFO)** behavior is exactly how a stack works

Additionally, ASCII values of matching brackets differ by a small fixed amount, which can be used to simplify matching.

---

### 🚀 Approach (Stack-Based)

1. Initialize an empty stack
2. Traverse the string character by character
3. For each character:
   - If it is an opening bracket → push onto stack
   - If it is a closing bracket:
     - If stack is empty → invalid
     - If top of stack does not match the closing bracket → invalid
     - Else → pop the stack
4. At the end:
   - If stack is empty → valid
   - Else → invalid

---

### Example

**Example 1**
#### Input
    s = "()[]{}"
#### Output
    True

**Example 2**
#### Input
    s = "(]"
#### Output
    False

**Example 3**
#### Input
    s = "({[]})"
#### Output
    True

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the string.

---

### ✅ Key Takeaways

- Stack enforces correct nesting and order
- Each bracket is pushed and popped at most once
- ASCII trick simplifies bracket matching
- Fundamental interview problem for stacks


---


## 2️⃣ Minimum Additions to Make Parentheses Valid (Using Stack)

### 📌 Problem Statement
Given a string `s` consisting only of `'('` and `')'`, determine the **minimum number of parentheses** that must be added to make the string **valid**.

A valid parentheses string satisfies:
- Every opening bracket `'('` has a corresponding closing bracket `')'`
- Parentheses are closed in the correct order

---

### 🧠 Intuition

An invalid parentheses string can have:
- Extra closing brackets `')'`
- Unmatched opening brackets `'('`

By simulating the process with a **stack**:
- Matched pairs cancel each other out
- Unmatched parentheses remain in the stack

The number of remaining characters in the stack equals the minimum additions required.

---

### 🚀 Approach (Stack-Based)

1. Initialize an empty stack
2. Traverse each character in the string:
   - If `'('` → push onto stack
   - If `')'`:
     - If stack top is `'('` → pop (valid match)
     - Else → push `')'` (unmatched closing)
3. At the end, the size of the stack is the answer

---

### 📝 Example

**Example 1**
#### Input
    s = "())"
#### Output
    1
**Process**
- ( → push
- ) → pop
- ) → unmatched

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the string.

---

### ✅ Key Takeaways

- Stack tracks unmatched parentheses
- Each character is processed once
- Remaining stack size gives minimum additions
- Clean and intuitive validation logic


---


## 3️⃣ Longest Valid Parentheses (Using Stack)

### 📌 Problem Statement
Given a string `s` consisting of only `'('` and `')'`,  
return the **length of the longest valid (well-formed) parentheses substring**.

---

### 🧠 Intuition

To find the longest valid substring:
- We need to track **matching parentheses**
- Also track where an invalid sequence begins

A stack helps by:
- Storing indices instead of characters
- Keeping track of the **last unmatched position**
- Allowing length calculation using index differences

The key trick:  
Initialize the stack with `-1` to handle edge cases and length calculation properly.

---

### 🚀 Approach (Stack-Based)

1. Initialize:
   - `stack = [-1]` (base index for length calculation)
   - `ans = 0`
2. Traverse the string:
   - If `'('` → push its index
   - If `')'`:
     - Pop the stack
     - If stack becomes empty:
       - Push current index (new base)
     - Else:
       - Calculate valid length:  
         `i - stack[-1]`
       - Update maximum length
3. Return `ans`

---

### 📝 Example

**Example 1**
#### Input
    s = "(()"
#### Output
    2

**Example 2**
#### Input
    s = ")()())"
#### Output
    4
Longest valid substring: "()()"

### 🔎 Why -1 in Stack?
- Acts as a base index
- Helps calculate length correctly when first valid pair appears
- Handles cases where the string starts with ')'

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the string.

Each index is pushed and popped at most once.

---

### ✅ Key Takeaways

- Store indices, not characters
- Use -1 as initial base index
- Stack helps track valid substring boundaries
- Efficient O(n) solution


---


## 4️⃣  Score of Parentheses (Stack Approach)

### 📌 Problem Statement

Given a balanced parentheses string `s`, return its **score**.

#### Scoring Rules:
1. `"()"` has score **1**
2. `"AB"` has score **A + B**, where A and B are balanced strings
3. `"(A)"` has score **2 × A**

---

### 🧠 Intuition

We use a **stack** to simulate nested structures.

Key idea:
- Push `0` for every `'('` to act as a marker.
- When encountering `')'`:
  - If it directly closes `"()"`, score is `1`
  - If it wraps a nested expression, score is `2 × (sum of inner scores)`

The stack helps:
- Track nested layers
- Accumulate scores inside parentheses
- Collapse them when closed

---

### 🚀 Approach (Stack Simulation)

1. Initialize:
   - `stack = []`
   - `count = 0`

2. Traverse string:
   - If `'('` → push `0` (marker)
   - If `')'`:
     - Pop values until reaching `0`
     - Sum all popped values → `val`
     - Compute:
       - `1` if empty pair `"()"`
       - `2 * val` if nested
     - Push computed value back to stack

3. After traversal:
   - Sum all values in stack

---

### 📝 Example

**Example 1**
#### Input
    s = "()"
#### Output
    1

**Example 2**
#### Input
    s = "(())"
#### Output
    2
**Explanation:**
- ( A )
- A = "()"
- Score = 2 × 1 = 2

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the string.

Each element is pushed and popped at most once.

---

### ✅ Key Takeaways

- Use 0 as a marker for '('
- Sum nested scores before doubling
- "()" → 1
- "(A)" → 2 × A
- Adjacent expressions add up