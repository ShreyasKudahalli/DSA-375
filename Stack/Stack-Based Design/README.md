# Stack-Based Design
Stack-Based Problem Solving Approach focuses on leveraging the Last-In-First-Out (LIFO) principle to efficiently manage nested structures, sequential processing, backtracking, and state tracking in algorithms. By pushing and popping elements strategically, stacks help solve problems involving parentheses validation, expression evaluation, undo/redo operations, monotonic comparisons, and minimum/maximum tracking in linear time, making them a powerful and widely used data structure in both interviews and real-world applications.

## 1️⃣ Min Stack (Optimized Space Approach)

### 📌 Problem Statement

Design a stack that supports the following operations in **O(1)** time:

- `push(val)` → Push element onto stack  
- `pop()` → Remove the top element  
- `top()` → Get the top element  
- `getMin()` → Retrieve the minimum element in the stack  

---

### 🧠 Key Idea (Without Extra Stack)

Instead of using an additional stack to track minimum values,  
this implementation uses a **mathematical encoding trick** to store previous minimum values.

#### 🔥 Core Concept

When pushing a new minimum:
- encoded_value = 2 * val - current_min
This encoded value helps us:
- Store the new minimum
- Recover the previous minimum during `pop()`

This allows us to maintain minimum values **without extra space**.

---

### 🚀 How It Works

#### ✅ Push Operation

- If stack is empty:
  - Push value normally
  - Set `min = val`
- If new value is smaller than current min:
  - Push encoded value `2*val - min`
  - Update `min = val`
- Else:
  - Push normally

#### ✅ Pop Operation

- Pop the top element
- If popped value is less than `min`:
  - It means it's an encoded value
  - Restore previous minimum using:
        - previous_min = 2*current_min - encoded_value

#### ✅ Top Operation

- If top value is less than `min`:
- Return `min`
- Else:
- Return top normally

#### ✅ Get Minimum

- Simply return `self.min`

---

### 📝 Example Walkthrough
**Operations:**
- push(5)
- push(3)
- push(7)
- getMin()
- pop()
- getMin()

---

### Stack Behavior

| Operation | Stack State        | Min |
|------------|--------------------|-----|
| push(5)    | [5]                | 5   |
| push(3)    | [5, encoded]       | 3   |
| push(7)    | [...]              | 3   |
| getMin()   | —                  | 3   |
| pop()      | —                  | 3   |
| getMin()   | —                  | 3   |

---

### ⏱️ Complexity Analysis (Min Stack)

| Operation | Time  | Space |
|------------|-------|--------|
| push       | O(1)  | O(1)  |
| pop        | O(1)  | O(1)  |
| top        | O(1)  | O(1)  |
| getMin     | O(1)  | O(1)  |

Overall space complexity: O(n) (only one stack used)

---

### 🔍 Why This Approach Is Powerful

- No extra stack required
- Constant time operations
- Efficient memory usage
- Uses mathematical transformation cleverly

---

### ✅ Key Takeaways

- Encoded values help store previous minimum
- If top < min, it is an encoded value
- Recover previous min using:
    - prev_min = 2*current_min - encoded_value


---


## 2️⃣ Max Stack (Get Maximum in O(1) Without Extra Space)

### 📌 Problem Statement

Design a stack that supports the following operations in **O(1)** time:

- `push(x)` → Insert element  
- `pop()` → Remove top element  
- `peek()` → Return top element  
- `isEmpty()` → Check if stack is empty  
- `getMax()` → Retrieve the maximum element  

⚡ Constraint:  
Do this **without using an extra stack**.

---

### 🧠 Key Idea (Mathematical Encoding Trick)

Instead of maintaining a separate max stack, we store a **transformed value** whenever a new maximum appears.

#### 🔥 Encoding Formula

When pushing a new maximum:
- encoded_value = 2*x - current_max
This encoded value helps:
- Store the new maximum
- Recover the previous maximum during pop

