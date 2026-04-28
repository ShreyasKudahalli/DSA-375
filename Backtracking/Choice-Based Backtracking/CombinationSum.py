class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i,sum,comb):
            if sum == target:
                res.append(comb.copy())
                return
            elif sum > target:
                return
            
            for i in range(i,len(candidates)):
                comb.append(candidates[i])
                backtrack(i,sum+candidates[i],comb)
                comb.pop()
        
        backtrack(0,0,[])
        return res
            
            