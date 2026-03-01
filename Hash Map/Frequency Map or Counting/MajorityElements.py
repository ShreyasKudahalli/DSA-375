class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mpp = {}
        n = len(nums)

        for x in nums:

            if x in mpp:
                mpp[x] += 1
            else:
                mpp[x] = 1
            
            if mpp[x] > n//2:
                return x