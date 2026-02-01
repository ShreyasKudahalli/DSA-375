class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                continue
            while stack and temperatures[stack[-1]] < temperatures[i]:
                ele = stack.pop()
                res[ele] = i-ele
            
            stack.append(i)
        return res