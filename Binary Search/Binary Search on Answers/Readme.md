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