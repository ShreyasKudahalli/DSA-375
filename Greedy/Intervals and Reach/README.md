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


## 2️⃣ Insert Interval 

### 📌 Problem Statement

You are given:

* `intervals` → a list of non-overlapping intervals sorted by start time
* `newInterval` → a new interval to insert

👉 Insert the new interval into the list and merge overlapping intervals if necessary.

---

### 🚀 Approach: Greedy Interval Processing

#### 🔹 Key Idea

Process intervals in **3 phases**:

1. Add all intervals completely before `newInterval`
2. Merge all overlapping intervals
3. Add remaining intervals after merging

---

### 🧠 Algorithm

1. Traverse intervals:

   * If current interval ends before `newInterval` starts:

     * Add directly to result

2. Merge overlaps:

   * If intervals overlap:

     * Update start and end of `newInterval`

3. Add merged interval to result

4. Append remaining intervals

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(n)       |

---

### 📎 Example

```text id="example"
Input:
intervals = [[1,3],[6,9]]
newInterval = [2,5]

Output:
[[1,5],[6,9]]
```

---

### 🔍 Dry Run

```text id="dryrun"
intervals = [[1,3],[6,9]]
newInterval = [2,5]

[1,3] overlaps with [2,5]
Merge → [1,5]

Append remaining:
[6,9]

Result:
[[1,5],[6,9]]
```

---

### 🌳 Visualization

```text id="visual"
Existing:
[1---3]   [6---9]

New:
   [2---5]

Merged:
[1-------5]   [6---9]
```

---

### ✅ Key Points

* Efficient linear traversal
* No need to re-sort intervals
* Greedy merging handles overlaps naturally
* Works because input intervals are already sorted

---

### ⚠️ Edge Cases

* Insert at beginning
* Insert at end
* Fully overlapping intervals
* No overlap at all
* Empty intervals list

---

### 🏁 Conclusion

This problem demonstrates how interval insertion and merging can be efficiently handled using greedy traversal by separating non-overlapping, overlapping, and remaining intervals into distinct phases.

---


## 3️⃣ Non-overlapping Intervals

### 📌 Problem Statement

You are given:

* `intervals` → a list of intervals `[start, end]`

👉 Return the **minimum number of intervals to remove** so that the remaining intervals are non-overlapping.

---

### 🚀 Approach: Greedy by Ending Time

#### 🔹 Key Idea

To keep the maximum number of non-overlapping intervals:

* Always select the interval with the **smallest ending time**

👉 This leaves more room for future intervals.

---

### 🧠 Algorithm

1. Sort intervals based on ending time

2. Initialize:

   * `count = 1`
   * `last = end time of first interval`

3. Traverse remaining intervals:

   * If current interval starts after or at `last`

     * Keep it
     * Update `last`
     * Increment `count`

4. Answer:

   * `total intervals - non-overlapping intervals kept`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n log n) |
| Space Complexity | O(1)       |

> Sorting dominates the runtime.

---

### 📎 Example

```text id="example"
Input:
intervals = [[1,2],[2,3],[3,4],[1,3]]

Output:
1
```

---

### 🔍 Dry Run

```text id="dryrun"
Sorted by end:
[[1,2],[2,3],[1,3],[3,4]]

Pick [1,2]
Pick [2,3]
Skip [1,3] ❌ (overlap)
Pick [3,4]

Kept = 3
Removed = 4 - 3 = 1
```

---

### 🌳 Visualization

```text id="visual"
Intervals:
[1---2]
    [2---3]
 [1-------3] ❌
         [3---4]

Remove:
[1---3]
```

---

### ✅ Key Points

* Classic **interval scheduling greedy problem**
* Sorting by end time gives optimal solution
* Maximizes number of intervals kept
* Minimum removals = total − kept intervals

---

### ⚠️ Edge Cases

* Empty interval list
* Single interval
* Fully overlapping intervals
* Already non-overlapping intervals

---

### 🏁 Conclusion

This problem demonstrates the greedy interval scheduling strategy where selecting intervals with the earliest finishing time ensures the maximum number of non-overlapping intervals can be retained.

---


## 4️⃣ Minimum Number of Arrows to Burst Balloons

### 📌 Problem Statement

You are given:

* `points` → a list of balloon intervals `[start, end]`

Each balloon spans a horizontal interval.

👉 An arrow shot at position `x` bursts all balloons where:

```text id="cond"
start <= x <= end
```

👉 Return the **minimum number of arrows** required to burst all balloons.

---

### 🚀 Approach: Greedy by Ending Coordinate

#### 🔹 Key Idea

* Sort balloons based on their ending position
* Shoot arrows at the earliest possible ending point

👉 This allows one arrow to burst the maximum overlapping balloons.

---

