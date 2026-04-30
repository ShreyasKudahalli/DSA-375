class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        
        def backtrack(comb,visited):
            if len(comb) == len(nums):
                res.append(comb.copy())
                return
            for x in nums:
                if x in visited:
                    continue
                comb.append(x)
                visited.add(x)
                backtrack(comb,visited)
                comb.pop()
                visited.remove(x)
        backtrack([],visited)
        return res