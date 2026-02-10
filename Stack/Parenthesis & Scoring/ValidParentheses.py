class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if not stack or abs(ord(stack[-1])-ord(ch))>2:
                    return False
                else:
                    stack.pop()
        return len(stack)==0