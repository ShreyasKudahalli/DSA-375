# 🔗 Merge / Sort Linked List

Merge and Sort operations on a linked list are fundamental problems that demonstrate strong understanding of pointer manipulation and efficient algorithm design. Merging involves combining two already sorted linked lists into a single sorted list by comparing nodes sequentially, while sorting a linked list is commonly done using the Merge Sort algorithm due to its optimal time complexity of **O(n log n)** and its suitability for linked structures (since it does not require random access like arrays). These problems highlight key concepts such as the fast and slow pointer technique, recursion, divide-and-conquer strategy, and in-place node rearrangement, making them essential for mastering data structures and technical interviews.


## 1️⃣ Merge Two Sorted Linked Lists

### 📌 Problem Statement

Given the heads of two **sorted singly linked lists**, merge them into one sorted linked list and return its head.

* The new list should be made by splicing together the nodes of the first two lists.
* The result must also be sorted.

This is a classic linked list problem frequently asked in coding interviews and platforms like LeetCode.

---

### 🧠 Approach

#### 🔹 Idea

We compare nodes from both linked lists one by one and always attach the smaller node to the merged list.

#### 🔹 Steps

1. Handle edge cases:

   * If `list1` is `None`, return `list2`
   * If `list2` is `None`, return `list1`

2. Initialize:

   * `head` → points to the first node of the merged list
   * `temp` → used to build the merged list

3. Traverse both lists:

   * Compare `list1.val` and `list2.val`
   * Attach the smaller node to `temp.next`
   * Move the corresponding pointer forward

4. If one list finishes:

   * Attach the remaining nodes of the other list

5. Return `head`

---

### 🔍 Example

#### Input

```
list1: 1 → 3 → 5
list2: 2 → 4 → 6
```

#### Output

```
1 → 2 → 3 → 4 → 5 → 6
```

---

### ⏱ Time & Space Complexity

| Complexity | Value    |
| ---------- | -------- |
| Time       | O(n + m) |
| Space      | O(1)     |

* `n` = length of list1
* `m` = length of list2
* We traverse both lists once.
* No extra space is used (in-place merging).

---

### 📚 Key Concepts Used

* Singly Linked List
* Two Pointer Technique
* Iterative Traversal
* Edge Case Handling

---

### 🚀 Why This Approach?

* Efficient (linear time)
* No extra memory allocation
* Clean pointer manipulation
* Interview-friendly solution


---


## 2️⃣ Sort Linked List (Merge Sort on Linked List)

### 📌 Problem Statement

Given the head of a singly linked list, sort the list in ascending order and return its head.

* The solution must run in **O(n log n)** time.
* Sorting must be done efficiently for a linked list structure.

---

### 🧠 Approach — Merge Sort (Divide & Conquer)

Unlike arrays, linked lists do not support random access, making algorithms like Quick Sort inefficient.
**Merge Sort** is the ideal choice because:

* It works efficiently with sequential access.
* It guarantees **O(n log n)** time complexity.
* It requires only constant extra space (excluding recursion stack).

---

### 🔹 Algorithm Steps

#### 1️⃣ Base Case

If the list is empty or contains only one node:

```python
if not head or not head.next:
    return head
```

The list is already sorted.

---

#### 2️⃣ Split the List (Find Middle)

Use **Slow & Fast Pointer technique**:

* `slow` moves one step at a time
* `fast` moves two steps at a time
* When `fast` reaches the end, `slow` is at the middle

Then split the list into two halves.

---

#### 3️⃣ Recursively Sort Both Halves

```python
left = self.sortList(head)
right = self.sortList(mid)
```

Each half is recursively sorted using Merge Sort.

---

#### 4️⃣ Merge Two Sorted Lists

Use a dummy node to simplify pointer handling and merge both sorted halves.

---

### 🔍 Example

#### Input

```
4 → 2 → 1 → 3
```

#### Output

```
1 → 2 → 3 → 4
```

---

### ⏱ Time & Space Complexity

| Complexity | Value                      |
| ---------- | -------------------------- |
| Time       | O(n log n)                 |
| Space      | O(log n) (recursion stack) |

* The list is divided into halves → log n levels.
* Each level processes n nodes during merge.

---

### 📚 Key Concepts Used

* Merge Sort
* Divide and Conquer
* Fast & Slow Pointer Technique
* Recursion
* Linked List Manipulation
* Dummy Node Optimization

---

### 🚀 Why Merge Sort for Linked List?

* Does not require random indexing.
* Efficient node splitting.
* Stable sorting algorithm.
* Optimal time complexity for linked list sorting.


---
