class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(nums,xor,n):
            if n < 0:
                nonlocal res
                res += xor
                return
            
            backtrack(nums,xor,n-1)
            backtrack(nums,xor^nums[n],n-1)

        backtrack(nums,0,len(nums)-1)
        return res