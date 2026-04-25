# Bellman-Ford
Bellman-Ford is a fundamental graph algorithm used to compute shortest paths from a single source in a **weighted graph that may contain negative edge weights**. Unlike Dijkstra’s algorithm, it can handle negative weights and also detect **negative weight cycles** by performing one extra relaxation after (V-1) iterations. The algorithm works by repeatedly relaxing all edges, ensuring that the shortest distances propagate through the graph, and is widely used in scenarios where edge weights can be negative or constraints limit path length.



## 1️⃣ Detect Negative Weight Cycle – Bellman-Ford Algorithm

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

### 🚀 Approach: Bellman-Ford Algorithm

#### 🔹 Key Idea

* Relax all edges **(n - 1) times**
* If you can still relax an edge on the **nth iteration** → cycle exists

👉 This works because shortest paths should stabilize after `n-1` relaxations

---

### 🧠 Algorithm

1. Initialize:

   * `dist[] = 0` for all nodes (to detect cycles anywhere in graph)

2. Relax edges `n - 1` times:

   * For each edge `(u, v, w)`:

     * If `dist[u] + w < dist[v]` → update

3. Check for cycle:

   * Run one more iteration
   * If any edge still relaxes → negative cycle exists

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(V × E)   |
| Space Complexity | O(V)       |

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
After n-1 relaxations:
Distances keep decreasing

Extra iteration:
Still updating → negative cycle detected ✔️
```

---

### ✅ Key Points

* Works with **negative weights**
* Detects cycles using **extra relaxation**
* Can detect cycles anywhere in graph
* Core algorithm for many shortest path problems

---

### ⚠️ Edge Cases

* No edges
* No negative weights
* Disconnected graph
* Multiple components

---

### 🏁 Conclusion

Bellman-Ford is a powerful algorithm that not only finds shortest paths but also detects **negative weight cycles**, making it essential for graphs where edge weights can be negative.


---


## 2️⃣ Cheapest Flights Within K Stops – Bellman-Ford Approach

### 📌 Problem Statement

You are given:

* `n` → number of cities
* `flights` → list of flights `[u, v, w]`

  * `u` → source city
  * `v` → destination city
  * `w` → cost
* `src` → starting city
* `dst` → destination city
* `k` → maximum number of stops

👉 Find the **minimum cost** to travel from `src` to `dst` with at most `k` stops
👉 If not possible → return `-1`

---

### 🚀 Approach: Bellman-Ford (Limited Relaxation)

#### 🔹 Key Idea

* Perform **edge relaxation up to `k + 1` times**
* Each iteration allows one more edge in the path

👉 Use a temporary array to prevent using updated values within the same iteration

---

### 🧠 Algorithm

1. Initialize:

   * `dist[] = ∞`
   * `dist[src] = 0`

2. Repeat `k + 1` times:

   * Copy `dist` → `temp`
   * For each edge `(u, v, w)`:

     * If `dist[u] + w < temp[v]` → update

3. Update `dist = temp` after each iteration

4. Return:

   * `dist[dst]` if reachable
   * Else `-1`

---

### 📊 Complexity Analysis

| Type             | Complexity     |
| ---------------- | -------------- |
| Time Complexity  | O((k + 1) × E) |
| Space Complexity | O(V)           |

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
Iteration 1:
dist = [0,100,500,∞]

Iteration 2:
dist = [0,100,200,600]

Stops ≤ k satisfied ✔️
```

---

### ✅ Key Points

* Variant of **Bellman-Ford Algorithm**
* Limits path length using iterations
* Uses **temporary array to avoid incorrect updates**
* Works even with complex graph structures

---

### ⚠️ Edge Cases

* No valid path → return `-1`
* `k = 0` → only direct flights
* Multiple paths with different costs
* Disconnected graph

---

### 🏁 Conclusion

This Bellman-Ford variation efficiently computes the cheapest path under a stop constraint by limiting relaxations, making it a powerful alternative to BFS and Dijkstra in constrained path problems.


---