class Solution:
    def minEatingSpeed(self, piles, h):
        low, high = 1, max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)

            if hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans