# Dynamic Programming on Stocks

Dynamic Programming on Stocks focuses on maximizing profit from stock transactions under different constraints such as limited transactions, cooldown periods, transaction fees, or multiple buy-sell operations. These problems are modeled using states that represent decisions like buying, selling, or holding a stock on a particular day. By defining transitions between these states and storing intermediate results, stock DP efficiently explores all valid trading strategies while avoiding redundant computations. This category highlights how dynamic programming can optimize sequential decision-making problems where each action affects future choices and overall profit.


## 1️⃣ Best Time to Buy and Sell Stock

### 📌 Problem Statement

You are given:

* `prices` → an array where `prices[i]` represents the stock price on day `i`

👉 You may choose:

1. One day to buy a stock
2. A later day to sell the stock

👉 Return the maximum profit possible.

If no profit can be made, return `0`.

---

### 🚀 Approach: Greedy

#### 🔹 Key Idea

To maximize profit:

* Keep track of the minimum stock price seen so far.
* For each day, calculate the profit if the stock is sold on that day.
* Update the maximum profit whenever a better profit is found.

So:

```text id="relation"
profit = max(
    profit,
    current_price - minimum_price_so_far
)
```

---

### 🧠 Algorithm

1. Initialize:

   * `mini = prices[0]`
   * `profit = 0`

2. Traverse the array

3. For each price:

   * Calculate potential profit
   * Update maximum profit
   * Update minimum price seen so far

4. Return maximum profit

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
prices = [7,1,5,3,6,4]

Output:
5
```

---

### 🔍 Dry Run

```text id="dryrun"
prices = [7,1,5,3,6,4]

mini = 7
profit = 0

Day 2:
mini = 1

Day 3:
profit = max(0, 5-1) = 4

Day 4:
profit = max(4, 3-1) = 4

Day 5:
profit = max(4, 6-1) = 5

Day 6:
profit = max(5, 4-1) = 5

Answer = 5
```

---

### 🌳 Visualization

```text id="visual"
Prices:

7   1   5   3   6   4
    ↑           ↑
   Buy        Sell

Profit = 6 - 1 = 5
```

---

### ✅ Key Points

* Classic greedy optimization problem
* Track minimum price seen so far
* Calculate profit at each step
* Single pass through the array

---

### ⚠️ Edge Cases

* Single day price
* Strictly decreasing prices
* All prices equal
* Large input arrays

---

### 🏁 Conclusion

This problem demonstrates how a greedy approach efficiently finds the maximum profit by continuously tracking the lowest buying price and evaluating the best selling opportunity in a single traversal.


---


## 2️⃣ Best Time to Buy and Sell Stock II

### 📌 Problem Statement

You are given:

* `prices` → an array where `prices[i]` represents the stock price on day `i`

👉 You may complete as many transactions as you like.

Rules:

* You can buy and sell multiple times.
* You must sell before buying again.

👉 Return the maximum profit that can be achieved.

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

For each day, we maintain two states:

* **Buy State (`buy = 1`)**

  * We are allowed to buy a stock.

* **Sell State (`buy = 0`)**

  * We currently hold a stock and can sell it.

For every day:

```text id="relation"
Buy State:

max(
    -price + next_sell_state,
    skip
)

Sell State:

max(
    price + next_buy_state,
    skip
)
```

The answer starts from day `0` in the buy state.

---

### 🧠 Algorithm

1. Initialize DP states for the future day.

2. Traverse days from right to left.

3. For each day:

   * Compute profit if buying or skipping.
   * Compute profit if selling or holding.

4. Store results in space-optimized arrays.

5. Return profit from day `0` when buying is allowed.

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
prices = [7,1,5,3,6,4]

Output:
7
```

---

### 🔍 Dry Run

```text id="dryrun"
prices = [7,1,5,3,6,4]

Buy at 1
Sell at 5
Profit = 4

Buy at 3
Sell at 6
Profit = 3

Total Profit = 7
```

---

### 🌳 Visualization

```text id="visual"
Prices:

7   1   5   3   6   4
    ↑   ↑
   Buy Sell

            ↑   ↑
           Buy Sell

Profit:
(5 - 1) + (6 - 3)
= 4 + 3
= 7
```

---

### ✅ Key Points

* Unlimited transactions allowed
* Cannot hold more than one stock at a time
* DP state tracks buy/sell decisions
* Space optimization reduces memory usage to O(1)

---

### ⚠️ Edge Cases

* Single day price
* Strictly decreasing prices
* Constant prices
* Large input arrays

---

### 🏁 Conclusion

This problem demonstrates how dynamic programming can model trading decisions using buy and sell states, allowing us to compute the maximum profit across unlimited transactions while respecting transaction constraints.
