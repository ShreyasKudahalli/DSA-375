# Binary Search Tree (BST) Operations

**Binary Search Tree (BST) Operations** form the foundation of efficient data organization and retrieval in tree-based structures, leveraging the inherent ordering property where left subtree values are smaller and right subtree values are larger than the root. Core operations such as search, insertion, deletion, and validation can be performed in optimal time by recursively or iteratively navigating the tree based on comparisons. BSTs are widely used in applications requiring sorted data, fast lookups, and dynamic updates, making them a crucial concept in data structures and algorithm design.


## 1️⃣ Search in a Binary Search Tree (Iterative)

### 📌 Problem Statement

Given the root of a **Binary Search Tree (BST)** and an integer `val`, return the node where the node’s value equals `val`.

👉 If such a node does not exist, return `None`.

---

### 🚀 Approach: Iterative Traversal (BST Property)

#### 🔹 Key Idea

A **Binary Search Tree** follows the property:

* Left subtree → values **less than** root
* Right subtree → values **greater than** root

👉 Use this property to **eliminate half of the tree at each step**.

---

### 🧠 Algorithm

1. Start from the root
2. While current node exists:

   * If `root.val == val` → return node
   * If `val < root.val` → move to left subtree
   * If `val > root.val` → move to right subtree
3. If not found → return `None`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(h)       |
| Space Complexity | O(1)       |

👉 `h` = height of the tree

* Best case (balanced BST): **O(log n)**
* Worst case (skewed tree): **O(n)**

---

### 📎 Example

```text id="example"
Input:
       4
      / \
     2   7
    / \
   1   3

val = 2

Output:
Subtree rooted at node 2
```

---

### 🔍 Dry Run

```text id="dryrun"
Start at root = 4

2 < 4 → go left  
Now at 2 → match found ✔️

Return node 2
```

---

### ✅ Key Points

* Leverages **BST property for efficient search**
* Iterative approach avoids recursion overhead
* Works in **O(log n)** for balanced trees
* Very similar to **binary search logic**

---

### ⚠️ Edge Cases

* Empty tree (`root = None`)
* Value not present in tree
* Single node tree
* Skewed BST

---

### 🏁 Conclusion

This iterative approach efficiently searches for a value in a BST by narrowing down the search space at each step, achieving optimal performance with minimal space usage.


---


## 2️⃣ Insert into a Binary Search Tree (Iterative)

### 📌 Problem Statement

Given the root of a **Binary Search Tree (BST)** and an integer `val`, insert a new node with value `val` into the BST.

👉 Return the root of the BST after insertion.
👉 The BST property must be maintained.

---

### 🚀 Approach: Iterative Traversal (BST Property)

#### 🔹 Key Idea

A **Binary Search Tree** follows:

* Left subtree → values **less than** root
* Right subtree → values **greater than or equal to** root

👉 Traverse the tree and find the correct position where the new node should be inserted.

---

### 🧠 Algorithm

1. **Base Case**:

   * If `root` is `None`, create and return a new node

2. **Traverse the Tree**:

   * Start from root
   * While traversing:

     * If `val < current.val`:

       * Move to left subtree
       * If left is `None` → insert here
     * Else:

       * Move to right subtree
       * If right is `None` → insert here

3. Return the original root

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(h)       |
| Space Complexity | O(1)       |

👉 `h` = height of the tree

* Best case (balanced BST): **O(log n)**
* Worst case (skewed BST): **O(n)**

---

### 📎 Example

```text id="example"
Input:
       4
      / \
     2   7
    / \
   1   3

val = 5

Output:
       4
      / \
     2   7
    / \  /
   1   3 5
```

---

### 🔍 Dry Run

```text id="dryrun"
Start at root = 4

5 > 4 → go right  
Now at 7  

5 < 7 → go left  
Left is empty → insert 5 here ✔️
```

---

### ✅ Key Points

* Uses **BST property for efficient insertion**
* Iterative approach avoids recursion overhead
* Maintains tree structure correctly
* Similar logic to **binary search traversal**

---

### ⚠️ Edge Cases

* Empty tree (`root = None`)
* Inserting duplicate values
* Skewed BST
* Large input tree

---

### 🏁 Conclusion

This iterative approach efficiently inserts a node into a BST by traversing down the tree and placing the node at the correct position, achieving optimal **O(h)** time complexity with constant space.

