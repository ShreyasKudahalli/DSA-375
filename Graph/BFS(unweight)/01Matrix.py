class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        m,n = len(mat),len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j))
                else:
                    mat[i][j] = float('inf')

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        while q:
            r,c = q.popleft()
            for dr , dc in dirs:
                nr,nc=r+dr,c+dc
                if 0 <= nc < n and 0 <= nr < m:
                    if mat[nr][nc] > mat[r][c]+1:
                        mat[nr][nc] = mat[r][c]+1
                        q.append((nr,nc))
        return mat

