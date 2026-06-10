class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if total+target<0 or (total+target)%2:
            return 0

        k = (total+target)//2
        n = len(nums)

        dp = [[0]*(k+1) for _ in range(n)]

        if nums[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        if nums[0] != 0 and nums[0] <= k:
            dp[0][nums[0]] = 1

        for i in range(1, n):
            for t in range(k + 1):
                not_take = dp[i-1][t]
                take = 0
                if nums[i] <= t:
                    take = dp[i-1][t-nums[i]]
                dp[i][t] = take+not_take

        return dp[n - 1][k]