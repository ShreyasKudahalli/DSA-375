# 🔁 Recursive Stack Operations

Recursive stack operations use the call stack itself to manipulate elements without relying on additional data structures. By leveraging recursion and backtracking, we can perform complex modifications such as inserting an element at the bottom, reversing the entire stack, or deleting the middle element while preserving order. These techniques showcase a deeper understanding of the LIFO (Last In, First Out) principle and are commonly used in coding interviews to test mastery of recursion and stack behavior.


## 1️⃣ Reverse a Stack Using Recursion

This project demonstrates how to **reverse a stack using recursion** without using any extra data structures.

---

### 📌 Problem Statement

Given a stack `st`, reverse it using recursion.

You are **not allowed** to use any additional stack or data structure.

---

### 💡 Approach

We use two recursive functions:

1. `reverse(st)`
- Removes the top element.
- Recursively reverses the remaining stack.
- Inserts the removed element at the bottom.
2. `helper(st, x)`
- Inserts element `x` at the **bottom** of the stack.
- Uses recursion to empty the stack temporarily.
- Pushes elements back after inserting `x`.

---

### 🧠 How It Works

**Example**

#### Input
    [10, 20, 30, 40]

#### Output
    [40, 30, 20, 10]

- Step 1: Pop 40
- Step 2: Reverse [10, 20, 30]
- Step 3: Insert 40 at bottom
- Step 4: Continue recursively

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(N²) |
| Space Complexity | O(N)  |


---

### 🚀 Key Points

- No extra stack used.
- Pure recursion-based solution.
- Elegant interview solution.
- Demonstrates understanding of stack internals.


---


## 2️⃣ Insert an Element at the Bottom of a Stack (Using Recursion)

This implementation inserts an element at the **bottom of a stack** using recursion — without using any extra data structure.

---

### 📌 Problem Statement

Given a stack `st` and an element `x`, insert `x` at the **bottom** of the stack.

You are **not allowed** to use another stack or loop.

---

### 💡 Approach

We use recursion to:

1. Pop elements until the stack becomes empty.
2. Insert the given element `x`.
3. Push all previously removed elements back in order.

This preserves the original order while placing `x` at the bottom.

---

### 🧠 How It Works

**Example**

#### Input 
    [10, 20, 30]
    Insert: 5

#### Final Stack
    [5, 10, 20, 30]

#### Steps:
1. Pop 30
2. Pop 20
3. Pop 10
4. Stack becomes empty → Insert 5
5. Push back 10
6. Push back 20
7. Push back 30

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(N)  |
| Space Complexity | O(N)  |

**✔ Why O(N) Time?**
- We pop all elements once.
- Then push them back once.
- Total operations proportional to N.

**✔ Why O(N) Space?**
- Recursive call stack depth is N.

### 🚀 Key Points

- No extra data structures used.
- Clean recursion-based solution.
- Very common interview question.
- Forms the foundation for:
    - Reversing a stack
    - Deleting middle element recursively


---


## 3️⃣ Delete Middle Element of a Stack (Using Recursion)

This implementation removes the **middle element** of a stack using recursion — without using any extra data structure.

---

### 📌 Problem Statement

Given a stack `stack`, delete its **middle element**.

- Do not use any additional stack.
- Use recursion only.

---

### 💡 Approach

1. Compute the middle index:
- mid = len(stack) // 2
2. Use a recursive function `solve(st, curr)`:
- Pop elements until the stack becomes empty.
- While backtracking:
  - Skip pushing the middle element.
  - Push all other elements back.

---

### 🧠 How It Works

**Example**

#### Input Stack
    [10, 20, 30, 40, 50]
#### Final Output
    [10, 20, 40, 50]
#### Recursive Flow
1. Pop all elements recursively.
2. While rebuilding the stack:
   - Skip element at mid index 2.
   - Push remaining elements back.

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(N)  |
| Space Complexity | O(N)  |

---

### 🚀 Key Points

- No extra data structure used.
- Pure recursion-based solution.
- Common interview problem.
- Demonstrates stack backtracking technique.