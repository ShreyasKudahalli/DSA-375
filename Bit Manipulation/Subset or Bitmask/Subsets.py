class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = (1 << n)
        ans = []
        for num in range(subset):
            res = []
            for i in range(n):
                if num & (1 << i):
                    res.append(nums[i])
            ans.append(res)
        return ans