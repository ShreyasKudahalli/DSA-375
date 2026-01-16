class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l,r,res = 0,0,0
        while r < len(nums):
            while r < len(nums) and nums[r]:
                res = max(res,r-l+1)
                r += 1
            r += 1
            l = r
        return res