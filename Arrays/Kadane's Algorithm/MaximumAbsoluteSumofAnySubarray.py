class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        cur_min_sum = min_sum = float("inf")
        cur_max_sum = max_sum = float("-inf")

        for i in range(len(nums)):
            cur_min_sum = min(cur_min_sum+nums[i],nums[i])
            cur_max_sum = max(cur_max_sum+nums[i],nums[i])
            max_sum = max(cur_max_sum,max_sum)
            min_sum = min(cur_min_sum,min_sum)

        return max(abs(max_sum),abs(min_sum))