### 🧠 Algorithm

1. Sort balloons by ending coordinate

2. Initialize:

   * `count = 1`
   * `last = end of first balloon`

3. Traverse remaining balloons:

   * If current balloon starts after `last`

     * Need a new arrow
     * Increment count
     * Update `last`

4. Return total arrows used

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n log n) |
| Space Complexity | O(1)       |

> Sorting dominates the runtime.

---

### 📎 Example

```text id="example"
Input:
points = [[10,16],[2,8],[1,6],[7,12]]

Output:
2
```

---

### 🔍 Dry Run

```text id="dryrun"
Sorted by end:
[[1,6],[2,8],[7,12],[10,16]]

Arrow 1 at x = 6
Bursts:
[1,6], [2,8]

Arrow 2 at x = 12
Bursts:
[7,12], [10,16]

Total arrows = 2
```

---

### 🌳 Visualization

```text id="visual"
[1------6]
   [2--------8]

        [7---------12]
             [10---------16]

Arrow1 → x = 6
Arrow2 → x = 12
```

---

### ✅ Key Points

* Classic **greedy interval coverage problem**
* Sorting by end position gives optimal solution
* One arrow can cover overlapping intervals
* Similar to activity selection scheduling

---

### ⚠️ Edge Cases

* Single balloon
* Fully overlapping balloons
* Non-overlapping balloons
* Large coordinate ranges

---

### 🏁 Conclusion

This problem demonstrates how greedy interval scheduling can minimize resources by always choosing the earliest finishing interval to maximize overlap coverage.

---


 
## 5️⃣ Car Pooling

### 📌 Problem Statement

You are given:

* `trips[i] = [numPassengers, from, to]`
* `capacity` → maximum passenger capacity of the vehicle

👉 Determine whether it is possible to complete all trips without exceeding the vehicle capacity at any point.

---

### 🚀 Approach: Sweep Line / Event Simulation

#### 🔹 Key Idea

Instead of checking every location individually:

* Treat each trip as:

  * Pickup event → `+passengers`
  * Drop event → `-passengers`

👉 Process events in sorted order to simulate passenger changes over time.

---

### 🧠 Algorithm

1. Create events list:

   * `(start, +numPassengers)`
   * `(end, -numPassengers)`

2. Sort events by location

3. Traverse events:

   * Update current passengers
   * If passengers exceed capacity:

     * Return `False`

4. If all events processed successfully:

   * Return `True`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n log n) |
| Space Complexity | O(n)       |

> Sorting events dominates the runtime.

---

### 📎 Example

```text id="example"
Input:
trips = [[2,1,5],[3,3,7]]
capacity = 4

Output:
False
```

---

### 🔍 Dry Run

```text id="dryrun"
Trips:
[2,1,5]
[3,3,7]

Events:
(1,+2)
(3,+3)
(5,-2)
(7,-3)

Passengers:
0 → 2
2 → 5 ❌ exceeds capacity

Return False
```

---

### 🌳 Visualization

```text id="visual"
Location:
1      3      5      7

+2 → passengers = 2
+3 → passengers = 5 ❌
-2
-3
```

---

### ✅ Key Points

* Uses **sweep line / event processing**
* Efficiently tracks interval overlaps
* Similar to meeting room scheduling problems
* Avoids checking every point individually

---

### ⚠️ Edge Cases

* Exact capacity match
* Fully overlapping trips
* Non-overlapping trips
* Multiple pickups/drop-offs at same location

---

### 🏁 Conclusion

This problem demonstrates how interval events and sweep line techniques can efficiently simulate overlapping ranges and capacity constraints in scheduling and transportation problems.

---


## 6️⃣ Jump Game 

### 📌 Problem Statement

You are given:

* `nums` → an array where `nums[i]` represents the maximum jump length from index `i`

👉 Determine whether you can reach the **last index** starting from the first index.

---

### 🚀 Approach: Greedy Reach Tracking

#### 🔹 Key Idea

* Keep track of the **farthest reachable index**
* At every position:

  * Update the maximum reach possible

👉 If current index becomes unreachable:

* Return `False`

---

### 🧠 Algorithm

1. Initialize:

   * `jump = 0` → farthest reachable index

2. Traverse array:

   * If current index `i > jump`

     * Cannot reach this position
     * Return `False`

3. Update:

   * `jump = max(jump, i + nums[i])`

4. If traversal completes:

   * Return `True`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(1)       |

---

### 📎 Example

```text id="example"
Input:
nums = [2,3,1,1,4]

Output:
True
```

---

### 🔍 Dry Run

```text id="dryrun"
nums = [2,3,1,1,4]

i = 0
jump = max(0, 0+2) = 2

i = 1
jump = max(2, 1+3) = 4

i = 2
reachable ✔️

i = 4
Reached end ✔️
```

