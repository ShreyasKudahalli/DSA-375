# 🔁 Basic Doubly Linked List (DLL) Operations

Basic Doubly Linked List (DLL) operations involve fundamental manipulations such as insertion (at beginning, end, or specific position), deletion, traversal (forward and backward), and updating node connections while maintaining both `next` and `prev` pointers. Unlike singly linked lists, DLLs allow bidirectional traversal, making operations like deletion and reverse navigation more efficient. Mastering these core operations strengthens understanding of pointer management, dynamic memory handling, and structural integrity, which are essential for implementing advanced data structures like LRU Cache, browser history systems, and undo/redo functionality.


## 1️⃣ Construct Doubly Linked List from Array

### 📌 Problem Statement

Given an array of integers, construct a **Doubly Linked List (DLL)** such that:

* Each array element becomes a node.
* `next` pointer connects to the next node.
* `prev` pointer connects to the previous node.
* Return the `head` of the constructed doubly linked list.

---

### 🧠 Approach

To build a doubly linked list:

1. Create a `Node` for each element in the array.
2. Maintain two pointers:

   * `head` → first node of the list
   * `tail` → last node (used to append new nodes)
3. For each new node:

   * Connect `tail.next` to the new node.
   * Connect `node.prev` to the current tail.
   * Move `tail` forward.
4. Return the `head`.

---

### 🔹 Node Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

Each node contains:

* `data` → value
* `next` → pointer to next node
* `prev` → pointer to previous node

---

### 🔍 Example

#### Input

```text
arr = [1, 2, 3, 4]
```

#### Constructed Doubly Linked List

```text
NULL ← 1 ⇄ 2 ⇄ 3 ⇄ 4 → NULL
```

* `1.prev = NULL`
* `4.next = NULL`
* Middle nodes are connected both ways

---

### ⏱ Time & Space Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(n)  |

* We iterate through the array once.
* One node is created for each element.

---

### 📚 Key Concepts Used

* Doubly Linked List
* Pointer Manipulation
* Tail Pointer Optimization
* Dynamic Node Creation

---

### 🚀 Why This Approach Works

* Efficient single-pass construction.
* Maintains both forward and backward links.
* Clean and easy-to-understand pointer handling.
* Commonly used in:

  * Browser history navigation
  * LRU Cache implementation
  * Undo/Redo functionality


---


## 2️⃣ Insert Node at Given Position in Doubly Linked List

### 📌 Problem Statement

Given the head of a **Doubly Linked List (DLL)**, insert a new node with value `x` **after position `p` (0-based index)** and return the updated head of the list.

* The position `p` represents the node after which the new node must be inserted.
* If position is invalid, return the original list unchanged.

---

### 🧠 Approach

To insert a node at a given position in a DLL:

1. Traverse the list until position `p`.
2. Create a new node with value `x`.
3. Adjust four pointers carefully:

   * `node.next`
   * `node.prev`
   * `temp.next`
   * `temp.next.prev` (if it exists)
4. Return the head.

Since this is a **doubly linked list**, both forward and backward links must be maintained correctly.

---

### 🔹 Node Structure

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
```

Each node contains:

* `data` → value stored
* `next` → pointer to next node
* `prev` → pointer to previous node

---

### 🔍 Example

#### Input

```text
List: 1 ⇄ 2 ⇄ 4 ⇄ 5
p = 1
x = 3
```

#### Output

```text
1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5
```

The new node `3` is inserted after position `1` (after value `2`).

---

### ⏱ Time & Space Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(1)  |

* We traverse the list once.
* Only one new node is created.

---

### 📚 Key Concepts Used

* Doubly Linked List
* Pointer Reassignment
* Position-Based Traversal
* Edge Case Handling

---

### ⚠️ Edge Cases Covered

* Invalid position (greater than list length)
* Insertion at the last position
* Empty list scenario

---

### 🚀 Why Careful Pointer Handling is Important

In a doubly linked list:

* Missing even one pointer update can break the list.
* Both `next` and `prev` connections must remain consistent.
* Ensures correct forward and backward traversal.

---