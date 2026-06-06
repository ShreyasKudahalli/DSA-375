class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * (k+1) for _ in range(2)] for _ in range(n+1)]
        

        for i in range(n-1,-1,-1):
            for buy in range(2):
                for count in range(1,k+1):
                    if buy:
                        dp[i][buy][count] = max(-prices[i]+dp[i+1][0][count],dp[i+1][1][count])
                    else:
                        dp[i][buy][count] = max(prices[i]+dp[i+1][1][count-1],dp[i+1][0][count])
        return dp[0][1][k]