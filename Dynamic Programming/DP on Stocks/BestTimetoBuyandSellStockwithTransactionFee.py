class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n+1)]
        cur = prev = [0,0]
        for indx in range(n-1,-1,-1):
            for buy in range(2):
                if buy:
                    cur[buy] = max(-prices[indx]+prev[0],prev[1])
                else:
                    cur[buy] = max((prices[indx]+prev[1])-fee,prev[0])
        return cur[1]