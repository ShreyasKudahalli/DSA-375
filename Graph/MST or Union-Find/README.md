

## 1️⃣ Kruskal’s Algorithm – Minimum Spanning Tree (MST)

### 📌 Problem Statement

You are given:

* `V` → number of vertices
* `edges` → list of edges `[u, v, w]`

  * `u`, `v` → vertices
  * `w` → weight of the edge

👉 Find the **total weight of the Minimum Spanning Tree (MST)**

---

### 🚀 Approach: Kruskal’s Algorithm + Disjoint Set (Union-Find)

#### 🔹 Key Idea

* Always pick the **smallest weight edge**
* Avoid cycles using **Disjoint Set (DSU)**

👉 Build MST greedily by adding safe edges

---

### 🧠 Algorithm

1. Sort all edges by weight (ascending)

2. Initialize DSU (Disjoint Set)

3. For each edge `(u, v, w)`:

   * If `u` and `v` are in different sets:

     * Add edge to MST
     * Union their sets
   * Else:

     * Skip (would form cycle)

4. Return total weight

---

### 🧩 Disjoint Set Features

* **Path Compression** → speeds up `find()`
* **Union by Rank** → keeps tree shallow

👉 Ensures near constant-time operations

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(E log E) |
| Space Complexity | O(V)       |

👉 Sorting edges dominates the complexity

---

### 📎 Example

```text id="example"
Input:
V = 4
edges = [
  [0,1,10],
  [0,2,6],
  [0,3,5],
  [1,3,15],
  [2,3,4]
]

Output: 19

Explanation:
MST edges:
(2,3)=4, (0,3)=5, (0,1)=10  
Total = 19 ✔️
```

---

### 🔍 Dry Run

```text id="dryrun"
Sorted edges:
(2,3)=4 → add  
(0,3)=5 → add  
(0,2)=6 → skip (cycle)  
(0,1)=10 → add  

MST complete ✔️
```

---

### ✅ Key Points

* Greedy algorithm
* Uses **DSU to avoid cycles**
* Efficient for sparse graphs
* Guarantees minimum total weight

---

### ⚠️ Edge Cases

* Disconnected graph (forms forest)
* Single node
* No edges
* Multiple edges with same weight

---

### 🏁 Conclusion

Kruskal’s Algorithm efficiently constructs the Minimum Spanning Tree by combining **greedy selection** with **Union-Find**, achieving optimal performance for large graphs.

---