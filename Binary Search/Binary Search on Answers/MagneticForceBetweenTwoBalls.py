class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        low = 0
        high = position[-1]-position[0]
        def possible(dist):
            balls = 1
            last_pos = position[0]
            
            for i in range(1, n):
                if position[i] - last_pos >= dist:
                    balls += 1
                    last_pos = position[i]
                if balls >= m:
                    return True
            return False
        while low <= high:
            mid = (low + high)//2
            if possible(mid):
                low = mid+1
            else:
                high = mid-1
        return high