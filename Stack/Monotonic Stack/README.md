# Monotonic Stack

## 1️⃣ Next Greater Element I

### 📌 Problem Statement

You are given two arrays:

- `nums1` – a subset of `nums2`
- `nums2` – all **unique elements**

For each element in `nums1`, find the **next greater element** in `nums2`.

> The next greater element of `x` is the first element to the **right of `x` in `nums2`** that is **greater than `x`**.  
If no such element exists, return `-1`.

---

### 📝 Example

#### Input:
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]

#### Output:
    [-1, 3, -1]

---

### 💡 Intuition

We need to efficiently find the next greater element for **every element in `nums2`**, then answer queries for `nums1`.

A **monotonic decreasing stack** helps us:
- Process elements from **right to left**
- Keep track of the next greater element
- Store results in a **hash map** for fast lookup

---

### 🚀 Approach (Monotonic Stack + Hash Map)

1. Traverse `nums2` from right to left
2. Maintain a stack such that elements are **strictly decreasing**
3. Pop elements smaller than or equal to current
4. The stack top gives the next greater element
5. Store result in a map: `value → next greater`
6. Build the final answer using `nums1`

---

### 🧠 Algorithm Steps

- Initialize an empty stack and hash map
- For each element in `nums2` (right → left):
  - Remove smaller elements from stack
  - Map current element to stack top (or `-1`)
  - Push index onto stack
- For each element in `nums1`, fetch result from map

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n + m)  |
| Space Complexity | O(n)  |

Where:

n = len(nums2)

m = len(nums1)

--

### ✅ Key Takeaways

- Use monotonic stacks for next/previous greater problems
- Preprocessing nums2 makes queries efficient
- Hash maps give O(1) lookups


---


## 2️⃣ Next Greater Element II

### 📌 Problem Statement

Given a **circular array** `nums`, return an array `res` where  
`res[i]` is the **next greater element** of `nums[i]`.

- The **next greater element** is the first element **greater than `nums[i]`** when traversing circularly to the right.
- If no such element exists, return `-1` for that position.

### 📝 Example

#### Input
        nums = [1, 2, 1]

#### Output
        [2, -1, 2]

---

### 💡 Intuition

Since the array is **circular**, elements at the end can look ahead to the beginning.

A **monotonic decreasing stack** helps efficiently track the next greater elements by:
- Traversing the array **twice**
- Simulating circular behavior using modulo (`% n`)

---

### 🚀 Approach (Monotonic Stack + Reverse Traversal)

1. Initialize:
   - `res` array filled with `-1`
   - Empty stack to store indices
2. Traverse from `2n-1` to `0`
3. Use modulo (`i % n`) to wrap around the array
4. Maintain a **strictly decreasing stack**
5. For indices `< n`, store the next greater element if available

---

### 🧠 Algorithm Steps

- Loop from `2n-1` to `0`
- Pop elements from stack while they are `<= current element`
- If index `< n`:
  - Stack top gives the next greater element
- Push current index onto stack

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Each element is pushed and popped at most once.

---

### ✅ Key Takeaways

- Circular array → iterate twice
- Use modulo (%) to simulate circular indexing
- Monotonic stack makes the solution optimal


---


## 3️⃣ Daily Temperatures

### 📌 Problem Statement

You are given an array `temperatures` where  
`temperatures[i]` represents the temperature on day `i`.

For each day, return how many days you would have to wait until a **warmer temperature**.
- If there is no future day for which this is possible, return `0`.

---

### 📝 Example

#### Input:
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

#### Output:
    [1, 1, 4, 2, 1, 1, 0, 0]

---

### 💡 Intuition

For each day, we need to find the **next day with a higher temperature**.

A **monotonic decreasing stack** (based on temperatures) allows us to:
- Track unresolved days
- Efficiently compute the number of days until a warmer temperature

---

### 🚀 Approach (Monotonic Stack)

1. Traverse the array from **left to right**
2. Maintain a stack of indices whose temperatures are **not yet resolved**
3. When the current temperature is higher than the stack top:
   - Pop the index
   - Calculate the difference in days
4. Push the current index into the stack

---

### 🧠 Algorithm Steps

- Initialize:
  - `stack` → stores indices
  - `res` → result array filled with `0`
- For each index `i`:
  - While stack is not empty and current temperature is higher:
    - Pop index `ele`
    - Set `res[ele] = i - ele`
  - Push current index onto stack

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Each index is pushed and popped at most once.

---

### ✅ Key Takeaways

- Classic Next Greater Element variation
- Stack stores indices, not values
- Left-to-right traversal fits naturally here


---


## 4️⃣ Stock Span Problem

### 📌 Problem Statement

Design a class `StockSpanner` that collects **daily stock prices** and returns the **stock span** for each new price.

The **stock span** of today’s price is defined as the maximum number of consecutive days (including today) for which the price was **less than or equal to today’s price**.

---

### 📝 Example

#### Input:
    Prices: [100, 80, 60, 70, 60, 75, 85]

#### Output:
    Spans: [1, 1, 1, 2, 1, 4, 6]

---

### 💡 Intuition

For each new price, we need to look back and count how many **previous consecutive prices** were smaller or equal.

A **monotonic decreasing stack** helps by:
- Removing irrelevant smaller prices
- Jumping directly to the previous greater price
- Achieving optimal performance

---

### 🚀 Approach (Monotonic Stack)

