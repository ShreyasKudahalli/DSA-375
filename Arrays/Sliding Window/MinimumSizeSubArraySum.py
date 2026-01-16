class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        res,cur=float('inf'),0
        while r < len(nums):
            cur += nums[r]
            r += 1

            while target <= cur:
                res = min(res,r-l)
                cur -= nums[l]
                l += 1
        return 0 if res==float('inf') else res