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


## 2️⃣ K Pairs with Smallest Sums

### 📌 Problem Statement

You are given two **sorted arrays** `nums1` and `nums2`, and an integer `k`.

A pair `(u, v)` consists of:

* `u` from `nums1`
* `v` from `nums2`

Return the **k pairs with the smallest sums**.

Each pair should be returned in the form:

```
[u, v]
```

---

### 🧠 Approach — Min Heap (Priority Queue)

Since both arrays are **sorted**, we can efficiently find the smallest pair sums using a **Min Heap**.

#### 🔹 Key Idea

* The smallest possible pair will always involve **smaller elements from the arrays**.
* Start by pairing the **first element of `nums2`** with the **first `k` elements of `nums1`**.
* Store these pairs in a **min heap based on their sum**.

Each heap element stores:

```
(sum, i, j)
```

Where:

* `sum = nums1[i] + nums2[j]`
* `i` → index in `nums1`
* `j` → index in `nums2`

When we remove the smallest pair from the heap, we then push the **next pair from the same row** (`j + 1`).

This ensures we always explore the **next possible smallest pair**.

---

### 🚀 Algorithm Steps

1️⃣ If either array is empty, return an empty list.

2️⃣ Initialize a **min heap**.

3️⃣ Push the first `k` pairs:

```
(nums1[i] + nums2[0], i, 0)
```

for `i` in `0 → min(k, len(nums1))`.

4️⃣ While the heap is not empty and we haven't found `k` pairs:

* Pop the smallest pair.
* Add `[nums1[i], nums2[j]]` to the result.
* Push the next pair `(i, j+1)` into the heap if it exists.

5️⃣ Return the result list.

---

### 🔍 Example

#### Input

```
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
```

#### Pair Sums

```
(1,2) = 3
(1,4) = 5
(1,6) = 7
(7,2) = 9
(7,4) = 11
(11,2) = 13
```

#### Output

```
[[1,2], [1,4], [1,6]]
```

These are the **3 pairs with the smallest sums**.

---

### ⏱ Time & Space Complexity

| Complexity | Value      |
| ---------- | ---------- |
| Time       | O(k log k) |
| Space      | O(k)       |

Where:

* `k` = number of pairs required.

The heap never grows larger than **k elements**.

---

### 🎯 Key Concepts Used

* Min Heap (Priority Queue)
* K-Way Merge Pattern
* Efficient Pair Generation
* Greedy Expansion Strategy

---

### 🔥 Why This Approach is Efficient

The brute force approach would generate **all possible pairs**:

```
O(n * m)
```

Then sort them.

Instead, using a **min heap**, we only explore the **next smallest candidates**, reducing the complexity significantly.

---
