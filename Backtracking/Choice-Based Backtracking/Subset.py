class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i,comb):
            if i == len(nums):
                res.append(comb.copy())
                return 
            comb.append(nums[i])
            backtrack(i+1,comb)
            comb.pop()
            backtrack(i+1,comb)
        
        backtrack(0,[])
        return res