- Maintain a stack storing **(price, index)**
- Stack is always in **decreasing order of price**
- For each new price:
  - Pop all prices smaller than or equal to current
  - Span = current index − index of previous greater price
  - If stack is empty → span = index + 1

---

### 🧠 Algorithm Steps

1. Initialize:
   - Empty stack
   - Index = -1
2. For each `next(price)` call:
   - Increment index
   - Pop all elements with price ≤ current price
   - If stack is not empty:
     - Span = current index − stack top index
   - Else:
     - Span = current index + 1
   - Push `(price, index)` onto stack

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(1) amortized  |
| Space Complexity | O(n)  |

Each price is pushed and popped at most once.

---

### ✅ Key Takeaways

- Classic monotonic stack application
- Stack stores both value and index
- Efficient handling of consecutive elements


---


## 5️⃣ Largest Rectangle in Histogram

### 📌 Problem Statement

You are given an array `heights` where  
`heights[i]` represents the height of a histogram bar with width `1`.

Find the **area of the largest rectangle** that can be formed within the histogram.

---

### 📝 Example

#### Input
    heights = [2, 1, 5, 6, 2, 3]

#### Output
    10

The largest rectangle is formed by bars of height `5` and `6`.

---

### 💡 Intuition

For each bar, consider it as the **minimum height** of a rectangle and try to expand:
- Left until a smaller bar appears (PSE – Previous Smaller Element)
- Right until a smaller bar appears (NSE – Next Smaller Element)

A **monotonic increasing stack** helps find these boundaries efficiently.

---

### 🚀 Approach (Monotonic Increasing Stack)

- Maintain a stack of indices with **increasing heights**
- When a smaller height is found:
  - Pop elements from stack
  - Calculate area using the popped bar as the smallest height
- After traversal, process remaining bars in the stack

---

### 🧠 Algorithm Steps

1. Traverse all bars from left to right
2. While stack top height is greater than current:
   - Pop index `ele`
   - Set `nse = current index`
   - Set `pse = stack top or -1`
   - Calculate area:  
     `height[ele] * (nse - pse - 1)`
3. Push current index onto stack
4. After loop, repeat area calculation for remaining stack elements with `nse = n`

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Each bar is pushed and popped once.

---

### ✅ Key Takeaways

- Use Previous Smaller Element (PSE) and Next Smaller Element (NSE)
- Monotonic stack converts brute force O(n²) → O(n)
- Fundamental problem for advanced stack patterns


---


## 6️⃣ Maximal Rectangle (Binary Matrix)

### 📌 Problem Statement

You are given a **binary matrix** filled with `'0'`s and `'1'`s.  
Find the **largest rectangle containing only `1`s** and return its area.

---

### 📝 Example

#### Input:
    matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
    ]

#### Output:
    6

The maximal rectangle has area **6**.

---

### 💡 Intuition

This problem is an extension of the **Largest Rectangle in Histogram**.

For each row:
- Treat the row as the **base of a histogram**
- Build heights by counting consecutive `1`s vertically
- Compute the largest rectangle area for that histogram

The maximum over all rows is the answer.

---

### 🚀 Approach (Histogram + Monotonic Stack)

#### Step 1: Build Height Matrix
- Convert matrix values to integers
- For each column, accumulate heights of consecutive `1`s

#### Step 2: Largest Rectangle in Histogram
- For each row (histogram):
  - Use a **monotonic increasing stack**
  - Find Previous Smaller Element (PSE) and Next Smaller Element (NSE)
  - Compute maximum rectangle area

---

### 🧠 Algorithm Steps

1. Convert binary matrix to integer matrix
2. Build prefix heights column-wise
3. For each row:
   - Apply Largest Rectangle in Histogram algorithm
4. Track the global maximum area

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(m*n)  |
| Space Complexity | O(n)  |

Where:

m = number of rows

n = number of columns

---

### ✅ Key Takeaways

- Powerful combination of 2D → 1D transformation
- Reuses Largest Rectangle in Histogram
- Monotonic stack enables optimal performance


---


## 7️⃣ Asteroid Collision

### 📌 Problem Statement

You are given an array `asteroids` where:
- Each value represents the **size** of an asteroid
- The **sign** represents the direction  
  - Positive → moving right  
  - Negative → moving left  

When two asteroids collide:
- The **smaller one explodes**
- If both are the same size, **both explode**
- Asteroids moving in the same direction never collide

Return the state of the asteroids after all collisions.

---

### 📝 Example

#### Input:
    asteroids = [5, 10, -5]

#### Output:
    [5, 10]

---

### 💡 Intuition

Collisions only happen when:
- A **right-moving asteroid** meets a **left-moving asteroid**

A **stack** is ideal to simulate collisions because:
- It keeps track of active asteroids
- The most recent asteroid is the first to collide

---

### 🚀 Approach (Stack Simulation)

1. Traverse each asteroid:
   - If moving right (`> 0`), push onto stack
   - If moving left (`< 0`), resolve collisions:
     - Pop smaller right-moving asteroids
     - If equal size → both explode
     - If stack is empty or top is moving left → push current asteroid

---

### 🧠 Algorithm Steps

- Initialize an empty stack
- For each asteroid `x`:
  - While stack top is positive and smaller than `|x|`, pop
  - If stack top equals `|x|`, pop and discard current
  - Else if no collision possible, push `x`
- Return the stack

---
### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

Each asteroid is pushed and popped at most once.

---

### ✅ Key Takeaways

- Stack perfectly models real-time collisions
- Only right vs left asteroids interact
- Clean simulation avoids nested loops