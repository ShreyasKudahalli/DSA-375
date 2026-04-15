class Solution:
	def isCycle(self, V, edges):
		#Code here
		from collections import defaultdict
		graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [0]*V
            
        def dfs(u,parent):
            visited[u] = 1
            
            for v in graph[u]:
                if not visited[v]:
                    if dfs(v,u):
                        return True
                else:
                    if v != parent:
                        return True
            return False
        
        for i in range(V):
            if not visited[i]:
                if dfs(i,-1):
                    return True
        return False
            