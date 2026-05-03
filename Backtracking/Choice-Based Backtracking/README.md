# Choice-based backtracking

Choice-based backtracking is a recursive problem-solving technique where, at each step, you make a decision among multiple possible choices (such as include/exclude, pick/skip, or try all options) and explore all resulting paths systematically. By building solutions incrementally and backtracking (undoing choices) when needed, it efficiently traverses the decision space to generate all valid combinations, permutations, or configurations, making it a powerful approach for combinatorial problems.


## 1️⃣ Subsets (Power Set) – Backtracking Approach

### 📌 Problem Statement

You are given:

* `nums` → a list of **distinct integers**

👉 Return **all possible subsets** (the power set)

#### 🎯 Constraints:

* Each element can either be **included or excluded**
* No duplicate subsets allowed

---

### 🚀 Approach: Backtracking

#### 🔹 Key Idea

* At each index, you have **two choices**:

  1. Include the element
  2. Exclude the element

👉 This creates a decision tree of size `2^n`

---

### 🧠 Algorithm

1. Start from index `0` with an empty subset

2. For each element:

   * Include it → move to next index
   * Exclude it → move to next index

3. When you reach the end:

   * Add the current subset to result

---

### 📊 Complexity Analysis

| Type             | Complexity             |
| ---------------- | ---------------------- |
| Time Complexity  | O(2ⁿ × n)              |
| Space Complexity | O(n) (recursion stack) |

---

### 📎 Example

```text id="example"
Input:
nums = [1,2,3]

Output:
[
 [],
 [1],
 [2],
 [1,2],
 [3],
 [1,3],
 [2,3],
 [1,2,3]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Start:
[]

Include 1 → [1]
Include 2 → [1,2]
Include 3 → [1,2,3]

Backtrack and explore all combinations ✔️
```

---

### 🌳 Recursion Tree

```text id="tree"
                []
           /           \
        [1]             []
      /     \        /     \
  [1,2]    [1]    [2]      []
   ...      ...    ...      ...
```

---

### ✅ Key Points

* Classic **Backtracking problem**
* Generates **power set (2ⁿ subsets)**
* Uses **include/exclude pattern**
* Ensures no duplicates (since input is distinct)

---

### ⚠️ Edge Cases

* Empty input → `[[]]`
* Single element
* Large input (exponential growth)

---

### 🏁 Conclusion

Backtracking provides a clean and intuitive way to generate all subsets by exploring every possible combination, making it a foundational pattern for many combinatorial problems.


---


## 2️⃣ Subsets II – Handling Duplicates (Backtracking)

### 📌 Problem Statement

You are given:

* `nums` → a list of integers (may contain duplicates)

👉 Return **all possible unique subsets** (the power set)

#### 🎯 Constraints:

* Subsets must be **unique**
* Order of subsets does not matter

---

### 🚀 Approach: Backtracking + Sorting

#### 🔹 Key Idea

* Sort the array to bring duplicates together
* Skip duplicate elements during recursion

👉 Avoid generating duplicate subsets by checking:

```
if i > start and nums[i] == nums[i-1]:
    continue
```

---

### 🧠 Algorithm

1. Sort the input array

2. Start backtracking from index `0`

3. At each step:

   * Add current combination to result
   * Iterate through remaining elements

4. Skip duplicates:

   * If current element is same as previous and not the first in loop → skip

5. Continue recursion

---

### 📊 Complexity Analysis

| Type             | Complexity             |
| ---------------- | ---------------------- |
| Time Complexity  | O(2ⁿ) (worst case)     |
| Space Complexity | O(n) (recursion stack) |

---

### 📎 Example

```text id="example"
Input:
nums = [1,2,2]

Output:
[
 [],
 [1],
 [1,2],
 [1,2,2],
 [2],
 [2,2]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Sorted nums = [1,2,2]

Start:
[]

Include 1 → [1]
Include 2 → [1,2]
Include 2 → [1,2,2]

Backtrack:
Skip duplicate 2 at same level ✔️
```