---

### 🚀 How It Works

#### ✅ Push Operation

- If stack is empty:
  - Push value normally
  - Set `max = x`
- If `x > current max`:
  - Push encoded value `2*x - max`
  - Update `max = x`
- Else:
  - Push normally

#### ✅ Pop Operation

- Pop top element
- If popped value is greater than `max`:
  - It means it was encoded
  - Restore previous max using:
        - previous_max = 2*current_max - encoded_value
- If stack becomes empty:
  - Reset max

#### ✅ Peek Operation

- If top value is greater than `max`:
  - Return `max`
- Else:
  - Return top normally

#### ✅ Get Maximum

- Return `self.max`

---

### 📝 Example Walkthrough
**Operations:**
- push(3)
- push(5)
- push(2)
- push(7)
- getMax()
- pop()
- getMax()

---

### Stack Behavior:

| Operation | Stack State         | Max |
|------------|---------------------|-----|
| push(3)    | [3]                 | 3   |
| push(5)    | [3, encoded]        | 5   |
| push(2)    | [...]               | 5   |
| push(7)    | [..., encoded]      | 7   |
| getMax()   | —                   | 7   |
| pop()      | —                   | 5   |
| getMax()   | —                   | 5   |

---

### ⏱️ Complexity Analysis (Special Stack)

| Operation | Time  | Space |
|------------|-------|--------|
| push       | O(1)  | O(1)  |
| pop        | O(1)  | O(1)  |
| peek       | O(1)  | O(1)  |
| getMax     | O(1)  | O(1)  |

Overall space complexity: O(n)

---

### 🔎 Why This Approach Is Efficient

- No extra stack required
- Constant time maximum retrieval
- Clever mathematical transformation
- Interview-optimized solution

---

### ✅ Key Takeaways

- Encoded value is pushed when a new max appears
- If top > max, it is encoded
- Recover previous max using:
    - previous_max = 2*current_max - encoded_value


---


## 3️⃣ Implement Queue Using Two Stacks (MyQueue)

### 📌 Problem Statement

Design a **Queue (FIFO – First In First Out)** using only stack operations.  

Implement the following methods:

- `push(x)` → Insert element at the back of the queue  
- `pop()` → Remove the front element  
- `peek()` → Get the front element  
- `empty()` → Check whether the queue is empty  

---

### 🧠 Approach

We use **two stacks**:

- `inputStack` → Used for push operations  
- `outputStack` → Used for pop and peek operations  

#### 🔁 Key Idea

- When pushing → Always push into `inputStack`.
- When popping/peeking:
  - If `outputStack` is empty, transfer all elements from `inputStack` to `outputStack`.
  - This reversal ensures FIFO behavior.
- `outputStack` always contains elements in correct queue order.

This technique is called **amortized stack transfer**.

---

### 📊 How It Works
**Example Operations**

| Operation | inputStack | outputStack | Result |
|------------|------------|-------------|--------|
| push(1) | [1] | [] | — |
| push(2) | [1,2] | [] | — |
| peek() | [] | [2,1] | 1 |
| pop() | [] | [2] | 1 |
| empty() | — | — | False |

---

### ⏱️ Complexity Analysis
| Operation | Time Complexity | Space Complexity |
|------------|----------------|------------------|
| push | O(1) | O(n) |
| pop | O(1) amortized | O(n) |
| peek | O(1) amortized | O(n) |
| empty | O(1) | O(1) |


---

### 🔎 Why Amortized O(1)?
Each element is moved at most once from inputStack to outputStack.
So even though transfer looks O(n), overall cost per operation averages to O(1).

---

### 🎯 Key Takeaways

- Stack reversal enables queue behavior.
- Two stacks simulate FIFO efficiently.
- Common interview question (LeetCode – Implement Queue using Stacks).
- Demonstrates understanding of data structure transformation.


---


