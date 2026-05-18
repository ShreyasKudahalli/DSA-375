class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = {}
        res = []

        for i,ch in enumerate(s):
            last[ch] = i

        start = 0
        end = 0

        for i,ch in enumerate(s):
            end = max(last[ch],end)

            if end == i:
                res.append(end-start+1)
                start = i+1
        return res

