class Solution:
    def postToPre(self, post_exp):
        
        stack = []
        
        for ch in post_exp:
            if ch.isalnum():
                stack.append(ch)
            else:
                a = stack.pop()
                b = stack.pop()
                
                stack.append(ch+b+a)
                
        return stack.pop()