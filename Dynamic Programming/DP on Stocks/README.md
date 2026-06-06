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


---


## 3️⃣ Best Time to Buy and Sell Stock with Transaction Fee

### 📌 Problem Statement

You are given:

* `prices` → an array where `prices[i]` represents the stock price on day `i`
* `fee` → transaction fee charged for every completed sale

👉 You may complete as many transactions as you like.

Rules:

* You can buy and sell multiple times.
* You must sell before buying again.
* Every sale incurs a transaction fee.

👉 Return the maximum profit that can be achieved.

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

For each day, we maintain two states:

* **Buy State (`buy = 1`)**

  * We are allowed to buy a stock.

* **Sell State (`buy = 0`)**

  * We currently hold a stock and can sell it.

When selling, the transaction fee is deducted from the profit.

State transitions:

```text id="relation"
Buy State:

max(
    -prices[i] + next_sell_state,
    next_buy_state
)

Sell State:

max(
    prices[i] - fee + next_buy_state,
    next_sell_state
)
```

---

### 🧠 Algorithm

1. Initialize DP states for future days as `0`.

2. Traverse the price array from right to left.

3. For each day:

   * Compute maximum profit for buying or skipping.
   * Compute maximum profit for selling (with fee) or holding.

4. Store results using space optimization.

5. Return profit from day `0` in the buy state.

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
prices = [1,3,2,8,4,9]
fee = 2

Output:
8
```

---

### 🔍 Dry Run

```text id="dryrun"
Buy at 1
Sell at 8

Profit = 8 - 1 - 2
       = 5

Buy at 4
Sell at 9

Profit = 9 - 4 - 2
       = 3

Total Profit = 8
```

---

### 🌳 Visualization

```text id="visual"
Prices:

1   3   2   8   4   9
↑           ↑
Buy        Sell

                ↑   ↑
               Buy Sell

Profit:
(8 - 1 - 2) + (9 - 4 - 2)
= 5 + 3
= 8
```

---

### ✅ Key Points

* Unlimited transactions allowed
* Every completed sale incurs a fee
* Dynamic Programming tracks buy and sell states
* Fee is deducted only when selling
* Space-optimized implementation uses constant memory

---

### ⚠️ Edge Cases

* Single day price
* Very large transaction fee
* Strictly decreasing prices
* All prices equal

---

### 🏁 Conclusion

This problem extends the classic stock trading DP by introducing a transaction fee. By incorporating the fee into the sell transition, dynamic programming efficiently determines the optimal sequence of buy and sell operations to maximize overall profit.


---


## 4️⃣ Best Time to Buy and Sell Stock with Cooldown

### 📌 Problem Statement

You are given:

* `prices` → an array where `prices[i]` represents the stock price on day `i`

👉 You may complete as many transactions as you like.

Rules:

* You can buy and sell multiple times.
* You must sell before buying again.
* After selling a stock, you cannot buy on the next day (cooldown of 1 day).

👉 Return the maximum profit that can be achieved.

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

For each day, we maintain two states:

* **Buy State (`buy = 1`)**

  * We are allowed to buy a stock.

* **Sell State (`buy = 0`)**

  * We currently hold a stock and can sell it.

The cooldown affects only the sell operation.

After selling on day `i`, the next action can only occur from day `i + 2`.

State transitions:

```text id="relation"
Buy State:

max(
    -prices[i] + dp[i+1][0],
    dp[i+1][1]
)

Sell State:

max(
    prices[i] + dp[i+2][1],
    dp[i+1][0]
)
```

---

### 🧠 Algorithm

1. Maintain DP states for:

   * Current day
   * Next day
   * Day after next

2. Traverse the prices array from right to left.

3. For each day:

   * Compute buy state profit.
   * Compute sell state profit using cooldown transition.

4. Update rolling DP arrays.

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
prices = [1,2,3,0,2]

Output:
3
```

---

### 🔍 Dry Run

```text id="dryrun"
Day 0:
Buy at 1

Day 2:
Sell at 3
Profit = 2

Cooldown:
Day 3 cannot buy immediately

Day 3:
Buy at 0

Day 4:
Sell at 2
Profit = 2

Maximum achievable profit = 3
```

---

### 🌳 Visualization

```text id="visual"
Prices:

1   2   3   0   2
↑       ↑
Buy    Sell

Cooldown

            ↑   ↑
           Buy Sell

Total Profit = 3
```

---

### ✅ Key Points

* Unlimited transactions allowed
* One-day cooldown after every sale
* DP state tracks buy and sell decisions
* Selling transitions jump to day `i + 2`
* Space optimization reduces memory to O(1)

---

### ⚠️ Edge Cases

* Single day price
* Two-day price array
* Strictly decreasing prices
* Large input arrays

---

### 🏁 Conclusion

This problem extends stock trading dynamic programming by introducing a cooldown constraint. By adjusting the sell transition to skip the next day, DP efficiently models trading decisions and computes the maximum achievable profit while respecting cooldown periods.


---


## 5️⃣ Best Time to Buy and Sell Stock III

### 📌 Problem Statement

You are given:

