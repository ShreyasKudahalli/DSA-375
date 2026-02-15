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

