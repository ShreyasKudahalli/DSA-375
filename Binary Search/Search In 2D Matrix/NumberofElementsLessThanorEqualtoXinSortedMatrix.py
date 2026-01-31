class Solution:
    def countLessEqual(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        r = 0
        c = n-1
        count = 0

        while r < m and c >= 0:
            if matrix[r][c] <= k:
                count += (c + 1)
                r += 1
            else:
                c -= 1
        
        return count