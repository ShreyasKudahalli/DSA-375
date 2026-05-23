class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j]:
                    obstacleGrid[i][j]=0
                else:
                    if i==0 and j==0:
                        obstacleGrid[i][j] = 1
                    elif i==0 and j!=0:
                        obstacleGrid[i][j]= obstacleGrid[i][j-1]
                    elif j==0 and i!=0:
                        obstacleGrid[i][j] = obstacleGrid[i-1][j]
                    else:
                        obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]

        return obstacleGrid[m-1][n-1]