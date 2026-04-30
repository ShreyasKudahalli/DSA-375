class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [False]*len(nums)
        res = []

        def backtrack(comb,visited):
            if len(comb) == len(nums):
                res.append(comb.copy())
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                comb.append(nums[i])
                visited[i] = True
                backtrack(comb,visited)
                comb.pop()
                visited[i] = False
        backtrack([],visited)
        return res