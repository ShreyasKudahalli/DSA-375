class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        n = len(stalls)
        low = 0
        high = stalls[-1]-stalls[0]
        def possible(dist):
            cows = 1
            last_pos = stalls[0]
            
            for i in range(1, n):
                if stalls[i] - last_pos >= dist:
                    cows += 1
                    last_pos = stalls[i]
                if cows >= k:
                    return True
            return False
        
        while low <= high:
            mid = (low + high)//2
            if possible(mid):
                low = mid+1
            else:
                high = mid-1
        return high
            
        