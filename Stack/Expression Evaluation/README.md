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


---


## 3️⃣ Evaluate Reverse Polish Notation

### 📌 Problem Statement

You are given an array of strings `tokens` representing an **arithmetic expression in Reverse Polish Notation (RPN)**.

Evaluate the expression and return the result.

#### Rules
- Operators: `+`, `-`, `*`, `/`
- Each operand is an integer
- Division **truncates toward zero**
- The expression is always valid

---

### 📝 Example

#### Input:
    tokens = ["2", "1", "+", "3", "*"]
#### Output:
    9

#### Input: 
    tokens = ["4", "13", "5", "/", "+"]
#### Output:
    6

---

### 💡 Intuition

Reverse Polish Notation removes the need for parentheses and operator precedence rules.

A **stack** is ideal because:
- Operands are pushed as they appear
- Operators apply to the most recent operands
- Evaluation is naturally left-to-right

---

### 🚀 Approach (Stack-Based Evaluation)

1. Traverse each token:
   - If token is a number → push onto stack
   - If token is an operator → pop two operands
2. Apply the operator
3. Push the result back onto the stack
4. Final stack value is the answer

---

### 🧠 Algorithm Steps

- Initialize an empty stack
- For each token:
  - Push numbers directly
  - Pop `b` then `a` for operators
  - Compute `a op b`
  - Push result
- Return the final value from the stack

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the number of tokens.

---

### ✅ Key Takeaways

- RPN avoids operator precedence complexity
- Stack naturally fits postfix expression evaluation
- Order of popping operands is crucial (a op b)


---


## 4️⃣ Decode String

### 📌 Problem Statement

You are given an encoded string `s` following the rule:

- k[encoded_string]

Where:
- `encoded_string` inside the square brackets is repeated exactly `k` times
- `k` is a positive integer
- The input string is always valid

Return the **decoded string**.

---

### 📝 Example

#### Input:
    s = "3[a]2[bc]"
#### Output:
    "aaabcbc"

#### Input:
    s = "3[a2[c]]"
#### Output:
    "accaccacc"

---

### 💡 Intuition

Nested brackets mean nested repetitions.

A **stack** helps by:
- Storing characters until a closing bracket `]` is found
- Decoding the most recent bracketed expression first
- Naturally handling nested patterns

---

### 🚀 Approach (Stack-Based Decoding)

1. Traverse each character in the string
2. Push characters to the stack until `]` is found
3. On `]`:
   - Pop characters to form the substring
   - Pop digits to get the repeat count
   - Push repeated substring back to stack
4. Join stack contents for final result

---

### 🧠 Algorithm Steps

- Initialize empty stack
- For each character:
  - Push if not `]`
  - On `]`:
    - Build substring until `'['`
    - Extract repetition number
    - Push repeated substring
- Return joined stack

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the string.

---

### ✅ Key Takeaways

- Stack is perfect for nested decoding
- Process innermost brackets first
- Handle multi-digit repeat counts carefully


