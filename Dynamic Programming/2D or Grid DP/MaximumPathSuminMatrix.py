#User function Template for python3
class Solution:
    def maximumPath(self, mat):
        # code here
        
        if len(mat) > 1:
            for i in range(1,len(mat)):
                for j in range(0,len(mat[i])):
                    mat[i][j] =  mat[i][j] + max(mat[i-1][j],mat[i-1][max(j-1,0)],mat[i-1][min(j+1,len(mat[i])-1)])
                    
        return max(mat[-1])