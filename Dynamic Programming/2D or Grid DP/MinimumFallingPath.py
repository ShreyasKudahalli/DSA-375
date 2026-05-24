class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) > 1:
            for i in range(1,len(matrix)):
                for j in range(0,len(matrix[i])):
                    matrix[i][j] =  matrix[i][j] + min(matrix[i-1][j],matrix[i-1][max(j-1,0)],matrix[i-1][min(j+1,len(matrix[i])-1)])
                    
        return min(matrix[-1])