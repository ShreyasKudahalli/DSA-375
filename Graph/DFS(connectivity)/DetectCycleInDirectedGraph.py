class Solution:
    def isCyclic(self, V, edges):
        # code here
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            
        pathvisited = [0]*V
        visited = [0]*V
        
        def dfs(u):
            visited[u] = 1
            pathvisited[u] = 1
            for v in adj[u]:
                if not visited[v]:
                    if dfs(v):
                        return True
                elif pathvisited[v]:
                    return True
            pathvisited[u] = 0
            return False
            
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        return False