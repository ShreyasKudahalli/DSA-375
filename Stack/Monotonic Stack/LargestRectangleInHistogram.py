class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nse,pse=0,0
        ans = 0
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                ele = stack.pop()
                nse = i
                if stack:
                    pse = stack[-1]
                else:
                    pse = -1
                ans = max(ans,heights[ele]*(nse-pse-1))
            stack.append(i)
        while stack:
            nse = n
            ele = stack.pop()
            if stack:
                pse = stack[-1]
            else:
                pse = -1
            ans = max(ans,heights[ele]*(nse-pse-1))
        return ans
                