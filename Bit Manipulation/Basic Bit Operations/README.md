# Basic Bit Manipulation operations
Basic Bit Manipulation operations involve directly working with the binary representation of numbers using operators such as **AND (`&`)**, **OR (`|`)**, **XOR (`^`)**, **NOT (`~`)**, and bit shifts (**`<<`**, **`>>`**). These operations enable efficient solutions for tasks like checking or setting bits, counting set bits, finding missing or unique numbers, testing powers of two, and performing arithmetic optimizations. Since bitwise operations are executed at the hardware level, they often provide highly optimized O(1) solutions and form a fundamental technique in competitive programming, system design, and low-level algorithmic problems.


## 1️⃣ Missing Number

### 📌 Problem Statement

You are given:

* `nums[]` → an array containing `n` distinct numbers in the range `[0, n]`

👉 Exactly one number is missing from the range.

👉 Return the missing number.

---

### 🚀 Approach: Bit Manipulation (XOR)

#### 🔹 Key Idea

The XOR operator (`^`) has two important properties:

```text id="properties"
a ^ a = 0
a ^ 0 = a
```

If we XOR:

* All indices `0...n`
* All numbers in the array

Every number that appears twice cancels out, leaving only the missing number.

So:

```text id="relation"
missing =
0 ^ 1 ^ 2 ^ ... ^ n
^
nums[0] ^ nums[1] ^ ... ^ nums[n-1]
```

All matching values disappear due to XOR cancellation.

---

### 🧠 Algorithm

1. Initialize:

   * `ans = n`

2. Traverse the array:

   * XOR current index with current number.

3. Since every number except the missing one appears twice:

   * They cancel each other.

4. Return the remaining value.

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

nums = [3,0,1]
```

Output:

```text id="output"
2
```

---

### 🔍 Dry Run

```text id="dryrun"
nums = [3,0,1]

ans = 3

ans ^= 0 ^ 3
     = 0

ans ^= 1 ^ 0
     = 1

ans ^= 2 ^ 1
     = 2

Final Answer = 2
```

---

### 🌳 Visualization

```text id="visual"
Numbers from 0 to 3:

0  1  2  3

Array:

3  0  1

XOR All:

0 ^ 1 ^ 2 ^ 3
^
3 ^ 0 ^ 1

Pairs cancel:

0^0 = 0
1^1 = 0
3^3 = 0

Remaining:

2
```

---

### ✅ Key Points

* XOR cancels identical values.
* No extra memory required.
* Single traversal of the array.
* Elegant bit manipulation solution.

---

### ⚠️ Edge Cases

* Missing number is `0`
* Missing number is `n`
* Single element array
* Large input sizes

---

### 🏁 Conclusion

The XOR approach efficiently finds the missing number by exploiting the cancellation property of XOR. Since every number except one appears exactly twice in the combined sequence of indices and array values, the missing number remains after all XOR operations, yielding an optimal O(n) time and O(1) space solution.


---


## 2️⃣ Number of 1 Bits (Hamming Weight)

### 📌 Problem Statement

You are given:

* `n` → a positive integer

👉 Return the number of `'1'` bits in its binary representation.

This count is also known as the **Hamming Weight**.

---

### 🚀 Approach: Bit Manipulation

#### 🔹 Key Idea

The least significant bit (LSB) of a number can be obtained using:

```text id="bit"
n & 1
```

* If the last bit is `1`, the result is `1`.
* Otherwise, the result is `0`.

After checking the last bit, shift the number right by one position:

```text id="shift"
n >>= 1
```

Repeat until the number becomes `0`.

---

### 🧠 Algorithm

1. Initialize:

   * `count = 0`

2. While `n > 0`:

   * Add `(n & 1)` to count.
   * Right shift `n` by one bit.

3. Return `count`.

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(log n)   |
| Space Complexity | O(1)       |

Since a number with value `n` contains `log₂(n)` bits.

---

### 📎 Example

```text id="example"
Input:

n = 11
```

Binary Representation:

```text id="binary"
11 = 1011₂
```

Output:

```text id="output"
3
```

---

### 🔍 Dry Run

```text id="dryrun"
n = 11

Binary: 1011

Iteration 1:
1011 & 1 = 1
count = 1

Iteration 2:
0101 & 1 = 1
count = 2

Iteration 3:
0010 & 1 = 0
count = 2

Iteration 4:
0001 & 1 = 1
count = 3

n becomes 0

Answer = 3
```

---

### 🌳 Visualization

```text id="visual"
Binary Number:

1 0 1 1
↑ ↑ ↑ ↑
1 0 1 1

Count of 1s:

1 + 0 + 1 + 1 = 3
```

---

### ✅ Key Points

* `n & 1` extracts the last bit.
* Right shift removes the processed bit.
* Processes bits one by one.
* Uses constant extra space.

---

### ⚠️ Edge Cases

* `n = 0`
* Number with all bits set
* Power of two numbers
* Very large integers

---

### 🏁 Conclusion

The Hamming Weight problem is a classic bit manipulation task. By repeatedly checking the least significant bit and shifting the number to the right, we can efficiently count the number of set bits in binary representation using O(log n) time and O(1) space.
