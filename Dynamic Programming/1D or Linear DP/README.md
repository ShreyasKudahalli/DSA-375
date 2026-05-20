# 1D or Linear DP

1D or Linear Dynamic Programming focuses on solving problems where the solution at each position depends on a small number of previous states in a sequential manner. These problems are typically optimized by storing intermediate results in a one-dimensional array, allowing efficient reuse of previously computed values instead of recalculating overlapping subproblems. Common patterns include counting ways, maximizing profit, minimizing cost, and making optimal choices across arrays or sequences, making linear DP a foundational technique for problems involving progression, decisions, and state transitions over a single dimension.


## 1️⃣ Climbing Stairs 

### 📌 Problem Statement

You are climbing a staircase.

At each step, you can either:

* climb `1` step, or
* climb `2` steps

👉 Given `n` stairs, return the number of distinct ways to reach the top.

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

To reach stair `i`:

* You can come from:

  * stair `i-1`
  * stair `i-2`

So:

```text id="relation"
dp[i] = dp[i-1] + dp[i-2]
```

👉 This follows the Fibonacci pattern.

---

### 🧠 Algorithm

1. Handle small cases:

   * `n <= 2`

2. Create DP array:

   * `dp[i]` stores ways to reach stair `i`

3. Initialize:

   * `dp[1] = 1`
   * `dp[2] = 2`

4. Build solution iteratively:

   * `dp[i] = dp[i-1] + dp[i-2]`

5. Return `dp[n]`

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

Output:
8
```

---

### 🔍 Dry Run

```text id="dryrun"
dp[1] = 1
dp[2] = 2

dp[3] = 3
dp[4] = 5
dp[5] = 8
```

---

### 🌳 Visualization

```text id="visual"
Step 5 can be reached from:
Step 4 + Step 3

Ways:
5 + 3 = 8
```

---

### ✅ Key Points

* Classic dynamic programming problem
* Uses previous two states only
* Fibonacci-style recurrence relation
* Efficient bottom-up computation

---

### ⚠️ Edge Cases

* `n = 1`
* `n = 2`
* Large `n`

---

### 🏁 Conclusion

This problem demonstrates how dynamic programming can efficiently solve counting problems by building solutions from previously computed subproblems.


---


## 2️⃣ House Robber

### 📌 Problem Statement

You are given:

* `nums` → amount of money in each house

👉 You cannot rob two adjacent houses because of the security system.

👉 Return the maximum amount of money you can rob without alerting the police.

---

### 🚀 Approach: Dynamic Programming

#### 🔹 Key Idea

For each house:

You have two choices:

1. Skip current house
2. Rob current house and add value from `i-2`

So:

```text id="relation"
dp[i] = max(
    dp[i-1],
    dp[i-2] + nums[i]
)
```

---

### 🧠 Algorithm

1. Handle small cases:

   * `n <= 2`

2. Create DP array:

   * `dp[i]` → maximum money robbed till index `i`

3. Initialize:

   * `dp[0] = nums[0]`
   * `dp[1] = max(nums[0], nums[1])`

4. Traverse remaining houses:

   * Either skip or rob current house

5. Return final maximum amount

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
nums = [2,7,9,3,1]

Output:
12
```

---

### 🔍 Dry Run

```text id="dryrun"
nums = [2,7,9,3,1]

dp[0] = 2
dp[1] = 7

dp[2] = max(7, 2+9) = 11
dp[3] = max(11, 7+3) = 11
dp[4] = max(11, 11+1) = 12
```

---

### 🌳 Visualization

```text id="visual"
House Values:
[2] [7] [9] [3] [1]

Rob:
2 + 9 + 1 = 12
```

---

### ✅ Key Points

* Classic include/exclude DP problem
* Adjacent houses cannot both be chosen
* Transition uses previous two states
* Similar to maximum non-adjacent sum problems

---

### ⚠️ Edge Cases

* Single house
* Two houses
* All houses same value
* Large input arrays

---

### 🏁 Conclusion

This problem demonstrates how dynamic programming efficiently handles optimization under adjacency constraints by choosing between robbing or skipping each house.


---