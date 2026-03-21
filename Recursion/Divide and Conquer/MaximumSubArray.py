class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def helper(left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            left_sum = helper(left, mid)
            right_sum = helper(mid + 1, right)

            cross_sum = maxCrossingSum(left, mid, right)

            return max(left_sum, right_sum, cross_sum)

        def maxCrossingSum(left, mid, right):
            left_max = float('-inf')
            curr = 0
            for i in range(mid, left - 1, -1):
                curr += nums[i]
                left_max = max(left_max, curr)

            right_max = float('-inf')
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                right_max = max(right_max, curr)

            return left_max + right_max

        return helper(0, len(nums) - 1)