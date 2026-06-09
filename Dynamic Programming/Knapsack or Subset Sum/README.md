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


---


## 3️⃣ Coin Change II

### 📌 Problem Statement

You are given:

* `coins[]` → available coin denominations
* `amount` → target amount

👉 Each coin denomination can be used **unlimited times**.

👉 Return the number of distinct combinations that can make up the given amount.

👉 The order of coins does **not** matter.

---

### 🚀 Approach: Dynamic Programming (Unbounded Knapsack Counting)

#### 🔹 Key Idea

Instead of finding the minimum number of coins, we count the number of valid combinations.

For every coin, we have two choices:

* **Don't take** the current coin
* **Take** the current coin and stay on the same coin because it can be reused

State definition:

```text id="relation"
dp[i][t]
=
Number of ways
to form target t
using coins[0...i]
```

Transition:

```text id="formula"
Not Take:

dp[i-1][t]

Take:

dp[i][t-coins[i]]

dp[i][t] =
notTake + take
```

The include transition remains on the same coin index because coins are available infinitely many times.

---

### 🧠 Algorithm

1. Initialize base case using the first coin:

   * If target is divisible by the first coin:

     * Ways = 1
   * Otherwise:

     * Ways = 0

2. Process each remaining coin.

3. For every target amount:

   * Count ways excluding the coin.
   * Count ways including the coin.
   * Add both counts.

4. Use space optimization with two arrays.

5. Return ways to form the target amount.

---

### 📊 Complexity Analysis

| Type             | Complexity    |
| ---------------- | ------------- |
| Time Complexity  | O(n × amount) |
| Space Complexity | O(amount)     |

Where:

* `n` = number of coin denominations

---

### 📎 Example

```text id="example"
Input:

amount = 5
coins = [1,2,5]

Output:
4
```

---

### 🔍 Dry Run

```text id="dryrun"
Target = 5

Possible combinations:

1+1+1+1+1
1+1+1+2
1+2+2
5

Total Ways = 4
```

---

### 🌳 Visualization

```text id="visual"
Amount = 5

Coins:
[1, 2, 5]

Ways:

5 × 1

3 × 1 + 1 × 2

1 × 1 + 2 × 2

1 × 5

Total = 4 Ways
```

---

### ✅ Key Points

* Unbounded Knapsack counting problem
* Coins can be reused unlimited times
* Order does not matter
* DP stores number of combinations instead of minimum coins
* Space optimized to O(amount)

---

### ⚠️ Edge Cases

* Amount = 0
* Single coin denomination
* No possible combination
* Large target amounts

---

### 🏁 Conclusion

Coin Change II is a classic counting variant of the Unbounded Knapsack problem. By considering both taking and not taking each coin and accumulating the number of valid ways, dynamic programming efficiently computes all unique combinations that form the target amount.
