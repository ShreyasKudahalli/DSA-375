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


---


## 3️⃣ Binary Number with Alternating Bits

### 📌 Problem Statement

You are given:

* `n` → a positive integer

👉 Return `True` if its binary representation has alternating bits.

👉 Two adjacent bits must always be different.

Otherwise, return `False`.

---

### 🚀 Approach: Bit Manipulation (XOR Trick)

#### 🔹 Key Idea

For a number with alternating bits:

```text id="examplebits"
1010
0101
101
```

If we XOR the number with itself shifted right by one position:

```text id="relation"
x = n ^ (n >> 1)
```

The result becomes a sequence of all `1`s.

Example:

```text id="xor"
n       = 1010
n >> 1  = 0101
----------------
x       = 1111
```

A number consisting entirely of `1`s satisfies:

```text id="property"
x & (x + 1) == 0
```

because:

```text id="proof"
1111
+
0001
-----
10000

1111 & 10000 = 0
```

---

### 🧠 Algorithm

1. Compute:

   ```text
   x = n ^ (n >> 1)
   ```

2. Check whether `x` is composed entirely of `1`s:

   ```text
   x & (x + 1) == 0
   ```

3. Return the result.

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(1)       |
| Space Complexity | O(1)       |

---

### 📎 Example

```text id="example"
Input:

n = 10
```

Binary:

```text id="binary"
1010
```

Output:

```text id="output"
True
```

---

### 🔍 Dry Run

```text id="dryrun"
n = 10

Binary:
1010

n >> 1:
0101

XOR:
1010
^0101
-----
1111

x = 15

Check:

1111 & 10000
= 0

Answer = True
```

---

### 🌳 Visualization

```text id="visual"
Alternating Bits:

1 0 1 0

Shift Right:

0 1 0 1

XOR:

1 1 1 1
```

All bits become `1`, confirming the alternating pattern.

---

### ✅ Key Points

* Uses a clever XOR observation.
* Alternating bits become all `1`s after XOR with the shifted version.
* `x & (x + 1) == 0` efficiently checks whether a number contains only `1`s.
* Constant time and space solution.

---

### ⚠️ Edge Cases

* Single-bit numbers
* Powers of two
* Consecutive equal bits (`110`, `1001`)
* Very large integers

---

### 🏁 Conclusion

This solution leverages a powerful bit manipulation trick: XORing a number with its right-shifted version transforms alternating-bit patterns into a sequence of all `1`s. A simple bitwise check then verifies this property, yielding an elegant O(1) time and O(1) space solution.


---


## 4️⃣ Power of Two

### 📌 Problem Statement

You are given:

* `n` → an integer

👉 Return `True` if `n` is a power of two.

👉 Otherwise, return `False`.

A number is a power of two if there exists an integer `x` such that:

```text id="definition"
n = 2^x
```

---

### 🚀 Approach: Bit Manipulation

#### 🔹 Key Idea

A power of two has exactly **one set bit** in its binary representation.

Examples:

```text id="powers"
1  = 0001
2  = 0010
4  = 0100
8  = 1000
16 = 10000
```

If we subtract `1` from a power of two:

```text id="subtract"
8  = 1000
7  = 0111
```

Performing:

```text id="and"
1000
&
0111
----
0000
```

Therefore, for every positive power of two:

```text id="property"
n & (n - 1) == 0
```

---

### 🧠 Algorithm

1. Check if `n` is positive.

   * Powers of two must be greater than `0`.

2. Compute:

   ```text
   n & (n - 1)
   ```

3. If the result is `0`:

   * Exactly one bit was set.
   * Return `True`.

4. Otherwise:

   * Return `False`.

---

### 📊 Complexity Analysis

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(1)       |
| Space Complexity | O(1)       |

---

### 📎 Example

```text id="example"
Input:

n = 16
```

Output:

```text id="output"
True
```

---

### 🔍 Dry Run

```text id="dryrun"
n = 16

Binary:

10000

n - 1:

01111

AND:

10000
&
01111
-----
00000

Result = 0

Answer = True
```

---

### 🌳 Visualization

```text id="visual"
Power of Two:

100000

Subtract 1:

011111

AND:

100000
&
011111
------
000000
```

Only powers of two produce zero after this operation.

---

### ✅ Key Points

* A power of two contains exactly one set bit.
* `n & (n - 1)` removes the lowest set bit.
* Result becomes zero only when there is a single set bit.
* Must explicitly check `n > 0`.

---

### ⚠️ Edge Cases

* `n = 1`
* `n = 0`
* Negative numbers
* Large powers of two
* Numbers with multiple set bits

---

### 🏁 Conclusion

The Power of Two problem can be solved elegantly using bit manipulation. Since powers of two contain exactly one set bit, the expression `n & (n - 1)` removes that bit and produces zero. Combined with a positivity check, this yields an optimal O(1) time and O(1) space solution.


---


## 5️⃣ Single Number

### 📌 Problem Statement

You are given:

* `nums[]` → a non-empty array of integers

👉 Every element appears exactly **twice** except for one element.

👉 Find and return that single element.

You must solve it using:

* Linear runtime
* Constant extra space

---

### 🚀 Approach: Bit Manipulation (XOR)

#### 🔹 Key Idea

The XOR operator (`^`) has the following properties:

```text id="properties"
a ^ a = 0
a ^ 0 = a
a ^ b = b ^ a
```

Since every number except one appears twice:

* Duplicate numbers cancel each other out.
* The unique number remains.

So:

```text id="relation"
x ^ x = 0

0 ^ unique = unique
```

---

### 🧠 Algorithm

1. Initialize:

   ```text
   ans = 0
   ```

2. Traverse the array.

3. XOR every element with `ans`.

4. Duplicate values cancel out.

5. Return the remaining value.

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

nums = [2,2,1]
```

Output:

```text id="output"
1
```

---

### 🔍 Dry Run

```text id="dryrun"
nums = [2,2,1]

ans = 0

ans ^= 2
= 2

ans ^= 2
= 0

ans ^= 1
= 1

Final Answer = 1
```

---

### 🌳 Visualization

```text id="visual"
Array:

2   2   1

XOR Process:

0 ^ 2 = 2
2 ^ 2 = 0
0 ^ 1 = 1

Result:

1
```

Duplicate elements cancel each other:

```text id="cancel"
2 ^ 2 = 0
```

Leaving only the unique number.

---

### ✅ Key Points

* XOR cancels identical values.
* Order of XOR operations does not matter.
* No extra data structures required.
* One-pass solution.

---

### ⚠️ Edge Cases

* Array contains only one element.
* Unique element is negative.
* Unique element appears at the beginning or end.
* Large input size.

---

### 🏁 Conclusion

The Single Number problem is a classic application of XOR. By leveraging the property that identical numbers cancel each other out, we can isolate the unique element in a single traversal using O(n) time and O(1) space, making it the most efficient solution.
