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


---


## 5️⃣ Infix to Prefix Conversion (Using Stack)

### 📌 Problem Statement
Given an **infix expression** (e.g. `A+B`, `(A-B/C)*(A/K-L)`), convert it into its **prefix expression** using a stack.

Prefix notation places the operator **before** its operands and removes the need for parentheses.

---

### 🧠 Key Idea

To convert **Infix → Prefix**, we use a clever transformation:
1. Reverse the infix expression
2. Swap opening and closing parentheses
3. Convert the modified expression to **postfix**
4. Reverse the postfix result → this becomes **prefix**

This approach avoids writing a separate algorithm from scratch.

---

### 🚀 Algorithm Steps

1. Reverse the infix string  
2. Replace:
   - `'('` with `')'`
   - `')'` with `'('`
3. Traverse the modified string:
   - If operand → add to result
   - If `'('` → push to stack
   - If `')'` → pop until `'('`
   - If operator:
     - Pop higher (or equal for `^`) precedence operators
     - Push current operator
4. Pop remaining operators from stack
5. Reverse the result → **Prefix expression**

---

### 📐 Operator Precedence
| Operator | Precedence |
|--------|------------|
| `^`    | 3 |
| `* /`  | 2 |
| `+ -`  | 1 |

---

### 📝 Example
#### Input
    (A-B/C)*(A/K-L)
#### Output
    *-A/BC-/AKL

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the expression.

---

### ✅ Key Takeaways

- Stack helps manage operators and precedence
- Reversal trick simplifies infix → prefix conversion
- Works for multi-operator and parenthesized expressions
- Clean and interview-friendly approach


---


## 6️⃣ Infix to Postfix Conversion (Using Stack)

### 📌 Problem Statement
Given an **infix expression** (e.g. `A+B`, `(A-B/C)*(A/K-L)`), convert it into a **postfix expression** (also known as Reverse Polish Notation).

In postfix notation, operators appear **after** their operands, and parentheses are no longer required.

---

### 🧠 Intuition

Infix expressions are easy for humans to read but hard for machines to evaluate directly because of:
- Operator precedence
- Parentheses

A **stack** helps us:
- Temporarily store operators
- Ensure correct precedence and associativity
- Output a valid postfix expression in one pass

---

### 🚀 Approach (Stack-Based)

#### Rules to follow:
- **Operands (letters/digits)** → add directly to result
- **`(`** → push to stack
- **`)`** → pop from stack until `(` is found
- **Operators (`+ - * / ^`)**:
  - Pop operators from stack with **higher precedence**
  - For equal precedence:
    - Pop if operator is **left associative**
    - Do NOT pop if operator is `^` (right associative)
  - Push current operator to stack

---

### 📐 Operator Precedence
| Operator | Precedence | Associativity |
|--------|------------|---------------|
| `^`    | 3 | Right |
| `* /`  | 2 | Left |
| `+ -`  | 1 | Left |

---

### 📝 Example
#### Input
    (A-B/C)*(A/K-L)
#### Output
    ABC/-AK/L-*

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the expression.

---

### ✅ Key Takeaways

- Stack efficiently handles precedence and parentheses
- Right associativity of ^ needs special handling
- Postfix expressions are easier to evaluate programmatically
- Commonly asked in DSA and compiler design interviews


---


## 7️⃣ Postfix to Infix Conversion (Using Stack)

### 📌 Problem Statement
Given a **postfix expression** (Reverse Polish Notation), convert it into an **infix expression**.

In postfix notation, operators come **after** their operands, whereas in infix notation, operators are placed **between** operands and may require parentheses to preserve evaluation order.

---

### 🧠 Intuition

Postfix expressions remove the need for parentheses and precedence rules, making them easy to evaluate.  
To reconstruct an infix expression:

- Operands can be used directly
- When an operator appears, it must combine the **two most recent operands**
- Parentheses are required to preserve the original evaluation order

A **stack** is perfect for this pattern.

---

### 🚀 Approach (Stack-Based)

#### Rules:
- **Operand (alphanumeric)** → push onto stack
- **Operator**:
  1. Pop two elements from stack  
     - First pop → right operand  
     - Second pop → left operand
  2. Combine them as `(left operator right)`
  3. Push the new expression back onto the stack

At the end, the stack contains a single valid infix expression.

---

### Example

#### Input
    ab+c*

#### Output
    ((a+b)*c)

#### Steps
- a → push
- b → push
- + → (a+b)
- c → push
- * → ((a+b)*c)

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the postfix expression.

---

### ✅ Key Takeaways

