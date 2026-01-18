class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=cur=float('-inf')
        for i in range(len(nums)):
            cur = max(cur+nums[i],nums[i])
            res = max(res,cur)
        return res