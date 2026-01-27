class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        ans = -1
        low = 1
        high = 10**7
        def possible(speed):
            total = 0

            for i in range(len(dist)-1):
                total += math.ceil(dist[i]/speed)
            total += dist[-1]/speed
            return total <= hour
        while low <= high:
            mid = (low+high)//2
            if possible(mid):
                ans = mid
                high = mid-1
            else:
                low = mid + 1
        return ans