- Stack helps rebuild expression structure
- Parentheses ensure correct evaluation order
- Operands are pushed, operators combine expressions
- Fundamental expression conversion problem in DSA


---


## 8️⃣ Prefix to Infix Conversion (Using Stack)

### 📌 Problem Statement
Given a **prefix expression**, convert it into an **infix expression**.

In prefix notation, operators appear **before** their operands, while in infix notation, operators are placed **between** operands and usually require parentheses to preserve evaluation order.

---

### 🧠 Intuition

Prefix expressions are evaluated from **right to left**.  
To convert prefix to infix:

- Operands can be used directly
- When an operator is encountered, it must combine the **next two operands**
- Parentheses are required to maintain correct precedence

A **stack** helps manage operands and intermediate expressions efficiently.

---

### 🚀 Approach (Stack-Based)

#### Rules:
- Traverse the prefix expression **from right to left**
- **Operand (alphanumeric)** → push onto stack
- **Operator**:
  1. Pop two elements from stack  
     - First pop → left operand  
     - Second pop → right operand
  2. Form a new expression: `(left operator right)`
  3. Push it back onto the stack

At the end, the stack will contain one valid infix expression.

---

### 📝 Example

#### Input
    *+ab-cd

#### Output
    ((a+b)*(c-d))

#### Steps
- Traverse from right to left
- d, c → operands
- - → (c-d)
- b, a → operands
- + → (a+b)
- * → ((a+b)*(c-d))

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the prefix expression.

---

### ✅ Key Takeaways

- Prefix expressions are processed right to left
- Stack stores operands and partial infix expressions
- Parentheses preserve operator precedence
- Classic stack-based expression conversion problem


---


## 9️⃣ Postfix to Prefix Conversion (Using Stack)

### 📌 Problem Statement
Given a **postfix expression** (Reverse Polish Notation), convert it into a **prefix expression**.

- **Postfix**: operator comes **after** operands  
- **Prefix**: operator comes **before** operands  

The goal is to transform the expression while preserving the correct order of evaluation.

---

### 🧠 Intuition

Postfix expressions are evaluated **left to right**.  
Whenever we encounter an operator, it applies to the **two most recent operands**.

To convert postfix → prefix:
- Operands are pushed directly
- Operators combine the last two operands into a new prefix expression

A **stack** naturally supports this behavior.

---

### 🚀 Approach (Stack-Based)

#### Rules:
- Traverse the postfix expression from **left to right**
- **Operand (alphanumeric)** → push onto stack
- **Operator**:
  1. Pop two elements from the stack  
     - First pop → right operand  
     - Second pop → left operand
  2. Form prefix expression:  
     `operator + left + right`
  3. Push the new expression back onto the stack

At the end, the stack contains a single valid prefix expression.

---

### 📝 Example

#### Input
    ab+c*

#### Output
    *+abc

#### Steps
- a, b → push
- + → +ab
- c → push
- * → *+abc

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the postfix expression.

---

### ✅ Key Takeaways

- Stack stores operands and intermediate expressions
- Operators combine two most recent operands
- Order matters: operator + left + right
- Clean and efficient expression conversion technique


---


## 1️⃣0️⃣ Prefix to Postfix Conversion (Using Stack)

### 📌 Problem Statement
Given a **prefix expression**, convert it into a **postfix expression**.

- **Prefix**: operator comes **before** operands  
- **Postfix**: operator comes **after** operands  

The conversion must preserve the correct order of evaluation.

---

### 🧠 Intuition

Prefix expressions are evaluated **right to left**.  
When an operator is encountered, it applies to the **next two operands**.

To convert prefix → postfix:
- Operands are pushed directly
- Operators combine the two most recent operands into a new postfix expression

A **stack** makes this conversion clean and efficient.

---

### 🚀 Approach (Stack-Based)

#### Rules:
- Traverse the prefix expression **from right to left**
- **Operand (alphanumeric)** → push onto stack
- **Operator**:
  1. Pop two elements from stack  
     - First pop → left operand  
     - Second pop → right operand
  2. Form postfix expression:  
     `left + right + operator`
  3. Push the new expression back onto the stack

At the end, the stack contains one valid postfix expression.

---

### 📝 Example

#### Input
    *+ab-cd

#### Output
    ab+cd-*

#### Steps
- Traverse from right to left
- d, c → operands
- - → cd-
- b, a → operands
- + → ab+
- * → ab+cd-*

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Where n is the length of the prefix expression.

---

### ✅ Key Takeaways

- Prefix expressions are processed right to left
- Stack stores operands and intermediate postfix expressions
- Operator placement is always at the end
- Fundamental expression conversion problem in DSA




