class Solution:
    def knapsack(self, W, val, wt):
        # code here
        
        n = len(val)
        dp = [[0] * (W + 1) for _ in range(n+1)]
        
        for i in range(1, n + 1):
            for w in range(W + 1):
                exclude = dp[i - 1][w]

                include = 0
                if wt[i - 1] <= w:
                    include = val[i - 1] + dp[i - 1][w - wt[i - 1]]

                dp[i][w] = max(include, exclude)

        return dp[n][W]