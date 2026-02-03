class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        prefix = [[int(cell) for cell in row] for row in matrix]
        m = len(prefix)
        n = len(prefix[0])
        for j in range(n):
            for i in range(1,m):
                if prefix[i][j] != 0:
                    prefix[i][j] += prefix[i-1][j]
        ans = 0
        def largestRArea(heights):
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
        for i in range(m):
            ans = max(ans,largestRArea(prefix[i]))
        
        return ans