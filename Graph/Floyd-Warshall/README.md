# Floyd-Warshall

Floyd-Warshall is a dynamic programming algorithm used to compute the **shortest paths between all pairs of vertices** in a weighted graph. It works by iteratively considering each node as an intermediate (via) point and updating the distance between every pair of nodes if a shorter path is found through that node. Capable of handling **negative edge weights (but not negative cycles)**, this algorithm is especially useful for dense graphs and multi-source queries, with a time complexity of **O(V³)**.


## 1️⃣ Floyd-Warshall Algorithm – All Pairs Shortest Path

### 📌 Problem Statement

You are given:

* A matrix `dist` of size `n × n`

  * `dist[i][j]` represents the weight of edge from node `i` to node `j`
  * `-1` indicates **no direct edge**

👉 Compute the **shortest distance between every pair of nodes**

---

### 🚀 Approach: Dynamic Programming (Floyd-Warshall)

#### 🔹 Key Idea

* Try every node as an **intermediate (via) node**
* Update shortest paths using:

[
dist[i][j] = \min(dist[i][j],; dist[i][via] + dist[via][j])
]

👉 This ensures all possible paths are considered

---

### 🧠 Algorithm

1. Preprocess:

   * Replace `-1` with `∞` (unreachable)

2. For each node `via`:

   * For every pair `(i, j)`:

     * Update shortest path through `via`

3. Postprocess:

   * Convert `∞` back to `-1`

4. Return updated matrix

---

### 📊 Complexity Analysis

| Type             | Complexity      |
| ---------------- | --------------- |
| Time Complexity  | O(V³)           |
| Space Complexity | O(1) (in-place) |

---

### 📎 Example

```text id="example"
Input:
dist = [
 [0, 3, -1],
 [-1, 0, 1],
 [2, -1, 0]
]

Output:
[
 [0, 3, 4],
 [3, 0, 1],
 [2, 5, 0]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Initially:
Use direct edges

After considering intermediate nodes:
Paths improve via other nodes

Final matrix contains shortest paths ✔️
```

---

### ✅ Key Points

* Solves **all-pairs shortest path**
* Works with **negative weights (no negative cycles)**
* Uses **dynamic programming**
* In-place matrix transformation

---

### ⚠️ Edge Cases

* No path between nodes → remains `-1`
* Self-loops (`dist[i][i] = 0`)
* Negative edges allowed
* Negative cycles ❌ (not handled explicitly here)

---

### 🏁 Conclusion

Floyd-Warshall is a powerful algorithm for computing shortest paths between all pairs of nodes, especially useful when dealing with dense graphs or when multiple queries are required.


---


## 2️⃣ Detect Negative Weight Cycle – Floyd-Warshall Algorithm

### 📌 Problem Statement

You are given:

* `n` → number of vertices
* `edges` → list of directed edges `[u, v, w]`

  * `u` → source node
  * `v` → destination node
  * `w` → edge weight (can be negative)

👉 Determine whether the graph contains a **negative weight cycle**

#### 🎯 Output:

* Return `1` → if a negative cycle exists
* Return `0` → otherwise

---

### 🚀 Approach: Floyd-Warshall Algorithm

#### 🔹 Key Idea

* Compute **shortest paths between all pairs of nodes**
* A graph contains a **negative cycle** if:

[
dist[i][i] < 0
]

👉 This means a node can reach itself with negative cost

---

### 🧠 Algorithm

1. Initialize:

   * `dist[i][j] = ∞`
   * `dist[i][i] = 0`

2. Fill direct edges:

   * `dist[u][v] = w`

3. Run Floyd-Warshall:

   * For each `via`:

     * Update all pairs `(i, j)`

4. Detect cycle:

   * If any `dist[i][i] < 0` → negative cycle exists

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(V³)      |
| Space Complexity | O(V²)      |

---

### 📎 Example

```text id="example"
Input:
n = 3
edges = [
 [0,1,1],
 [1,2,-1],
 [2,0,-1]
]

Output: 1

Explanation:
Cycle: 0 → 1 → 2 → 0  
Total weight = -1 → negative cycle ✔️
```

---

### 🔍 Dry Run

```text id="dryrun"
After Floyd-Warshall:
dist[0][0] becomes negative

→ Negative cycle detected ✔️
```

---

### ✅ Key Points

* Uses **Floyd-Warshall for all-pairs shortest path**
* Detects cycle via **negative diagonal values**
* Works with negative weights
* Checks cycles globally in graph

---

### ⚠️ Edge Cases

* No edges
* No negative weights
* Disconnected graph
* Multiple negative cycles

---

### 🏁 Conclusion

This approach leverages Floyd-Warshall to detect negative cycles by analyzing the diagonal of the distance matrix, making it a reliable method for identifying cycles across the entire graph.


---


## 3️⃣ Transitive Closure of a Graph

### 📌 Problem Statement

You are given:

* `N` → number of vertices
* `graph` → adjacency matrix (`N × N`)

  * `graph[i][j] = 1` → edge exists from `i` to `j`
  * `graph[i][j] = 0` → no direct edge

👉 Compute the **transitive closure** of the graph

#### 🎯 Goal:

Determine whether a path exists between every pair of nodes

---

### 🚀 Approach: Floyd-Warshall (Reachability Version)

#### 🔹 Key Idea

* Instead of shortest paths, compute **reachability**
* A node `j` is reachable from `i` if:

[
reach[i][j] = reach[i][j] ;\text{OR}; (reach[i][via] \land reach[via][j])
]

👉 Uses logical operations instead of distances

---

### 🧠 Algorithm

1. Initialize:

   * `reach[i][j] = 1` if direct edge exists
   * `reach[i][i] = 1` (self reachable)

2. For each intermediate node `via`:

   * For every pair `(i, j)`:

     * Update reachability using:

       ```
       reach[i][j] = reach[i][j] OR (reach[i][via] AND reach[via][j])
       ```

3. Return `reach` matrix

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(N³)      |
| Space Complexity | O(N²)      |

---

### 📎 Example

```text id="example"
Input:
graph = [
 [0,1,0],
 [0,0,1],
 [0,0,0]
]

Output:
[
 [1,1,1],
 [0,1,1],
 [0,0,1]
]

Explanation:
0 → 1 → 2 → reachable ✔️
```

---

### 🔍 Dry Run

```text id="dryrun"
Initially:
Only direct edges marked

After processing via nodes:
Indirect paths are discovered

Final matrix shows all reachable nodes ✔️
```

---

### ✅ Key Points

* Computes **reachability (not distance)**
* Based on **Floyd-Warshall algorithm**
* Uses logical operations (`OR`, `AND`)
* Useful in path existence problems

---

### ⚠️ Edge Cases

* No edges → only diagonal = 1
* Fully connected graph
* Disconnected components
* Self loops

---

### 🏁 Conclusion

Transitive closure helps determine reachability between all pairs of nodes and is widely used in graph analysis, dependency resolution, and connectivity problems.


---