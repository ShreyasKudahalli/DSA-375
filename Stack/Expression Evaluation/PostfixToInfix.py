class Solution:
    def postToInfix(self, postfix):
        
        stack = []
        
        for ch in postfix:
            if ch.isalnum():
                stack.append(ch)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append('('+a+ch+b+')')
        
        return stack.pop()