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


---


## 2️⃣ Coin Change

### 📌 Problem Statement

You are given:

* `coins[]` → available coin denominations
* `amount` → target amount

👉 You may use each coin denomination **unlimited times**.

👉 Return the minimum number of coins required to make up the given amount.

👉 If it is impossible to form the amount, return `-1`.

---

### 🚀 Approach: Dynamic Programming (Unbounded Knapsack)

#### 🔹 Key Idea

For each coin, we have two choices:

* **Exclude** the current coin
* **Include** the current coin and stay on the same row because the coin can be used again

State definition:

```text id="relation"
dp[i][t]
=
Minimum coins needed
to form target t
using coins[0...i]
```

Transition:

```text id="formula"
Exclude:

dp[i-1][t]

Include:

1 + dp[i][t - coins[i]]

dp[i][t] =
min(include, exclude)
```

Since coins can be reused, the include transition remains on the same index `i`.

---

### 🧠 Algorithm

1. Create a DP table:

   * `dp[i][t]` stores the minimum coins needed.

2. Initialize the first row:

   * If target `t` is divisible by the first coin:

     * `dp[0][t] = t / coins[0]`
   * Otherwise:

     * `∞`

3. Process each remaining coin.

4. For every target:

   * Compute include choice.
   * Compute exclude choice.
   * Store minimum.

5. If final answer is infinity:

   * Return `-1`

6. Otherwise:

   * Return minimum coins.

---

### 📊 Complexity Analysis

| Type             | Complexity    |
| ---------------- | ------------- |
| Time Complexity  | O(n × amount) |
| Space Complexity | O(n × amount) |

Where:

* `n` = number of coin denominations

---

### 📎 Example

```text id="example"
Input:

coins = [1,2,5]
amount = 11

Output:
3
```

---

### 🔍 Dry Run

```text id="dryrun"
Target = 11

Using coin 5:

11 = 5 + 5 + 1

Coins used = 3

No solution exists with fewer coins.

Answer = 3
```

---

### 🌳 Visualization

```text id="visual"
Amount = 11

Coins:
[1, 2, 5]

Best Combination:

5 + 5 + 1

Total Coins = 3
```

---

### ✅ Key Points

* Classic Unbounded Knapsack problem
* Each coin can be reused infinitely many times
* DP stores minimum coins for every target value
* Include transition stays on the same coin index

---

### ⚠️ Edge Cases

* Amount = 0
* Single coin denomination
* Impossible target amount
* Large amount values

---

### 🏁 Conclusion

The Coin Change problem demonstrates the Unbounded Knapsack DP pattern, where each denomination can be used multiple times. By evaluating include and exclude choices for every target amount, dynamic programming efficiently finds the minimum number of coins needed to reach the desired sum.
