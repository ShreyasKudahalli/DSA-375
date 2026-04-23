# Dijkstra’s Algorithm 
Dijkstra’s Algorithm is a fundamental greedy technique used to find the shortest path from a source node to all other nodes in a **weighted graph with non-negative edge weights**. It works by always selecting the node with the smallest known distance (using a priority queue/min-heap) and relaxing its edges to update neighboring distances efficiently. Widely applied in navigation systems, network routing, and optimization problems, Dijkstra ensures optimal shortest paths in **O((V + E) log V)** time, making it one of the most efficient algorithms for weighted graph traversal.


## 1️⃣ Dijkstra’s Algorithm – Shortest Path in Weighted Graph

### 📌 Problem Statement

You are given:

* `V` → number of vertices
* `edges` → list of edges `[u, v, w]`

  * `u`, `v` → vertices
  * `w` → weight of the edge
* `src` → source vertex

👉 Find the **shortest distance from `src` to all other vertices**

---

### 🚀 Approach: Greedy + Min Heap (Priority Queue)

#### 🔹 Key Idea

* Always process the node with the **smallest distance**
* Use a **min heap** to efficiently get the next closest node

👉 Relax edges to update shortest distances

---

### 🧠 Algorithm

1. Build adjacency list

2. Initialize:

   * `dist[] = ∞` for all nodes
   * `dist[src] = 0`

3. Push `(0, src)` into min heap

4. While heap is not empty:

   * Pop node with smallest distance
   * If already processed with shorter distance → skip
   * For each neighbor:

     * Relax edge:

       * If new distance < current → update
       * Push updated value to heap

5. Return `dist[]`

---

### 📊 Complexity Analysis

| Type             | Complexity       |
| ---------------- | ---------------- |
| Time Complexity  | O((V + E) log V) |
| Space Complexity | O(V + E)         |

👉 Efficient for sparse graphs

---

### 📎 Example

```text id="example"
Input:
V = 5
edges = [
 [0,1,2],
 [0,2,4],
 [1,2,1],
 [1,3,7],
 [2,4,3],
 [3,4,1]
]
src = 0

Output:
[0, 2, 3, 9, 6]
```

---

### 🔍 Dry Run

```text id="dryrun"
Start at node 0:
dist = [0, ∞, ∞, ∞, ∞]

→ update neighbors:
1 → 2
2 → 4

Next pick node 1:
→ update 2 → 3
→ update 3 → 9

Continue until all nodes processed ✔️
```

---

### ✅ Key Points

* Uses **Greedy approach**
* Works with **non-negative weights only**
* Uses **min heap for efficiency**
* Avoids unnecessary processing using distance check

---

### ⚠️ Edge Cases

* Disconnected graph → unreachable nodes remain `∞`
* Single node
* Zero-weight edges
* Negative weights ❌ (not supported)

---

### 🏁 Conclusion

Dijkstra’s Algorithm efficiently computes shortest paths in weighted graphs using a priority queue, making it ideal for real-world problems like navigation, routing, and network optimization.

---


## 2️⃣ Cheapest Flights Within K Stops

### 📌 Problem Statement

You are given:

* `n` → number of cities
* `flights` → list of flights `[u, v, w]`

  * `u` → source city
  * `v` → destination city
  * `w` → cost
* `src` → starting city
* `dst` → destination city
* `k` → maximum allowed stops

👉 Find the **cheapest price** from `src` to `dst` with at most `k` stops
👉 If not possible → return `-1`

---

### 🚀 Approach: BFS + Cost Relaxation

#### 🔹 Key Idea

* Use **BFS traversal with state tracking**
* Each state includes:

  * current node
  * current cost
  * number of stops

👉 Only explore paths within `k` stops
👉 Update cost only if it's cheaper

---

### 🧠 Algorithm

1. Build adjacency list from flights

2. Initialize:

   * Queue → `(node, cost, stops)`
   * `dist[] = ∞`
   * `dist[src] = 0`

3. Start BFS:

   * Pop node from queue
   * If stops exceed `k` → skip

