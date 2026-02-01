class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(n*2-1,-1,-1):
            while stack and nums[stack[-1]%n] <= nums[(i%n)]:
                stack.pop()
            if i<n:
                if stack:
                    res[i] = nums[stack[-1]%n]
                else:
                    res[i] = -1
            stack.append(i)
        return res