---

### 🌳 Recursion Tree (Simplified)

```text id="tree"
        []
     /   |   \
   [1]  [2]  (skip duplicate)
   / \    \
[1,2] [1]  [2,2]
```

---

### ✅ Key Points

* Sorting helps **group duplicates**
* Skip duplicates using **index check**
* Generates **unique subsets only**
* Efficient pruning avoids redundant work

---

### ⚠️ Edge Cases

* Empty input → `[[]]`
* All elements same → limited subsets
* Large input → exponential growth

---

### 🏁 Conclusion

This approach efficiently generates all unique subsets by combining backtracking with smart duplicate handling, making it a common pattern for problems involving combinations with repeated elements.


---


## 3️⃣ Combination Sum 

### 📌 Problem Statement

You are given:

* `candidates` → a list of **distinct integers**
* `target` → a target sum

👉 Find all **unique combinations** where the chosen numbers sum to `target`

#### 🎯 Constraints:

* You can use the **same number multiple times**
* Combinations must be **unique**
* Order of elements inside a combination does not matter

---

### 🚀 Approach: Backtracking (Choice-Based)

#### 🔹 Key Idea

* At each index, you can:

  * Pick the element (stay at same index → reuse allowed)
  * Move forward to explore other elements

👉 Stop when:

* Sum equals target → valid combination
* Sum exceeds target → prune branch

---

### 🧠 Algorithm

1. Start from index `0` with:

   * `current_sum = 0`
   * `combination = []`

2. For each index:

   * Add element to combination
   * Recurse with same index (allow reuse)
   * Backtrack (remove element)

3. Base Cases:

   * If `sum == target` → store result
   * If `sum > target` → stop

---

### 📊 Complexity Analysis

| Type             | Complexity             |
| ---------------- | ---------------------- |
| Time Complexity  | O(2^T) (exponential)   |
| Space Complexity | O(T) (recursion depth) |

> `T` = target value (approximate bound)

---

### 📎 Example

```text id="example"
Input:
candidates = [2,3,6,7]
target = 7

Output:
[
 [2,2,3],
 [7]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Start:
[]

→ Pick 2 → [2]
→ Pick 2 → [2,2]
→ Pick 3 → [2,2,3] ✔️

Backtrack

→ Pick 7 → [7] ✔️
```

---

### 🌳 Recursion Tree (Simplified)

```text id="tree"
            []
        /    |    \
      [2]   [3]   [6]
     /  \
 [2,2]  [2,3]
   |
[2,2,3] ✔️
```

---

### ✅ Key Points

* Classic **backtracking + recursion**
* Allows **repetition of elements**
* Uses **pruning for efficiency**
* Explores combinations, not permutations

---

### ⚠️ Edge Cases

* No combination possible → return `[]`
* Single element equals target
* Large target → deep recursion
* Candidates contain large values

---

### 🏁 Conclusion

Combination Sum is a foundational backtracking problem that demonstrates how to explore combinations with repetition while efficiently pruning invalid paths.


---


## 4️⃣ Combination Sum 2

### 📌 Problem Statement

You are given:

* `candidates` → a list of **distinct integers**
* `target` → a target sum

👉 Find all **unique combinations** where the chosen numbers sum to `target`

#### 🎯 Constraints:

* You can use the **same number multiple times**
* Combinations must be **unique**
* Order of elements inside a combination does not matter

---

### 🚀 Approach: Backtracking (Choice-Based)

#### 🔹 Key Idea

* At each index, you can:

  * Pick the element (stay at same index → reuse allowed)
  * Move forward to explore other elements

👉 Stop when:

* Sum equals target → valid combination
* Sum exceeds target → prune branch

---

### 🧠 Algorithm

1. Start from index `0` with:

   * `current_sum = 0`
   * `combination = []`

2. For each index:

   * Add element to combination
   * Recurse with same index (allow reuse)
   * Backtrack (remove element)

