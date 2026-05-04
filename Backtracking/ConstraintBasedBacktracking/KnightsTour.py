from collections import deque

class Solution:
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        # Convert to 0-based index
        sx, sy = KnightPos[0] - 1, KnightPos[1] - 1
        tx, ty = TargetPos[0] - 1, TargetPos[1] - 1
        
        moves = [(-2,1),(2,-1),(-2,-1),(2,1),
                 (-1,2),(1,-2),(-1,-2),(1,2)]
        
        visited = [[False]*N for _ in range(N)]
        q = deque()
        
        q.append((sx, sy, 0)) 
        visited[sx][sy] = True
        
        while q:
            x, y, steps = q.popleft()
            
            if (x, y) == (tx, ty):
                return steps
            
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, steps + 1))
        
        return -1