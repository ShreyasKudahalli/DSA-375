# 🔗 Linked List + Stack

Combining a **Linked List** with a **Stack** enables efficient solutions to problems that require tracking previous nodes, handling next greater elements, removing specific nodes, or reversing parts of the list. While a linked list provides dynamic memory structure and flexible node manipulation, a stack adds Last-In-First-Out (LIFO) behavior that helps process nodes in reverse order or maintain monotonic patterns. This combination is especially useful in problems involving next greater node, node removal based on future values, palindrome checks, and structural reordering, allowing optimized solutions with linear time complexity and clean pointer management.


## 1️⃣ Remove Nodes From Linked List (Monotonic Stack Approach)

### 📌 Problem Statement

Given the head of a singly linked list, remove every node that has a node with a **greater value to its right**.
Return the head of the modified linked list.

#### 🔎 In Simple Words

If a node has a bigger number somewhere after it in the list, delete that node.

---

### 🧠 Approach — Monotonic Stack

To efficiently determine whether a node has a greater value to its right, we use a **monotonic decreasing stack**.

#### 🔹 Why Stack?

* We traverse from left to right.
* If the current node is greater than the stack's top node,

  * It means the previous node should be removed.
* We pop all smaller elements before pushing the current node.

This ensures that only nodes that **do not have a greater value to their right** remain in the stack.

---

### 🔹 Algorithm Steps

#### 1️⃣ Edge Case

If the list is empty or has only one node:

```python
if not head or not head.next:
    return head
```

No removal is needed.

---

#### 2️⃣ Traverse and Maintain Monotonic Stack

* Initialize an empty stack.
* For each node:

  * While stack is not empty and `stack[-1].val < current.val`

    * Pop from stack.
  * Push current node into stack.

This guarantees stack values are in decreasing order.

---

#### 3️⃣ Rebuild the Linked List

Since stack preserves valid nodes in order:

* Pop nodes from stack
* Reconstruct the list in reverse order

---

### 🔍 Example

#### Input

```
5 → 2 → 13 → 3 → 8
```

#### Step-by-step intuition:

* 5 → keep
* 2 → removed (13 is greater later)
* 13 → keep
* 3 → removed (8 is greater later)
* 8 → keep

#### Output

```
13 → 8
```

---

### ⏱ Time & Space Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(n)  |

* Each node is pushed and popped at most once.
* Stack stores up to `n` nodes.

---

### 📚 Key Concepts Used

* Monotonic Stack
* Linked List Traversal
* In-place Reconstruction
* Greedy Removal Strategy

---

### 🚀 Why This Approach Works Well

* Avoids nested loops (which would be O(n²))
* Efficient one-pass logic
* Clean and interview-friendly solution
* Uses stack to simulate "future comparison"


---


## 2️⃣ Remove Nodes From Linked List (Monotonic Stack Approach)

### 📌 Problem Statement

Given the head of a singly linked list, remove every node that has a node with a **greater value to its right**.
Return the head of the modified linked list.

#### 🔎 In Simple Words

If a node has a bigger number somewhere after it in the list, delete that node.

---

### 🧠 Approach — Monotonic Stack

To efficiently determine whether a node has a greater value to its right, we use a **monotonic decreasing stack**.

#### 🔹 Why Stack?

* We traverse from left to right.
* If the current node is greater than the stack's top node,

  * It means the previous node should be removed.
* We pop all smaller elements before pushing the current node.

This ensures that only nodes that **do not have a greater value to their right** remain in the stack.

---

### 🔹 Algorithm Steps

#### 1️⃣ Edge Case

If the list is empty or has only one node:

```python
if not head or not head.next:
    return head
```

No removal is needed.

---

#### 2️⃣ Traverse and Maintain Monotonic Stack

* Initialize an empty stack.
* For each node:

  * While stack is not empty and `stack[-1].val < current.val`

    * Pop from stack.
  * Push current node into stack.

This guarantees stack values are in decreasing order.

---

#### 3️⃣ Rebuild the Linked List

Since stack preserves valid nodes in order:

* Pop nodes from stack
* Reconstruct the list in reverse order

---

### 🔍 Example

#### Input

```
5 → 2 → 13 → 3 → 8
```

#### Step-by-step intuition:

* 5 → keep
* 2 → removed (13 is greater later)
* 13 → keep
* 3 → removed (8 is greater later)
* 8 → keep

#### Output

```
13 → 8
```

---

### ⏱ Time & Space Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(n)  |

* Each node is pushed and popped at most once.
* Stack stores up to `n` nodes.

---

### 📚 Key Concepts Used

* Monotonic Stack
* Linked List Traversal
* In-place Reconstruction
* Greedy Removal Strategy

---

### 🚀 Why This Approach Works Well

* Avoids nested loops (which would be O(n²))
* Efficient one-pass logic
* Clean and interview-friendly solution
* Uses stack to simulate "future comparison"


---