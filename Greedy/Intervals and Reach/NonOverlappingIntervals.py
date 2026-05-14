class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        count = 1
        intervals.sort(key = lambda x: x[1])
        last = intervals[0][1]
        if len(intervals)<2:
            return 0
        for i in range(1,len(intervals)):
            if intervals[i][0] >= last:
                count += 1
                last = intervals[i][1] 
        return n-count