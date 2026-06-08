class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf')]*(amount+1) for _ in range(n)]

        for t in range(amount+1):
            if t % coins[0] == 0:
                dp[0][t] = t//coins[0]
        
        for i in range(1,n):
            for t in range(amount+1):
                include = float('inf')
                if coins[i] <= t:
                    include = 1 + dp[i][t-coins[i]]
                exclude = 0 + dp[i-1][t]
                dp[i][t] = min(exclude,include)
        
        if dp[n-1][amount] == float('inf'):
            return -1
        return dp[n-1][amount]
