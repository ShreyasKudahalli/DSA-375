class Solution:
    def deleteMid(self, stack):
        #code here
        n = len(stack)
        mid = n // 2

        def solve(st, curr):
            if not st:
                return
            
            top = st.pop()
            solve(st, curr + 1)
            
            if curr != mid:
                st.append(top)

        solve(stack, 0)
        return stack