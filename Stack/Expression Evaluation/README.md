# 🧮 Expression Evaluation Using Stack
Expression Evaluation focuses on parsing and computing mathematical expressions involving numbers, operators, and sometimes parentheses while respecting operator precedence and associativity. Using stack-based techniques, we can efficiently handle multi-digit numbers, resolve higher-precedence operations like multiplication and division immediately, and manage nested expressions by storing intermediate results. This approach enables single-pass, optimal solutions that are both clean and interview-friendly, making expression evaluation a fundamental pattern in data structures and algorithms.

## 1️⃣ Basic Calculator

### 📌 Problem Statement

Given a string `s` representing a **valid mathematical expression**, evaluate the expression and return the result.

The expression may contain:
- Non-negative integers
- `+` and `-` operators
- Parentheses `(` and `)`
- Spaces

⚠️ No use of built-in evaluation functions is allowed.

---

### 📝 Example

#### Input:
    s = "1 + 1"

#### Output:
    2

#### Input:
    s = "(1 + (4 + 5 + 2) - 3) + (6 + 8)"

#### Output:
    23

---

### 💡 Intuition

Parentheses introduce **nested expressions**, so we need a way to:
- Save the current calculation state
- Reset and evaluate inner expressions independently
- Restore the previous state once parentheses close

A **stack** is perfect for handling this behavior.

---

### 🚀 Approach (Stack-Based Evaluation)

- Use variables to track:
  - `result` → current evaluated value
  - `num` → number being built
  - `sign` → current operator (`+` or `-`)
- Use a stack to store:
  - Previous `result`
  - Previous `sign`

---

### 🧠 Algorithm Steps

1. Traverse the string character by character
2. Build numbers digit by digit
3. On `+` or `-`:
   - Apply the previous number to the result
   - Update the sign
4. On `(`:
   - Push current result and sign to stack
   - Reset result and sign
5. On `)`:
   - Complete current expression
   - Apply sign and previous result from stack
6. Return final computed result

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the string.

---

### ✅ Key Takeaways

- Stack helps manage nested expressions
- Track sign separately to simplify calculations
- Handles multi-digit numbers cleanly


---


## 2️⃣ Basic Calculator II

### 📌 Problem Statement

Given a string `s` representing a **valid mathematical expression**, evaluate the expression and return the result.

The expression contains:
- Non-negative integers
- Operators: `+`, `-`, `*`, `/`
- Spaces

⚠️ Division should **truncate toward zero**.  
⚠️ The expression does **not** contain parentheses.

---

### 📝 Example

#### Input:
    s = "3+2*2"

#### Output:
    7

#### Input:
    s = " 3/2 "

#### Output:
    1

---

### 💡 Intuition

The key challenge is handling **operator precedence**:
- `*` and `/` must be evaluated **before** `+` and `-`

A **stack** allows us to:
- Defer addition and subtraction
- Immediately compute multiplication and division

---

### 🚀 Approach (Stack-Based Evaluation)

- Traverse the string once
- Build numbers digit by digit
- On encountering an operator:
  - Apply the **previous operator** to the current number
  - Push results into the stack
- At the end, sum the stack

---

### 🧠 Algorithm Steps

1. Initialize:
   - `stack` to store intermediate values
   - `num` to build numbers
   - `sign` to track the previous operator
2. Traverse the string:
   - Build numbers when digits are found
   - When an operator or end of string is found:
     - Apply the previous operator
3. Return the sum of the stack

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the string.

--

### ✅ Key Takeaways

- Stack handles operator precedence naturally
- Multiplication and division are resolved immediately
- Clean single-pass solution