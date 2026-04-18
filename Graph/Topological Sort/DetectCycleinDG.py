class Solution:
    def isCyclic(self, V, edges):
        # code here
        
        graph = [[] for _ in range(V)]
        indegree = [0] * V
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        
        while q:
            node = q.popleft()
            count += 1
            
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return count != V