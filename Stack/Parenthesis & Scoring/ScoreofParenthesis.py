class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count = 0
        stack = []
        for ch in s:
            val = 0
            if ch == '(':
                stack.append(0)
            else:
                while stack[-1] != 0:
                    val += stack.pop()
                val = max(val*2,1)
                stack.pop()
                stack.append(val)
        while stack:
            count += stack.pop()
        return count