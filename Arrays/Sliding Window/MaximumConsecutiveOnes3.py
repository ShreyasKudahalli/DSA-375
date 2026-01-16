class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        r,l,res = 0,0,0
        while r < len(nums):
            while k <= 0 and nums[r] == 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            if nums[r] == 0:
                k -= 1
            res = max(res,r-l+1)
            r += 1
        
        return res
