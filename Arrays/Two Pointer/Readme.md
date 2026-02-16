
# Two Pointer Technique

The **Two Pointer Technique** is commonly used to solve array and linked list problems efficiently, especially when the input is sorted or when we need in-place modifications.

---

# 1️⃣ Move Zeroes

## 🧩 Problem Statement

* Given an integer array `nums`, move all `0`s to the end while maintaining the relative order of the non-zero elements.
* The operation must be done **in-place**.
* Do not create a copy of the array.

---

## 💡 Approach: Two Pointers

We use two pointers:

* `l` → Points to the position where the next non-zero element should be placed
* `r` → Iterates through the array

---

## 🔁 Algorithm

1. Initialize both pointers `l = 0` and `r = 0`.
2. Traverse the array using `r`.
3. If `nums[r]` is non-zero:

   * Swap `nums[l]` and `nums[r]`
   * Increment `l`
4. Always increment `r`.

### ✅ This ensures:

* All non-zero elements move to the front.
* All zeroes shift to the end.
* The relative order of non-zero elements is preserved.

**Time Complexity:** O(N)
**Space Complexity:** O(1)

---

# 2️⃣ Two Sum II – Input Array Is Sorted

## 🧩 Problem Statement

* Given a **1-indexed, sorted array** `numbers` and an integer `target`, find two numbers such that they add up to `target`.
* Return their indices (1-based).

### Constraints

* Exactly one valid solution exists.
* You may not use the same element twice.
* The array is sorted in non-decreasing order.

---

## 💡 Approach: Two Pointers

Since the array is sorted, we can use two pointers efficiently.

### Pointer Strategy

* `left` → Start of the array
* `right` → End of the array

---

## 🔁 Algorithm

1. While `left < right`:

   * Compute `current_sum = numbers[left] + numbers[right]`
   * If `current_sum > target` → move `right` leftward.
   * If `current_sum < target` → move `left` rightward.
   * If `current_sum == target` → return `[left + 1, right + 1]`.

This avoids extra space and ensures optimal performance.

**Time Complexity:** O(N)
**Space Complexity:** O(1)

---

# 3️⃣ 3Sum

## 🧩 Problem Statement

* Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that:

  * `i != j`, `i != k`, and `j != k`
  * `nums[i] + nums[j] + nums[k] == 0`
* The solution set must not contain duplicate triplets.

---

## 💡 Approach: Sorting + Two Pointers

### Why Sorting?

* Helps skip duplicates.
* Enables controlled pointer movement based on sum comparison.

---

## 🔁 Algorithm

1. Sort the array.
2. Iterate through the array using index `i`.

   * Skip duplicate values of `nums[i]`.
3. For each `i`, set:

   * `left = i + 1`
   * `right = len(nums) - 1`
4. While `left < right`:

   * Compute the sum.
   * If sum == 0 → store the triplet.
   * If sum < 0 → move `left` forward.
   * If sum > 0 → move `right` backward.
   * Skip duplicates for `left` and `right`.

**Time Complexity:** O(N²)
**Space Complexity:** O(1) (excluding result storage)

---

# 4️⃣ Sort Colors (Dutch National Flag Problem)

## 🧩 Problem Statement

* Given an array `nums` with values:

  * `0` → Red
  * `1` → White
  * `2` → Blue
* Sort them in-place in the order: **Red → White → Blue**.
* Do not use the built-in sort function.
* Must use constant extra space.

---

## 💡 Approach: Three Pointers

We divide the array into three sections:

* `left` → Boundary of 0s
* `mid` → Current element
* `right` → Boundary of 2s

---

## 🔁 Algorithm

1. Initialize:

   * `left = 0`
   * `mid = 0`
   * `right = len(nums) - 1`
2. While `mid <= right`:

   * If `nums[mid] == 0`:

     * Swap with `nums[left]`
     * Increment both `left` and `mid`
   * If `nums[mid] == 1`:

     * Increment `mid`
   * If `nums[mid] == 2`:

     * Swap with `nums[right]`
     * Decrement `right`

This partitions the array in a single pass.

**Time Complexity:** O(N)
**Space Complexity:** O(1)

---

# 5️⃣ Container With Most Water

## 🧩 Problem Statement

* Given an array `height`, where each element represents a vertical line.
* Find two lines that form a container holding the maximum water.
* You cannot tilt the container.

Area formula:

```
Area = (right - left) × min(height[left], height[right])
```

---

## 💡 Approach: Two Pointers

### Pointer Strategy

* `l` → Start of the array
* `r` → End of the array

---

## 🔁 Algorithm

1. Initialize `res = 0`.
2. While `l < r`:

   * Compute:

     ```
     area = (r - l) × min(height[l], height[r])
     ```
   * Update `res = max(res, area)`
   * Move the pointer pointing to the shorter height inward.
3. Return `res`.

### Why Move the Shorter Line?

Because the area is limited by the smaller height. Moving the taller line cannot increase the area.

**Time Complexity:** O(N)
**Space Complexity:** O(1)

---

# 6️⃣ Trapping Rain Water

## 🧩 Problem Statement

* Given an elevation map `height`, compute how much water it can trap after raining.

Water trapped at position `i`:

```
min(max height to left, max height to right) - height[i]
```

---

## 💡 Approach: Two Pointers

### Variables

* `l` → Left pointer
* `r` → Right pointer
* `lmax` → Maximum height from the left
* `rmax` → Maximum height from the right
* `total` → Total trapped water

---

## 🔁 Algorithm

1. Initialize:

   * `l = 0`
   * `r = len(height) - 1`
   * `lmax = 0`
   * `rmax = 0`
   * `total = 0`
2. While `l < r`:

   * If `height[l] < height[r]`:

     * If `height[l] >= lmax`, update `lmax`
     * Else add `lmax - height[l]` to `total`
     * Move `l` forward
   * Else:

     * If `height[r] >= rmax`, update `rmax`
     * Else add `rmax - height[r]` to `total`
     * Move `r` backward
3. Return `total`.

**Time Complexity:** O(N)
**Space Complexity:** O(1)

---

# 🎯 Summary of Two Pointer Problems

| Problem                   | Time Complexity | Space Complexity |
| ------------------------- | --------------- | ---------------- |
| Move Zeroes               | O(N)            | O(1)             |
| Two Sum II                | O(N)            | O(1)             |
| 3Sum                      | O(N²)           | O(1)             |
| Sort Colors               | O(N)            | O(1)             |
| Container With Most Water | O(N)            | O(1)             |
| Trapping Rain Water       | O(N)            | O(1)             |

*Excluding result storage.

---
