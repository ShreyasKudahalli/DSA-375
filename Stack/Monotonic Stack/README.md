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

