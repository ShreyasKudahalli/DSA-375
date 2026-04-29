class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  

        def backtrack(start, comb, Combsum):
            if Combsum == target:
                res.append(comb.copy())
                return
            if Combsum > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                backtrack(i+1, comb, Combsum + candidates[i])  
                comb.pop()

        backtrack(0, [], 0)
        return res

