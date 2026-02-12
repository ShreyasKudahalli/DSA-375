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