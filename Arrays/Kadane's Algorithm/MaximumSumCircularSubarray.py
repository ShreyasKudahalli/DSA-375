class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_min_sum = min_sum = float("inf")
        cur_max_sum = max_sum = float("-inf")
        total = 0

        for n in nums:
            cur_min_sum = min(cur_min_sum+n,n)
            cur_max_sum = max(cur_max_sum+n,n)

            min_sum = min(cur_min_sum,min_sum)
            max_sum = max(cur_max_sum,max_sum)

            total += n
        if max_sum < 0:
            return max_sum
        return max(max_sum,total-min_sum)