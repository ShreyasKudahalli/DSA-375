# Linked List Basic Operations
Linked List Basic Operations involve fundamental manipulations such as insertion (at beginning, end, or position), deletion, traversal, and searching within a dynamically connected sequence of nodes. Unlike arrays, linked lists use pointers to connect elements, allowing efficient memory utilization and flexible data management, making them essential for understanding dynamic data structures and building more advanced structures like stacks, queues, and graphs.

## 1️⃣ Search Key in Singly Linked List

### 📌 Problem Statement

Given the head of a **singly linked list** and a value `key`,  
determine whether the key exists in the linked list.

Return:
- `True` → if key is found  
- `False` → if key is not present  

---

### 🧠 Approach

Since a singly linked list does not allow random access,  
we must **traverse the list node by node**.

#### 🔹 Steps:
1. Start from the `head`
2. Compare each node’s `data` with `key`
3. If match found → return `True`
4. If end of list reached → return `False`

---

### 📊 Example
#### Input 1
    Linked List:1 → 2 → 3 → 4 → 5
    Key: 3
#### Output 1
    True

#### Input 2
    Linked List:1 → 2 → 3 → 4 → 5
    Key: 8
#### Output 2
    False

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(1)  |

- In the worst case, we traverse all nodes → O(n)
- No extra space used → O(1)

---

### 🎯 Key Points

- Linear traversal is required
- Stops early if key is found
- Simple and efficient implementation
- Works for empty list as well


---


## 2️⃣ Delete Node at Given Position in Singly Linked List

### 📌 Problem Statement

Given the head of a **singly linked list** and a position `x` (1-based index),  
delete the node at position `x` and return the updated head of the linked list.

If:
- The list is empty → return `None`
- `x = 1` → delete the head node

---

### 🧠 Approach

We handle the problem in three steps:

#### 🔹 Case 1: Empty List
If `head is None`, return `None`.

#### 🔹 Case 2: Delete First Node
If `x == 1`, return `head.next`.

#### 🔹 Case 3: Delete Node at Position x
- Traverse the list until reaching node at position `x-1`
- Update pointer:
  
temp.next = temp.next.next

python
Copy code

This skips the node at position `x`.

---
### 📊 Example
#### Input
    Linked List:1 → 2 → 3 → 4 → 5
    Position: 3
#### Output
    1 → 2 → 4 → 5

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(1)  |

- We traverse the list at most once → O(n)
- No extra space used → O(1)

---

### 🎯 Key Points

- Uses 1-based indexing
- Handles deletion of head separately
- Avoids breaking the list structure
- Efficient single traversal solution


---


## 3️⃣ Insert Node at End of Singly Linked List

### 📌 Problem Statement

Given the head of a **singly linked list** and a value `x`,  
insert a new node with value `x` at the **end** of the list  
and return the updated head.

If:
- The list is empty → create a new node and return it as head.

---

### 🧠 Approach

Since a singly linked list does not maintain a tail pointer,  
we must traverse the list until we reach the last node.

#### 🔹 Steps

1. If `head` is `None`
   - Create a new node
   - Return it as the new head

2. Otherwise:
   - Traverse until `temp.next` is `None`
   - Attach the new node at the end:
     
     ```
     temp.next = Node(x)
     ```

3. Return the original `head`

---

### 📊 Example
#### Input
    Linked List:1 → 2 → 3
    Insert: 4
#### Output
    1 → 2 → 3 → 4

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(1)  |

- We traverse the list once → O(n)
- Only one new node is created → O(1) extra space

---

### 🎯 Key Points

- Handles empty list case
- Maintains original head
- Requires full traversal to reach end
- Efficient and clean implementation


Here is the **cleaned, properly formatted, and consistent version** of your README section:

---

## 4️⃣ Odd Even Linked List

Rearrange a singly linked list such that all **odd-indexed nodes** are grouped together followed by the **even-indexed nodes**.

> ⚠️ **Note:**
> Indexing is based on the **node position (1-based index)**, NOT the node values.

---

### 🧩 Problem Statement

Given the head of a singly linked list, group all nodes positioned at odd indices together followed by nodes positioned at even indices, and return the reordered list.

**Requirements:**

* The relative order inside the odd and even groups must remain the same.
* The solution must run in **O(N)** time complexity.
* The solution must use **O(1)** extra space.

---

### 💡 Approach

#### ✅ Key Idea

