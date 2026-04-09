class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        count = 0
        time = 0

        n,m = len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                elif grid[i][j] == 1:
                    count += 1

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        while q:
            r,c,time = q.popleft()
            
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc]==1:
                    grid[nr][nc] = 2
                    count -= 1
                    q.append((nr,nc,time+1))
        if count:
            return -1
        return time



