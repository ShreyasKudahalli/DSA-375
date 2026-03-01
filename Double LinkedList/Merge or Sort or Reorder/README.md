# 🔁 Doubly Linked List Merge, Sort & Reorder Operations

This section covers essential transformation operations on a **Doubly Linked List (DLL)** including merging two sorted DLLs into a single sorted list, performing efficient sorting using techniques like Merge Sort, and reordering nodes to achieve specific structural patterns. These operations strengthen understanding of bidirectional pointer manipulation (`next` and `prev`), in-place restructuring, and optimized time–space complexity handling, making them fundamental concepts for mastering advanced linked list problems in data structures and coding interviews.


## 1️⃣ Flatten a Multilevel Doubly Linked List

### 📌 Problem Statement

You are given the head of a **multilevel doubly linked list**, where in addition to `next` and `prev` pointers, each node may also have a `child` pointer pointing to another doubly linked list.

Your task is to **flatten the list** so that:

* All nodes appear in a single-level doubly linked list.
* The flattened list follows **depth-first traversal order**.
* All `child` pointers are set to `None`.

---

### 🧠 Understanding the Structure

Each node contains:

```python
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
```

#### 🔹 Key Pointers

* `next` → Next node at same level
* `prev` → Previous node
* `child` → Points to a sub-level doubly linked list

---

### 🧠 Approach

We traverse the list node by node.

Whenever we encounter a node that has a `child`:

1️⃣ Save the child list
2️⃣ Find the tail of the child list
3️⃣ Connect:

* Child tail → original next node
  4️⃣ Connect:
* Current node → child
  5️⃣ Remove the child pointer

This effectively inserts the entire child list between the current node and its next node.

---

### 🔹 Algorithm Steps

#### 1️⃣ Handle Edge Case

```python
if not head:
    return head
```

---

#### 2️⃣ Traverse the List

For each node:

* If `node.child` exists:

  * Traverse child list to find its tail.
  * Connect child tail to `node.next`.
  * Update `prev` pointers accordingly.
  * Connect `node.next` to child.
  * Set `node.child = None`.

* Move to `node.next`.

---

### 🔍 Example

#### Input Structure

```text
1 - 2 - 3 - 4
        |
        7 - 8 - 9
```

#### Output (Flattened)

```text
1 - 2 - 3 - 7 - 8 - 9 - 4
```

All nodes now exist in a single-level doubly linked list.

---

### ⏱ Time & Space Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(1)  |

* Each node is visited once.
* No extra data structures are used.

---

### 📚 Key Concepts Used

* Doubly Linked List
* Pointer Rewiring
* Depth-First Flattening
* In-place Modification
* Child Pointer Handling

---

### ⚠️ Important Insight

* The order is **depth-first**.
* Always connect the child list before moving forward.
* Carefully update both `next` and `prev` pointers.
* Set `child = None` to avoid cycles.

---

### 🚀 Why This Approach Works

* Efficient in-place modification.
* Avoids recursion stack.
* Maintains proper doubly linked structure.
* Interview-friendly and optimized.

---


## 2️⃣ Merge Two Sorted Doubly Linked Lists

### 📌 Problem Statement

Given the heads of **two sorted Doubly Linked Lists (DLLs)**, merge them into a single **sorted doubly linked list** and return its head.

* The resulting list must maintain:

  * Sorted order
  * Proper `next` and `prev` connections
  * No extra nodes created (in-place merge)

---

### 🧠 Doubly Linked List Structure

Each node contains:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

---

### 🚀 Approach

This solution uses the **Two Pointer Technique** (similar to merging in Merge Sort).

#### 🔹 Steps:

1️⃣ Handle edge cases (if one list is empty).
2️⃣ Create a **dummy node** to simplify merging logic.
3️⃣ Compare nodes from both lists:

* Attach the smaller node to the merged list.
* Move the corresponding pointer forward.
  4️⃣ Attach any remaining nodes.
  5️⃣ Remove the dummy node and fix the head’s `prev` pointer.

---

### 🔍 Example

#### Input

```
List 1: 1 ⇄ 3 ⇄ 5  
List 2: 2 ⇄ 4 ⇄ 6
```

#### Output

```
1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5 ⇄ 6
```

---

### ⏱ Time & Space Complexity

| Complexity | Value    |
| ---------- | -------- |
| Time       | O(n + m) |
| Space      | O(1)     |

* `n` = length of first list
* `m` = length of second list
* No extra space used (in-place merge)

---

### 🎯 Key Concepts Used

* Two Pointer Technique
* Dummy Node Optimization
* In-place List Merging
* Pointer Manipulation (`next` & `prev`)
* Merge Sort Concept (merge step)

---

### ⚠️ Important Notes

* Always update both `next` and `prev` pointers.
* Reset `head.prev = None` after removing the dummy node.
* Works only if both input lists are **already sorted**.

---

### 🏆 Why This Approach is Good for Interviews

* Clean logic
* Efficient (linear time)
* No extra memory usage
* Demonstrates strong pointer handling skills

---


