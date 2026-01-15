**Two Pointer Technique**



1. Move Zeroes (Two Pointers)

🧩 Problem Statement :

-> Given an integer array nums, move all 0s to the end of the array while maintaining the relative order of the non-zero elements.
-> The operation must be done in-place0
-> Do not create a copy of the array


💡 Approach: Two Pointers

We use two pointers:
    l → points to the position where the next non-zero element should be placed
    r → iterates through the array


Algorithm:

>> Initialize both pointers l and r to 0
>> Traverse the array using r
>> If nums[r] is non-zero:
        Swap nums[l] and nums[r]
        Increment l
>> Always increment r
This ensures:
    All non-zero elements are shifted to the front
    All zeroes move to the end
    Relative order of non-zero elements is preserved

Time : O(N)
Space : O(1)




2. Two Sum II – Input Array Is Sorted

🧩 Problem Statement

-> Given a 1-indexed, sorted array of integers numbers and an integer target, find two numbers such that they add up to target.
-> Return the indices (1-based) of the two numbers.


Constraints :
-> Exactly one valid solution exists
-> You may not use the same element twice
-> The input array is sorted in non-decreasing order


💡 Approach: Two Pointers

Since the array is already sorted, we can efficiently solve this using the two pointers technique.

Pointer Strategy:
    left starts at the beginning of the array
    right starts at the end of the array


Algorithm:

>> Calculate current_sum = numbers[left] + numbers[right]
>> If current_sum > target, move right leftward
>> If current_sum < target, move left rightward
>> If current_sum == target, return the indices (1-based)

This avoids using extra space and ensures optimal performance.

Time : O(N)
Space : O(1)




3. 3Sum

🧩 Problem Statement :

-> Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that:
        i != j, i != k, and j != k
-> nums[i] + nums[j] + nums[k] == 0
-> The solution set must not contain duplicate triplets


💡 Approach: Sorting + Two Pointers

This problem is efficiently solved using sorting combined with the two pointers technique.

Why Sorting?
    Helps avoid duplicate triplets
    Allows controlled pointer movement based on sum comparison


🧠 Algorithm:

>> Sort the input array
>> Iterate through the array using index i
        Skip duplicate values for i
>> For each i, use two pointers:
        left = i + 1
        right = len(nums) - 1
>> Compute the sum of nums[i] + nums[left] + nums[right]
        If sum == 0 → store the triplet
        If sum < 0 → move left forward
        If sum > 0 → move right backward
>> Skip duplicate values for left and right to avoid repeated triplets
>> Continue until all valid triplets are found

Time : O(N^2)
Space : O(1) ("Without result Array")




4. Sort Colors (Dutch National Flag Problem)

🧩 Problem Statement :

-> Given an array nums with n objects colored red (0), white (1), or blue (2), sort them in-place so that objects of the same color are adjacent, in the order red → white → blue.
-> Do not use the library’s sort function
-> Must be done in-place with constant space


💡 Approach: Dutch National Flag / Three Pointers

We use three pointers to partition the array into three sections:
    left → boundary of 0s (reds)
    mid → current element being checked
    right → boundary of 2s (blues)


Algorithm :

>> Initialize left = 0, mid = 0, right = len(nums) - 1
>> While mid <= right:
        If nums[mid] == 0 → swap with nums[left], move left and mid forward
        If nums[mid] == 1 → just move mid forward
        If nums[mid] == 2 → swap with nums[right], move right backward
>> Continue until mid > right
This ensures all 0s are at the beginning, 2s at the end, and 1s in the middle.

Time : O(N)
Space : O(1)




5. Container With Most Water

🧩 Problem Statement :

-> Given an array height of n non-negative integers, where each integer represents the height of a vertical line on the x-axis, find two lines that together with the x-axis form a container, such that the container contains the most water.
-> Return the maximum area of water the container can store.
    You may not slant the container
    The area of water is determined by width × min(height[left], height[right])


💡 Approach: Two Pointers

We can solve this efficiently using the two pointers technique:
Pointer Strategy:
    l → start of the array
    r → end of the array


Algorithm:

>> Initialize res = 0 to track the maximum area
>> While l < r:
        Calculate current_area = (r - l) * min(height[l], height[r])
        Update res = max(res, current_area)
        Move the pointer pointing to the shorter line inward (l or r)
         (because moving the taller line cannot increase area)
>> Return res after scanning the array

Time : O(N)
Space : O(1)




6. Trapping Rain Water

🧩 Problem Statement :

-> Given n non-negative integers representing the elevation map where the width of each bar is 1, compute how much water it can trap after raining
-> Water is trapped between the bars based on the min height of surrounding bars.


💡 Approach: Two Pointers

We use two pointers and two variables to track the maximum heights from both sides:
Variables:
    l → left pointer
    r → right pointer
    lmax → maximum height from the left
    rmax → maximum height from the right
    total → total trapped water


Algorithm:

>> Initialize l = 1, r = len(height)-2, lmax = height[0], rmax = height[-1]
>> While l <= r:
        If lmax < rmax:
            If height[l] >= lmax, update lmax
            Else, add lmax - height[l] to total
            Move l forward
        Else:
            If height[r] >= rmax, update rmax
            Else, add rmax - height[r] to total
            Move r backward
>> Return total after processing all bars

This works because the trapped water at a position is determined by the smaller of the maximum heights to its left and right.

Time : O(N)
Space : O(1)