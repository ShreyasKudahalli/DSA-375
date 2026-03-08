class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) == 0 or len(s) < len(t):
            return ''
        tCount = {}
        windowCount = {}

        for ch in t:
            tCount[ch] = tCount.get(ch, 0) + 1
        
        l,start,minlen = 0,0,float('inf')
        have = 0

        for r in range(len(s)):
            windowCount[s[r]] = windowCount.get(s[r], 0) + 1

            if s[r] in tCount and windowCount[s[r]] <= tCount[s[r]]:
                have += 1

            while have==len(t):
                if r-l+1 < minlen:
                    start = l
                    minlen = r-l+1
                windowCount[s[l]] -= 1
                if s[l] in tCount and windowCount[s[l]] < tCount[s[l]]:
                    have -= 1

                l += 1
        
        return "" if minlen == float("inf") else s[start:start + minlen]