class Solution:
    def longestSubstringKDistinct(self, s: str, k: int) -> str:
        if k == 0:
            return 0
        l = 0
        freq = {}
        start = 0
        size = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0) + 1

            while len(freq) > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            
            if size < r-l+1:
                start = l
                size = r-l+1
        
        return s[start:start+size]