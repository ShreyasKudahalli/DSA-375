#User function Template for python3

class Solution:
    def preToInfix(self, pre_exp):
        
        stack = []
        ans = ''
        
        for i in range(len(pre_exp)-1,-1,-1):
            if pre_exp[i].isalnum():
                stack.append(pre_exp[i])
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append('('+a+pre_exp[i]+b+')')
        
        return stack.pop()