# Merge K Sorted

The **Merge K Sorted** pattern is used when we need to combine multiple sorted data structures—such as linked lists or arrays—into a single sorted result efficiently. Instead of repeatedly scanning all lists to find the smallest element, which would be inefficient, we use a **Min Heap (Priority Queue)** to always extract the smallest available element in **O(log k)** time, where `k` is the number of lists. By pushing the first element of each list into the heap and continuously inserting the next element from the list of the extracted node, we can build the final sorted structure efficiently. This technique is widely used in problems like **Merge K Sorted Lists**, **external sorting**, and **k-way merge algorithms**.


## 1️⃣ Merge K Sorted Linked Lists

### 📌 Problem Statement

Given an array of `k` linked lists, where each linked list is **sorted in ascending order**, merge all the linked lists into **one sorted linked list** and return its head.

---

### 🧠 Approach — Min Heap (Priority Queue)

To efficiently merge `k` sorted lists, we use a **Min Heap (Priority Queue)**.

#### 🔹 Key Idea

* Each list is already sorted.
* The smallest element among the current heads of all lists should appear first in the merged list.
* A **min heap** helps us quickly retrieve the smallest element among the heads.

#### Why store `(value, index, node)` in the heap?

Python cannot directly compare `ListNode` objects when values are equal.
To avoid comparison errors, we push:

```
(node.val, list_index, node)
```

Where:

* `node.val` → used for heap ordering
* `list_index` → ensures uniqueness
* `node` → the actual linked list node

---

### 🚀 Algorithm Steps

1️⃣ Initialize an empty **min heap**.

2️⃣ Insert the **head node of each non-empty list** into the heap.

3️⃣ Create a **dummy node** to build the result list.

4️⃣ While the heap is not empty:

* Extract the smallest node from the heap.
* Attach it to the merged list.
* If the extracted node has a `next` node, push it into the heap.

5️⃣ Return `dummy.next` as the head of the merged list.

---

### 🔍 Example

#### Input

```
lists = [
1 → 4 → 5,
1 → 3 → 4,
2 → 6
]
```

#### Step-by-Step Merge

Heap initially contains:

```
(1, list1), (1, list2), (2, list3)
```

Merged order becomes:

```
1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

#### Output

```
1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

---

### ⏱ Time & Space Complexity

| Complexity | Value      |
| ---------- | ---------- |
| Time       | O(N log K) |
| Space      | O(K)       |

Where:

* `N` = total number of nodes across all lists
* `K` = number of linked lists

Each heap operation costs **O(log K)**.

---

### 🎯 Key Concepts Used

* Heap (Priority Queue)
* Linked List Manipulation
* Dummy Node Technique
* K-Way Merge Pattern

---

### 🔥 Why This Approach is Efficient

Instead of repeatedly scanning all lists to find the smallest element (**O(K)** each time), the heap allows us to find the smallest element in **O(log K)** time.

This significantly improves performance for large values of `K`.


---