class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i==0 and j==0:
                    res = grid[i][j]
                    continue
                elif i==0 and j!=0:
                    grid[i][j] += grid[i][j-1]
                elif j==0 and i!=0:
                    grid[i][j] += grid[i-1][0]
                else:
                    grid[i][j] += min(grid[i-1][j],grid[i][j-1])
                
                res = grid[i][j]
        return res