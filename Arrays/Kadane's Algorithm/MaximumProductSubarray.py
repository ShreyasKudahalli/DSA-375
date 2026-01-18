class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l_prod = r_prod = 1
        res = float("-inf")
        n = len(nums)
        for i in range(n):
            if l_prod == 0:
                l_prod = 1
            if r_prod == 0:
                r_prod = 1
            
            l_prod *= nums[i]
            r_prod *= nums[n-i-1]

            res = max(res,max(l_prod,r_prod))
            
        return res