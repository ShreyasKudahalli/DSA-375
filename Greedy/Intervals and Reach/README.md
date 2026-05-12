# Interval and reach
Interval and reach problems focus on processing ranges, overlaps, and coverage efficiently to determine how far a condition, connection, or influence can extend within a sequence or timeline. These problems often involve sorting intervals, merging overlaps, tracking active ranges, or expanding reachable boundaries using greedy techniques, sweeping algorithms, or graph traversal concepts. They are commonly used in scheduling, range merging, meeting rooms, coverage analysis, and path expansion problems where managing continuous segments and their reachability is essential.


## 1️⃣ Merge Intervals – Greedy Approach

### 📌 Problem Statement

You are given:

* `intervals` → a list of intervals where each interval is represented as `[start, end]`

👉 Merge all overlapping intervals and return the resulting non-overlapping intervals.

---

### 🚀 Approach: Sorting + Greedy Merging

#### 🔹 Key Idea

* Sort intervals based on starting time
* Compare each interval with the last merged interval

👉 If intervals overlap:

* Merge them by updating the ending value

👉 Otherwise:

* Add a new interval to the result

---

### 🧠 Algorithm

1. Sort intervals by starting point

2. Initialize result list with first interval

3. Traverse remaining intervals:

   * If current interval overlaps:

     * Merge by updating end value
   * Else:

     * Append interval to result

4. Return merged intervals

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n log n) |
| Space Complexity | O(n)       |

> Sorting dominates the complexity.

---

### 📎 Example

```text id="example"
Input:
intervals = [[1,3],[2,6],[8,10],[15,18]]

Output:
[[1,6],[8,10],[15,18]]
```

---

### 🔍 Dry Run

```text id="dryrun"
Sorted:
[[1,3],[2,6],[8,10],[15,18]]

Start:
res = [[1,3]]

Compare [2,6]
Overlap ✔️
Merge → [1,6]

Compare [8,10]
No overlap ❌
Append

Result:
[[1,6],[8,10],[15,18]]
```

---

### 🌳 Visualization

```text id="visual"
[1----3]
     [2------6]

Merged:
[1----------6]
```

---

### ✅ Key Points

* Classic **greedy interval problem**
* Sorting makes overlap detection easy
* Merge only when intervals intersect
* Efficient single traversal after sorting

---

### ⚠️ Edge Cases

* Single interval
* Fully overlapping intervals
* Non-overlapping intervals
* Nested intervals

---

### 🏁 Conclusion

This problem demonstrates how sorting combined with greedy merging can efficiently combine overlapping intervals into a minimal set of non-overlapping ranges.

---