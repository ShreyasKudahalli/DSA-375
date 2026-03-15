# Heap Implementation

Heap implementation focuses on building a **binary heap data structure** using an array to efficiently support operations such as **insertion, deletion, peek, and heap property maintenance**. A heap follows the **complete binary tree structure**, where elements are arranged so that either the **maximum element (Max Heap)** or **minimum element (Min Heap)** is always at the root. The heap property is preserved using two key operations: **heapify-up (shift up)** during insertion and **heapify-down (shift down)** during deletion or extraction. By representing the heap in an array and calculating parent and child indices using simple formulas, heap operations achieve efficient time complexities—typically **O(log n)** for insertion and deletion, and **O(1)** for accessing the top element—making heaps ideal for **priority queues, scheduling systems, and many algorithmic problems involving ordered data processing**.



## 1️⃣ Max Heap Implementation (From Scratch)

### 📌 Overview

A **Max Heap** is a special type of **binary heap** where the value of each parent node is **greater than or equal to its children**. This property ensures that the **largest element is always at the root** of the heap. Max heaps are commonly used in problems involving **priority queues, scheduling systems, Top-K problems, and heap sort**.

This implementation builds a **Max Heap from scratch using a Python list** and supports the following operations:

* **Insert (`push`)**
* **Remove Maximum (`pop`)**
* **Peek Maximum (`peek`)**
* **Get Heap Size (`size`)**

The heap maintains its structure using **heapify-up** and **heapify-down** operations.

---

### 🧠 Heap Structure

A heap is stored using an **array representation**.

For any node at index `i`:

| Relationship | Formula        |
| ------------ | -------------- |
| Parent       | `(i - 1) // 2` |
| Left Child   | `2*i + 1`      |
| Right Child  | `2*i + 2`      |

Example heap array:

```
        50
       /  \
     30    40
    / \ 
   10 20
```

Stored as:

```
[50, 30, 40, 10, 20]
```

---

### 🚀 Supported Operations

#### 1️⃣ Insert Element (`push`)

When inserting a new element:

1. Add it to the **end of the heap**
2. Perform **heapify-up**
3. Swap with its parent until the **max heap property** is restored.

##### Example

Insert `60`

```
Before:
[50, 30, 40]

After insertion:
[50, 30, 40, 60]

Heapify Up:
[60, 50, 40, 30]
```

##### Time Complexity

```
O(log n)
```

---

#### 2️⃣ Remove Maximum (`pop`)

Removing the maximum element involves:

1. Store the root value.
2. Replace root with the **last element**.
3. Remove the last element.
4. Perform **heapify-down** to restore heap order.

##### Example

```
Before:
[60, 50, 40, 30]

Remove 60

Replace root with last element:
[30, 50, 40]

Heapify Down:
[50, 30, 40]
```

##### Time Complexity

```
O(log n)
```

---

#### 3️⃣ Peek Maximum (`peek`)

Returns the maximum element without removing it.

Since the root contains the maximum value:

```
return heap[0]
```

##### Time Complexity

```
O(1)
```

---

#### 4️⃣ Heap Size (`size`)

Returns the total number of elements in the heap.

```
len(self.heap)
```

##### Time Complexity

```
O(1)
```

---

### ⏱ Time & Space Complexity

| Operation | Complexity |
| --------- | ---------- |
| Push      | O(log n)   |
| Pop       | O(log n)   |
| Peek      | O(1)       |
| Size      | O(1)       |
| Space     | O(n)       |

---

### 🔑 Key Concepts Used

* Binary Heap
* Heapify Up
* Heapify Down
* Priority Queue Implementation
* Array-based Tree Representation


---


## 2️⃣ Min Heap Implementation (From Scratch)

### 📌 Overview

A **Min Heap** is a type of **binary heap** where the value of every parent node is **less than or equal to its children**. This property ensures that the **smallest element is always located at the root** of the heap. Min heaps are widely used in algorithms involving **priority queues, shortest path algorithms, scheduling systems, and heap-based optimizations**.

This implementation builds a **Min Heap from scratch using a Python list** and supports the following core operations:

* **Insert (`push`)**
* **Remove Minimum (`pop`)**
* **Peek Minimum (`peek`)**
* **Get Heap Size (`size`)**

The heap structure is maintained using **heapify-up** and **heapify-down** operations after every insertion or deletion.

---

### 🧠 Heap Structure

A heap is stored using an **array representation of a complete binary tree**.

For any node at index `i`:

| Relationship | Formula        |
| ------------ | -------------- |
| Parent       | `(i - 1) // 2` |
| Left Child   | `2*i + 1`      |
| Right Child  | `2*i + 2`      |

Example Min Heap:

```
        5
       / \
      8   10
     / \
    15  20
```

Array representation:

```
[5, 8, 10, 15, 20]
```

The **smallest value is always at index `0`**.

---

### 🚀 Supported Operations

#### 1️⃣ Insert Element (`push`)

When inserting a new element:

1. Add the element to the **end of the heap**.
2. Perform **heapify-up**.
3. Swap the element with its parent until the **min heap property** is restored.

##### Example

Insert `3`

