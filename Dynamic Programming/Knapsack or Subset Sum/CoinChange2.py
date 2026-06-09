class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        cur = [0]*(amount+1)
        prev = [0]*(amount+1)

        for t in range(amount+1):
            if t % coins[0] == 0:
                prev[t] = 1
            else:
                prev[t] = 0
        for i in range(1,n):
            for t in range(amount+1):
                nottake = prev[t]
                take = 0
                if coins[i] <= t:
                    take = cur[t-coins[i]]
                cur[t] = nottake+take
            prev = cur
        return prev[amount]