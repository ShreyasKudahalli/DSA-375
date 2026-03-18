class Solution:
    def fib(self, n: int) -> int:
        def helper(a,b,n):
            if n == 0:
                return a
            return helper(b,a+b,n-1)
        
        return helper(0,1,n)
