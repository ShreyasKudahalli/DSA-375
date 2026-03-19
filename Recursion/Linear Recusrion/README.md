# Linear Recursion

**Linear recursion** is a recursive pattern where each function call makes **exactly one recursive call**, progressing step by step toward a base case. In this approach, the problem is broken down into a **smaller subproblem of the same type**, and the recursion continues in a single chain until a terminating condition is met. It is commonly used in problems like **factorial computation, Fibonacci (tail recursion), reversing arrays/strings, and traversing linear data structures**. Although simple and easy to understand, linear recursion typically uses **O(n) time and O(n) space** due to the recursive call stack, making it important to consider iterative alternatives when optimizing for space.


## 1️⃣ Fibonacci Number (Tail Recursion)

### 📌 Problem Statement

Given an integer `n`, return the **nth Fibonacci number**.

The Fibonacci sequence is defined as:

```text
F(0) = 0  
F(1) = 1  
F(n) = F(n-1) + F(n-2)  for n ≥ 2
```

---

### 🧠 Approach — Tail Recursion

Instead of using the traditional recursive approach (which is inefficient due to repeated calculations), this solution uses **tail recursion**, which is an optimized recursive technique.

#### 🔹 Key Idea

We maintain two values:

* `a` → represents `F(n-2)`
* `b` → represents `F(n-1)`

At each recursive step:

```text
Next Fibonacci = a + b
```

We shift values forward:

```text
a = b  
b = a + b
```

This way, we compute the result **without recomputation**, similar to an iterative approach.

---

### 🚀 Algorithm Steps

1️⃣ Define a helper function:

```python
helper(a, b, n)
```

2️⃣ Base Case:

* If `n == 0`, return `a`

3️⃣ Recursive Step:

* Call:

```python
helper(b, a + b, n - 1)
```

4️⃣ Initial Call:

```python
helper(0, 1, n)
```

---

### 🔍 Example

#### Input

```text
n = 5
```

#### Execution Trace

| Step  | a | b | n |
| ----- | - | - | - |
| Start | 0 | 1 | 5 |
| 1     | 1 | 1 | 4 |
| 2     | 1 | 2 | 3 |
| 3     | 2 | 3 | 2 |
| 4     | 3 | 5 | 1 |
| 5     | 5 | 8 | 0 |

#### Output

```text
5
```

---

### ⏱ Time & Space Complexity

| Complexity | Value    |
| ---------- | -------- |
| Time       | **O(n)** |
| Space      | **O(n)** |

#### Why Space is O(n)?

* Due to the **recursive call stack**.
* Each recursive call adds a new stack frame.

👉 Note: Some languages optimize tail recursion to **O(1)** space, but Python **does not**.

---

### 🔑 Key Concepts Used

* Recursion
* Tail Recursion
* Dynamic State Transition
* Fibonacci Sequence

---

### ⚠️ Important Insight

Although this looks efficient, Python does **not support tail call optimization**, so deep recursion may lead to:

```text
RecursionError: maximum recursion depth exceeded
```

---


## 2️⃣ Reverse String (Recursion - In Place)

### 📌 Problem Statement

Given an array of characters `s`, reverse the array **in-place**.

* You must modify the input array directly.
* Do not return anything.

Example:

```text
Input:  ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

---

### 🧠 Approach — Recursion (Two-Pointer Technique)

This solution uses **recursion with a two-pointer approach**.

#### 🔹 Key Idea

* Use an index `i` starting from the beginning.
* Swap:

```text
s[i] ↔ s[n - 1 - i]
```

* Move inward recursively until reaching the middle of the array.

This avoids using extra space and keeps the solution clean and intuitive.

---

### 🚀 Algorithm Steps

1️⃣ Start recursion from index `i = 0`

2️⃣ Base Case:

```python
if i >= len(s) // 2:
    return
```

* Stop when pointers meet or cross the middle.

3️⃣ Swap elements:

```python
s[i], s[n-1-i] = s[n-1-i], s[i]
```

4️⃣ Recursive Call:

```python
helper(i + 1)
```

---

### 🔍 Example

#### Input

```text
s = ["a","b","c","d"]
```

#### Steps

| Step | i     | Swap  | Result       |
| ---- | ----- | ----- | ------------ |
| 1    | 0     | a ↔ d | [d, b, c, a] |
| 2    | 1     | b ↔ c | [d, c, b, a] |
| Stop | i = 2 | —     | Done         |

#### Output

```text
["d","c","b","a"]
```

---

### ⏱ Time & Space Complexity

| Complexity | Value    |
| ---------- | -------- |
| Time       | **O(n)** |
| Space      | **O(n)** |

#### Why Space is O(n)?

* Due to the **recursive call stack**.
* Each recursive call consumes stack memory.

---

### 🔑 Key Concepts Used

* Recursion
* Two-Pointer Technique
* In-place Swapping
* Divide and Conquer

---

### ⚠️ Important Insight

* The recursion stops at **half of the array**, so only `n/2` swaps are performed.
* Although the logic is optimal, recursion uses extra stack space.

---


## 3️⃣ Factorial of a Number (Recursion)

### 📌 Problem Statement

Given an integer `n`, return the **factorial of n**.

The factorial of a number is defined as:

```text
n! = n × (n-1) × (n-2) × ... × 1
```

#### Examples

```text
Input:  n = 5
Output: 120
```

```text
Input:  n = 3
Output: 6
```

---

### 🧠 Approach — Linear Recursion

This solution uses **linear recursion**, where each function call reduces the problem size by **1** until it reaches the base case.

#### 🔹 Key Idea

* The factorial of `n` depends on the factorial of `n-1`:

```text
n! = n × (n-1)!
```

* Keep calling the function recursively until we reach:

```text
1! = 1
```

---

### 🚀 Algorithm Steps

1️⃣ Base Case:

```python
if n == 1:
    return 1
```

2️⃣ Recursive Case:

```python
return n * factorial(n - 1)
```

3️⃣ Repeat until base case is reached.

---

### 🔍 Example

#### Input

```text
n = 4
```

#### Execution Flow

```text
factorial(4)
= 4 × factorial(3)
= 4 × 3 × factorial(2)
= 4 × 3 × 2 × factorial(1)
= 4 × 3 × 2 × 1
= 24
```

#### Output

```text
24
```

---

### ⏱ Time & Space Complexity

| Complexity | Value    |
| ---------- | -------- |
| Time       | **O(n)** |
| Space      | **O(n)** |

#### Why Space is O(n)?

* Each recursive call adds a **stack frame**.
* Total recursive calls = `n`

---

### 🔑 Key Concepts Used

* Recursion
* Linear Recursion
* Mathematical Recurrence
* Call Stack


---
