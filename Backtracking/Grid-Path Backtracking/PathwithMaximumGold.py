class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c):
            gold = grid[r][c]
            
            grid[r][c] = 0
            
            max_gold = 0
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] > 0):
                    
                    max_gold = max(max_gold, dfs(nr, nc))
            
            grid[r][c] = gold
            
            return gold + max_gold
        
        ans = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    ans = max(ans, dfs(r, c))
        
        return ans