## 4️⃣ Implement Stack Using Queue (MyStack)

### 📌 Problem Statement

Design a **Stack (LIFO – Last In First Out)** using only queue operations.

Implement the following methods:

- `push(x)` → Push element onto stack  
- `pop()` → Remove the top element  
- `top()` → Get the top element  
- `empty()` → Check whether the stack is empty  

---

### 🧠 Approach

We use **one queue (deque)** to simulate stack behavior.

#### 🔁 Key Idea

- When pushing an element:
  1. Add it to the queue.
  2. Rotate the previous elements behind it.
- This ensures the **newly added element always stays at the front** of the queue.
- So:
  - `pop()` → Simply remove from front.
  - `top()` → Return front element.

This makes the queue behave like a stack.

---
### 📊 How It Works
**Example Operations**

| Operation | Queue State | Stack View |
|------------|------------|------------|
| push(1) | [1] | [1] |
| push(2) | [2,1] | [1,2] |
| push(3) | [3,2,1] | [1,2,3] |
| pop() | [2,1] | [1,2] |
| top() | — | 2 |

👉 The **front of the queue** always represents the **top of the stack**.

---

### ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|------------|----------------|------------------|
| push | O(n) | O(n) |
| pop | O(1) | O(1) |
| top | O(1) | O(1) |
| empty | O(1) | O(1) |

---

### 🔎 Why O(n) for Push?
Each push requires rotating all existing elements to maintain LIFO order.

---

### 🎯 Key Takeaways

- Queue rotation helps simulate stack behavior.
- Only one queue is sufficient.
- Good example of data structure transformation.
- Frequently asked in coding interviews.


---


## 5️⃣ Custom Stack with Increment Operation

### 📌 Problem Statement

Design a stack that supports the following operations:

- `push(x)` → Push element onto stack (only if stack size < maxSize)  
- `pop()` → Remove and return the top element  
- `increment(k, val)` → Increment the bottom `k` elements by `val`  

If:
- The stack is full → `push` does nothing  
- The stack is empty → `pop` returns `-1`

---

### 🧠 Approach

We maintain:

- `maxSize` → Maximum capacity of stack  
- `curSize` → Current number of elements  
- `Stack` → List to store elements  

#### 🔹 Push Logic
- Only insert if `curSize < maxSize`
- Increase `curSize` after successful insertion

#### 🔹 Pop Logic
- Remove top element if stack is not empty
- Decrease `curSize`
- Return popped value
- Return `-1` if stack is empty

#### 🔹 Increment Logic
- Find `n = min(k, curSize)`
- Increment the first `n` (bottom) elements by `val`

---
### 📊 Example Walkthrough
**Operations**
- CustomStack(3)
- push(1)
- push(2)
- pop()
- push(2)
- push(3)
- push(4)
- increment(5, 100)
- pop()
- pop()
- pop()
- pop()


**Execution Table**
| Operation | Stack State | Output |
|------------|------------|--------|
| push(1) | [1] | — |
| push(2) | [1,2] | — |
| pop() | [1] | 2 |
| push(2) | [1,2] | — |
| push(3) | [1,2,3] | — |
| push(4) | [1,2,3] | (ignored, full) |
| increment(5,100) | [101,102,103] | — |
| pop() | [101,102] | 103 |
| pop() | [101] | 102 |
| pop() | [] | 101 |
| pop() | [] | -1 |

---

### ⏱️ Complexity Analysis
| Operation | Time Complexity | Space Complexity |
|------------|----------------|------------------|
| push | O(1) | O(n) |
| pop | O(1) | O(1) |
| increment | O(k) | O(1) |

Where:
- n = stack size
- k = number of elements to increment

---

### 🎯 Key Takeaways

- Enforces stack capacity constraint
- Supports bottom-element modification
- Demonstrates stack manipulation beyond basic operations
- Frequently asked in coding interviews (LeetCode – Design a Stack With Increment Operation)


