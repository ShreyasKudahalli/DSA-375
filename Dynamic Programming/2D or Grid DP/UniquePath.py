class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if j==0 or i==0:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i][j-1]+dp[i-1][j]
        
        return dp[m-1][n-1]