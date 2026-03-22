# Recursive Approach for Stack & Linked List

Recursion is a powerful technique for solving problems involving stacks and linked lists, as both naturally follow a **last-in-first-out (LIFO)** or **sequential node-based structure**. By leveraging the call stack, recursion allows us to break down operations like insertion, reversal, and merging into smaller subproblems, eliminating the need for explicit auxiliary data structures. In stacks, recursion helps temporarily hold elements during operations like inserting at the bottom or reversing, while in linked lists, it simplifies pointer manipulation by processing nodes one at a time and resolving links during backtracking. This results in clean, elegant solutions that closely mirror the underlying structure of these data types.


## 1️⃣ Insert Element at Bottom of Stack

### 📌 Problem Statement

Given a stack `st` and an element `x`, insert `x` at the **bottom of the stack** using recursion.

👉 You are **not allowed** to use any extra data structures.

---

### 🚀 Approach: Recursion

The idea is to use recursion to temporarily remove all elements from the stack until it becomes empty, insert the element at the bottom, and then **rebuild the stack** in the correct order.

---

### 🧠 Key Idea

* Pop all elements one by one
* Insert the new element when the stack becomes empty
* Push all previously removed elements back

---

### 🧩 Algorithm

1. Base case:

   * If stack is empty → insert `x` and return

2. Recursive case:

   * Pop the top element
   * Recursively call function to insert `x` at bottom
   * Push the popped element back

---

### 📊 Complexity Analysis

| Type             | Complexity               |
| ---------------- | ------------------------ |
| Time Complexity  | O(n)                     |
| Space Complexity | O(n) *(recursion stack)* |

---

### 📎 Example

```text id="example1"
Input:  st = [1, 2, 3], x = 0  
Output: [0, 1, 2, 3]
```

```text id="example2"
Input:  st = [5, 6], x = 4  
Output: [4, 5, 6]
```

---

### 🔍 Dry Run (Step-by-Step)

```text id="dryrun"
Stack: [1,2,3]

Pop → 3
Pop → 2
Pop → 1
Stack empty → insert 0

Push back:
1 → [0,1]
2 → [0,1,2]
3 → [0,1,2,3]
```

---

### ✅ Key Points

* Uses **recursion instead of extra space**
* Maintains original order of stack elements
* Demonstrates stack manipulation using function call stack
* Useful building block for other stack problems

---

### ⚠️ Edge Cases

* Empty stack → directly insert element
* Single element stack
* Large stack (may cause recursion depth issues)

---

### 🏁 Conclusion

This recursive approach efficiently inserts an element at the bottom of a stack without using any additional data structures. It leverages the **call stack** to temporarily hold elements, making it both elegant and intuitive.


---


## 2️⃣ Reverse a Linked List (Recursion)

### 📌 Problem Statement

Given the head of a singly linked list, reverse the list and return the new head.

```text
Input:  1 → 2 → 3 → 4 → 5 → NULL  
Output: 5 → 4 → 3 → 2 → 1 → NULL
```

---

### 🚀 Approach: Recursion

This approach uses recursion to reverse the linked list by:

* Reversing the rest of the list
* Fixing the current node at the end

---

### 🧠 Key Idea

* Recursively reverse the list starting from `head.next`
* Adjust pointers while backtracking:

  * Make `head.next.next = head`
  * Set `head.next = None` to avoid cycles

---

### 🧩 Algorithm

1. Base case:

   * If `head` is `None` or only one node → return `head`

2. Recursive step:

   * Reverse the rest of the list:

     * `new_head = reverseList(head.next)`

3. Adjust pointers:

   * `head.next.next = head`
   * `head.next = None`

4. Return new head

---

### 📊 Complexity Analysis

| Type             | Complexity               |
| ---------------- | ------------------------ |
| Time Complexity  | O(n)                     |
| Space Complexity | O(n) *(recursion stack)* |

---

### 📎 Example

```text
Input:  head = [1,2,3,4,5]  
Output: [5,4,3,2,1]
```

---

### 🔍 Dry Run (Brief)

```text
Call Stack:
reverse(1→2→3)

→ reverse(2→3)
→ reverse(3) → returns 3

Backtracking:
2.next.next = 2 → 3→2
1.next.next = 1 → 3→2→1
```

---

### 🔁 Iterative vs Recursive

| Approach  | Space | Style              |
| --------- | ----- | ------------------ |
| Iterative | O(1)  | More optimal       |
| Recursive | O(n)  | Cleaner, intuitive |

---

### ✅ Key Points

* Uses **recursion and backtracking**
* Reverses links instead of values
* Elegant but uses extra stack space
* Important for understanding pointer manipulation

---

### ⚠️ Edge Cases

* Empty list (`head = None`)
* Single node list
* Large list (recursion depth limit)

---

### 🏁 Conclusion

Recursive reversal of a linked list is a clean and intuitive approach that demonstrates the power of recursion and pointer manipulation, though iterative solutions are more space-efficient.


---


## 3️⃣ Merge Two Sorted Linked Lists (Recursion)

### 📌 Problem Statement

Given the heads of two **sorted linked lists** `list1` and `list2`, merge them into a single **sorted linked list** and return its head.

```text
Input:
list1: 1 → 2 → 4  
list2: 1 → 3 → 4  

Output:
1 → 1 → 2 → 3 → 4 → 4
```

---

### 🚀 Approach: Recursion

We recursively compare the nodes of both lists and build the merged list:

* Pick the smaller node
* Recursively merge the remaining lists
* Link the chosen node to the result

---

### 🧠 Key Idea

* At each step, choose the node with the **smaller value**
* Recursively merge the rest
* This naturally builds the sorted merged list

---

### 🧩 Algorithm

1. Base cases:

   * If `list1` is `None` → return `list2`
   * If `list2` is `None` → return `list1`

2. Compare values:

   * If `list1.val <= list2.val`:

     * Set `list1.next = merge(list1.next, list2)`
     * Return `list1`
   * Else:

     * Set `list2.next = merge(list1, list2.next)`
     * Return `list2`

---

### 📊 Complexity Analysis

| Type             | Complexity                   |
| ---------------- | ---------------------------- |
| Time Complexity  | O(n + m)                     |
| Space Complexity | O(n + m) *(recursion stack)* |

---

### 📎 Examples

```text
Input: list1 = [1,2,4], list2 = [1,3,4]  
Output: [1,1,2,3,4,4]
```

```text
Input: list1 = [], list2 = [0]  
Output: [0]
```

---

### 🔍 Dry Run (Brief)

```text
merge(1→2→4, 1→3→4)

→ pick 1 (list1)
→ merge(2→4, 1→3→4)

→ pick 1 (list2)
→ merge(2→4, 3→4)

→ pick 2 → pick 3 → pick 4 → pick 4
```

---

### 🔁 Iterative vs Recursive

| Approach  | Space  | Style              |
| --------- | ------ | ------------------ |
| Iterative | O(1)   | More optimal       |
| Recursive | O(n+m) | Cleaner, intuitive |

---

### ✅ Key Points

* Uses **recursion + comparison**
* Maintains sorted order automatically
* Elegant and concise solution
* Widely asked in coding interviews

---

### ⚠️ Edge Cases

* One or both lists are empty
* Lists of different lengths
* Duplicate values

---

### 🏁 Conclusion

This recursive approach provides a clean and intuitive way to merge two sorted linked lists by leveraging the natural structure of recursion, though iterative solutions are more space-efficient.


---
