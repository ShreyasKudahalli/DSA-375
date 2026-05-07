class Solution:
    def ratInMaze(self, maze):
        # code here
        n = len(maze)
        dirs = [(1,0,'D'),(0,-1,'L'),(0,1,'R'),(-1,0,'U')]
        visited = [[False]*n for _ in range(n) ]
        res = []
        
        if maze[0][0] == 0:
            return res
        
        def backtrack(i,j,comb):
            if i == n-1 and j == n-1:
                res.append(comb)
                return
        
            for r,c,d in dirs:
                nr,nc = i+r,j+c
                if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    backtrack(nr,nc,comb+d)
                    visited[nr][nc] = False
        visited[0][0] = True
        backtrack(0,0,"")
        return res
                
            
            
            