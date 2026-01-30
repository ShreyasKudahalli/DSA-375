class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        high = matrix[m-1][n-1]
        low = matrix[0][0] 

        def possible(mid):
            count = 0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] <= mid:
                        count += 1
            return count >= k
        while low <= high:
            mid = (low + high) // 2
            if possible(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
