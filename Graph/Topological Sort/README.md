# Topological Sort
Topological Sort is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge (u \rightarrow v), node (u) appears before node (v) in the ordering. It is widely used in problems involving dependencies, such as task scheduling, course prerequisites, and build systems. Topological sorting can be performed using either **DFS (with recursion stack)** or **BFS (Kahn’s Algorithm using indegree)**, and it inherently helps detect cycles—since a valid ordering exists only if the graph is acyclic.


## 1️⃣ Course Schedule – Can Finish All Courses

### 📌 Problem Statement

You are given:

* `numCourses` → total number of courses
* `prerequisites` → list of pairs `[a, b]`

  * To take course `a`, you must first complete course `b`

👉 Determine whether it is possible to **finish all courses**

---

### 🚀 Approach: BFS (Topological Sort – Kahn’s Algorithm)

#### 🔹 Key Idea

* Represent courses as a **directed graph**
* Use **Topological Sorting** to detect cycles

👉 If a cycle exists → impossible to complete all courses

---

### 🧠 Algorithm

1. Build graph:

   * Edge: `b → a` (b must be done before a)

2. Compute `indegree[]`:

   * Number of prerequisites for each course

3. Initialize queue:

   * Add all nodes with `indegree = 0`

4. Perform BFS:

   * Remove node from queue
   * Reduce indegree of neighbors
   * Add neighbors with `indegree = 0`

5. Count processed nodes

6. If `count == numCourses`:

   * No cycle → return `True`
     Else:
   * Cycle exists → return `False`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(V + E)   |
| Space Complexity | O(V + E)   |

👉 `V` = courses, `E` = prerequisites

---

### 📎 Example

```text id="example"
Input:
numCourses = 2
prerequisites = [[1,0]]

Output: True

Explanation:
Take course 0 → then 1 ✔️
```

---

### 🔍 Dry Run

```text id="dryrun"
Initial:
indegree = [0,1]

Queue = [0]

Process 0:
→ reduce indegree of 1 → becomes 0  
→ add 1 to queue  

Process 1:
All courses processed ✔️
```

---

### ❌ Cycle Example

```text id="cycle"
Input:
numCourses = 2
prerequisites = [[1,0],[0,1]]

Output: False

Explanation:
Cycle exists → cannot complete courses ❌
```

---

### ✅ Key Points

* Uses **BFS Topological Sort**
* Detects cycles using indegree
* Efficient for dependency resolution
* Common pattern for scheduling problems

---

### ⚠️ Edge Cases

* No prerequisites → all courses possible
* Single course
* Fully cyclic graph
* Disconnected components

---

### 🏁 Conclusion

This problem is a classic application of **Topological Sorting using Kahn’s Algorithm**, where detecting cycles determines if all tasks (courses) can be completed efficiently in **O(V + E)** time.


---


## 2️⃣ Course Schedule II – Find Course Order

### 📌 Problem Statement

You are given:

* `numCourses` → total number of courses
* `prerequisites` → list of pairs `[a, b]`

  * To take course `a`, you must first complete course `b`

👉 Return a **valid order** to complete all courses
👉 If impossible (cycle exists) → return an empty list `[]`

---

### 🚀 Approach: BFS (Topological Sort – Kahn’s Algorithm)

#### 🔹 Key Idea

* Represent courses as a **directed graph**
* Use **Topological Sorting** to find a valid order

👉 If a cycle exists → no valid ordering

---

### 🧠 Algorithm

1. Build graph:

   * Edge: `b → a`

2. Compute `indegree[]`:

   * Number of prerequisites for each course

3. Initialize queue:

   * Add all nodes with `indegree = 0`

4. Perform BFS:

   * Pop node → add to result
   * Reduce indegree of neighbors
   * Add neighbors with `indegree = 0`

5. Check:

   * If result size == `numCourses` → valid order
   * Else → return `[]`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(V + E)   |
| Space Complexity | O(V + E)   |

👉 `V` = courses, `E` = prerequisites

---

### 📎 Example

```text id="example"
Input:
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

Output:
[0,1,2,3]  (or [0,2,1,3])
```

---

### 🔍 Dry Run

```text id="dryrun"
Initial:
indegree = [0,1,1,2]

Queue = [0]

Process 0:
→ reduce indegree of 1 and 2 → both become 0  

Queue = [1,2]

Process 1:
→ reduce indegree of 3 → becomes 1  

Process 2:
→ reduce indegree of 3 → becomes 0  

Queue = [3]

Final Order = [0,1,2,3] ✔️
```

---

### ❌ Cycle Case

```text id="cycle"
Input:
numCourses = 2
prerequisites = [[1,0],[0,1]]

Output: []

Explanation:
Cycle exists → no valid ordering ❌
```

---

### ✅ Key Points

* Uses **BFS Topological Sort**
* Builds valid ordering of tasks
* Detects cycles automatically
* Multiple valid answers possible

---

### ⚠️ Edge Cases

* No prerequisites → any order works
* Single course
* Fully cyclic graph
* Disconnected graph

---

### 🏁 Conclusion

This problem extends topological sorting to not only check feasibility but also construct a valid execution order, making it essential for dependency resolution problems in **O(V + E)** time.

---