4. For each neighbor:

   * Calculate new cost
   * If cheaper → update and push to queue

5. Return:

   * `dist[dst]` if reachable
   * Else `-1`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(V + E)   |
| Space Complexity | O(V + E)   |

👉 Efficient due to limited stops constraint

---

### 📎 Example

```text id="example"
Input:
n = 4
flights = [
 [0,1,100],
 [1,2,100],
 [2,3,100],
 [0,2,500]
]
src = 0, dst = 3, k = 1

Output: 600

Explanation:
0 → 2 → 3 (cost = 500 + 100 = 600) ✔️
```

---

### 🔍 Dry Run

```text id="dryrun"
Start at 0:
Queue = [(0,0,0)]

→ Visit 1 (cost 100)
→ Visit 2 (cost 500)

From 1:
→ Visit 2 (cost 200)

From 2:
→ Visit 3 (cost 600)

Stops constraint satisfied ✔️
```

---

### ✅ Key Points

* Uses **BFS with additional state (stops)**
* Applies **cost relaxation similar to Dijkstra**
* Limits traversal using `k` stops
* Efficient for constrained shortest path problems

---

### ⚠️ Edge Cases

* No path exists → return `-1`
* `k = 0` → direct flights only
* Large graph with many paths
* Multiple cheaper intermediate paths

---

### 🏁 Conclusion

This approach combines BFS traversal with cost optimization to efficiently find the cheapest route under stop constraints, making it ideal for real-world routing problems like flight planning.

---


## 3️⃣ Network Delay Time – Shortest Signal Propagation

### 📌 Problem Statement

You are given:

* `times` → list of directed edges `[u, v, w]`

  * `u` → source node
  * `v` → destination node
  * `w` → time taken
* `n` → number of nodes
* `k` → starting node (signal source)

👉 Determine the **minimum time required** for all nodes to receive the signal
👉 If not all nodes can be reached → return `-1`

---

### 🚀 Approach: Dijkstra’s Algorithm (Min Heap)

#### 🔹 Key Idea

* Use a **min heap (priority queue)** to always process the node with the **smallest time**
* Track visited nodes to avoid reprocessing

👉 The maximum time taken to reach any node = final answer

---

### 🧠 Algorithm

1. Build adjacency list from `times`

2. Initialize:

   * Min heap → `(time, node)` starting with `(0, k)`
   * `visited` set
   * `t = 0` → stores max delay

3. While heap is not empty:

   * Pop `(time, node)`
   * If already visited → skip
   * Update `t = max(t, time)`
   * Mark node as visited

4. Push neighbors:

   * `(current_time + edge_weight, neighbor)`

5. Final check:

   * If all nodes visited → return `t`
   * Else → return `-1`

---

### 📊 Complexity Analysis

| Type             | Complexity       |
| ---------------- | ---------------- |
| Time Complexity  | O((V + E) log V) |
| Space Complexity | O(V + E)         |

---

### 📎 Example

```text id="example"
Input:
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4, k = 2

Output: 2

Explanation:
2 → 1 (1)
2 → 3 (1)
3 → 4 (2)

All nodes reached in 2 units ✔️
```

---

### 🔍 Dry Run

```text id="dryrun"
Start at node 2:
Heap = [(0,2)]

→ Visit 2 → push (1,1), (1,3)

→ Visit 1 → no new nodes
→ Visit 3 → push (2,4)

→ Visit 4

Max time = 2 ✔️
```

---

### ✅ Key Points

* Uses **Dijkstra’s Algorithm**
* Tracks maximum delay among shortest paths
* Efficient for weighted directed graphs
* Uses **visited set instead of dist array**

---

### ⚠️ Edge Cases

* Disconnected graph → return `-1`
* Single node
* Multiple paths with different weights
* Large graphs

---

### 🏁 Conclusion

This problem is a classic application of **Dijkstra’s Algorithm**, where the goal is not just shortest paths but the **maximum shortest time** needed to reach all nodes, making it ideal for network propagation problems.

---