---


## 3️⃣ Validate Binary Search Tree (DFS + Range Check)

### 📌 Problem Statement

Given the root of a binary tree, determine if it is a **valid Binary Search Tree (BST)**.

👉 A BST must satisfy:

* Left subtree contains values **strictly less than** the node
* Right subtree contains values **strictly greater than** the node
* Both left and right subtrees must also be valid BSTs

---

### 🚀 Approach: DFS with Value Range Constraints

#### 🔹 Key Idea

Instead of checking only immediate children, maintain a **valid range (`low`, `high`)** for each node.

👉 Each node must satisfy:

```
low < node.val < high
```

* Left subtree → upper bound becomes current node value
* Right subtree → lower bound becomes current node value

---

### 🧠 Algorithm

1. Define a recursive function:

   ```
   valid(node, low, high)
   ```

2. **Base Case**:

   * If node is `None` → return `True`

3. **Check Validity**:

   * If `node.val` is not in `(low, high)` → return `False`

4. **Recurse**:

   * Left → `valid(node.left, low, node.val)`
   * Right → `valid(node.right, node.val, high)`

5. Start with:

   ```
   (-∞, +∞)
   ```

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(h)       |

👉 `n` = number of nodes
👉 `h` = height of the tree (recursion stack)

---

### 📎 Example

```text id="example"
Input:
       5
      / \
     1   7
        / \
       6   8

Output: True
```

```text id="example2"
Input:
       5
      / \
     1   4
        / \
       3   6

Output: False
```

---

### 🔍 Dry Run (Invalid Case)

```text id="dryrun"
Node = 4

Expected range: (5, +∞)  
But 4 < 5 ❌

Hence not a valid BST
```

---

### ✅ Key Points

* Uses **DFS with range constraints**
* Ensures **global BST validity**, not just local checks
* Avoids common mistakes with subtree violations
* Elegant and optimal solution

---

### ⚠️ Edge Cases

* Empty tree → valid BST
* Single node tree
* Duplicate values (invalid in strict BST)
* Skewed tree

---

### 🏁 Conclusion

This DFS-based approach ensures correctness by maintaining valid value ranges for each node, making it a robust and optimal solution with **O(n)** time complexity.


---


## 4️⃣ Convert Sorted Array to Binary Search Tree (Balanced BST)


### 📌 Problem Statement

Given a **sorted (ascending order) array**, convert it into a **height-balanced Binary Search Tree (BST)**.

👉 A height-balanced BST is defined as a tree where the depth of the two subtrees of every node never differs by more than one.

---

### 🚀 Approach: Divide & Conquer (DFS)

#### 🔹 Key Idea

* The **middle element** of the array becomes the root
* Left half → left subtree
* Right half → right subtree

👉 This ensures the tree remains **balanced**.

---

### 🧠 Algorithm

1. Define a recursive function:

   ```
   build(left, right)
   ```

2. **Base Case**:

   * If `left > right` → return `None`

3. **Choose Middle Element**:

   * `mid = (left + right) // 2`
   * Create root node with `nums[mid]`

4. **Build Subtrees**:

   * Left subtree → `build(left, mid - 1)`
   * Right subtree → `build(mid + 1, right)`

5. Return root

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(log n)   |

👉 `n` = number of elements
👉 Recursion depth = height of balanced BST

---

### 📎 Example

```text id="example"
Input:
nums = [-10, -3, 0, 5, 9]

Output (One Possible BST):
        0
       / \
     -3   9
     /   /
   -10  5
```

---

### 🔍 Dry Run

```text id="dryrun"
nums = [-10, -3, 0, 5, 9]

mid = 2 → root = 0

Left:
[-10, -3] → root = -3 → left = -10

Right:
[5, 9] → root = 9 → left = 5
```

---

### ✅ Key Points

* Uses **Divide & Conquer**
* Always picks **middle element** → ensures balance
* Result is a **height-balanced BST**
* Efficient construction in linear time

---

### ⚠️ Edge Cases

* Empty array → return `None`
* Single element → single node tree
* Even number of elements → multiple valid BSTs

---

### 🏁 Conclusion

This approach constructs a balanced BST efficiently by recursively selecting the middle element, ensuring optimal height and performance with **O(n)** time complexity.


---