---

### 🌳 Visualization

```text id="visual"
Index:  0  1  2  3  4
Nums : [2, 3, 1, 1, 4]

0 → can reach up to 2
1 → can reach up to 4 ✔️
```

---

### ✅ Key Points

* Classic **greedy reachability problem**
* Track farthest reachable index dynamically
* Single-pass efficient solution
* No recursion or DP required

---

### ⚠️ Edge Cases

* Single element array
* Array starting with `0`
* Unreachable gap in middle
* Large jumps skipping many indices

---

### 🏁 Conclusion

This problem demonstrates how greedy techniques can efficiently solve reachability problems by continuously maintaining the farthest reachable position while traversing the array.

---


## 7️⃣ Jump Game II 

### 📌 Problem Statement

You are given:

* `nums` → an array where `nums[i]` represents the maximum jump length from index `i`

👉 Return the **minimum number of jumps** required to reach the last index.

---

### 🚀 Approach: Greedy Level Expansion

#### 🔹 Key Idea

Treat the array like BFS levels:

* `[l, r]` represents the current jump range
* Explore all positions in the current range
* Compute the farthest reachable position for the next jump

👉 Each range expansion corresponds to one jump.

---

### 🧠 Algorithm

1. Initialize:

   * `l = 0`
   * `r = 0`
   * `res = 0`

2. While end not reached:

   * Compute farthest reachable index from current range
   * Move to next range
   * Increment jump count

3. Return total jumps

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(1)       |

---

### 📎 Example

```text id="example"
Input:
nums = [2,3,1,1,4]

Output:
2
```

---

### 🔍 Dry Run

```text id="dryrun"
nums = [2,3,1,1,4]

Range [0,0]
Reach = 2
Jumps = 1

Range [1,2]
Reach = 4
Jumps = 2

Reached end ✔️
```

---

### 🌳 Visualization

```text id="visual"
Index:  0  1  2  3  4
Nums : [2, 3, 1, 1, 4]

Jump 1:
0 → [1,2]

Jump 2:
[1,2] → 4 ✔️
```

---

### ✅ Key Points

* Greedy + BFS-level traversal pattern
* Expands reachable range layer by layer
* Each layer represents one jump
* Optimized linear-time solution

---

### ⚠️ Edge Cases

* Single element array → 0 jumps
* Large jumps skipping indices
* Already reachable in one jump

---

### 🏁 Conclusion

This problem demonstrates how greedy range expansion can efficiently compute the minimum number of jumps by exploring reachable positions level by level, similar to BFS on an implicit graph.

---

## 8️⃣ Minimum Number of Taps to Open to Water a Garden

### 📌 Problem Statement

You are given:

* `n` → length of the garden `[0...n]`
* `ranges[i]` → watering range of tap `i`

A tap at position `i` can water:

```text id="range"
[i - ranges[i], i + ranges[i]]
```

👉 Return the minimum number of taps needed to water the entire garden.

👉 If impossible, return `-1`.

---

### 🚀 Approach: Greedy Reach Expansion

#### 🔹 Key Idea

Convert each tap into an interval:

```text id="interval"
[left, right]
```

Then solve it like a **minimum interval coverage / jump game** problem.

👉 Track:

* current coverage
* farthest reachable point

---

### 🧠 Algorithm

1. Create an array `arr`

   * `arr[left] = farthest right coverage`

2. For every tap:

   * Compute:

     * `left = max(0, i - ranges[i])`
     * `right = min(n, i + ranges[i])`

3. Traverse garden from `0 → n`:

   * Update farthest reachable point
   * If current index exceeds reachable range:

     * return `-1`

4. When reaching current coverage boundary:

   * Open a new tap
   * Extend coverage

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(n)       |

---

### 📎 Example

```text id="example"
Input:
n = 5
ranges = [3,4,1,1,0,0]

Output:
1
```

---

### 🔍 Dry Run

```text id="dryrun"
Tap 1 covers:
[0,5]

Garden fully covered using 1 tap ✔️
```

---

### 🌳 Visualization

```text id="visual"
Garden:
0 ----------- 5

Tap at position 1:
[0----------------5]

Coverage complete ✔️
```

---

### ✅ Key Points

* Converts watering ranges into interval coverage
* Similar to **Jump Game II**
* Greedy expansion minimizes taps
* Efficient linear traversal

---

### ⚠️ Edge Cases

* Impossible coverage → return `-1`
* Single tap covers entire garden
* Multiple overlapping ranges
* Sparse coverage gaps

---

### 🏁 Conclusion

This problem demonstrates how interval coverage and greedy reach expansion can efficiently solve minimum coverage problems by always extending the farthest reachable boundary.

---