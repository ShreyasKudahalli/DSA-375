class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sCount = [0] * 26
        pCount  = [0] * 26
        l = 0
        res = []
        for ch in p:
            pCount[ord(ch)-ord('a')] += 1
        
        for r in range(len(s)):
            if r-l+1>len(p):
                sCount[ord(s[l])-ord('a')] -= 1
                l += 1
            sCount[ord(s[r])-ord('a')] += 1
            
            if sCount == pCount:
                res.append(l)
        return res