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

## 3️⃣ Delete Node at Given Position in Doubly Linked List

### 📌 Problem Statement

Given the head of a **Doubly Linked List (DLL)** and a position `x` (1-based index), delete the node at position `x` and return the updated head of the list.

* If the list is empty, return `None`.
* If the position is invalid (greater than list length), return the original list unchanged.

---

### 🧠 Approach

To delete a node from a DLL, we must carefully update both:

* `next` pointer of the previous node
* `prev` pointer of the next node

Since it’s a doubly linked list, pointer updates must maintain **bidirectional integrity**.

---

### 🔹 Algorithm Steps

#### 1️⃣ Handle Empty List

If `head` is `None`, return `None`.

---

#### 2️⃣ Deleting the First Node (x = 1)

* Move `head` to `head.next`
* Set `head.prev = None` (if head exists)

This removes the first node safely.

---

#### 3️⃣ Traverse to Position `x`

* Use a counter starting from 1
* Move forward until reaching position `x`

If position exceeds list length, return original head.

---

#### 4️⃣ Adjust Pointers

For node `temp` at position `x`:

* If `temp.next` exists →
  `temp.next.prev = temp.prev`

* If `temp.prev` exists →
  `temp.prev.next = temp.next`

This disconnects the node from both sides.

---

### 🔍 Example

#### Input

```text
List: 1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5
x = 3
```

#### Output

```text
1 ⇄ 2 ⇄ 4 ⇄ 5
```

Node with value `3` is removed.

---

### ⏱ Time & Space Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(1)  |

* We traverse the list once.
* No extra memory is used.

---

### 📚 Key Concepts Used

* Doubly Linked List
* Pointer Reassignment
* Edge Case Handling
* Position-Based Deletion
* Bidirectional Link Maintenance

---

### ⚠️ Edge Cases Covered

* Empty list
* Deleting the first node
* Deleting the last node
* Invalid position
* Single-node list

---

### 🚀 Why Proper Pointer Handling is Important

In a doubly linked list:

* Both `prev` and `next` must be updated.
* Missing one update can break traversal.
* Ensures consistent forward and backward movement.


---


## 4️⃣ Reverse a Doubly Linked List

### 📌 Problem Statement

Given the head of a **Doubly Linked List (DLL)**, reverse the list and return the new head.

After reversing:

* The `next` pointers should point backward.
* The `prev` pointers should point forward.
* The last node becomes the new head.

---

### 🧠 Approach

Unlike a singly linked list, a DLL contains both:

* `next` pointer
* `prev` pointer

To reverse the list, we simply **swap the `next` and `prev` pointers for each node**.

---

### 🔹 Algorithm Steps

#### 1️⃣ Handle Edge Case

If the list is empty:

```python
if not head:
    return None
```

---

#### 2️⃣ Traverse and Swap Pointers

For each node:

* Store `current.prev` temporarily
* Swap:

  ```python
  current.prev = current.next
  current.next = temp
  ```
* Move to the next node (which is `current.prev` after swapping)

---

#### 3️⃣ Update Head

After the loop ends:

* `temp` will be pointing to the previous node reference
* Set new head using:

  ```python
  head = temp.prev
  ```

---

### 🔍 Example

#### Input

```
NULL ← 1 ⇄ 2 ⇄ 3 ⇄ 4 → NULL
```

#### Output

```
NULL ← 4 ⇄ 3 ⇄ 2 ⇄ 1 → NULL
```

---

### ⏱ Time & Space Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(1)  |

* We traverse the list once.
* No extra data structures are used.

---

### 📚 Key Concepts Used

* Doubly Linked List
* Pointer Swapping
* In-place Reversal
* Bidirectional Traversal

---

### ⚠️ Important Insight

After swapping `prev` and `next`:

* The traversal direction changes.
* That’s why we move using `current = current.prev`.

This is the key trick in reversing a doubly linked list efficiently.

---

### 🚀 Why This Approach is Efficient

* Single traversal
* No extra memory usage
* Clean pointer manipulation
* Interview-friendly solution

---


## 5️⃣ LRU Cache Implementation (HashMap + Doubly Linked List)

### 📌 Problem Statement

Design and implement a **Least Recently Used (LRU) Cache** with the following operations:

* `get(key)` → Return the value of the key if it exists, otherwise return `-1`.
* `put(key, value)` → Insert or update the key-value pair.
* When the cache exceeds its capacity, remove the **least recently used** item.

#### ⚡ Constraint:

Both operations must run in **O(1)** time complexity.

---

### 🧠 Approach — HashMap + Doubly Linked List

To achieve **O(1)** time for both operations, we combine:

#### 1️⃣ HashMap (`dict`)

* Maps `key → node`
* Provides O(1) lookup.

#### 2️⃣ Doubly Linked List (DLL)

* Maintains usage order.
* Most Recently Used (MRU) → near right.
* Least Recently Used (LRU) → near left.
* Allows O(1) insertion & deletion.

---

### 🏗 Design Structure

We use two dummy nodes:

```text
LEFT <-> ... <-> RIGHT
```

* `left` → LRU boundary
* `right` → MRU boundary
* Real nodes are inserted between them.

This avoids edge-case checks when inserting/removing nodes.

---

### 🔹 Key Helper Functions

#### ✅ remove(node)

Removes a node from the doubly linked list.

```python
prev.next = next
next.prev = prev
```

---

#### ✅ insert(node)

Inserts a node at MRU position (just before `right`).

```python
prev = right.prev
prev.next = node
node.prev = prev
node.next = right
right.prev = node
```

---

### 🔍 Example

```python
obj = LRUCache(2)

obj.put(1, 10)
obj.put(2, 20)
obj.get(1)       # returns 10
obj.put(3, 30)   # evicts key 2
obj.get(2)       # returns -1
```

#### Explanation:

* Capacity = 2
* After inserting 1 and 2 → cache full
* Access 1 → becomes MRU
* Insert 3 → evict LRU (key 2)

---

### ⏱ Time & Space Complexity

| Operation | Time |
| --------- | ---- |
| get()     | O(1) |
| put()     | O(1) |

| Space | O(capacity) |

* HashMap stores at most `capacity` elements.
* DLL stores the same nodes.

---

### 📚 Key Concepts Used

* Doubly Linked List
* HashMap (Dictionary)
* O(1) Deletion & Insertion
* Cache Eviction Policy
* System Design Fundamentals

---

### 🚀 Why This Design is Optimal

* HashMap gives instant access to nodes.
* DLL maintains order of usage.
* Dummy nodes eliminate edge-case checks.
* Industry-standard approach used in:

  * Browser caching
  * Database buffering
  * Memory management systems

---

### 🏁 Summary

This LRU Cache implementation achieves:

* Constant time operations
* Clean pointer manipulation
* Efficient eviction strategy
* Interview-ready optimized solution

---
