class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        window = 1
        ans,r,l = 0,0,0
        while r < len(nums):
            window *= nums[r]

            while l<=r and window >= k:
                window /= nums[l]
                l += 1
            ans += r-l+1
            r += 1
        return ans