3. Base Cases:

   * If `sum == target` → store result
   * If `sum > target` → stop

---

### 📊 Complexity Analysis

| Type             | Complexity             |
| ---------------- | ---------------------- |
| Time Complexity  | O(2^T) (exponential)   |
| Space Complexity | O(T) (recursion depth) |

> `T` = target value (approximate bound)

---

### 📎 Example

```text id="example"
Input:
candidates = [2,3,6,7]
target = 7

Output:
[
 [2,2,3],
 [7]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Start:
[]

→ Pick 2 → [2]
→ Pick 2 → [2,2]
→ Pick 3 → [2,2,3] ✔️

Backtrack

→ Pick 7 → [7] ✔️
```

---

### 🌳 Recursion Tree (Simplified)

```text id="tree"
            []
        /    |    \
      [2]   [3]   [6]
     /  \
 [2,2]  [2,3]
   |
[2,2,3] ✔️
```

---

### ✅ Key Points

* Classic **backtracking + recursion**
* Allows **repetition of elements**
* Uses **pruning for efficiency**
* Explores combinations, not permutations

---

### ⚠️ Edge Cases

* No combination possible → return `[]`
* Single element equals target
* Large target → deep recursion
* Candidates contain large values

---

### 🏁 Conclusion

Combination Sum is a foundational backtracking problem that demonstrates how to explore combinations with repetition while efficiently pruning invalid paths.


---


## 5️⃣ Permutations

### 📌 Problem Statement

You are given:

* `nums` → a list of **distinct integers**

👉 Return **all possible permutations**

#### 🎯 Constraints:

* Each element must appear **exactly once** in each permutation
* Order **matters**
* All permutations must be **unique**

---

### 🚀 Approach: Backtracking with Visited Set

#### 🔹 Key Idea

* Build permutations step by step
* At each step, pick an element that is **not already used**

👉 Use a `visited` set to track used elements

---

### 🧠 Algorithm

1. Start with:

   * Empty combination `[]`
   * Empty `visited` set

2. For each element in `nums`:

   * If not visited:

     * Add to combination
     * Mark as visited
     * Recurse

3. When combination size == `n`:

   * Add to result

4. Backtrack:

   * Remove element
   * Mark as unvisited

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n! × n)  |
| Space Complexity | O(n)       |

---

#### 📎 Example

```text id="example"
Input:
nums = [1,2,3]

Output:
[
 [1,2,3],
 [1,3,2],
 [2,1,3],
 [2,3,1],
 [3,1,2],
 [3,2,1]
]
```

---

#### 🔍 Dry Run

```text id="dryrun"
Start:
[]

Pick 1 → [1]
Pick 2 → [1,2]
Pick 3 → [1,2,3] ✔️

Backtrack:
Try other combinations ✔️
```

---

#### 🌳 Recursion Tree (Simplified)

```text id="tree"
          []
     /     |     \
   [1]    [2]    [3]
   / \    / \    / \
[1,2]... etc...
```

---

### ✅ Key Points

* Generates **all permutations**
* Uses **visited set to avoid reuse**
* Order matters → different permutations
* Classic **backtracking problem**

---

### ⚠️ Edge Cases

* Empty input → `[]`
* Single element → one permutation
* Large input → factorial growth

---

### 🏁 Conclusion

This approach systematically explores all possible arrangements using backtracking, making it a fundamental technique for permutation-based problems.


---


## 6️⃣ Permutations II 

### 📌 Problem Statement

You are given:

* `nums` → a list of integers (may contain duplicates)

👉 Return **all unique permutations**

#### 🎯 Constraints:

* Each element must be used **exactly once**
* Result must **not contain duplicate permutations**

---

### 🚀 Approach: Backtracking + Sorting + Visited Array

#### 🔹 Key Idea

* Sort the array to group duplicates
* Use a `visited` array to track used elements
* Skip duplicates intelligently

👉 Avoid duplicates using:

```python
if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
    continue
```

