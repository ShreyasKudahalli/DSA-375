class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                temp = ''
                while stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num
                stack.append(int(num) * temp)
        return ''.join(stack)