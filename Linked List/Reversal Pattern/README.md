# 🔁 Reversal Pattern

The **Reversal Pattern** is a fundamental linked list technique where we reverse the direction of node pointers using three pointers: `prev`, `current`, and `next`. Instead of creating a new list, we modify the existing links in-place by storing the next node temporarily, reversing the current node’s pointer to the previous node, and then advancing all pointers forward. This pattern is commonly used in problems like full list reversal, reversing a sublist, checking for palindrome, and reversing in k-groups, and it works efficiently in **O(N) time and O(1) space**.


## 1️⃣ Reverse Linked List (Iterative Approach)

### 🧩 Problem Statement

Given the head of a **singly linked list**, reverse the list and return the new head.

You must reverse the links between nodes so that the last node becomes the first, and all pointers are flipped.

---

### 💡 Approach: Iterative (Three Pointers)

We use **three pointers** to reverse the linked list:

* `prev` → Keeps track of the previous node (initially `None`)
* `cur` → Points to the current node (starts at `head`)
* `next` → Temporarily stores the next node to prevent losing the list

#### 🔄 Algorithm Steps

1. Initialize:

   * `prev = None`
   * `cur = head`
2. Traverse the list while `cur` is not `None`
3. Store the next node → `next = cur.next`
4. Reverse the link → `cur.next = prev`
5. Move `prev` one step forward → `prev = cur`
6. Move `cur` one step forward → `cur = next`
7. When loop ends, `prev` becomes the new head

---

### 🖼 Example

#### Input:

```
1 → 2 → 3 → 4 → 5 → None
```

#### Output:

```
5 → 4 → 3 → 2 → 1 → None
```

---

### ⏱️ Complexity Analysis

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(1)  |

* **Time Complexity:** We traverse the list once → `O(N)`
* **Space Complexity:** No extra space used → `O(1)`

---

### 🚀 Key Points

* In-place reversal (no extra data structures)
* Uses constant memory
* Most optimal solution for reversing a linked list
* Common interview question (very important!)


---


## 2️⃣ Reverse Linked List II (Reverse Between Positions)

### 🧩 Problem Statement

Given the head of a **singly linked list** and two integers `left` and `right`, reverse the nodes of the list from position `left` to position `right`, and return the modified list.

* Positions are **1-indexed**
* Reversal must be done **in-place**

---

### 💡 Approach: Head Insertion Technique

Instead of reversing the entire list, we reverse only the sublist between `left` and `right`.

#### 🛠 Key Idea

1. Use a **dummy node** to handle edge cases (like reversing from position 1).
2. Move a pointer `prev` to the node **just before** position `left`.
3. Let `cur` point to the first node of the sublist.
4. Perform in-place reversal using the **head insertion method**:

   * Remove the next node
   * Insert it right after `prev`
   * Repeat until the sublist is reversed

---

### 🔍 How It Works (Step-by-Step)

Example:

#### Input:

```
1 → 2 → 3 → 4 → 5
left = 2, right = 4
```

#### Steps:

* Sublist to reverse → `2 → 3 → 4`
* Perform head insertion repeatedly

#### Output:

```
1 → 4 → 3 → 2 → 5
```

---

### 🎯 Why Use a Dummy Node?

* Handles edge case when `left = 1`
* Prevents losing the head reference
* Simplifies pointer manipulation

---

### ⏱️ Complexity Analysis

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(1)  |

* **Time:** Single traversal → `O(N)`
* **Space:** In-place reversal → `O(1)`

---

### 🚀 Key Concepts Used

* Dummy node technique
* Pointer manipulation
* In-place reversal
* Head insertion method

---

### 🏁 Summary

✔ Efficient single-pass solution
✔ No extra memory used
✔ Handles edge cases cleanly
✔ Very common coding interview problemV


---


## 3️⃣ Palindrome Linked List

### 🧩 Problem Statement

Given the head of a **singly linked list**, determine whether the list is a **palindrome**.

A linked list is a palindrome if it reads the same forward and backward.

---

### 💡 Approach: Fast & Slow Pointers + Reverse Second Half

To solve this efficiently in **O(N) time and O(1) space**, we:

1. Find the **middle** of the linked list using the **fast and slow pointer technique**.
2. Reverse the **second half** of the list.
3. Compare the first half and the reversed second half node by node.
4. If all values match → it’s a palindrome.

---

### 🔍 Step-by-Step Example

#### Input:

```
1 → 2 → 2 → 1
```

#### Step 1: Find Middle

Slow pointer stops at the second `2`.

#### Step 2: Reverse Second Half

Second half becomes:

```
1 → 2
```

#### Step 3: Compare Halves

| Left | Right |
| ---- | ----- |
| 1    | 1     |
| 2    | 2     |

All values match ✅ → Palindrome

---

### 📌 Why This Works

* The fast pointer moves twice as fast as slow.
* When fast reaches the end, slow is at the middle.
* Reversing half the list allows direct comparison without extra space.

---

### ⏱️ Complexity Analysis

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(1)  |

* **Time:** One pass to find middle + one pass to reverse + one pass to compare → `O(N)`
* **Space:** In-place reversal → `O(1)`

---

### 🚀 Key Concepts Used

* Fast & Slow pointer technique
* In-place linked list reversal
* Two-pointer comparison

---

### 🏁 Summary

✔ Efficient and optimal solution
✔ No extra data structures used
✔ Very common interview question
✔ Works for both even and odd length lists


---