---

### 🧠 Algorithm

1. Sort `nums`

2. Initialize:

   * `visited[] = False` for all indices
   * empty `combination`

3. For each index:

   * Skip if already visited
   * Skip duplicates if previous identical element was not used

4. Choose element:

   * Add to combination
   * Mark visited
   * Recurse

5. Backtrack:

   * Remove element
   * Mark unvisited

6. When combination length == `n`:

   * Add to result

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n! × n)  |
| Space Complexity | O(n)       |

---

### 📎 Example

```text id="example"
Input:
nums = [1,1,2]

Output:
[
 [1,1,2],
 [1,2,1],
 [2,1,1]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Sorted nums = [1,1,2]

Start:
[]

Pick first 1 → [1]
Pick second 1 → [1,1]
Pick 2 → [1,1,2] ✔️

Backtrack:
Skip duplicate when previous identical not used ✔️
```

---

### 🌳 Recursion Tree (Simplified)

```text id="tree"
            []
        /     |     
      [1]    [2]
     /   \
 [1,1]  [1,2]
   |       |
[1,1,2]  [1,2,1]
```

---

### ✅ Key Points

* Sorting helps **identify duplicates**
* `visited[]` ensures elements are used once
* Skip condition prevents duplicate permutations
* Classic **backtracking with pruning**

---

### ⚠️ Edge Cases

* All elements same → only one permutation
* Empty array
* Large input → factorial growth

---

### 🏁 Conclusion

This solution efficiently generates all unique permutations by combining backtracking with careful duplicate handling, making it a standard pattern for permutation problems with repeated elements.



---


## 7️⃣ Next Permutation

### 📌 Problem Statement

You are given:

* `nums` → an array of integers

👉 Rearrange numbers into the **next lexicographically greater permutation**

#### 🎯 Rules:

* If such arrangement is not possible → rearrange into **lowest (sorted ascending) order**
* Must be done **in-place**
* Use **constant extra memory**

---

### 🚀 Approach: Greedy + Two Pointers

#### 🔹 Key Idea

To find the next permutation:

1. Find the **first decreasing element from the right**
2. Swap it with the **next greater element**
3. Reverse the suffix to get the smallest order

---

### 🧠 Algorithm

1. Find index `i` such that:

   ```
   nums[i] < nums[i+1]
   ```

   (Traverse from right)

2. If found:

   * Find index `j` such that:

     ```
     nums[j] > nums[i]
     ```
   * Swap `nums[i]` and `nums[j]`

3. Reverse the subarray from `i+1` to end

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
nums = [1,2,3]

Output:
[1,3,2]

Explanation:
Next permutation after [1,2,3] is [1,3,2]
```

---

### 🔍 Dry Run

```text id="dryrun"
nums = [1,3,2]

Step 1:
Find i → index 0 (1 < 3)

Step 2:
Find j → index 2 (2 > 1)

Swap:
[2,3,1]

Step 3:
Reverse suffix:
[2,1,3] ✔️
```

---

### 🔁 Edge Case

```text id="edgecase"
Input:
[3,2,1]

Output:
[1,2,3]

Explanation:
No larger permutation exists → return smallest
```

---

### ✅ Key Points

* Finds **next lexicographical permutation**
* Uses **greedy + reverse technique**
* Works **in-place**
* Handles descending order edge case

---

### ⚠️ Edge Cases

* Already largest permutation
* Single element
* Duplicate elements
* Strictly decreasing array

---

### 🏁 Conclusion

This algorithm efficiently computes the next permutation in linear time by identifying the pivot, swapping intelligently, and reversing the suffix—making it optimal for permutation-based problems.


---


## 8️⃣ Generate Parentheses – Backtracking Approach

### 📌 Problem Statement

You are given:

* `n` → number of pairs of parentheses

👉 Generate **all combinations of well-formed (valid) parentheses**

---

### 🚀 Approach: Backtracking (Constraint-Based)

#### 🔹 Key Idea

* Build the string step by step
* Ensure validity at every step

👉 Rules:

* Add `'('` if `open < n`
* Add `')'` only if `close < open`

---

### 🧠 Algorithm

1. Initialize:

   * `openN = 0`, `closeN = 0`
   * empty stack

2. Recursively build:

   * If `openN < n` → add `'('`
   * If `closeN < openN` → add `')'`

3. Base case:

   * If `openN == closeN == n` → valid combination

4. Backtrack after each choice

---

### 📊 Complexity Analysis

| Type             | Complexity                  |
| ---------------- | --------------------------- |
| Time Complexity  | O(4ⁿ / √n) (Catalan number) |
| Space Complexity | O(n) (recursion stack)      |

---

### 📎 Example

```text id="example"
Input:
n = 3

