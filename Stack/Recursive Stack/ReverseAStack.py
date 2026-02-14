class Solution:
    def reverseStack(self, st):
        
        def helper(st,x):
            if len(st) == 0:
                st.append(x)
                return
            top = st.pop()
            helper(st,x)
            st.append(top)
        
        def reverse(st):
            if not st:
                return
            top = st.pop()
            reverse(st)
            helper(st,top)
        reverse(st)
        return st