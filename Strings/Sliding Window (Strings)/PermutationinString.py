class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) or s1 == "":
            return False
        s1Count = [0] * 26
        s2Count = [0] * 26

        for ch in s1:
            s1Count[ord(ch)-ord('a')] += 1
        
        l,r=0,0

        while r < len(s2):
            s2Count[ord(s2[r])-ord('a')] += 1
            if r-l+1 == len(s1):
                if s2Count == s1Count:
                    return True
                s2Count[ord(s2[l])-ord('a')] -= 1
                l += 1
            r += 1
        return False
