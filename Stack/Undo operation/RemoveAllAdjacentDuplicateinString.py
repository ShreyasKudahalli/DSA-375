class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for x in s:
            if not stack:
                stack.append(x)
            else:
                if stack[-1]==x:
                    stack.pop()
                else:
                    stack.append(x)
        return ''.join(stack)
    