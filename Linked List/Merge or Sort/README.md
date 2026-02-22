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


## 3️⃣ Remove Duplicates from Sorted Linked List

### 📌 Problem Statement

Given the head of a **sorted singly linked list**, delete all duplicate elements such that each element appears only once.
Return the head of the modified list.

> ⚠️ The linked list is already sorted, which makes duplicate detection straightforward.

---

### 🧠 Approach

Since the list is sorted, duplicate elements will always appear **next to each other**.
This allows us to solve the problem in a single traversal.

---

### 🔹 Algorithm Steps

1️⃣ **Handle Edge Case**

If the list is empty or contains only one node:

```python
if not head or not head.next:
    return head
```

It is already free of duplicates.

---

2️⃣ **Traverse the List**

* Use a pointer `temp` starting from `head`.
* While `temp.next` exists:

  * If `temp.val == temp.next.val`

    * Skip the duplicate node by updating:

      ```python
      temp.next = temp.next.next
      ```
  * Otherwise, move `temp` forward.

---

3️⃣ **Return Head**

Return the modified linked list.

---

### 🔍 Example

#### Input

```
1 → 1 → 2 → 3 → 3
```

#### Output

```
1 → 2 → 3
```

---

### ⏱ Time & Space Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(1)  |

* We traverse the list only once.
* No extra memory is used (in-place modification).

---

### 📚 Key Concepts Used

* Singly Linked List
* Pointer Manipulation
* In-place Node Deletion
* Sorted List Property Utilization

---

### 🚀 Why This Works Efficiently

Because the list is sorted:

* Duplicates are adjacent.
* No need for extra data structures like sets or hash maps.
* A simple linear scan is enough.


---


## 4️⃣ Reorder Linked List

### 📌 Problem Statement

Given the head of a singly linked list, reorder the list in-place to follow this pattern:

```
L0 → L1 → L2 → ... → Ln-1 → Ln
```

Reorder it to:

```
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
```

⚠️ You must **modify the list in-place** and not return a new list.

---

### 🧠 Approach Overview

This problem can be solved efficiently in **three major steps**:

1️⃣ **Find the Middle of the List**
2️⃣ **Reverse the Second Half**
3️⃣ **Merge the Two Halves Alternately**

This ensures an optimal time complexity of **O(n)** and space complexity of **O(1)**.

---

### 🔹 Step 1: Find the Middle (Slow & Fast Pointers)

* `slow` moves one step at a time.
* `fast` moves two steps at a time.
* When `fast` reaches the end, `slow` will be at the middle.

Then split the list into two halves.

---

### 🔹 Step 2: Reverse the Second Half

Reverse the second half of the list using standard linked list reversal logic.

Example:

```
Original second half: 4 → 5 → 6
Reversed:             6 → 5 → 4
```

---

### 🔹 Step 3: Merge Alternately

Merge nodes from:

* First half
* Reversed second half

By alternating between them:

```
1 → 2 → 3
6 → 5 → 4

Result:
1 → 6 → 2 → 5 → 3 → 4
```

---

### 🔍 Example

#### Input

```
1 → 2 → 3 → 4 → 5
```

#### Output

```
1 → 5 → 2 → 4 → 3
```

---

### ⏱ Time & Space Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(1)  |

* One pass to find middle
* One pass to reverse
* One pass to merge
* No extra data structures used

---

### 📚 Key Concepts Used

* Fast & Slow Pointer Technique
* Linked List Reversal
* In-place Modification
* Two-Pointer Merging
* Pointer Manipulation

---

### 🚀 Why This Approach is Optimal

* Avoids using extra space (like arrays or stacks)
* Uses only pointer manipulation
* Runs in linear time
* Commonly asked in interviews


---


## 5️⃣ Merge K Sorted Linked Lists (Min-Heap Approach)

### 📌 Problem Statement

Given an array of `k` sorted singly linked lists, merge them into one sorted linked list and return its head.

* Each linked list is sorted in ascending order.
* The final merged list must also be sorted.

---

### 🧠 Approach — Min Heap (Priority Queue)

Merging two lists can be done using the two-pointer technique.
However, when merging **K lists**, a better and more efficient approach is to use a **Min Heap (Priority Queue)**.

#### 🔹 Why Use a Heap?

* At any moment, we only need the **smallest current node** among all K lists.
* A Min Heap allows us to retrieve the smallest element in **O(log k)** time.
* This keeps the overall time complexity optimal.

---

### 🔹 Algorithm Steps

#### 1️⃣ Initialize Heap

* Traverse all input lists.
* Push the first node of each non-empty list into the heap.
* Store elements as a tuple:

```python
(val, index, node)
```

* `val` → for sorting
* `index` → to avoid comparison issues if values are equal
* `node` → actual linked list node

---

#### 2️⃣ Build Result List

* Create a `dummy` node to simplify pointer handling.
* Maintain a `current` pointer for building the merged list.

---

#### 3️⃣ Process Heap

While the heap is not empty:

1. Pop the smallest node.
2. Attach it to the result list.
3. If the popped node has a `next`, push it into the heap.

---

### 🔍 Example

#### Input

```text
[
  1 → 4 → 5,
  1 → 3 → 4,
  2 → 6
]
```

#### Output

```text
1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

---

### ⏱ Time & Space Complexity

| Complexity | Value      |
| ---------- | ---------- |
| Time       | O(N log k) |
| Space      | O(k)       |

* `N` = total number of nodes across all lists
* `k` = number of linked lists

Each node is pushed and popped from the heap once → `log k` cost each time.

---

### 📚 Key Concepts Used

* Min Heap (Priority Queue)
* Linked List Manipulation
* Dummy Node Technique
* Efficient Multi-way Merge
* Greedy Selection Strategy

---

### 🚀 Why This Approach is Optimal

* Much faster than merging lists one by one.
* Scales efficiently when `k` is large.
* Commonly used in:

  * External sorting
  * Merge operations in databases
  * Distributed data processing

---
