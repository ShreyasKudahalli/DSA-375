class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start, comb):
            res.append(comb.copy())
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                comb.append(nums[i])
                backtrack(i + 1, comb)
                comb.pop()
        
        backtrack(0, [])
        return res