```
Before:
[5, 8, 10]

After insertion:
[5, 8, 10, 3]

Heapify Up:
[3, 5, 10, 8]
```

##### Time Complexity

```
O(log n)
```

---

#### 2️⃣ Remove Minimum (`pop`)

Removing the minimum element involves:

1. Store the root value.
2. Replace the root with the **last element**.
3. Remove the last element.
4. Perform **heapify-down** to restore heap order.

##### Example

```
Before:
[3, 5, 10, 8]

Remove 3

Replace root with last element:
[8, 5, 10]

Heapify Down:
[5, 8, 10]
```

##### Time Complexity

```
O(log n)
```

---

#### 3️⃣ Peek Minimum (`peek`)

Returns the smallest element without removing it.

Since the root always contains the minimum value:

```
return heap[0]
```

##### Time Complexity

```
O(1)
```

---

#### 4️⃣ Heap Size (`size`)

Returns the number of elements present in the heap.

```
len(self.heap)
```

##### Time Complexity

```
O(1)
```

---

### ⏱ Time & Space Complexity

| Operation | Complexity |
| --------- | ---------- |
| Push      | O(log n)   |
| Pop       | O(log n)   |
| Peek      | O(1)       |
| Size      | O(1)       |
| Space     | O(n)       |

---

### 🔑 Key Concepts Used

* Binary Heap
* Heapify Up
* Heapify Down
* Priority Queue Implementation
* Array-Based Tree Representation

---

### ⚠️ Important Insights

* A **Min Heap is a complete binary tree**, meaning all levels are filled except possibly the last.
* Using an **array representation avoids the need for explicit tree nodes**, making operations efficient.
* Heap operations maintain the **heap property after every update**.

---

### 🧩 Applications of Min Heap

Min heaps are widely used in:

* **Priority Queues**
* **Dijkstra’s Shortest Path Algorithm**
* **Prim’s Minimum Spanning Tree Algorithm**
* **K Smallest Elements Problems**
* **Merge K Sorted Lists**
* **Task Scheduling Systems**


---


## 3️⃣ Extract Maximum from Max Heap

### 📌 Overview

The **Extract Max** operation is one of the fundamental operations in a **Max Heap** data structure. In a Max Heap, the **largest element is always stored at the root** (index `0`). The `extractMax` function removes and returns this maximum element while ensuring that the heap structure and heap property are preserved.

To maintain the heap property after removal, the algorithm replaces the root with the **last element in the heap** and then performs a **shift-down (heapify-down)** operation to restore the correct ordering.

---

### 🧠 Heap Representation

The heap is stored using an **array representation of a binary tree**.

For any node at index `i`:

| Relationship | Formula        |
| ------------ | -------------- |
| Parent       | `(i - 1) // 2` |
| Left Child   | `2*i + 1`      |
| Right Child  | `2*i + 2`      |

Example Max Heap:

```
        50
       /  \
     30    40
    /  \
   10  20
```

Array representation:

```
[50, 30, 40, 10, 20]
```

The **maximum element is always at index `0`**.

---

### 🚀 Extract Max Operation

The `extractMax()` function performs the following steps:

#### 1️⃣ Check if Heap is Empty

If the heap size `s` is less than `0`, it means the heap is empty.

```
if s < 0:
    return -1
```

---

#### 2️⃣ Store Maximum Element

The root element `H[0]` contains the largest value.

```
result = H[0]
```

---

#### 3️⃣ Replace Root with Last Element

The last element in the heap replaces the root.

```
H[0] = H[s]
```

---

#### 4️⃣ Reduce Heap Size

The heap size is decreased by one.

```
s -= 1
```

---

#### 5️⃣ Restore Heap Property

Since replacing the root may break the heap property, we perform a **shiftDown operation** to push the element down until the heap property is restored.

```
shiftDown(0)
```

---

### 🔍 Example

#### Initial Heap

```
H = [50, 30, 40, 10, 20]
s = 4
```

#### Step 1 — Extract Max

```
max = 50
```

#### Step 2 — Replace Root with Last Element

```
[20, 30, 40, 10]
```

#### Step 3 — Shift Down

```
[40, 30, 20, 10]
```

#### Result

```
Extracted Value: 50
Updated Heap: [40, 30, 20, 10]
```

---

### ⏱ Time & Space Complexity

| Operation   | Complexity |
| ----------- | ---------- |
| Extract Max | O(log n)   |
| Space       | O(1)       |

Explanation:

* The **shiftDown operation** moves the element at most the **height of the heap**.
* A binary heap has height **log n**, so the operation runs in **O(log n)** time.

---

### 🔑 Key Concepts Used

* Max Heap Property
* Heapify Down (Shift Down)
* Array-based Heap Representation
* Priority Queue Behavior

---

### ⚠️ Important Insight

After removing the root element, simply deleting it would **break the complete binary tree structure**. Replacing the root with the last element keeps the structure intact, and **shiftDown restores the heap order efficiently**.

---

### 🧩 Applications of Extract Max

The `extractMax` operation is widely used in:

* **Priority Queues**
* **Heap Sort**
* **Task Scheduling Systems**
* **Top K Elements Problems**
* **Greedy Algorithms**


---
