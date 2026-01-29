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


---


## 5️⃣ Median of a Row-wise Sorted Matrix

### 📌 Problem Statement

Given a matrix `mat` of size `n x m` where **each row is sorted in non-decreasing order**, find the **median** of the matrix.

- The total number of elements (`n * m`) is **odd**
- The median is the element that has exactly half of the elements less than or equal to it

---

### 💡 Approach: Binary Search on Answer

Instead of flattening and sorting the matrix (which is inefficient), we apply **Binary Search on the value range** of the matrix.

For any guessed value `x`, we count how many elements in the matrix are **strictly less than `x`**.  
Based on this count, we adjust our search range.

---

#### 🧠 Key Observations

- Each row is already sorted → we can use **binary search (upper bound)** on each row
- Minimum possible median = smallest element in the matrix
- Maximum possible median = largest element in the matrix
- If count of elements `< x` is `<= (n*m)//2`, then `x` can be a valid median candidate

---

### 🧩 Algorithm

1. Set search range:
   - `low = min(first element of each row)`
   - `high = max(last element of each row)`
2. For each `mid`:
   - Count elements less than `mid` using upper bound in each row
3. If count `<= (n*m)//2`, move right
4. Else, move left
5. Final `low` gives the median

---

### 🧪 Example

#### Input
      mat = [
      [1, 3, 5],
      [2, 6, 9],
      [3, 6, 9]
      ]

#### Output
      5

#### Explanation
Sorted elements → [1,2,3,3,5,6,6,9,9]

Median → 5

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n log m log V)  |
| Space Complexity | O(1)  |

Where:

n = number of rows

m = number of columns

V = range of matrix values

---

### ✅ Key Takeaways

- Efficient use of Binary Search on Answer
- Leverages row-wise sorted property
- Avoids extra space and full sorting
- Common interview & competitive programming problem


---


## 6️⃣ Aggressive Cows

### 📌 Problem Statement

You are given an array `stalls` representing the positions of stalls along a line and an integer `k` representing the number of cows.

You need to place **`k` cows in the stalls** such that the **minimum distance between any two cows is maximized**.

Return the **largest minimum distance** possible.

---

### 💡 Approach: Binary Search on Answer

This problem is a classic example of **Binary Search on Answer**.

#### Key Idea:
- The answer lies between `0` and `max(stalls) - min(stalls)`
- For a given distance `d`, check whether it is possible to place all cows such that the minimum distance between them is at least `d`
- Use binary search to find the maximum feasible distance

---

### 🧠 Algorithm

1. Sort the stall positions.
2. Initialize:
   - `low = 0`
   - `high = stalls[-1] - stalls[0]`
3. Define a helper function `possible(dist)`:
   - Place the first cow in the first stall
   - Place remaining cows in the next possible stalls maintaining at least `dist` distance
   - Return `True` if all cows can be placed, otherwise `False`
4. Apply binary search:
   - If placement is possible, try a larger distance
   - Otherwise, reduce the distance
5. Return the maximum valid distance

---

### 🧪 Example

#### Input
      stalls = [1, 2, 4, 8, 9]
      k = 3

#### Output
      3

#### Explanation
Cows can be placed at positions 1, 4, and 8
Minimum distance = 3 (maximum possible)

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n log D)  |
| Space Complexity | O(1)  |

Where:

n = number of stalls

D = distance between the first and last stall

--

### ✅ Key Notes

- Stalls must be sorted
- Uses greedy placement with binary search
- Maximizes the minimum distance
- Very popular interview problem


---


## 7️⃣ Minimum Days to Make `m` Bouquets

### 📌 Problem Statement

You are given an integer array `bloomDay`, where `bloomDay[i]` represents the day the `iᵗʰ` flower blooms.  
To make **one bouquet**, you need **`k` adjacent flowers** that have all bloomed.  
Find the **minimum number of days** required to make **`m` bouquets**.

If it is **not possible**, return `-1`.

---

### 💡 Approach: Binary Search on Answer

This problem uses **Binary Search on Answers**, where we search over the range of days instead of indices.  
For a given day, we check whether it is possible to form at least `m` bouquets.

---

#### 🧠 Key Observations

- If `len(bloomDay) < m * k`, it is impossible to form `m` bouquets
- Minimum possible day → `min(bloomDay)`
- Maximum possible day → `max(bloomDay)`
- For a chosen day:
  - Count consecutive flowers bloomed on or before that day
  - Every `k` consecutive flowers form one bouquet

---

