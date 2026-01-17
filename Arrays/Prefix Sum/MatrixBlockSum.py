class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        psum = [row[:] for row in mat]
        n,m = len(psum),len(psum[0])
        for i in range(n):
            for j in range(1,m):
                psum[i][j] += psum[i][j-1]
        for i in range(1,n):
            for j in range(m):
                psum[i][j] += psum[i-1][j]
        
        def area(r1,r2,c1,c2):
            res = psum[r2][c2]

            if r1 > 0:
                res -= psum[r1-1][c2]
            if c1 > 0:
                res -= psum[r2][c1-1]
            if r1 > 0 and c1 >0:
                res += psum[r1-1][c1-1]
            return res
        
        for i in range(n):
            for j in range(m):
                r1,r2,c1,c2 = max(0,i-k),min(n-1,k+i),max(0,j-k),min(m-1,j+k)
                mat[i][j] = area(r1,r2,c1,c2)
        return mat