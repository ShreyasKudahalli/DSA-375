class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        def possible(capacity):
            day = 1
            load = 0
            for x in weights:
                if x+load > capacity:
                    day += 1
                    load = x
                else:
                    load += x
            return day <= days
        while low <= high:
            mid = (low+high)//2
            if possible(mid):
                high = mid-1
            else:
                low = mid+1
        return low