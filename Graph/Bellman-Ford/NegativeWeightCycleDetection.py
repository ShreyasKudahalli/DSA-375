#User function Template for python3

class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		
		dist = [0]*n
		dist[0] = 0
		
		for i in range(n-1):
		    for u,v,w in edges:
		        if dist[u] != float('inf') and dist[u]+w < dist[v]:
		            dist[v] = dist[u]+w
		
		for u,v,w in edges:
		        if dist[u] != float('inf') and dist[u]+w < dist[v]:
		            return 1
		return 0