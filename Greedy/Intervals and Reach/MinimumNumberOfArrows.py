class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 1
        points.sort(key = lambda x: x[1])
        last = points[0][1]

        for i in range(1,len(points)):
            if points[i][0] > last:
                count += 1
                last = points[i][1] 
        return count