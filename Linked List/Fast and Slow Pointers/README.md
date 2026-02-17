# 🚀 Fast and Slow Pointers (Two-Pointer Technique)
The Fast and Slow Pointer technique, also known as Floyd’s Algorithm or the Tortoise and Hare approach, is a powerful pattern used mainly in linked list problems where two pointers traverse the structure at different speeds—one moving one step at a time (slow) and the other moving two steps at a time (fast). This difference in speed helps efficiently solve problems such as finding the middle of a linked list, detecting cycles, locating the start of a cycle, and removing the nth node from the end, all in linear time and constant space without modifying the data structure. 


## 1️⃣ Middle of the Linked List

### 🧩 Problem Statement

Given the `head` of a **singly linked list**, return the **middle node** of the linked list.

* If there are **two middle nodes**, return the **second middle node**.
* You must solve it efficiently.

---

### 💡 Approach: Two-Pointer (Tortoise and Hare)

We use the **slow and fast pointer technique**:

* `slow` pointer moves **one step** at a time.
* `fast` pointer moves **two steps** at a time.

#### 🔁 Logic

* Initialize both `slow` and `fast` at `head`.
* Move:

  * `slow = slow.next`
  * `fast = fast.next.next`
* When `fast` reaches the end (`None`), `slow` will be at the **middle node**.

This works because `fast` moves twice as fast as `slow`.

---

### 🧠 Why It Works

* If the list has **odd** number of nodes → `slow` lands exactly in the middle.
* If the list has **even** number of nodes → `slow` lands on the **second middle node** (as required).

---

### ⏱️ Complexity Analysis

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(1)  |

* **Time:** We traverse the list once.
* **Space:** No extra data structures used.

---

### 📊 Example

#### Input:

```
1 → 2 → 3 → 4 → 5
```

#### Output:

```
3
```

---

#### Input:

```
1 → 2 → 3 → 4 → 5 → 6
```

#### Output:

```
4
```

---

### 🚀 Key Takeaway

The **Two-Pointer technique** is one of the most important patterns for linked list problems.
It helps solve problems efficiently in **one pass** with **constant space**.


---



## 2️⃣ Linked List Cycle Detection 

### 🧩 Problem Statement

Given the `head` of a **singly linked list**, determine if the linked list contains a **cycle**.

A cycle exists if a node in the list can be reached again by continuously following the `next` pointer.

Return:

* `True` → if there is a cycle
* `False` → if there is no cycle

---

### 💡 Approach: Floyd’s Cycle Detection (Tortoise and Hare)

This solution uses the **Two-Pointer Technique**:

* `slow` pointer moves **one step** at a time.
* `fast` pointer moves **two steps** at a time.

#### 🔁 Logic

1. Initialize both `slow` and `fast` at `head`.
2. Traverse the list:

   * `slow = slow.next`
   * `fast = fast.next.next`
3. If at any point `slow == fast`, a cycle exists.
4. If `fast` reaches `None`, there is no cycle.

---

### 🧠 Why It Works

* If there is a cycle, the fast pointer will eventually "lap" the slow pointer and meet it inside the cycle.
* If there is no cycle, the fast pointer will reach the end of the list.

This is an efficient way to detect cycles without modifying the list or using extra memory.

---

### ⏱️ Complexity Analysis

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(1)  |

* **Time:** In the worst case, we traverse the entire list once.
* **Space:** No extra data structures are used.

---

### 📊 Example

#### Example 1

Input:

```
3 → 2 → 0 → -4
     ↑       ↓
     ← ← ← ← ←
```

Output:

```
True
```

---

#### Example 2

Input:

```
1 → 2 → 3 → 4
```

Output:

```
False
```

---

### 🚀 Key Takeaway

Floyd’s Cycle Detection Algorithm is a powerful pattern for linked list problems.
It detects cycles efficiently using:

* ✅ One traversal
* ✅ Constant space
* ✅ No modifications to the list


---


## 3️⃣ Linked List Cycle II – Detect Start of Cycle

### 🧩 Problem Statement

Given the `head` of a **singly linked list**, return the **node where the cycle begins**.

* If there is **no cycle**, return `None`.
* You must solve it **without modifying the linked list**.
* Use **O(1) extra space**.

---

### 💡 Approach: Floyd’s Cycle Detection Algorithm (Tortoise and Hare)

This solution uses the classic **two-pointer technique** in two phases.

---

### 🔁 Phase 1: Detect If Cycle Exists

* Initialize:

  * `slow = head`
  * `fast = head`
* Move:

  * `slow = slow.next`
  * `fast = fast.next.next`
* If `slow == fast`, a cycle exists.
* If `fast` reaches `None`, there is no cycle.

---

### 🔄 Phase 2: Find the Start of the Cycle

Once `slow` and `fast` meet:

1. Create a new pointer `temp = head`
2. Move:

   * `temp = temp.next`
   * `slow = slow.next`
3. The node where `temp == slow` is the **start of the cycle**.

---

### 🧠 Why It Works

Let:

* `L` = distance from head to cycle start
* `C` = length of cycle

When `slow` and `fast` meet:

* The distance from head to cycle start equals the distance from meeting point to cycle start.

So moving one pointer from `head` and one from meeting point at the same speed guarantees they meet at the **cycle start node**.

---

### ⏱️ Complexity Analysis

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(1)  |

* **Time:** At most two passes of the linked list.
* **Space:** No extra data structures used.

---

### 📊 Example

#### Input:

```
3 → 2 → 0 → -4
     ↑       ↓
     ← ← ← ← ←
```

#### Output:

```
Node with value 2
```

---

### 🚀 Key Takeaway

Floyd’s Algorithm not only detects a cycle but also helps find the **exact starting node of the cycle** in:

* ✅ One traversal
* ✅ Constant space
* ✅ No list modification


---


## 4️⃣ Remove Nth Node From End of List

### 🧩 Problem Statement

Given the `head` of a **singly linked list**, remove the **nth node from the end** of the list and return its head.

* The solution must be done in **one pass**.
* Do not modify node values — adjust pointers only.

---

### 💡 Approach: Two-Pointer Technique (One Pass)

To solve this efficiently, we use:

* A **dummy node** to handle edge cases (like removing the head).
* Two pointers: `slow` and `fast`.

---

### 🔁 Algorithm Steps

1. Create a dummy node pointing to `head`.
2. Initialize both `slow` and `fast` at `dummy`.
3. Move `fast` forward by `n` steps.
4. Move both `slow` and `fast` together until `fast.next` becomes `None`.
5. Now `slow.next` is the node to delete.
6. Remove it by:

   ```
   slow.next = slow.next.next
   ```
7. Return `dummy.next`.

---

### 🧠 Why We Use a Dummy Node

The dummy node helps handle cases where:

* The head node itself needs to be removed.
* It avoids special conditional checks.

Example:

```
1 → 2 → 3 → 4 → 5
Remove n = 5
```

Without a dummy node, removing the head becomes tricky.

---

### ⏱️ Complexity Analysis

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(1)  |

* **Time:** Single traversal of the list.
* **Space:** No extra data structures used.

---

### 📊 Example

#### Input:

```
1 → 2 → 3 → 4 → 5
n = 2
```

#### Output:

```
1 → 2 → 3 → 5
```

---

#### Edge Case

#### Input:

```
1
n = 1
```

#### Output:

```
None
```

---

### 🚀 Key Takeaway

The **Two-Pointer pattern with a dummy node** is extremely powerful for:

* Removing nodes
* Handling edge cases
* Achieving one-pass solutions

---
