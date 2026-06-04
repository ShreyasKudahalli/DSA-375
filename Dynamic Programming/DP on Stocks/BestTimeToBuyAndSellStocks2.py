class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prev = [0,0]
        cur = [0,0]

        for indx in range(n-1,-1,-1):
            for buy in range(2):
                if buy:
                    cur[buy] = max(-prices[indx]+prev[0],0+prev[1])
                else:
                    cur[buy] = max(prices[indx]+prev[1],0+prev[0])
                prev = cur
        return prev[1]
