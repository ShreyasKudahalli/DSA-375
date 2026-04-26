class Solution:
    def floydWarshall(self, dist):
        n = len(dist)
        
        for i in range(n):
            for j in range(n):
                if dist[i][j] == -1:
                    dist[i][j] = float('inf')
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][via] != float('inf') and dist[via][j] != float('inf'):
                        dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])
        
        for i in range(n):
            for j in range(n):
                if dist[i][j] == float('inf'):
                    dist[i][j] = -1
        
        return dist