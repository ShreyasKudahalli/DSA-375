class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        size = 1

        def expand(l,r):
            nonlocal start,size
            while l>=0 and r<len(s) and s[l]==s[r]:
                if(r-l+1 > size):
                    size = r-l+1
                    start = l
                l -= 1
                r += 1
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)
        return s[start:start+size]