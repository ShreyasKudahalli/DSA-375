class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n+2)]
        pprev = [0,0]
        prev = [0,0]
        cur = [0,0] 

        for indx in range(n-1,-1,-1):
            for buy in range(2):
                if buy:
                    cur[buy] = max(-prices[indx]+prev[0],0+prev[1])       
                else:
                    cur[buy] = max(prices[indx]+pprev[1],0+prev[0])
            pprev = prev
            prev = cur.copy()

        return prev[1]