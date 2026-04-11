class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m,n = len(grid),len(grid[0])
        ans = 0

        def mark(r,c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == "1":
                grid[r][c] = "0"
                mark(r+1,c)
                mark(r-1,c)
                mark(r,c+1)
                mark(r,c-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    mark(i,j)
        return ans

            