* Maintain two pointers:

  * `odd` → tracks odd-indexed nodes
  * `even` → tracks even-indexed nodes
* Store the starting node of the even list (`evenHead`) to connect later.
* Traverse the list and rearrange pointers.
* Finally, attach the even list after the odd list.

---

### 🔁 Step-by-Step Logic

1. Handle edge cases (empty list or single node).
2. Initialize:

   * `odd = head`
   * `even = head.next`
   * `evenHead = even`
3. While `even` and `even.next` exist:

   * Connect odd to next odd node.
   * Connect even to next even node.
4. Attach even list after odd list.
5. Return `head`.

---

### 🧪 Example

#### Input

```
1 → 2 → 3 → 4 → 5
```

#### Output

```
1 → 3 → 5 → 2 → 4
```

---

### ⏱️ Complexity Analysis

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(1)  |

* The list is traversed once.
* No extra data structures are used.

---

### 🎯 Why This Works

* The list is logically split into two sublists (odd & even).
* Nodes are rearranged using pointer manipulation.
* No new nodes are created.
* Constant extra space is maintained.

---

---

# 5️⃣ Design Linked List (Singly Linked List Implementation)

A complete implementation of a **Singly Linked List** supporting the following operations:

* `get(index)`
* `addAtHead(val)`
* `addAtTail(val)`
* `addAtIndex(index, val)`
* `deleteAtIndex(index)`

This implementation maintains:

* A `head` pointer
* A `size` counter for efficient boundary checks

---

## 🧱 Data Structure Design

### 🔹 Node Structure

Each node contains:

* `val` → Value of the node
* `next` → Pointer to the next node

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## 🏗️ Linked List Class

```python
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
```

* `head` → Points to the first node
* `size` → Tracks the number of elements in the list

---

## 📌 Operations

---

### 1️⃣ get(index)

Returns the value of the node at the given index.

#### ✔️ Rules

* If the index is invalid → return `-1`
* Traverse from the head to the desired index

#### ⏱ Complexity

* **Time:** O(N)
* **Space:** O(1)

---

### 2️⃣ addAtHead(val)

Adds a node at the beginning.

#### ✔️ Steps

* Create a new node
* Point the new node to the current head
* Update the head
* Increment size

#### ⏱ Complexity

* **Time:** O(1)
* **Space:** O(1)

---

### 3️⃣ addAtTail(val)

Adds a node at the end.

#### ✔️ Steps

* If the list is empty → set head to new node
* Otherwise, traverse to the last node
* Attach the new node
* Increment size

#### ⏱ Complexity

* **Time:** O(N)
* **Space:** O(1)

---

### 4️⃣ addAtIndex(index, val)

Adds a node before the node at the given index.

#### ✔️ Rules

* If `index > size` → do nothing
* If `index == 0` → add at head
* Otherwise:

  * Traverse to `(index - 1)`
  * Insert node
  * Increment size

#### ⏱ Complexity

* **Time:** O(N)
* **Space:** O(1)

---

### 5️⃣ deleteAtIndex(index)

Deletes the node at the given index.

#### ✔️ Rules

* If index is invalid → do nothing
* If deleting head → move head to `head.next`
* Otherwise:

  * Traverse to `(index - 1)`
  * Skip the target node
  * Decrement size

#### ⏱ Complexity

* **Time:** O(N)
* **Space:** O(1)

---

## 🧪 Example Usage

```python
obj = MyLinkedList()

obj.addAtHead(1)        # 1
obj.addAtTail(3)        # 1 → 3
obj.addAtIndex(1, 2)    # 1 → 2 → 3

print(obj.get(1))       # 2

obj.deleteAtIndex(1)    # 1 → 3
print(obj.get(1))       # 3
```

---

## 📊 Complexity Summary

| Operation     | Time Complexity | Space Complexity |
| ------------- | --------------- | ---------------- |
| get           | O(N)            | O(1)             |
| addAtHead     | O(1)            | O(1)             |
| addAtTail     | O(N)            | O(1)             |
| addAtIndex    | O(N)            | O(1)             |
| deleteAtIndex | O(N)            | O(1)             |

---

## 🎯 Key Concepts Covered

* Pointer manipulation
* Linked list traversal
* Edge case handling
* Maintaining list size
* Constant space design

---

## 🚀 Why Maintain `size`?

Maintaining a `size` variable:

* Allows index validation in O(1)
* Avoids unnecessary boundary traversal
* Improves readability and structure of the implementation

---