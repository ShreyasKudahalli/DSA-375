class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def helper(nums,k):
            count = 0
            l,r = 0,0
            mmp = {}
            while r < len(nums):
                mmp[nums[r]] = mmp.get(nums[r], 0) + 1
                while len(mmp) > k:
                    mmp[nums[l]] -= 1
                    if mmp[nums[l]] == 0:
                        del mmp[nums[l]]
                    l += 1
                count += r-l+1
                r += 1
            return count
        return helper(nums,k) - helper(nums,k-1)