* `prices` → an array where `prices[i]` represents the stock price on day `i`

👉 You may complete at most **two transactions**.

Rules:

* You can buy and sell multiple times.
* You must sell before buying again.
* A transaction consists of one buy and one sell.

👉 Return the maximum profit that can be achieved.

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

Unlike unlimited transactions, we now have a transaction limit.

We define three DP states:

* `i` → current day
* `buy` → whether we can buy (`1`) or must sell (`0`)
* `count` → remaining transactions

State transitions:

```text id="relation"
Buy State:

max(
    -prices[i] + dp[i+1][0][count],
    dp[i+1][1][count]
)

Sell State:

max(
    prices[i] + dp[i+1][1][count-1],
    dp[i+1][0][count]
)
```

Whenever we sell a stock, one transaction is completed, so the transaction count decreases.

---

### 🧠 Algorithm

1. Create a 3D DP table:

   * `dp[i][buy][count]`

2. Traverse days from right to left.

3. For each day:

   * Compute buy state profit.
   * Compute sell state profit.

4. Reduce transaction count only when selling.

5. Return:

   * `dp[0][1][2]`

---

### 📊 Complexity Analysis

| Type             | Complexity          |
| ---------------- | ------------------- |
| Time Complexity  | O(n × 2 × 2) ≈ O(n) |
| Space Complexity | O(n × 2 × 3) ≈ O(n) |

---

### 📎 Example

```text id="example"
Input:
prices = [3,3,5,0,0,3,1,4]

Output:
6
```

---

### 🔍 Dry Run

```text id="dryrun"
Transaction 1:

Buy at 0
Sell at 3

Profit = 3

Transaction 2:

Buy at 1
Sell at 4

Profit = 3

Total Profit = 6
```

---

### 🌳 Visualization

```text id="visual"
Prices:

3  3  5  0  0  3  1  4
         ↑     ↑
        Buy  Sell

               ↑     ↑
              Buy  Sell

Profit:
3 + 3 = 6
```

---

### ✅ Key Points

* At most two transactions allowed
* DP state includes remaining transaction count
* Transaction count decreases only on selling
* Extension of the classic stock DP pattern

---

### ⚠️ Edge Cases

* Empty prices array
* Single day price
* No profitable transactions
* Strictly decreasing prices

---

### 🏁 Conclusion

This problem extends stock trading dynamic programming by introducing a transaction limit. By tracking the day, buy/sell state, and remaining transactions, DP efficiently explores all valid trading decisions and computes the maximum achievable profit with at most two transactions.


---


## 6️⃣ Best Time to Buy and Sell Stock IV

### 📌 Problem Statement

You are given:

* `prices` → an array where `prices[i]` represents the stock price on day `i`
* `k` → maximum number of transactions allowed

👉 You may complete at most `k` transactions.

Rules:

* You must sell before buying again.
* A transaction consists of one buy and one sell.

👉 Return the maximum profit that can be achieved.

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

To make optimal trading decisions, we track:

* `i` → current day
* `buy` → whether we can buy (`1`) or need to sell (`0`)
* `count` → remaining transactions

For each state, we have two choices:

* Perform the action (buy/sell)
* Skip the current day

State transitions:

```text id="relation"
Buy State:

max(
    -prices[i] + dp[i+1][0][count],
    dp[i+1][1][count]
)

Sell State:

max(
    prices[i] + dp[i+1][1][count-1],
    dp[i+1][0][count]
)
```

A transaction is considered completed only when a stock is sold, so the transaction count decreases during the sell operation.

---

### 🧠 Algorithm

1. Create a DP table:

   * `dp[i][buy][count]`
   * Represents maximum profit starting from day `i`.

2. Initialize base cases:

   * Profit is `0` when no days remain.
   * Profit is `0` when no transactions remain.

3. Traverse days from right to left.

4. For each day:

   * Evaluate buy state.
   * Evaluate sell state.

5. Return:

   * `dp[0][1][k]`

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n × k)   |
| Space Complexity | O(n × k)   |

---

### 📎 Example

```text id="example"
Input:
k = 2
prices = [2,4,1]

Output:
2
```

---

### 🔍 Dry Run

```text id="dryrun"
Day 0:
Buy at 2

Day 1:
Sell at 4

Profit = 2

Transactions Used = 1

Maximum Profit = 2
```

---

### 🌳 Visualization

```text id="visual"
Prices:

2   4   1
↑   ↑
Buy Sell

Profit = 4 - 2 = 2
```

---

### ✅ Key Points

* Generalization of Stock III
* Supports any transaction limit `k`
* Transaction count decreases only when selling
* Uses 3D DP state:

  * Day
  * Buy/Sell state
  * Remaining transactions

---

### ⚠️ Edge Cases

* Empty price array
* `k = 0`
* Single day price
* Strictly decreasing prices
* Very large values of `k`

---

### 🏁 Conclusion

This problem demonstrates a powerful stock trading dynamic programming pattern where the state is extended with the number of remaining transactions. By tracking the day, trading state, and transaction count, DP efficiently computes the maximum achievable profit under a transaction limit.
