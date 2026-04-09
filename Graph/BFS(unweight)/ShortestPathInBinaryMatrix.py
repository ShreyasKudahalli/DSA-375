class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)

        if grid[0][0] or grid[n-1][n-1]:
            return -1

        q = deque([(0,0,1)])
        visited = {(0,0)}
        dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]


        while q:
            r,c,length = q.popleft()

            if r == n-1 and c == n-1:
                return length

            if min(r,c) < 0 or max(r,c) >= n or grid[r][c]:
                continue
            
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if (nr,nc) not in visited:
                    q.append((nr,nc,length+1))
                    visited.add((nr,nc))
        return -1

