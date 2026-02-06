class Solution:
    def infixtoPostfix(self, s):
        stack = []
        ans = ''
        
        def pred(ch):
            if ch == '^':
                return 3
            elif ch == '*' or ch == '/':
                return 2
            elif ch == '+' or ch == '-':
                return 1
            return 0
        
        for ch in s:
            if ch.isalnum():
                ans += ch
            elif ch == "(":
                stack.append(ch)
            elif ch == ")":
                while stack[-1] != '(':
                    ans += stack.pop()
                stack.pop()
            else:
                while stack and stack[-1] != '(' and (pred(stack[-1]) > pred(ch) or(pred(stack[-1]) == pred(ch) and ch != '^')):
                    ans += stack.pop()
                    
                stack.append(ch)
        while stack:
            ans += stack.pop()
        
        return ans
                
        
        