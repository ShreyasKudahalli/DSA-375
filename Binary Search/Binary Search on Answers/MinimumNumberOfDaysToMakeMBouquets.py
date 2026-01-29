class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < (m*k):
            return -1
        def possible(day):
            count = 0
            b = 0
            for x in bloomDay:
                if x <= day:
                    count += 1
                else:
                    b += count // k
                    count = 0
            b += count // k
            return b >= m

        low = min(bloomDay)
        high = max(bloomDay)
        while low <= high:
            mid = (low + high)//2
            if possible(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low