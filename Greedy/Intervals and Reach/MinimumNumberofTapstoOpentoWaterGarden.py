class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        arr = [0]*(n+1)
        for i in range(n+1):
            left = max(0,i-ranges[i])
            arr[left] = max(arr[left],min(n,i+ranges[i]))
        taps = 0
        curr_end = 0
        farthest = 0

        for i in range(n + 1):
            if i > farthest:
                return -1

            farthest = max(farthest, arr[i])

            if i == curr_end:
                if i != n:
                    taps += 1
                    curr_end = farthest

        return taps