Output:
[
 "((()))",
 "(()())",
 "(())()",
 "()(())",
 "()()()"
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Start:
""

Add '(' → "("
Add '(' → "(("
Add ')' → "(()"
...

Continue until valid combinations ✔️
```

---

### 🌳 Recursion Tree (Simplified)

```text id="tree"
            ""
         /     
       "("     
     /     \   
   "(("    "()"
   ...
```

---

### ✅ Key Points

* Uses **backtracking with constraints**
* Ensures **valid parentheses at every step**
* Avoids invalid sequences early (pruning)
* Based on **Catalan numbers**

---

### ⚠️ Edge Cases

* `n = 0` → `[""]`
* `n = 1` → `["()"]`
* Larger `n` → exponential growth

---

### 🏁 Conclusion

This problem showcases constraint-based backtracking where only valid sequences are generated, making it efficient despite exponential possibilities.


---


## 9️⃣ Restore IP Addresses

### 📌 Problem Statement

You are given:

* `s` → a string containing only digits

👉 Return all possible **valid IP address combinations**

---

### 🎯 IP Address Rules

A valid IP address consists of **4 parts**:

1. Each part is between **0 and 255**
2. No leading zeros

   * ✅ `"0"` is valid
   * ❌ `"01"`, `"00"` are invalid
3. Exactly **4 segments separated by dots**

---

### 🚀 Approach: Backtracking

#### 🔹 Key Idea

* Try placing **dots** to split the string into 4 parts
* Each part must be **valid (0–255 and no leading zero)**

👉 Maximum length of string = 12 (since 4 parts × 3 digits)

---

### 🧠 Algorithm

1. If length > 12 → return empty

2. Use backtracking:

   * Track:

     * current index `i`
     * number of segments (`dots`)
     * current string

3. For each position:

   * Try substring of length 1 to 3
   * Check:

     * value < 256
     * no leading zeros

4. Base case:

   * If 4 segments and end reached → valid IP

---

### 📊 Complexity Analysis

| Type             | Complexity           |
| ---------------- | -------------------- |
| Time Complexity  | O(1) (bounded by 3⁴) |
| Space Complexity | O(1)                 |

> The search space is limited since max length is 12

---

### 📎 Example

```text id="example"
Input:
s = "25525511135"

Output:
[
 "255.255.11.135",
 "255.255.111.35"
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Start:
"25525511135"

Try splits:
255 | 255 | 11 | 135 ✔️
255 | 255 | 111 | 35 ✔️

Other splits invalid ❌
```

---

### 🌳 Recursion Tree (Simplified)

```text id="tree"
          ""
     /     |     \
   "2"    "25"   "255"
   ...
```

---

### ✅ Key Points

* Backtracking with **string partitioning**
* Validate each segment carefully
* Use **pruning** for invalid cases
* Limited search space → efficient

---

### ⚠️ Edge Cases

* Length < 4 → no valid IP
* Length > 12 → no valid IP
* Leading zeros
* All zeros → `"0.0.0.0"`

---

### 🏁 Conclusion

This problem demonstrates how backtracking can be used to generate valid structured strings by applying constraints at each step, ensuring only valid IP combinations are formed.

---
