class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        required = (n * m) // 2 + 1
        
        def possible(x):
            count = 0
            for i in range(n):
                count += bisect_right(mat[i], x)
            return count >= required
        
        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)
        
        while low <= high:
            mid = (low + high) // 2
            if possible(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
