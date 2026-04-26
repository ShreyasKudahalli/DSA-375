#User function Template for python3

class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		
		dist = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
        
        for u, v, w in edges:
            dist[u][v] = w
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][via] != float('inf') and dist[via][j] != float('inf'):
                        dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])
        
        for i in range(n):
            if dist[i][i] < 0:
                return 1
        
        return 0