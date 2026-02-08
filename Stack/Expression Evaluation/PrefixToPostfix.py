class Solution:
    def preToPost(self, pre_exp):
        
        n = len(pre_exp)
        stack = []
        
        for i in range(n-1,-1,-1):
            if pre_exp[i].isalnum():
                stack.append(pre_exp[i])
            else:
                a = stack.pop()
                b = stack.pop()
                
                stack.append(a+b+pre_exp[i])
                
        return stack.pop()
        