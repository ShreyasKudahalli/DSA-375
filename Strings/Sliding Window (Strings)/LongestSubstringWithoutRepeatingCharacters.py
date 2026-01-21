class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = set()
        res,l,r=0,0,0

        for r in range(0,len(s)):
            while s[r] in word:
                word.remove(s[l])
                l+=1
            word.add(s[r])
            res = max((r+1)-l,res)

        return res