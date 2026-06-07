# Knapsack and Subset Sum DP

Knapsack and Subset Sum Dynamic Programming problems revolve around making optimal include-or-exclude decisions for a collection of items under constraints such as weight, capacity, target sum, or value maximization. These problems typically define states based on the current item and remaining capacity or target, allowing solutions to be built from smaller subproblems. This pattern forms the foundation for many DP topics, including 0/1 Knapsack, Unbounded Knapsack, Partition Equal Subset Sum, Target Sum, Coin Change, and various subset-selection optimization problems, making it one of the most fundamental and widely applicable dynamic programming techniques.

## 1️⃣ 0/1 Knapsack

### 📌 Problem Statement

You are given:

* `W` → maximum capacity of the knapsack
* `wt[]` → weight of each item
* `val[]` → value of each item

👉 Each item can be chosen **at most once**.

👉 Return the maximum total value that can be obtained without exceeding the knapsack capacity.

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

For every item, we have two choices:

* **Exclude** the item
* **Include** the item (if it fits in the remaining capacity)

State definition:

```text id="relation"
dp[i][w]
=
Maximum value obtainable
using first i items
with capacity w
```

Transition:

```text id="formula"
Exclude:

dp[i-1][w]

Include:

val[i-1] + dp[i-1][w-wt[i-1]]

dp[i][w] =
max(include, exclude)
```

---

### 🧠 Algorithm

1. Create a DP table:

   * `dp[i][w]` stores the maximum value obtainable.

2. Initialize:

   * Row `0` = 0 (no items)
   * Column `0` = 0 (zero capacity)

3. For every item:

   * Compute value if excluded.
   * Compute value if included (if weight allows).

4. Store the maximum of the two choices.

5. Return:

   * `dp[n][W]`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n × W)   |
| Space Complexity | O(n × W)   |

Where:

* `n` = number of items
* `W` = knapsack capacity

---

### 📎 Example

```text id="example"
Input:

W = 4

wt  = [4, 5, 1]
val = [1, 2, 3]

Output:
3
```

---

### 🔍 Dry Run

```text id="dryrun"
Capacity = 4

Item 1:
Weight = 4
Value  = 1

Item 2:
Weight = 5
Cannot fit

Item 3:
Weight = 1
Value  = 3

Best Choice:
Take Item 3

Maximum Value = 3
```

---

### 🌳 Visualization

```text id="visual"
Capacity = 4

Items:

Weight  Value
  4       1
  5       2
  1       3

Possible Selections:

Take Item 1 → Value = 1
Take Item 3 → Value = 3

Maximum = 3
```

---

### ✅ Key Points

* Classic include/exclude dynamic programming problem
* Each item can be selected only once
* State depends on:

  * Current item
  * Remaining capacity
* Foundation for many subset and resource allocation problems

---

### ⚠️ Edge Cases

* Capacity = 0
* No items
* All items heavier than capacity
* Single item exactly fitting the capacity

---

### 🏁 Conclusion

The 0/1 Knapsack problem is one of the most important dynamic programming problems. By evaluating the choice of including or excluding each item and storing intermediate results, DP efficiently finds the maximum achievable value within the given capacity constraint.