### 🧩 Algorithm

1. Check if total flowers are sufficient; if not, return `-1`
2. Set binary search range from minimum to maximum bloom day
3. For each mid-day:
   - Count how many bouquets can be formed
4. If bouquets ≥ `m`, try earlier days
5. Otherwise, increase the day range
6. Return the minimum valid day

---

### 🧪 Example

#### Input
      bloomDay = [1, 10, 3, 10, 2]
      m = 3
      k = 1

#### Output
      3

#### Explanation
By day 3, three flowers have bloomed, allowing the formation of 3 bouquets.

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n log D)  |
| Space Complexity | O(1)  |

Where:

n = number of flowers

D = range of bloom days

---

### ✅ Key Takeaways

- Classic Binary Search on Answer problem
- Efficient for large inputs
- Uses greedy counting with feasibility check
- Frequently asked in coding interviews


---


## 8️⃣ Magnetic Force Between Two Balls

### 📌 Problem Statement

You are given an array `position` representing the positions of baskets on a number line and an integer `m` representing the number of balls to place.  
Place the balls in the baskets such that the **minimum distance between any two balls is maximized**.

Return the **maximum possible minimum distance**.

---

### 💡 Approach: Binary Search on Answer

This problem is a classic example of **Binary Search on Answers** combined with a **greedy feasibility check**.

Instead of trying all distances, we binary search on the possible distance values and check whether it is feasible to place all `m` balls while maintaining at least that distance.

---

#### 🧠 Key Observations

- Positions must be **sorted** to apply greedy placement
- Minimum possible distance → `0`
- Maximum possible distance → `max(position) - min(position)`
- If we can place `m` balls with distance `d`, then we can also place them with any smaller distance

---

### 🧩 Algorithm

1. Sort the `position` array
2. Set binary search range:
   - `low = 0`
   - `high = position[-1] - position[0]`
3. For each `mid` distance:
   - Try placing balls greedily from left to right
4. If placement is possible, try a larger distance
5. Otherwise, reduce the distance
6. Return the largest feasible distance

---

### 🧪 Example

#### Input
      position = [1, 2, 3, 4, 7]
      m = 3

#### Output
      3

#### Explanation
Place balls at positions 1, 4, and 7

Minimum distance = 3

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n log D)  |
| Space Complexity | O(1)  |

Where:

n = number of baskets

D = range of distances

---

### ✅ Key Takeaways

- Uses Binary Search on Answer
- Greedy placement ensures feasibility
- Efficient for large inputs
- Commonly asked interview problem


---


## 9️⃣ Allocate Minimum Number of Pages

### 📌 Problem Statement

You are given an array `arr` where each element represents the number of pages in a book.  
There are `k` students, and the books must be allocated **contiguously** to students.

Your task is to allocate the books such that the **maximum number of pages assigned to any student is minimized**.

If it is not possible to allocate books to all students, return `-1`.

---

### 💡 Approach: Binary Search on Answer

This is a classic **Binary Search on Answers** problem where we search for the minimum possible value of the maximum pages a student can get.

For a chosen value `pages`, we check whether it is possible to allocate the books among `k` students without exceeding this limit.

---

#### 🧠 Key Observations

- Each student must get **at least one book**
- If number of books `< k`, allocation is impossible
- Minimum possible pages = `max(arr)`
- Maximum possible pages = `sum(arr)`
- If allocation is possible with `X` pages, it is also possible with any value greater than `X`

---

### 🧩 Algorithm

1. If `len(arr) < k`, return `-1`
2. Set binary search range:
   - `low = max(arr)`
   - `high = sum(arr)`
3. For each `mid`:
   - Try assigning books sequentially
   - If pages exceed `mid`, assign books to next student
4. If number of students used ≤ `k`, try a smaller value
5. Otherwise, increase the value
6. Return the minimum valid number of pages

---

### 🧪 Example

#### Input
      arr = [12, 34, 67, 90]
      k = 2

#### Output
      113

#### Explanation

Student 1 → [12, 34, 67] → 113 pages

Student 2 → [90] → 90 pages

Maximum pages minimized to 113

---

### ⏱️ Complexity Analysis
| Metric            | Value |
|------------------|-------|
| Time Complexity  | O(n log S)  |
| Space Complexity | O(1)  |

Where:

n = number of books

S = sum of pages

---

### ✅ Key Takeaways

- Classic Binary Search on Answer problem
- Greedy allocation with feasibility check
- Contiguous allocation is mandatory
- Frequently asked in interviews and exams