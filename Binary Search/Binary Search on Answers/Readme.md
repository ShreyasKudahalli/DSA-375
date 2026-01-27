# Binary Search on Answers
Binary Search on Answers is a powerful optimization technique where binary search is applied not on array indices but on a range of possible values, systematically narrowing down the minimum or maximum feasible solution by checking a condition at each step, and is commonly used in problems involving minimization or maximization under constraints, achieving efficient solutions in O(log range) time.

## 1️⃣ Split Array Largest Sum

### 📌 Problem Statement

Given an array `nums` and an integer `k`, split the array into **`k` or fewer non-empty continuous subarrays** such that the **largest subarray sum is minimized**.

Return the **minimum possible value** of the largest subarray sum.

---

### 💡 Approach: Binary Search on Answer

Instead of trying all possible splits, we apply **Binary Search on the answer**.

#### Search Space:
- **Minimum possible sum** = `max(nums)`  
  (since at least one subarray must contain the largest element)
- **Maximum possible sum** = `sum(nums)`  
  (when the entire array is one subarray)

For a given maximum allowed sum, we check whether the array can be split into at most `k` subarrays.

---

### 🧠 Algorithm

1. Initialize:
   - `low = max(nums)`
   - `high = sum(nums)`
2. Define a helper function `canSplit(maxSum)`:
   - Traverse the array and form subarrays
   - Start a new subarray when adding an element exceeds `maxSum`
   - Count total subarrays formed
   - Return `True` if subarrays ≤ `k`
3. Apply binary search:
   - If splitting is possible, try a smaller maximum sum
   - Otherwise, increase the allowed sum
4. Return `low` as the minimum largest subarray sum

---

### 🧪 Example

#### Input
    nums = [7, 2, 5, 10, 8]
    k = 2

#### Output
    18

#### Explanation
Split into [7, 2, 5] and [10, 8]
Largest sum = 18 (minimum possible)

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n log S)  |
| Space Complexity | O(1)  |

Where:

n = length of the array

S = sum of all elements

---

### ✅ Key Notes

- Classic Binary Search on Answer problem
- Uses greedy validation for feasibility
- Guarantees optimal solution
- Frequently asked in interviews


---


## 2️⃣ Koko Eating Bananas 

### 📌 Problem Statement

Koko loves to eat bananas. There are `n` piles of bananas, where the `i-th` pile has `piles[i]` bananas.  
Koko can decide her **eating speed `k`** (bananas per hour).

Each hour, she eats **up to `k` bananas from a single pile**.  
If a pile has fewer than `k` bananas, she eats the entire pile and does not eat more bananas in that hour.

Given an integer `h`, return the **minimum integer eating speed `k`** such that Koko can eat all the bananas within `h` hours.

---

### 💡 Approach: Binary Search on Answer

Instead of checking every possible eating speed, we apply **Binary Search on the range of possible speeds**.

#### Search Space:
- Minimum speed = `1`
- Maximum speed = `max(piles)`

For a given speed `k`, we check whether Koko can finish all bananas within `h` hours.

---

### 🧠 Algorithm

1. Initialize:
   - `low = 1`
   - `high = max(piles)`
2. Define a helper function to check feasibility:
   - Calculate total hours needed to eat all piles at speed `k`
   - If total hours ≤ `h`, the speed is valid
3. Apply binary search:
   - If current speed is valid, try a smaller speed
   - Otherwise, increase the speed
4. Return the minimum valid speed

---

### 🧪 Example

#### Input
    piles = [3, 6, 7, 11]
    h = 8

#### Output
    4

#### Explanation
At speed 4 bananas/hour, Koko can finish all piles within 8 hours.

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n log m)  |
| Space Complexity | O(1)  |

Where:

n = number of piles

m = maximum bananas in a pile

---

### ✅ Key Notes

- Classic example of Binary Search on Answer
- Search space is numeric, not index-based
- Efficient for large inputs
- Frequently asked interview problem


---


## 3️⃣ Capacity To Ship Packages Within D Days

### 📌 Problem Statement

You are given an array `weights` where `weights[i]` represents the weight of the `i-th` package.  
You are also given an integer `days`, representing the number of days within which all packages must be shipped.

Each day, the ship can carry packages **in order** with a total weight **not exceeding its capacity**.

Return the **minimum ship capacity** required to ship all packages within `days`.

---

### 💡 Approach: Binary Search on Answer

This is a classic **Binary Search on Answer** problem.

#### Search Space:
- **Minimum capacity** = `max(weights)`  
  (a ship must at least carry the heaviest package)
- **Maximum capacity** = `sum(weights)`  
  (carry all packages in one day)

For a given ship capacity, we check whether it is possible to ship all packages within the given number of days.

---

### 🧠 Algorithm

1. Initialize:
   - `low = max(weights)`
   - `high = sum(weights)`
2. Define a helper function `possible(capacity)`:
   - Simulate shipping packages day by day
   - Start a new day if current load exceeds capacity
   - Count total days required
   - Return `True` if days required ≤ `days`
3. Apply binary search:
   - If capacity is sufficient, try a smaller capacity
   - Otherwise, increase the capacity
4. Return `low` as the minimum valid capacity

---

### 🧪 Example

#### Input
      weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  days = 5

#### Output
      15

#### Explanation
Minimum capacity to ship all packages in 5 days is 15

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n log S)  |
| Space Complexity | O(1)  |

Where:

n = number of packages

S = sum of all weights

---

### ✅ Key Notes

- Packages must be shipped in order
- Capacity is minimized using binary search
- Greedy check ensures feasibility
- Very common interview problem


---


## 4️⃣ Minimum Speed to Arrive on Time

### 📌 Problem Statement

You are given an array `dist` where `dist[i]` represents the distance of the `i-th` train ride.  
You are also given a floating-point number `hour` representing the total time available.

You must choose a **constant integer speed** such that you can travel all distances **in order** and arrive within `hour`.

- For all rides except the last one, travel time is **rounded up** to the nearest integer.
- The last ride can take **fractional time**.

Return the **minimum speed** required to arrive on time.  
If it is not possible, return **`-1`**.

---

### 💡 Approach: Binary Search on Answer

This is a classic **Binary Search on Answer** problem.

#### Search Space:
- **Minimum speed** = `1`
- **Maximum speed** = `10⁷` (given by constraints)

For a given speed, we check whether the total travel time is within the allowed `hour`.

---

### 🧠 Algorithm

1. Initialize:
   - `low = 1`
   - `high = 10^7`
   - `ans = -1`
2. Define a helper function `possible(speed)`:
   - For each segment except the last, add `ceil(dist[i] / speed)`
   - For the last segment, add exact division
   - Check if total time ≤ `hour`
3. Apply binary search:
   - If current speed is sufficient, update answer and try a smaller speed
   - Otherwise, increase the speed
4. Return `ans`

---

### 🧪 Example

#### Input
      dist = [1, 3, 2],  hour = 2.7

#### Output
      3

#### Explanation
At speed 3, total travel time = ceil(1/3) + ceil(3/3) + (2/3)
= 1 + 1 + 0.67 = 2.67 ≤ 2.7

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n log M)  |
| Space Complexity | O(1)  |

Where:

n = number of distances

M = maximum possible speed (10^7)

---

### ✅ Key Notes

- Uses Binary Search on Answer
- Rounding rule applies only to intermediate segments
- Speed must be an integer
- If no valid speed exists, return -1